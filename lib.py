# imports
from typing import Union


# get the value from a nested dictionary given a path
def get_value_from_path(d:dict, path:list) ->  Union[str, int]:
    for key in path:
        d = d[key]
    return d


# find the path to a specific key in a nested dictionary
def find_path_to_key(d:Union[dict, list], target_key:Union[str, int], path:list=None) -> list:
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



    
