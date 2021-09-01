from flat import flatten_json_array
import json

# Open example file
file = open("firehose-file-example.json", "r")
# Convert it to array
json_array = json.load(file)

# Flatten it with functions above
result = flatten_json_array(json_array)

# Write result to json
with open("result-from-script.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
