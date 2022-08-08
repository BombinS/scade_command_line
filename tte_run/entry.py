#!/usr/bin/env python

from modules import process
import config

def main():
    # валидация директории тестов

    # валидация директории бинарников

    # валидация головной модели Scade

    # поиск проектов
    dummy = process.search_etp_files(config.path_to_test_folder)
    print(dummy)
    
    # для каждого проекта

        # модификация проекта

        # поиск тестовой процедуры

        # для каждой процедуры

            # формирование команды

            # выполнение команды

    pass

if __name__ == '__main__':
    main()
