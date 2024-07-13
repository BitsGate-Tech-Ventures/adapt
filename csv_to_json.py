import csv
import json

# Function to convert CSV to JSON
def csv_to_json(csv_file_path, json_file_path):
    data = {}
    
    # Read the CSV file
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Iterate over each row and populate the data dictionary
        for row in csv_reader:
            command = row['Command']
            data[command] = {
                'Description': row['Description'],
                'Details': row['Details']
            }
    
    # Write the data dictionary to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Paths to the input CSV file and output JSON file
csv_file_path = 'nmap_commands_1.csv'
json_file_path = 'nmap_commands_1.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)
