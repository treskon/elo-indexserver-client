import mimetypes
import os
import re
from datetime import datetime, timezone

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_create_doc, ix_service_port_if_checkin_doc_end, \
    ix_service_port_if_checkout_sord
from eloclient.models import BRequestIXServicePortIFCreateDoc, Sord, BRequestIXServicePortIFCheckinDocEnd, SordZ, LockZ, \
    LockC, Document, FileData, BStreamReference, DocVersion, BRequestIXServicePortIFCheckoutSord, ObjKey
from eloservice import eloconstants as elo_const
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection

FILENAME_OBJKEY_ID_DEFAULT = "51"


class FileUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def update_file(self, file_path: str, file_id: str, filename="", filename_objkey_id=FILENAME_OBJKEY_ID_DEFAULT,
                    filename_objkey="",
                    filedate=None) -> str:
        """
        This function updates a file in ELO
        :param filename: The name of the file in ELO, if not given the name of the file_path is used. This is the filename
        which is shown in the directory tree. However, also referred to as kurzbezeichnung in ELO.
        :param filedate: The date of the file, in UTC, default is the modification date of the file. Format is in ISO 8601 e.g.
        "2021-08-25T15:00:00".
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param file_id: The sordID of the file which should be updated
        :param filename_objkey_id: The objkeyID of the filename objkey in ELO, default is "51" (--> objkey "ELO_FNAME")
        this sets the filename in the tab 'Options'
        :param filename_objkey: This will be the filename in the tab 'Options' in ELO. If not set correctly, consider
        setting filename_objkey_id to your specific elo instance, the ID can be found checking the objkeys db table.
        :return: The sordID of the updated file
        """
        file_content, file_name_path = self._read_file(file_path)
        filedate = self._getfiledate(file_path, filedate)
        sord = self.checkout_sord(file_id)
        filename_elo, kurzbezeichnung = self._prepare_checkin_doc(file_name_path, filename, filename_objkey)
        return self._checkin_doc(sord, filecontent=file_content,
                                 kurzbezeichnung=kurzbezeichnung, filename=filename_elo,
                                 filename_objkey_id=filename_objkey_id,
                                 x_date_iso=filedate)

    def upload_file(self, file_path: str, parent_id: str, filemask_id="0", filename="",
                    filename_objkey_id=FILENAME_OBJKEY_ID_DEFAULT,
                    filename_objkey="",
                    filedate=None) -> str:
        """
        This function uploads a file to ELO
        :param filename: The name of the file in ELO, if not given the name of the file_path is used. This is the filename
        which is shown in the directory tree. However, also referred to as kurzbezeichnung in ELO.
        :param filedate: The date of the file, in UTC, default is the modification date of the file. Format is in ISO 8601 e.g.
        "2021-08-25T15:00:00".
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param parent_id: The sordID of the parent folder in ELO
        :param filename_objkey_id: The objkeyID of the filename objkey in ELO, default is "51" (--> objkey "ELO_FNAME")
        this sets the filename in the tab 'Options'
        :param filename_objkey: This will be the filename in the tab 'Options' in ELO. If not set correctly, consider
        setting filename_objkey_id to your specific elo instance, the ID can be found checking the objkeys db table.
        :return: The sordID of the uploaded file
        """
        file_content, file_name_path = self._read_file(file_path)
        filedate = self._getfiledate(file_path, filedate)
        filename_elo, kurzbezeichnung = self._prepare_checkin_doc(file_name_path, filename, filename_objkey)
        document_sord = self._create_doc(filemask_id, parent_id)
        return self._checkin_doc(document_sord, filecontent=file_content,
                                 kurzbezeichnung=kurzbezeichnung, filename=filename_elo,
                                 filename_objkey_id=filename_objkey_id,
                                 x_date_iso=filedate)

    def download_file(self, sord_id: str, file_path: str):
        """
        This function downloads a file from ELO
        :param sord_id: The sordID of the file which should be downloaded
        :param file_path: The path where the file should be saved
        """
        sord = self.checkout_sord(sord_id)
        doc_url = sord.doc_version.url
        # often the url is not directly accessible due to it being behind a reverse proxy or firewall.
        # therefore we need to replace the url with the hostname and port of the elo connection
        regex = "http(s)?://(.*):(\\d+)"
        # get only the http(s)://hostname:port part of the url
        hostname_port = re.search(regex, self.elo_connection.url).group(0)
        replaced_url = re.sub(regex, hostname_port, doc_url)
        stream = self.elo_client.get_httpx_client().get(replaced_url)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            file.write(stream.content)
        return file

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

    def _read_file(self, file_path):
        try:
            # read file as binary and return it together with the file name
            with open(file_path, "rb") as file:
                file_content = file.read()
                file_name = file.name[file.name.rfind("/") + 1:]
                return file_content, file_name
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found")
        except Exception as e:
            raise ValueError(f"Error while reading file {file_path}: {e}")

    def _getfiledate(self, file_path, filedate):
        """
        This function returns the filedate of a file. If filedate is given, it will be returned, otherwise the
        modification date of the file will be returned.
        :param file_path:
        :param filedate:
        :return:
        """
        if filedate:
            try:
                datetime.fromisoformat(filedate)
            except ValueError:
                raise ValueError("The filedate is not in the correct format. Please use ISO 8601 format e.g. "
                                 "2021-08-25T15:00:00")
            return filedate

        modified_filedate = datetime.fromtimestamp(os.path.getmtime(file_path))

        # get the time difference between the local time and UTC; WE read the filedate 'now' therefore we need to use
        # this difference to convert the filedate to UTC. And not the offset of the filedate itself.
        # e.g if the file was created in wintertime and we read it in summertime, the offset would be wrong.
        tzinfo = datetime.now(timezone.utc).astimezone().tzinfo
        time_difference = tzinfo.utcoffset(datetime.now())

        # subtract the time difference to the modified file date so we get UTC time
        modified_filedate = modified_filedate - time_difference
        return modified_filedate.isoformat()

    def _prepare_checkin_doc(self, file_name_path, filename, filename_objkey):
        if filename:
            kurzbezeichnung = filename
            filename_elo = file_name_path
        else:
            kurzbezeichnung = file_name_path
            filename_elo = file_name_path
        if filename_objkey:
            filename_elo = filename_objkey
        return filename_elo, kurzbezeichnung

    def _checkin_doc(self, document_sord, filecontent, kurzbezeichnung, filename,
                     filename_objkey_id=FILENAME_OBJKEY_ID_DEFAULT,
                     x_date_iso=datetime.now().isoformat()) -> str:
        """

        :param document_sord:
        :param filecontent:
        :param kurzbezeichnung:
        :param filename:
        :param objidate: Internal = Sord.objidate = Time of the archiving
        :param objxdate: External = Sord.objxdate = Primary document date (optional)
        :param filename_objkey_id:
        :return:
        """
        document_sord.name = kurzbezeichnung
        document_sord.x_date_iso = x_date_iso
        document_sord.obj_keys = [
            ObjKey(data=[filename], name="ELO_FNAME", id=filename_objkey_id, obj_id=document_sord.id)]
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
