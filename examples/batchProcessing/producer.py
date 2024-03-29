import pika
import pandas as pd
import sys
import json
import os


def connect_rabbitmq():
    if os.environ.get('RABBITMQ_HOST') is None:
        print("RABBITMQ_HOST is not set. using localhost")
        host = 'localhost'
    else:
        host = os.environ.get('RABBITMQ_HOST')
    print(f"Connecting to rabbitmq at {host}")

    # Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()

    # Declare a persistent queue
    channel.queue_declare(queue='sales-import-queue',
                          durable=True)

    return channel


def send_message(channel, message):
    # see note on persistence here: https://www.rabbitmq.com/tutorials/tutorial-two-python#note-on-message-persistence
    channel.basic_publish(exchange='', routing_key='sales-import-queue', body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=pika.DeliveryMode.Persistent
                          ))
    print(f" [x] Sent {message}")


def build_json_message(row):
    row = row[["SALE_NAME", "SALE_DATE_ELO", "SALE_PRODUCT", "SALE_AMOUNT"]]
    return json.dumps(row.to_dict())


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


def main():
    channel = connect_rabbitmq()
    df = load_dataset()
    for index, row in df.iterrows():
        message = build_json_message(row)
        send_message(channel, str(message))
    print(" [x] Done")
    sys.exit(0)


if __name__ == "__main__":
    main()
