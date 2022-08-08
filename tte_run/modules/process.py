import os

def search_etp_files(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            name = file.lower()
            if '.etp' in name and not '_result.etp' in name:
                result.append(os.path.abspath(os.path.join(root, file)))

    return result


def search_stp_files(path):
    result = []

    search_directory = os.path.dirname(path)
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            name = file.lower()
            if '.stp' in name and not '\\gen\\':
                result.append(os.path.abspath(os.path.join(root, file)))

    return result