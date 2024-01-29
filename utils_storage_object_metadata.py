from google.cloud import storage

def set_blob_metadata(bucket_name: str, blob_name: str, metadata_values: dict):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    metageneration_match_precondition = None

    metageneration_match_precondition = blob.metageneration

    metadata = metadata_values
    blob.metadata = metadata
    blob.patch(if_metageneration_match=metageneration_match_precondition)

    print(f"The metadata for the blob '{blob.name}' was set succesfully")