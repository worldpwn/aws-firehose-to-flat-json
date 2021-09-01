import json


def flatten_json_array(array):
    """
    It will convert an array of objects into flatten data.
    As soon as it hit nested data it will be JSON stringified.

    Parameters:
    array: array of objects
    """
    result = []
    for item in array:
        flat_item = flatten_json_object(item)
        result.append(flat_item)
    return result


def flatten_json_object(item):
    """
    It will convert the object into flatten data.
    As soon as it hit nested data it will be JSON stringified.
    """
    global currentLevel
    currentLevel = 0
    result = {}

    def flatten(x, name=""):
        global currentLevel
        print("currentLevel", currentLevel)
        print(name, x)
        if currentLevel == 2:
            """In this case, we stop the flattening and will JSON stringify"""
            result[name[:-1]] = json.dumps(x)
        elif type(x) is dict:
            """If the object has properties continue flattening"""
            currentLevel = currentLevel + 1
            for a in x:
                flatten(x[a], name + a + "_")
        else:
            """Stop flattening"""
            currentLevel = 0
            result[name[:-1]] = x

    flatten(item)
    return result
