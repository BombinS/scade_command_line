#!/usr/bin/env python

import config, validate, process, init

def job_failed():
    print('Process has failed')
    exit()        

def main():

    # очистка и инициализация логера
    init.cleanup_and_setup()
    
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
    
    # получить общий отчет
    command = process.get_command(config.tte_report_results, test_results_file, config.author)
    status_info = process.execute(command)
    for info in status_info:
        print(info)

if __name__ == '__main__':
    main()
