import requests, os
from azure.storage.blob import BlobServiceClient
CONN = os.getenv("AZURITE_CONN", "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;")
URL = os.getenv("SOURCE_URL", "https://httpbin.org/get")
CONTAINER = os.getenv("CONTAINER", "raw")
BLOB_NAME = os.getenv("BLOB_NAME", "sample.json")
def main():
    bs = BlobServiceClient.from_connection_string(CONN)
    try: bs.create_container(CONTAINER)
    except Exception: pass
    data = requests.get(URL, timeout=30).text.encode()
    bs.get_blob_client(CONTAINER, BLOB_NAME).upload_blob(data, overwrite=True)
    print(f"Uploaded to {CONTAINER}/{BLOB_NAME}")
if __name__ == "__main__":
    main()
