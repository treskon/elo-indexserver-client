import logging


def _check_response(erg):
    try:
        if erg is None:
            raise ValueError("No response from ELO IX server")
        if erg.status_code != 200:
            if (erg.parsed is not None) and (erg.parsed.exception is not None):
                logging.error(f"Error from ELO IX server: {erg.status_code} - {erg.parsed.result} - "
                              f"{erg.parsed.exception}")
            raise ValueError(
                f"Error from ELO IX server: {erg.status_code}")
        if erg.parsed.result is None:
            raise ValueError(
                f"Error from ELO IX server: {erg.status_code} - {erg.parsed.result} - {erg.parsed.exception}")
        if erg.content is not None and "\"exception\"" in str(erg.content):
            raise ValueError(
                f"Error from ELO IX server: {erg.content}")
    except Exception as e:
        logging.error(f"Error from ELO IX server: {e}")
        raise e
