import os
import logging

def is_directory_exist(path):
    status = os.path.exists(path)
    if status == False:
        logging.error(f"The path \"{path}\" isn't exist. Check the config file.")
    else:
        logging.info(f"The path \"{path}\" successfully recognized.")
    return status