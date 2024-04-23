import mimetypes

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_create_doc, ix_service_port_if_checkin_doc_end, \
    ix_service_port_if_checkout_sord
from eloclient.models import BRequestIXServicePortIFCreateDoc, Sord, BRequestIXServicePortIFCheckinDocEnd, SordZ, LockZ, \
    LockC, Document, FileData, BStreamReference, DocVersion, BRequestIXServicePortIFCheckoutSord, EditInfoZ, EditInfoC
from eloservice import eloconstants as elo_const
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


def _read_file(file_path):
    # read file as binary and return it together with the file name
    with open(file_path, "rb") as file:
        file_content = file.read()
        file_name = file.name[file.name.rfind("/") + 1:]
        return file_content, file_name


class FileUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def update_file(self, file_path: str, file_id: str, filename="") -> str:
        """
        This function updates a file in ELO
        :param filename:
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param file_id: The sordID of the file which should be updated
        :return: The sordID of the updated file
        """
        file_content, file_name_path = _read_file(file_path)
        sord = self.checkout_sord(file_id)
        return self._checkin_doc(sord, self.elo_connection, file_content, filename if filename else file_name_path)

    def upload_file(self, file_path: str, parent_id: str, filemask_id="0", filename="") -> str:
        """
        This function uploads a file to ELO
        :param filename:
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param parent_id: The sordID of the parent folder in ELO
        :return: The sordID of the uploaded file
        """
        file_content, file_name_path = _read_file(file_path)
        return self._checkin_new_doc(self.elo_connection, parent_id, filename if filename else file_name_path,
                                     file_content, filemask_id)

    def _checkin_new_doc(self, elo_connection, parent_id, filename, filecontent, filemask_id="0"):
        document_sord = self._create_doc(filemask_id, parent_id)
        return self._checkin_doc(document_sord, elo_connection, filecontent, filename)

    def checkout_sord(self, sord_id) -> Sord:
        body = BRequestIXServicePortIFCheckoutSord(
           
            obj_id=sord_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL,
            lock_z=LockZ(LockC().bset_no)
        )
        res = ix_service_port_if_checkout_sord.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        if type(res.parsed.result.sord) is not Sord:
            raise ValueError(f"Sord with ID {sord_id} not found")
        return res.parsed.result.sord

    def _checkin_doc(self, document_sord, elo_connection, filecontent, filename):
        document_sord.name = filename
        mimetype = mimetypes.guess_type(filename)[0]
        # upload File and get the reference link
        streamID = self._upload_file(filecontent)
        document = Document(
            docs=[
                DocVersion(
                    version="1.0",
                    comment="",
                    content_type=mimetype,
                    file_data=FileData(
                        stream=BStreamReference(
                            stream_id=streamID
                        )
                    ),
                    work_version=True
                )],
            atts=[]

        )
        body = BRequestIXServicePortIFCheckinDocEnd(
            sord=document_sord,
            sord_z=SordZ(bset=elo_const.ElobitsetEditz.MB_ALL.value),
            unlock_z=LockZ(LockC().bset_yes),
            document=document
        )
        res = ix_service_port_if_checkin_doc_end.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        return res.parsed.result.obj_id

    def _upload_file(self, filecontent) -> str:
        """
        This function uploads a file to ELO. Which according to their documentation "is kept there for a few minutes."
        :param filecontent: the bytestream of the file
        :return: the streamID of the uploaded file, which can be used to reference the file in checkinDocEnd
        """
        # OPENAPI Spec provided by elo does not match with the real API, therefore we have to use the httpx client
        # directly
        erg = self.elo_client.get_httpx_client().request("POST", "/BUtility/upload", data=filecontent)
        # expected b'{"result":{"streamId":"8066662033750693538"}}'
        return erg.json()["result"]["streamId"]

    def _create_doc(self, filemask_id, parent_id) -> Sord:
        body = BRequestIXServicePortIFCreateDoc(
            parent_id=parent_id,
            mask_id=filemask_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL
        )
        res = ix_service_port_if_create_doc.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        document_sord = res.parsed.result.sord
        return document_sord
