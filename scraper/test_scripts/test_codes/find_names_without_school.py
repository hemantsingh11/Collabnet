import json

# Load the JSON data from a file
file_path = 'final_data1.json'  # Replace with your JSON file path

try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Count and collect names based on the presence and content of the 'school' key
    without_school_key = [entry['name'] for entry in data if 'school' not in entry]
    with_school_key = [entry['name'] for entry in data if 'school' in entry]
    with_school_key_not_empty = [entry['name'] for entry in data if 'school' in entry and entry['school'].strip()]

    # Display results
    print(f"Count of entries without 'school' key: {len(without_school_key)}")
    print(f"Count of entries with 'school' key: {len(with_school_key)}")
    print(f"Count of entries with 'school' key and not empty: {len(with_school_key_not_empty)}\n")

    print("Entries without 'school' key:")
    print(without_school_key)

    print("\nEntries with 'school' key:")
    print(with_school_key)

    print("\nEntries with 'school' key and not empty:")
    print(with_school_key_not_empty)

except FileNotFoundError:
    print("Error: JSON file not found. Please check the file path.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format. Please check the file content.")
