import os, subprocess, logging, datetime

def search_etp_files(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            name = file.lower()
            if '.etp' in name and not '_result.etp' in name and not '_results.etp' in name :
                result.append(os.path.abspath(os.path.join(root, file)))

    return result


def search_stp_files(path):
    logging.info('------------------------------------------------------------------------------------------------------')
    logging.info(f'found test project {path}')
    result = []

    search_directory = os.path.dirname(path)
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            name = file.lower()
            if '.stp' in name:
                fullname = os.path.abspath(os.path.join(root, file))
                if not '\\gen\\' in fullname:
                    result.append(fullname)
                    logging.info(f'found test procedure {fullname}')

    return result


def get_command(scade_bin, root_model, procedure):
    result_directory = os.path.splitext(procedure)[0]+'_Auto_Results'
    result_directory = os.path.join(result_directory,'QTE_TEE')
    scade_executable = os.path.join(scade_bin, 'QTE.exe')
    command = f'\"{scade_executable}\" -tee -tee:nobuild -conf "KCG" -test_file \"{procedure}\" -target_dir \"{result_directory}\" \"{root_model}\"'
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