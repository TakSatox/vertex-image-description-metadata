from google.cloud import storage
from pypdf import PdfReader
# from utils_gemini_image_parser import generate_text
import tempfile

storage_client = storage.Client()

def extract_pdf_images(blob_name, bucket_name):
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir = "./images"
    bucket = storage_client.bucket(bucket_name)

    if (blob_name.endswith(".pdf")):
        blob = bucket.blob(blob_name)
        path = f"{temp_dir}/content.pdf"
        blob.download_to_filename(path)
        reader = PdfReader(path)
        for page in reader.pages:
            page_count = 0
            for image in page.images:
                path = f"{temp_dir}/page{str(page_count)}_image{image.name}"
                with open(path, "wb") as fp:
                    fp.write(image.data)
                    page_count += 1
    
    return temp_dir.name

# def parse_each_image(dir_path):
#     prompt_text = "Descreva a imagem deste prompt de forma detalhada"
#     response = generate_text()

    
        


# def iterate_pdfs(bucket_name):
#     blobs = storage_client.list_blobs(bucket_name)
    
#     for blob in blobs:
#         extract_pdf_images(blob, bucket_name)