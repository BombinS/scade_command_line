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

        # поиск тестовой процедуры
        procedures = process.search_stp_files(project)
        number_of_procedures = len(procedures)

        # для каждой процедуры
        nn = 1
        for procedure in procedures:

            # прогресс
            print('----------------------------------------------------------------------------------------------------------------------------')
            print(f'project {n}/{number_of_projects} procedure {nn}/{number_of_procedures}')
            print(f'{project} {procedure}', flush=True)

            # формирование команды
            command = process.get_command(config.path_to_scade_bin, config.path_to_root_model, procedure)

            # выполнение команды
            process.execute_command(command)
            nn = nn + 1

        n = n + 1

if __name__ == '__main__':
    main()
