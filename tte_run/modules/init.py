import os, logging
import config

def cleanup_and_setup():
    
    # удаление предыдущего лога
    log_filename = config.tte_run_log
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)


