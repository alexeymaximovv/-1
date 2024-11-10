
import csv
import json

def csv_to_json(file_path, delimiter=',', line_terminator='\n'):
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        data = [row for row in reader]
    json_output = json.dumps(data, indent=4)

    print(json_output)

file_path = 'input.csv'
csv_to_json(file_path)
