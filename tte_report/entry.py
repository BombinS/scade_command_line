#!/usr/bin/env python

import subprocess
import logging
import os

import config
import validate
import process

def process_failed():
    print('Process has failed')
    exit()        

def main():
    
    # очистка
    if (os.path.exists(config.log_filename)):   
        os.remove(config.log_filename)

    # инициализация логера
    logging.basicConfig(filename=config.log_filename, level=logging.DEBUG)
    
    # валидация пути к директории Scade
    if validate.is_directory_exist(config.path_to_scade_bin) == False:
        process_failed()

    # валидация пути к директориям тестов
    if validate.is_directory_exist(config.path_to_test_results) == False:
        process_failed()

    # поиск результатов тестов, валидация поиска
    test_results = process.search_raw_test_result_files(config.path_to_test_results)
    if validate.is_test_results_exist(test_results) == False:
        process_failed()

    # сформировать файл с путями к raw файлам результатов

    # собрать общий отчет

    print('Process completed successfully')

if __name__ == '__main__':
    main()
