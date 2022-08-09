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
    projects = process.search_etp_files(config.path_to_test_folder)
    number_of_projects = len(projects)

    # для каждого проекта
    n = 1
    for project in projects:

        # прогресс
        print('----------------------------------------------------------------------------------------------------------------------------')
        print(f'project {n}/{number_of_projects}')
        print(project, flush=True)
        
        # поиск тестовой процедуры
        procedures = process.search_stp_files(project)

        # для каждой процедуры
        for procedure in procedures:
        
            # формирование команды
            command = process.get_command(config.path_to_scade_bin, config.path_to_root_model, procedure)

            # выполнение команды
            process.execute_command(command)
            n += 1

    
if __name__ == '__main__':
    main()
