import os, logging, shutil
import config

def cleanup_and_setup():
    
    # удаление предыдущего лога
    log_filename = config.clcm_merge_log
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)

    # очистка директории сбора общего покрытия
    coverage_directory = os.path.join(os.curdir, config.clcm_temp_directory)
    if os.path.exists(coverage_directory):
        shutil.rmtree(coverage_directory)
    os.mkdir(coverage_directory)

    # очистка временной директории сбора общего покрытия
    temp_coverage_directory = os.path.join(os.curdir, 'tmp')
    if os.path.exists(temp_coverage_directory):
        shutil.rmtree(temp_coverage_directory)
    os.mkdir(temp_coverage_directory)



    



