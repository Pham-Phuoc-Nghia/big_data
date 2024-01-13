import json
import sys

json_data, res_data = [], []

def parse(line_from_lines):
    for line in line_from_lines:
        new_line = line.split("\n")[0].replace("'", "\"")
        json_data.append(json.loads(new_line))

def work():
    for element in json_data:
        local_array = {"location": element["location"],
                       "result": (element["values"]["total_diff"] / element["values"]["days_count"])}
        res_data.append(local_array)

def show():
    for element in res_data:
        print('{:<15} {:<15}'.format(element['location'],element['result']))

def save_to_json(output_file_path):
    with open(output_file_path, "w") as file:
        json.dump(res_data, file)

parse(line_from_lines=sys.stdin)
work()
save_to_json(output_file_path="./Out/red.json")
show()