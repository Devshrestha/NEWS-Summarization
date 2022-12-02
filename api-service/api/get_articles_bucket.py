import os
from google.cloud import storage
from pathlib import Path


gcp_project = os.environ["GCP_PROJECT"]
bucket_name = "news-storage"
persistent_folder = "/app/persistent"


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""

    storage_client = storage.Client(project=gcp_project)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

def download_folder(bucket_name,prefix):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        if blob.name.endswith("/"):
            continue
        file_split = blob.name.split("/")
        directory = "/".join(file_split[0:-1])
        Path(directory).mkdir(parents=True, exist_ok=True)
        blob.download_to_filename(blob.name) 
print(gcp_project)

# Test access
if __name__ =="__main__":
    article_folder = "persistent-folder/articles"
    #download_blob(bucket_name, article_folder,os.path.join(persistent_folder))
    download_folder(bucket_name,article_folder)