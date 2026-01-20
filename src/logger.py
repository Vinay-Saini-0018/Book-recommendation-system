import os
import logging
from datetime import datetime

file_name = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
# Get the parent directory of the src folder (project root)
logs_main_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"Logs")
logs_dir = os.path.join(logs_main_dir,datetime.now().strftime('%y_%m_%d'))

print(f"Creating logs directory: {logs_dir}")
os.makedirs(logs_dir,exist_ok=True)
print(f"Logs directory created successfully")

log_file_path = os.path.join(logs_dir,file_name)

logging.basicConfig(filename=log_file_path,level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

'''print(logs_dir)
print(logs_main_dir)
print(file_name)'''