import json


def flatten_json_array(array, stringifyLevel):
    """
    It will convert an array of objects into flatten data.
    Use stringifyLevel to set the level at which the rest of the data will be JSON stringify.

    Parameters:
    array: array of objects
    stringifyLevel: the level at which we will stop the flattening recursion and convert the rest data into JSON stringify
    """
    result = []
    for item in array:
        flat_item = flatten_json_object(item, stringifyLevel)
        result.append(flat_item)
    return result


def flatten_json_object(item, stringifyLevel):
    """
    Here we receive the object and the level at which we will stringify it.
    We set the current level to zero and start recursion.
    """
    global currentLevel
    currentLevel = 0
    result = {}

    def flatten(x, name=""):
        global currentLevel
        if currentLevel == stringifyLevel:
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
