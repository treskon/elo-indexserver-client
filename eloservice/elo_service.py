from eloclient import Client
from eloclient.api.ix_service_port_if import (ix_service_port_if_checkin_sord_path, ix_service_port_if_delete_sord)
from eloclient.api.ix_service_port_if import (ix_service_port_if_copy_sord)
from eloclient.models import (BRequestIXServicePortIFCheckinSordPath, BRequestIXServicePortIFDeleteSord)
from eloclient.models import (BRequestIXServicePortIFCopySord)
from eloclient.models import Sord
from eloservice.eloconstants import COPY_SORD_C_MOVE, SORD_Z_EMPTY
from eloservice.error_handler import _check_response
from eloservice.file_util import FileUtil, FILENAME_OBJKEY_ID_DEFAULT
from eloservice.login_util import LoginUtil
from eloservice.map_util import MapUtil
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
    map_util = None
    file_util = None
    search_util = None
    cache_enable = None
    cache_ttl = None
    cache_maxsize = None

    def __init__(self, url: str, user: str, password: str,
                 cache_enable: bool = True, cache_ttl: int = 600, cache_maxsize: int = 128):
        """
        Known issue: Due to encoding issues the user and password should not contain special characters.
        :param url:  The URL to the ELO IX server rest endpoint e.g. http://eloserver.com:6056/ix-Archive/rest/
        :param user:  The user for the ELO IX server e.g. Administrator
        :param password:  The password for the ELO IX server user e.g. secret
        :param cache_enable: If the caching should be enabled (default = True)
                             Currently, the caching is only used for:
                               * function overwrite_mask_fields (cache of existing masks and mask details)
        :param cache_ttl:   The time to live of the cache in seconds (default = 600, so 10 minutes) only used if
                            cache_enable is True
        :param cache_maxsize: The maximum size of the cache (default = 128) only used if cache_enable is True
        """
        self.login_util = LoginUtil(url, user, password)
        self.cache_enable = cache_enable
        self.cache_ttl = cache_ttl
        self.cache_maxsize = cache_maxsize
        self._update_utils()

    def _update_utils(self):
        self.elo_client = self.login_util.elo_client
        self.elo_connection = self.login_util.elo_connection
        self.mask_util = MaskUtil(self.elo_client, self.elo_connection, cache_enable=self.cache_enable,
                                  cache_ttl=self.cache_ttl, cache_maxsize=self.cache_maxsize)
        self.map_util = MapUtil(self.elo_client, self.elo_connection)
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

        Note: a mask and metadata can not directly be assigned consistently to the folder in the same call. As they
        would only be assigned if the folder did not exist before. If the folder already exists, the mask and metadata
        would not be written. To write the mask and metadata, use the method :func:`overwrite_mask_fields` after the
        folder was created.
        """
        parent_id = "1"  # the parent ID of the root element
        sords: list[Sord] = self._split_path_elements(path, separator)

        body = BRequestIXServicePortIFCheckinSordPath(
            parent_id=parent_id,
            sords=sords,
            sord_z=SORD_Z_EMPTY,  # we need to set an empty bitset and not MB_ALL. Otherwise, the indexserver tries
            # to assign the document mask 'Freie Eingabe' to the folder which fails
        )

        erg = ix_service_port_if_checkin_sord_path.sync_detailed(client=self.elo_client, body=body)
        _check_response(erg)
        object_id = erg.parsed.result[-1]
        if object_id is None:
            raise ValueError("Could not create folder")
        return object_id

    def overwrite_mask_fields(self, sord_id: str, mask_name: str, metadata: dict, metadata_force: dict = None):
        """
        This function removes the old metadata and overwrite it with the new metadata

        :param sord_id: The sordID of the mask in ELO
        :param mask_name: The name of the mask in ELO
        :param metadata: The metadata which should be overwritten
        :param metadata_force: The metadata which should be overwritten even if the given key is not in the mask. Can be
            needed for special metadata like the filename. The key in the dict is used as ID and as 'name' at the same time.
            Setting the key name in ELO seems to be irrelevant anyway, the ID seems to always have priority.(default = None)
        """
        self.mask_util.overwrite_mask_fields(sord_id, mask_name, metadata, metadata_force)

    def write_map_fields(self, sord_id: str, fields: dict, map_domain: str = "Objekte",
                         value_type: MapUtil.ValueType = MapUtil.ValueType.string,
                         content_type="text/plain; charset=ISO_8859_1"):
        """
        This function writes map fields to a sord in ELO.

        Existing map fields are overwritten when writing the same key. Old map fields which are not overwritten will
        remain.

        There are three different value types:
        * string: The value is stored as a string. The value is limited to 255 characters.
        * blob_string: The value is stored as a blob. The value is unlimited in size.
        * blob_file: The value is stored as a blob. The value is unlimited in size. The param content_type should be
        used to specify the content type of the blob.

        Map Fields in ELO are defined as follows:
        * the map_domain specifies the database table in which the map fields are stored. There are two common ones
        'objekte' and 'formdata'. Furthermore, there can also be special map domains unique to each server.
        * The fields are a key value pair, unique to that domain. That are assigned to a SORD object.

        Implementation details:
        The key is a string. The value can either be a string (limited to 255 characters) or a blob (unlimited size).
        The value_type specifies the type of the value. Internally the string value is stored as varchar(255) and the
        blob value is stored as varchar(*). Therefore, if a string value is larger than
        255 characters, the value is stored as a blob.

        :param sord_id: The sordID of the sord in ELO
        :param fields: The fields that should be written
                key: The key of the map field: str
                value: The value of the map field. The type of the value depends on the value_type parameter.
                For value_type = MapUtil.ValueType.string: str
                For value_type = MapUtil.ValueType.blob_string: str
                For value_type = MapUtil.ValueType.blob_file. It can either be a str which is interpreted as a file path
                or bytes which is interpreted as the content blob.
        :param map_domain: The map domain in ELO (default = "Objekte")
        :param value_type: The value type of the fields (default = MapUtil.ValueType.string)
        :param content_type: The content type of the blob (default = "text/plain; charset=ISO_8859_1")
        """
        self.map_util.write_map_fields(sord_id, fields, map_domain, value_type, content_type)

    def read_map_fields(self, sord_id: str, keys: list[str] = None, map_domain: str = "Objekte") -> dict[
        str, MapUtil.MapValue]:
        """
        This function read either all map fields or a list of specific map field from a sord in ELO. In both cases, the
        return type is a dictionary with the key as the key of the map field and the value as the value of the map field.

        :param sord_id: The sordID of the sord in ELO you want to read the map fields from
        :param keys: A list of keys which should be read. If None or empty list, all keys are read (default = None)
        :param map_domain: The map domain in ELO (default = "Objekte"). This is what is displayed in the ELO client in
            the additional infos tab. Common map domains are 'Objekte' and 'Formdata'.
        """
        return self.map_util.read_map_fields(sord_id=sord_id, keys=keys, map_domain=map_domain)

    def serialize_map_fields_table(self, map_fields: dict[str, MapUtil.MapValue],
                                   column_names: list[str]):
        """
        Helper Method to serializes, given the raw elo map fields, a table like format. The table is represented as a list
        of dictionaries, where each dictionary represents a row in the table.
        All operations are done in memory and no ELO operations are performed.

        In Elo a table is faked by formatting the keys of the map fields. Example:
        We assume some employee table with columns are "EMPLOYEE_NAME", "AGE", and we assume 2 rows, then the keys are
        formatted as follows:
        "EMPLOYEE_NAME1", "AGE1", "EMPLOYEE_NAME2", "AGE2"

        Notice that the row number is appended to the column name. Where the row number is a positive integer starting
        from 1 and can be any number of digits.
        Also Notice that there is no "table name" in the keys. The column names are arbitrary and do not need to contain
        any information about the table.

        :param map_fields: a dictionary of map fields, comes from the function read_map_fields
        :param column_names: a list of column names
        :return: a list of dictionaries, each dictionary represents a row in the table
        """
        return self.map_util.serialize_table(map_fields, column_names)

    def deserialize_map_fields_table(self, table: list[dict[str, MapUtil.MapValue]]) -> dict[str, str]:
        """
        The reverse of serialize_map_fields_table.
        Given a table, it transforms it to a dictionary of map fields.
        Which can be directly written to elo via the method write_map_fields.
        All operations are done in memory and no ELO operations are performed.

        In Elo a table is faked by formatting the keys of the map fields. Example:
        We assume some employee table with columns are "EMPLOYEE_NAME", "AGE", and we assume 2 rows, then the keys are
        formatted as follows:
        "EMPLOYEE_NAME1", "AGE1", "EMPLOYEE_NAME2", "AGE2"

        Notice that the row number is appended to the column name. Where the row number is a positive integer starting
        from 1 and can be any number of digits.
        Also Notice that there is no "table name" in the keys. The column names are arbitrary and do not need to contain
        any information about the table.

        the result can directly be used in the function write_map_fields

        :param table: a list of dictionaries, each dictionary represents a row in the table
        :return: a dictionary of map fields, for the use in the function write_map_fields
        """
        return self.map_util.deserialize_table(table)

    def upload_file(self, file_path: str, parent_id: str, filemask_id="0", filename="",
                    filename_objkey_id=FILENAME_OBJKEY_ID_DEFAULT,
                    filename_objkey="",
                    filedate=None) -> str:
        """
        This function uploads a file to ELO

        :param filename: The name of the file in ELO, if not given the name of the file_path is used. This is the filename
         which is shown in the directory tree. However, also referred to as kurzbezeichnung in ELO.
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param parent_id: The sordID of the parent folder in ELO
        :param filename_objkey_id: The objkeyID of the filename objkey in ELO, default is "51" (--> objkey "ELO_FNAME")
         this sets the filename in the tab 'Options'
        :param filename_objkey The filename in the tab 'Options' in ELO
        :param filedate: The date of the file, in UTC, default is the modification date of the file. Format is in
         ISO 8601 e.g."2021-08-25T15:00:00". The date is stored in UTC in ELO and displayed in the local time zone of the
         user client.
        :return: The sordID of the uploaded file
        """
        return self.file_util.upload_file(file_path=file_path, parent_id=parent_id, filemask_id=filemask_id,
                                          filename=filename, filename_objkey_id=filename_objkey_id,
                                          filename_objkey=filename_objkey,
                                          filedate=filedate)

    def update_file(self, sord_id: str, file_path: str, filename="", filename_objkey_id=FILENAME_OBJKEY_ID_DEFAULT,
                    filename_objkey="",
                    filedate=None):
        """
        This function updates a file in ELO

        :param sord_id: The sordID of the file in ELO
        :param filename: The name of the file in ELO, if not given the name of the file_path is used
        :param file_path: The path of the file which should be uploaded
        :param filename_objkey_id: The objkeyID of the filename objkey in ELO, default is "51" (--> objkey "ELO_FNAME")
        :param filename_objkey: The filename in the tab 'Options' in ELO
        :param filedate: The date of the file, in UTC, default is the modification date of the file. Format is in
        ISO 8601 e.g."2021-08-25T15:00:00". The date is stored in UTC in ELO and displayed in the local time zone of the
         user client.
        """
        self.file_util.update_file(file_path=file_path, file_id=sord_id, filename=filename,
                                   filename_objkey_id=filename_objkey_id, filename_objkey=filename_objkey,
                                   filedate=filedate)

    def download_file(self, sord_id: str, file_path: str):
        """
        This function downloads a file from ELO
        :param sord_id: The sordID of the file which should be downloaded
        :param file_path: The path where the file should be saved
        """
        self.file_util.download_file(sord_id, file_path)

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

    def get_mask_fields(self, sord_id: str) -> dict:
        """
        This function returns the mask fields of a sord in ELO

        ELOFIELD -> Python type:

        * text -> str

        * numerical -> float, int, Decimal

        * date(time) -> datetime

        * list -> list of str

        :param sord_id: The sordID of the sord in ELO
        :return: The mask fields of the sord
        """
        return self.mask_util.get_mask_fields(sord_id)

    def remove(self, sord_id: str):
        """
        This function removes a sord in ELO

        :param sord_id: The sordID of the sord in ELO
        """
        body = BRequestIXServicePortIFDeleteSord(obj_id=sord_id)
        res = ix_service_port_if_delete_sord.sync_detailed(client=self.elo_client, body=body)
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
        res = ix_service_port_if_copy_sord.sync_detailed(client=self.elo_client, body=body)
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
