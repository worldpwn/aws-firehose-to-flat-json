
import json


def flatten_json_array(array):
    """
    It will convert an array of objects into flatten data up to 2n level deep. 
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
    Here we receive the object and the level at which we will stringify it. 
    It will flatten up to level 2 and then convert data to JSON stringify
    """
    result = {}

    print(item)
    if type(item) is dict:
        for p in item:
            firstLevelProp = item[p]
            if type(firstLevelProp) is dict:
                for x in firstLevelProp:
                    secondLevelProp = firstLevelProp[x]
                    name = p + '_' + x 
                    if type(secondLevelProp) is dict:
                        result[name] = json.dumps(secondLevelProp)
                        value =  json.dumps(secondLevelProp)
                        print(p + '_' + x + ': ' + json.dumps(secondLevelProp))
                    else:
                        result[name] = secondLevelProp
                        print(p + '_' + x + ': ' + str(secondLevelProp))
            else:
                result[p] = firstLevelProp
                print(p + ': ' + str(firstLevelProp))

    return result
