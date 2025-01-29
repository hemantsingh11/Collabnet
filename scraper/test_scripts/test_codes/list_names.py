# ## Total count 

import json

def load_json(file_path):
    """ Load JSON data from a file """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_name_format(name):
    """ Convert name from 'Last, First' to 'First Last' format """
    parts = name.split(", ")
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

def count_json_objects(data):
    """ Count the total number of JSON objects in the dataset """
    return len(data)

def check_coauthors_of_coauthors(data, target_name):
    """ Check which co-authors of co-authors are present and missing """
    # Find the target entry
    target_entry = next((entry for entry in data if entry["name"] == target_name), None)

    if not target_entry or "co_author_details" not in target_entry:
        return None, None

    # Extract co-authors of co-authors and convert names
    co_authors_of_co_authors = [
        convert_name_format(author["Name"]["value"]) 
        for author in target_entry["co_author_details"].get("Co-Authors of Co-Authors", [])
    ]

    # Extract all names in the JSON data with formatted name style
    existing_names = {convert_name_format(entry["name"]) for entry in data}

    # Determine which co-authors are present or missing
    present = [name for name in co_authors_of_co_authors if name in existing_names]
    missing = [name for name in co_authors_of_co_authors if name not in existing_names]

    return present, missing

def main(json_path, target_name):
    """ Main function to process the JSON file """
    data = load_json(json_path)
    total_count = count_json_objects(data)
    present_coauthors, missing_coauthors = check_coauthors_of_coauthors(data, target_name)

    print(f"Total JSON objects: {total_count}")

    if present_coauthors is None:
        print(f"No entry found for '{target_name}' or co-author details are missing.")
    else:
        print("\nCo-Authors of Co-Authors Present in Data:")
        for name in present_coauthors:
            print(name)
        
        print("\nCo-Authors of Co-Authors NOT Present in Data:")
        for name in missing_coauthors:
            print(name)

# Example usage
json_file_path = 'final_data1 copy.json'  # Replace with your JSON file path
target_person = 'Huimin Cheng'  # Replace with the target name you want to check

main(json_file_path, target_person)




# ## List of names below huiming cheng

# import json

# def load_json(file_path):
#     """ Load JSON data from a file """
#     with open(file_path, 'r', encoding='utf-8') as f:
#         return json.load(f)

# def get_names_after_target(data, target_name):
#     """ Get all 'name' values from JSON objects that appear after the target object """
#     names = []
#     found_target = False

#     for entry in data:
#         if found_target:
#             if "name" in entry:
#                 names.append(entry["name"])
#         if entry.get("name") == target_name:
#             found_target = True

#     return names

# def main(json_path, target_name):
#     """ Main function to process the JSON file """
#     data = load_json(json_path)
#     names_after_target = get_names_after_target(data, target_name)

#     if names_after_target:
#         print(f"Names in the JSON objects after '{target_name}':")
#         for name in names_after_target:
#             print(name)
#     else:
#         print(f"No JSON objects found after '{target_name}'.")

# # Example usage
# json_file_path = 'final_data3copy.json'  # Replace with your JSON file path
# target_person = 'Huimin Cheng'  # Replace with the target name you want to check

# main(json_file_path, target_person)



# ### school of public health professor names

# import json

# # Load JSON data from a file
# def get_names_by_school(file_path, target_school):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     # Extract names where school matches the target school
#     filtered_names = [item["name"] for item in data if item.get("school") == target_school]

#     return filtered_names

# # File path to your JSON file
# file_path = 'final_data2copy.json'  # Replace with your actual file path
# target_school = "Boston University School of Public Health"

# # Get names
# names_list = get_names_by_school(file_path, target_school)

# # Print the names
# print("Names of individuals from the target school:")
# for name in names_list:
#     print(name)
