import os, logging

def cleanup_and_setup():
    
    # удаление предыдущего лога
    log_filename = 'tte_report.log'
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # удаление предыдущих результатов
    results_filename = 'tte_report_results.txt'
    if (os.path.exists(results_filename)):   
        os.remove(results_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)
