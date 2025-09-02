import os, json, datetime
import requests
from azure.storage.blob import BlobServiceClient

AZ_CONN = os.getenv("AZURITE_CONNECTION_STRING",
    "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://host.docker.internal:10000/devstoreaccount1;")
RAW_CONTAINER = os.getenv("RAW_CONTAINER", "raw")
RAW_BLOB = os.getenv("RAW_BLOB", "sample.json")
CUR_CONTAINER = os.getenv("CURATED_CONTAINER", "curated")
CUR_BLOB = os.getenv("CURATED_BLOB", "processed.json")
SOURCE_URL = os.getenv("SOURCE_URL", "https://httpbin.org/json")

def ensure_container(bs, name):
    try:
        bs.create_container(name)
    except Exception:
        pass

def main():
    # 1) ADF 전처리 모사: HTTP에서 원천 데이터 수집 → raw에 적재(없으면 생성)
    bs = BlobServiceClient.from_connection_string(AZ_CONN)

    ensure_container(bs, RAW_CONTAINER)
    ensure_container(bs, CUR_CONTAINER)

    text = requests.get(SOURCE_URL, timeout=30).text
    bs.get_blob_client(RAW_CONTAINER, RAW_BLOB).upload_blob(text.encode(), overwrite=True)

    data = json.loads(text)
    # 2) 간단 전처리: 타임스탬프/길이 필드 추가
    enriched = {
        "ingested_at": datetime.datetime.utcnow().isoformat() + "Z",
        "source_len": len(text),
        "source_title": data.get("slideshow", {}).get("title", "n/a"),
        "raw_preview": text[:120]
    }
    bs.get_blob_client(CUR_CONTAINER, CUR_BLOB).upload_blob(
        json.dumps(enriched, ensure_ascii=False, indent=2).encode(),
        overwrite=True
    )
    print(f"OK: wrote {RAW_CONTAINER}/{RAW_BLOB} and {CUR_CONTAINER}/{CUR_BLOB}")

if __name__ == "__main__":
    main()
