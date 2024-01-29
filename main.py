from utils_images_description import iterate_pdfs
import time


bucket_name_test = "brtecppar-search-dataset"
prompt_text = "Descreva a imagem de forma resumida sem perder o que há de relevante"


start_time = time.time()
iterate_pdfs(bucket_name_test, prompt_text)
end_time = time.time()

elapsed_time_seconds = end_time - start_time

minutes = int(elapsed_time_seconds // 60)
seconds = int(elapsed_time_seconds % 60)

print(f"Total operation time: {minutes} min {seconds} sec")