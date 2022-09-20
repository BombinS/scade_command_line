#!/usr/bin/env python

from modules import process, init
import config

def main():
    # чистка и инициализация логера
    init.cleanup_and_setup()

    # валидация директории тестов

    # валидация директории бинарников

    # валидация головной модели Scade

    # поиск покрытий по модели
    coverage_files = process.search_coverage_files(config.path_to_test_folder)
    amount_of_coverage_files = len(coverage_files)

    # для каждого проекта
    n = 1
    for i in range(0, amount_of_coverage_files - 1):
        # прогресс
        print('----------------------------------------------------------------------------------------------------------------------------')
        print(f'iteration {n}/{amount_of_coverage_files - 1}')

        # формирование команды
        command = process.get_command(config.path_to_scade_bin, config.path_to_root_model, config.mtc_temp_directory, coverage_files[i], coverage_files[i+1])
        print(command)

        # выполнение команды
        process.execute_command(command)

        # перемещение результатов последнего слияния
        process.move_results(config.mtc_temp_directory)

        n += 1

    
if __name__ == '__main__':
    main()
