import os
import logging

def is_directory_exist(path):
    status = os.path.exists(path)
    if status == False:
        logging.error(f"The path \"{path}\" isn't exist. Check the config file.")
    else:
        logging.info(f"The path \"{path}\" successfully recognized.")
    return status

def is_test_results_exist(results):
    status = len(results) != 0
    if status == False:
        logging.error("Test results not found")
    else:
        logging.info(f"Found {len(results)} test results.")
    return status
