import os

PROJECT_ID = os.environ.get("PROJECT_ID", "poc-genia-hml")
LOCATION = os.environ.get("LOCATION", "us-central1")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "brtecppar-search-dataset")
PROMPT_TEXT = os.environ.get("PROMPT_TEXT", "Descreva a imagem de forma resumida sem perder o que há de relevante")
