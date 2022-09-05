#!/usr/bin/env python

from modules import process, init
import config

def main():
    # чистка и инициализация логера
    init.cleanup_and_setup()

    # валидация директории тестов

    # валидация директории бинарников

    # валидация головной модели Scade

    # поиск проектов
    projects = process.search_coverage_files(config.path_to_test_folder)
    number_of_projects = len(projects)

    # для каждого проекта
    n = 1
    for i in range(0, number_of_projects - 1):
        # прогресс
        print('----------------------------------------------------------------------------------------------------------------------------')
        print(f'project {n}/{number_of_projects}')

        # формирование команды
        command = process.get_command(config.path_to_scade_bin, config.path_to_root_model, config.clcm_temp_directory, projects[i], projects[i+1])
        print(command)

        # выполнение команды
        process.execute_command(command)

        # перемещение результатов последнего слияния
        process.move_results(config.clcm_temp_directory)

        n += 1

    
if __name__ == '__main__':
    main()
