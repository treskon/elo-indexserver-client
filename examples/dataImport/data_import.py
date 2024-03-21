from decouple import AutoConfig
from eloservice.elo_service import EloService
import pandas as pd
from tqdm import tqdm
import sys


def load_elo_service():
    config = AutoConfig(search_path='./')  # load .env file from current directory with connection details
    rest_baseurl = config("TEST_ELO_IX_URL")
    rest_user = config("TEST_ELO_IX_USER")
    rest_password = config("TEST_ELO_IX_PASSWORD")
    return EloService(url=rest_baseurl, user=rest_user, password=rest_password)


def load_dataset():
    df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')
    df["SALE_AMOUNT"] = df["QUANTITYORDERED"] * df["PRICEEACH"]
    df["SALE_PRODUCT"] = df["PRODUCTLINE"]
    df["SALE_DATE"] = df["ORDERDATE"]
    df["SALE_NAME"] = df["ORDERNUMBER"].astype(str) + " " + df["PRODUCTCODE"].astype(str) + " " + df[
        "CUSTOMERNAME"].astype(str)
    # remove \n and multiple spaces from sale_name
    df["SALE_NAME"] = df["SALE_NAME"].str.replace("\n", " ").str.replace(" +", " ", regex=True)

    df = df[["SALE_NAME", "SALE_DATE", "SALE_PRODUCT", "SALE_AMOUNT"]]
    df["SALE_DATE"] = pd.to_datetime(df["SALE_DATE"])
    df["SALE_DATE_ELO"] = df["SALE_DATE"].dt.strftime("%Y%m%d%H%M%S")
    return df


def create_sord_singlethreaded(row, elo_service, base_path, separator):
    folderName = row["SALE_NAME"]
    fullPath = base_path + separator + folderName
    sordID = elo_service.create_folder(fullPath)
    print(f"Created folder {fullPath} with sordID {sordID}")
    elo_service.overwrite_mask_fields(sord_id=sordID,
                                      mask_name="SALE",
                                      metadata={"SALE_NAME": row["SALE_NAME"],
                                                # formatted with yyyyMMddHHmmss
                                                "SALE_DATE": row["SALE_DATE_ELO"],
                                                "SALE_PRODUCT": row["SALE_PRODUCT"],
                                                "SALE_AMOUNT": row["SALE_AMOUNT"]})
    print(f"Updated metadata for sord {sordID}")
    return sordID


def do_import(df, elo_service, base_path, separator):
    tqdm.pandas(file=sys.stdout)
    df.progress_apply(lambda row: create_sord_singlethreaded(row, elo_service, base_path, separator), axis=1)


def main():
    elo_service = load_elo_service()
    df = load_dataset()
    base_path = "¶Sales¶PythonExampleDataImport2"
    separator = "¶"
    do_import(df, elo_service, base_path, separator)


if __name__ == "__main__":
    main()
