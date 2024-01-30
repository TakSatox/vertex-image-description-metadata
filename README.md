
# PDF Embedded Images Description

This code parse every embedded image in each PDF file in a Cloud Storage Bucket using Gemini.

## Architecture
![ ](https://drive.google.com/uc?export=view&id=1drXGO1p3S0vYa8YZ-xoHY9fiV8d0sDDT)

## Getting Started

### Installing

* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt

### Setting Config Values

* open utils_config.py
* set project_id, location, bucket_name and prompt_text

### Running
* execute main.py