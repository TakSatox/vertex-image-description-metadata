from utils_images_description import iterate_pdfs
from utils_config import BUCKET_NAME, PROMPT_TEXT
import time


start_time = time.time()
iterate_pdfs(BUCKET_NAME, PROMPT_TEXT)
end_time = time.time()

elapsed_time_seconds = end_time - start_time

minutes = int(elapsed_time_seconds // 60)
seconds = int(elapsed_time_seconds % 60)

print(f"Total operation time: {minutes} min {seconds} sec")