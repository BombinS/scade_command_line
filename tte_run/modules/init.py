import os, logging, shutil
import config

def cleanup_and_setup():
    
    # удаление предыдущего лога
    log_filename = config.tte_run_log
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # удаление предыдущих результатов
    for root, dirs, files in os.walk(config.path_to_test_folder):
        for dir in dirs:
            if '_Result' in dir:
                shutil.rmtree(os.path.join(root,dir))

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)

    



