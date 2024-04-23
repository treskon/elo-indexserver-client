import logging
from http import HTTPStatus

from eloclient.types import Response, Unset


def _check_response(erg: Response):
    if erg is None:
        raise ValueError("No response from ELO IX server")
    code: HTTPStatus = erg.status_code
    if 200 <= code < 300:
        # ELO IX server returns a 200 status code even if an error occurred
        if (erg.parsed is not None) and (erg.parsed.exception is not None) and not isinstance(erg.parsed.exception,
                                                                                              Unset):
            logging.error(f"Error from ELO IX server: {erg.status_code} - {erg.parsed.result} - "
                          f"{erg.parsed.exception}")
            raise ValueError(
                f"Error from ELO IX server: {erg.status_code} - {erg.parsed.exception}")
        if erg.content is not None and "\"exception\"" in str(erg.content):
            raise ValueError(
                f"Error from ELO IX server: {erg.content}")
        return
    logging.warning(f"Response from ELO IX server: {erg.status_code}"
                    f" - {str(erg.content)}")
    raise ValueError(
        f"Error from ELO IX server: {erg.status_code} - {str(erg.content)}")