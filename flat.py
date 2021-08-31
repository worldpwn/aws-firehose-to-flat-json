
# Will flatten the json array


def flatten_json_array(array):
    result = []
    for item in array:
        flat_item = flatten_json_object(item)
        result.append(flat_item)
    return result

# Will flatten json object


def flatten_json_object(y):
    result = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            result[name[:-1]] = x

    flatten(y)
    return result
