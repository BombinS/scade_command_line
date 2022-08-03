import os, shutil, logging, subprocess

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
    tte_report_tmp = os.path.join(temp_directory,'tte_report_tmp.txt')

    try:
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
        os.mkdir(temp_directory)

        f = open(tte_report_tmp, 'w' ) 
        for test_result in test_results:   
            f.write(f'{test_result}\n')
        f.close()    

        logging.info(f'The file with all test results created as \"{tte_report_tmp}\"')
        return tte_report_tmp
    
    except:
        logging.error('Unexpected error due creation of file with all test results')
        return False


def get_command(dst, src, author):
    executable = os.path.join(config.path_to_scade_bin,'QTEREPORT.exe')
    command = f'\"{executable}\" -out {dst} -files {src} -author {author}'
    return command

def execute(command):
    p = subprocess.run(command, capture_output=True, text=True)
    if (p.returncode != 0):
        logging.error(p.stderr)
        return
    else:
        return p.stdout.splitlines()