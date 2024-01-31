from google.cloud import storage
from pypdf import PdfReader
from utils_gemini import generate_text
from utils_config import PROJECT_ID, LOCATION
from utils_storage_object_metadata import set_blob_metadata
import os
import tempfile


storage_client = storage.Client()

def extract_pdf_images(blob_name, bucket_name):
    bucket = storage_client.bucket(bucket_name)
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = temp_dir.name + "/"
    
    if (blob_name.endswith(".pdf")):
        blob = bucket.blob(blob_name)
        path = f"{temp_dir_path}content.pdf"
        blob.download_to_filename(path)
        reader = PdfReader(path)
        for page in reader.pages:
            page_count = 0
            for image in page.images:
                path = f"{temp_dir_path}page{str(page_count)}_{image.name}"
                with open(path, "wb") as fp:
                    fp.write(image.data)
                    page_count += 1
    return temp_dir


def parse_each_image(dir_path, prompt_text) -> dict:
    path = dir_path.name + "/"
    list_dir = os.listdir(path)
    dir_png_files = [file for file in list_dir if file.endswith(".png")]
    total_files = len(dir_png_files)
    metadata_dict = {"total_images": total_files}
    max_attempts = 5

    for count, file in enumerate(dir_png_files):
        filename = os.fsdecode(file)
        file_path = os.path.join(path, filename)
        # print(f"parsing image file ({count+1}/{total_files+1}) in: ", file_path)
        attempt = 0
        while attempt < max_attempts:
            try:
                response = generate_text(PROJECT_ID, LOCATION, prompt_text, file_path)
                break
            except Exception as e:
                print(f"Error: {e} (trying again)")
                attempt += 1
        metadata_dict[f'image_{count}'] = response
    
    dir_path.cleanup()
    return metadata_dict


def iterate_pdfs(bucket_name, prompt_text):
    blobs = storage_client.list_blobs(bucket_name)
    blobs_name = [blob.name for blob in blobs if blob.name.endswith(".pdf") and not blob.metadata.get("total_images", "")]
    total_files = len(blobs_name)

    for count, blob_name in enumerate(blobs_name):
        print(f"Saving metadata in blob: '{blob_name}' ({count+1}/{total_files})")
        dir = extract_pdf_images(blob_name, bucket_name)
        metadata = parse_each_image(dir, prompt_text)
        set_blob_metadata(bucket_name, blob_name, metadata)
