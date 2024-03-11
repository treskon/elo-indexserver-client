from eloclient import Client
from eloclient.api.ix_service_port_if import (ix_service_port_if_checkin_sord_path, ix_service_port_if_delete_sord)
from eloclient.api.ix_service_port_if import (ix_service_port_if_copy_sord)
from eloclient.models import (BRequestIXServicePortIFCheckinSordPath, BRequestIXServicePortIFDeleteSord)
from eloclient.models import (BRequestIXServicePortIFCopySord)
from eloclient.models import Sord, SordZ, SordC
from eloservice.eloconstants import COPY_SORD_C_MOVE
from eloservice.error_handler import _check_response
from eloservice.file_util import FileUtil
from eloservice.login_util import LoginUtil
from eloservice.mask_util import MaskUtil
from eloservice.search_util import SearchUtil


class EloService:
    """
    This class is the main class for the ELO service
    """
    elo_client: Client
    login_util: LoginUtil
    elo_connection = None
    mask_util = None
    file_util = None
    search_util = None

    def __init__(self, url: str, user: str, password: str):
        self.login_util = LoginUtil(url, user, password)
        self._update_utils()

    def _update_utils(self):
        self.elo_client = self.login_util.elo_client
        self.elo_connection = self.login_util.elo_connection
        self.mask_util = MaskUtil(self.elo_client, self.elo_connection)
        self.file_util = FileUtil(self.elo_client, self.elo_connection)
        self.search_util = SearchUtil(self.elo_client, self.elo_connection)

    def create_folder(self, path: str, separator="¶") -> str:
        """
        This function creates new folder in ELO

        Depending on the given path it is possible to create 1 or multiple folders. If the folder already exists,
        nothing is changed and the sordID of the existing folder is returned.

        :param path: The path in ELO to the needed folder/ doc (e.g. = ¶Alpha AG¶Eingangsrechnungen¶2023¶November¶20¶)
        :param separator: The separator which should be used to split the path (default = "¶")

        :return: The sordID of the created folder
        """
        parent_id = "1"  # the parent ID of the root element
        sords = self._split_path_elements(path, separator)

        body = BRequestIXServicePortIFCheckinSordPath(
           
            parent_id=parent_id,
            sords=sords,
            sord_z=SordZ(SordC().mb_all)
        )

        erg = ix_service_port_if_checkin_sord_path.sync_detailed(client=self.elo_client, json_body=body)
        _check_response(erg)
        object_id = erg.parsed.result[-1]
        if object_id is None:
            raise ValueError("Could not create folder")
        return object_id

    def overwrite_mask_fields(self, sord_id: str, mask_name: str, metadata: dict):
        """
        This function removes the old metadata and overwrite it with the new metadata

        :param sord_id: The sordID of the mask in ELO
        :param mask_name: The name of the mask in ELO
        :param metadata: The metadata which should be overwritten
        """
        self.mask_util.overwrite_mask_fields(sord_id, mask_name, metadata)

    def upload_file(self, file_path: str, parent_id: str, filemask_id="0", filename="") -> str:
        """
        This function uploads a file to ELO

        :param filename: The name of the file in ELO, if not given the name of the file_path is used
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param parent_id: The sordID of the parent folder in ELO

        :return: The sordID of the uploaded file
        """
        return self.file_util.upload_file(file_path=file_path, parent_id=parent_id, filemask_id=filemask_id, filename=filename)

    def update_file(self, sord_id: str, file_path: str, filename=""):
        """
        This function updates a file in ELO

        :param sord_id: The sordID of the file in ELO
        :param filename: The name of the file in ELO, if not given the name of the file_path is used
        :param file_path: The path of the file which should be uploaded
        """
        self.file_util.update_file(file_path=file_path, file_id=sord_id, filename=filename)

    def search(self, search_mask_fields: dict = None, search_mask_id: str = None, max_results: int = 100) -> [str]:
        """
        This function searches for objects that match all the given metadata

        :param search_mask_fields: The metadata that should be searched for (default = None)
        :param search_mask_id: The maskID of the mask that should be searched (default = None)
        :param max_results:  The maximum number of results that should be returned (default = 100)

        :return: The sordIDs of the found objects
        """
        return self.search_util.search(search_mask_fields, search_mask_id, max_results)

    def exists(self, search_mask_fields: dict = None, search_mask_id: str = None) -> bool:
        """
        This function checks if an object exists that matches all the given metadata

        :param search_mask_fields: The metadata that should be searched for (default = None)
        :param search_mask_id: The maskID of the mask that should be searched (default = None)
        :return: True if an object exists, False if not
        """
        return len(self.search_util.search(search_mask_fields, search_mask_id, max_results=1)) > 0

    def checkout(self, sord_id: str) -> Sord:
        """
        This function checks out a sord in ELO

        :param sord_id: The sordID of the sord in ELO
        :return: The checked out sord
        """
        return self.file_util.checkout_sord(sord_id)

    def remove(self, sord_id: str):
        """
        This function removes a sord in ELO

        :param sord_id: The sordID of the sord in ELO
        """
        body = BRequestIXServicePortIFDeleteSord(obj_id=sord_id)
        res = ix_service_port_if_delete_sord.sync_detailed(client=self.elo_client, json_body=body)
        _check_response(res)
        if res.parsed.result is None:
            raise ValueError("Could not delete sord")

    def move(self, source_sord_id: str, path: str, separator="¶"):
        """
        This function moves a sord in ELO

        :param source_sord_id: The sordID of the sord in ELO which should be moved
        :param path: The path of the new parent folder in ELO

        :param separator: The separator which should be used to split the path (default = "¶")
        :return: The sordId of the moved sord
        """
        new_destination_sordid = self.create_folder(path, separator)
        return self._move_sord(source_sord_id=source_sord_id, new_parent_id=new_destination_sordid)

    def _move_sord(self, source_sord_id: str, new_parent_id: str):
        """
        This function moves a sord in ELO

        :param source_sord_id: The sordID of the sord in ELO
        :param new_parent_id: The new parentID of the sord in ELO

        :return: The sordId of the moved sord
        """
        body = BRequestIXServicePortIFCopySord(
           
            new_parent_id=new_parent_id,
            obj_id=source_sord_id,
            copy_sord_z=COPY_SORD_C_MOVE
        )
        res = ix_service_port_if_copy_sord.sync_detailed(client=self.elo_client, json_body=body)
        _check_response(res)
        return new_parent_id

    def _split_path_elements(self, path, separator="¶") -> list[Sord]:
        """
        This help function splits a path in subparts and return the splitte parts

        :param path: A path with a given separator, e.g = "/Alpha AG/Eingangsrechnungen/2023/November/20"
        :param separator: The separator which should be used to split the path (default = "¶")

        :return: The subparts of the path = path slices
        """
        return [Sord(name=path_element) for path_element in filter(None, path.split(separator))]
