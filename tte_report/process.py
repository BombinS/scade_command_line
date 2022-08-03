import os

def search_raw_test_result_files(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            name = file.lower()
            if '.txt' in name and '_raw' in name:
                result.append(os.path.join(root, file))
    return result