#!/usr/bin/env python

import subprocess
import logging
import os

import config
import validate
import process

def job_failed():
    print('Process has failed')
    exit()        

def main():
    
    # очистка
    log_filename = 'tte_report.log'
    if (os.path.exists(log_filename)):   
        os.remove(log_filename)

    # инициализация логера
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)
    
    # валидация пути к директории Scade
    if validate.is_directory_exist(config.path_to_scade_bin) == False:
        job_failed()

    # валидация пути к директориям тестов
    if validate.is_directory_exist(config.path_to_test_results) == False:
        job_failed()

    # поиск результатов тестов, валидация поиска
    test_results = process.search_raw_test_result_files(config.path_to_test_results)
    if validate.is_test_results_exist(test_results) == False:
        job_failed()

    # сформировать файл с путями к raw файлам результатов
    test_results_file = process.form_test_results_file(test_results)
    if test_results_file == False:
        job_failed()
    
    # собрать общий отчет
    command = process.get_command(config.tte_report_results, test_results_file, 'bombin')
    print(command)

    print('Process completed successfully')

if __name__ == '__main__':
    main()
