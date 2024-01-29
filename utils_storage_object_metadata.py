from google.cloud import storage


def set_blob_metadata(bucket_name, blob_name, metadata_values):
    """Set a blob's metadata."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    metageneration_match_precondition = None

    # Optional: set a metageneration-match precondition to avoid potential race
    # conditions and data corruptions. The request to patch is aborted if the
    # object's metageneration does not match your precondition.
    metageneration_match_precondition = blob.metageneration

    metadata = metadata_values
    blob.metadata = metadata
    blob.patch(if_metageneration_match=metageneration_match_precondition)

    print(f"The metadata for the blob {blob.name} is {blob.metadata}")

set_blob_metadata("brtecppar-search-dataset", "Chip Corporativo.pdf")