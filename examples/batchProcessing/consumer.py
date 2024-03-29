import pika
from eloservice.elo_service import EloService
from decouple import AutoConfig
import json
import os


def load_elo_service():
    config = AutoConfig(search_path='./')  # load .env file from current directory with connection details
    rest_baseurl = config("TEST_ELO_IX_URL")
    rest_user = config("TEST_ELO_IX_USER")
    rest_password = config("TEST_ELO_IX_PASSWORD")
    return EloService(url=rest_baseurl, user=rest_user, password=rest_password)


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


def connect_rabbitmq():
    if os.environ.get('RABBITMQ_HOST') is None:
        print("RABBITMQ_HOST is not set. using localhost")
        host = 'localhost'
    else:
        host = os.environ.get('RABBITMQ_HOST')
    # Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)

    # Declare a persistent queue
    channel.queue_declare(queue='sales-import-queue', durable=True)

    return channel


def consume_message(channel, elo_service, base_path, separator):
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        create_sord_singlethreaded(row=json.loads(body),
                                   elo_service=elo_service,
                                   base_path=base_path,
                                   separator=separator)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='sales-import-queue', on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def main():
    elo_service = load_elo_service()
    base_path = "¶Sales¶PythonExampleDataImport3"
    separator = "¶"
    channel = connect_rabbitmq()
    consume_message(channel, elo_service, base_path, separator)


if __name__ == "__main__":
    main()
