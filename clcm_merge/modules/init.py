import os, logging, shutil
import config

def cleanup_and_setup():
    
    # удаление предыдущего лога
    log_filename = config.clcm_merge_log
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)

    # очистка временной директории сбора общего покрытия
    temp_coverage_directory = os.path.join(os.curdir, config.clcm_temp_directory)
    if os.path.exists(temp_coverage_directory):
        shutil.rmtree(temp_coverage_directory)
    os.mkdir(temp_coverage_directory)

    # удаление предыдущих результатов
    # for root, dirs, files in os.walk(config.path_to_test_folder):
    #     for dir in dirs:
    #         if '_Result' in dir:
    #             shutil.rmtree(os.path.join(root,dir))


    



