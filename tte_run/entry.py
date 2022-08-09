#!/usr/bin/env python

from modules import process, modify
import config

def main():
    # валидация директории тестов

    # валидация директории бинарников

    # валидация головной модели Scade

    # поиск проектов
    projects = process.search_etp_files(config.path_to_test_folder)
    
    # для каждого проекта
    for project in projects:
        
        # модификация проекта
        # modify.modify_ept_file(project)

        # поиск тестовой процедуры
        procedures = process.search_stp_files(project)

        # для каждой процедуры
        for procedure in procedures:
            # формирование команды
            command = process.get_command(config.path_to_scade_bin, config.path_to_root_model, procedure)

            # выполнение команды
            command_execution_result = process.execute_command(command)

    pass

if __name__ == '__main__':
    main()
