import csv
import json

source_data = 'sales_data.txt'
json_file = 'sales.json'

# Read CSV File


def read_csv(source_data, json_file):
    csv_rows = []
    with open(source_data) as csv_file:
        reader = csv.DictReader(csv_file)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)

# Convert csv data into json


def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        f.write(json.dumps(data))


read_csv(source_data, json_file)