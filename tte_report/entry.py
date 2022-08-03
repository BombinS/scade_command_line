#!/usr/bin/env python

import subprocess
import logging
import os

import config
import validate

def main():
    
    # очистка
    if (os.path.exists(config.log_filename)):   
        os.remove(config.log_filename)

    # инициализация логера
    logging.basicConfig(filename=config.log_filename, level=logging.DEBUG)
    
    # валидация пути к директории Scade
    if validate.is_directory_exist(config.path_to_scade_bin) == False:
        print('Process failed')
        exit()

    # валидация пути к директориям тестов
    if validate.is_directory_exist(config.path_to_test_results) == False:
        print('Process failed')
        exit()

    # поиск результатов тестов

    # валидация поиска результатов тестов

    # сформировать файл с путями к raw файлам результатов

    # собрать общий отчет

if __name__ == '__main__':
    main()
