
# PDF Embedded Images Description

This code parse every embedded image in each PDF file in a Cloud Storage Bucket using Gemini. If the PDF has "total_images" in custom metadata it will skip so when we upload more documents into cloud storage bucket the code won't parse everything again. It will parse only the new PDF files. If you want to parse again a specific PDF document, just delete the "total_image" from its custom metadata.

## Architecture
![ ](https://drive.google.com/uc?export=view&id=1drXGO1p3S0vYa8YZ-xoHY9fiV8d0sDDT)

## Getting Started

### Local Authentication
* gcloud auth login
* gcloud config set project {project_id}

### Installing

* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt

### Setting Config Values

* open utils_config.py
* set project_id, location, bucket_name and prompt_text

### Running
* execute main.py