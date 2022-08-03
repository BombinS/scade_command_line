import os, shutil, logging

import config

def search_raw_test_result_files(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            name = file.lower()
            if '.txt' in name and '_raw' in name:
                result.append(os.path.abspath(os.path.join(root, file)))
    
    return result

def form_test_results_file(test_results):
    temp_directory = 'tmp'
    source_of_test_results = os.path.join(temp_directory,'source_of_test_results.txt')

    try:
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
        os.mkdir(temp_directory)

        f = open(source_of_test_results, 'w' ) 
        for test_result in test_results:   
            f.write(f'{test_result}\n')
        f.close()    

        logging.info(f'The file with all test results created as \"{source_of_test_results}\"')
        return True
    
    except:
        logging.error('Unexpected error due creation of file with all test results')
        return False
