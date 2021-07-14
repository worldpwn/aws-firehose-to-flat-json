import json

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
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            result[name[:-1]] = x

    flatten(y)
    return result

# Open example file
file = open("firehose-file-example.json", "r")
# Convert it to array
json_array = json.load(file)
# Flatten it with functions above
result = flatten_json_array(json_array)

# Write result to json
with open('result-from-script.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)


