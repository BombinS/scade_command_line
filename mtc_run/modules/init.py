import os, logging, shutil
import config

def cleanup_and_setup():

    log_filename = config.tte_run_log

    # удаление предыдущего лога
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)



    



