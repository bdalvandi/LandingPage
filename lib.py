import json

# get the value from a nested dictionary given a path
def get_value_from_path(data, path):
    for key in path:
        data = data[key]
    return data


# find the path to a specific key in a nested dictionary
def find_path_to_key(d, target_key, path=None):
    if path is None:
        path = []

    if isinstance(d, dict):
        for key, value in d.items():
            new_path = path + [key]
            if key == target_key:
                return new_path
            if isinstance(value, (dict, list)):
                result = find_path_to_key(value, target_key, new_path)
                if result:
                    return result
    elif isinstance(d, list):
        for index, item in enumerate(d):
            new_path = path + [index]
            if isinstance(item, (dict, list)):
                result = find_path_to_key(item, target_key, new_path)
                if result:
                    return result
    return None



    
