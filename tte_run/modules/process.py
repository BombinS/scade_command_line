import os

def search_etp_files(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            name = file.lower()
            if '.etp' in name:
                result.append(os.path.abspath(os.path.join(root, file)))

    return result