import os, subprocess, logging, datetime, shutil
from posixpath import splitext

def search_coverage_files(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            name = file.lower()
            if '.crf' in name:
                fullname = os.path.abspath(os.path.join(root, file))
                if '_Auto_Results' in fullname:
                    result.append(os.path.abspath(os.path.join(root, file)))

    return result


def get_command(scade_bin, root_model, temp_coverage_directory,  coverage1, coverage2):
    temp_coverage_directory = os.path.abspath(os.path.join(os.curdir, temp_coverage_directory))
    temp_directory = os.path.abspath(os.path.join(os.curdir,'tmp'))
    scade_executable = os.path.join(scade_bin, 'SCADE.EXE')
    if not os.listdir(temp_coverage_directory):
        print('first')
        command = f'\"{scade_executable}\" -mtc_merge \"{root_model}\" -cov_files \"{coverage1}\" \"{coverage2}\" -target_dir \"{temp_directory}\" '
    else:
        print('second')
        merged_coverage = ''
        for root, dirs, files in os.walk(temp_coverage_directory):
            for file in files:
                name = file.lower()
                if 'merged.crf' in name:
                    merged_coverage = os.path.abspath(os.path.join(root, file))
        command = f'\"{scade_executable}\" -mtc_merge \"{root_model}\" -cov_files \"{merged_coverage}\" \"{coverage2}\" -target_dir \"{temp_directory}\" '

    return command


def execute_command(command):
    logging.info(f'execute command: {command}')
    t1 = datetime.datetime.now()
    p = subprocess.run(command, capture_output=True, text=True)    
    t2 = datetime.datetime.now()
    delta = t2 - t1
    logging.info(f'elapsed time: {delta.seconds} seconds')
    
    if p.returncode != 0:
        print(p.stderr, flush=True)
        logging.error('failure')
    else:
        logging.info('success')

def move_results(temp_coverage_directory):
    shutil.rmtree(temp_coverage_directory)
    shutil.move('tmp', temp_coverage_directory)
    os.mkdir('tmp')