import json

def extract_values(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        
    values = []
    extract_values_recursive(data, values)
    
    return values

def extract_values_recursive(data, values):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                extract_values_recursive(value, values)
            else:
                values.append(value)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                extract_values_recursive(item, values)
            else:
                values.append(item)
                
def find_missing_items(source_file, target_file, output_file):
    with open(source_file, 'r') as src, open(target_file, 'r') as tgt:
        source_lines = src.readlines()
        target_lines = tgt.readlines()

    source_items = set(source_lines[2::4])
    target_items = set(target_lines)

    missing_items = source_items - target_items

    with open(output_file, 'w') as out:
        for item in missing_items:
            out.write(item.strip() + '\n')

    print("Scanning complete. Missing items saved to:", output_file)
    
# Specify the path to the JSON file
json_file = 'path/to/followers.json'

# Extract values from the JSON file
result = extract_values(json_file)

# Specify the path to the output file
output_file = 'path/to/followers.txt'

# Save the extracted values to a new file
with open(output_file, 'w') as f:
    for value in result:
        f.write(str(value) + '\n')

print("Followers extraction complete. Values saved to:", output_file)

# Specify the path to the JSON file
json_file = 'path/to/following.json'

# Extract values from the JSON file
result = extract_values(json_file)

# Specify the path to the output file
output_file = 'path/to/following.txt'

# Save the extracted values to a new file
with open(output_file, 'w') as f:
    for value in result:
        f.write(str(value) + '\n')

print("Following extraction complete. Values saved to:", output_file)

# Specify the paths to the source file, target file, and output file
target_file = 'path/to/followers.txt'
source_file = 'path/to/following.txt'
output_file = 'path/to/followDiff.txt'

# Find missing items and save them to the output file
find_missing_items(source_file, target_file, output_file)