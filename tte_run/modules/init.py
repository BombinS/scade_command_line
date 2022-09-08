import os, logging, shutil
import config

def cleanup_and_setup():

    log_filename = config.tte_run_log

    # удаление предыдущего лога
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)

    # удаление предыдущих результатов
    for root, dirs, files in os.walk(config.path_to_test_folder):
        for dir in dirs:
            if '_auto_results' in dir.lower():
                path = os.path.join(root,dir)
                logging.info(f'remove {path}')
                shutil.rmtree(path)



    



