import json
import datetime
import sys
from itertools import groupby

csv_data, temp_data, res_data = [], [], []

def parse(lines_from_file):
    for index, line in enumerate(lines_from_file):
        if index != 0:
            local_dict = {
                            "location": line.split(";")[2],
                            "date": line.split(";")[3],
                            "total_cases": line.split(";")[4]
                         }
            csv_data.append(local_dict)
            
def get_data():
    locations, dates, total_cases = [], [], []
    for element in csv_data:
        locations.append(element["location"])
        dates.append(element["date"])
        total_cases.append(element["total_cases"])

    temp_data = list(zip(locations, dates, total_cases))
    keyfunc = lambda x: x[0]

    for location, action in groupby(temp_data, key=keyfunc):
        model = {}
        init_values= []
        for _, date, total in action:
            values_model = {"date": date, "total_cases": total}
            init_values.append(values_model)
        last_date = datetime.datetime.strptime(init_values[-1]["date"], "%Y-%m-%d")
        first_date = datetime.datetime.strptime(init_values[0]["date"], "%Y-%m-%d")
        days_count = (last_date - first_date).days
        last_total = int(init_values[-1]["total_cases"])
        first_total = int(init_values[0]["total_cases"])
        total_diff = last_total - first_total
        if len(init_values) > 1:
            model["location"] = location
            model["values"] = {"days_count": days_count, "total_diff": total_diff}
            res_data.append(model)

def show():
    for element in res_data:
        print(element)

def save_to_json(output_file_path):
    with open(output_file_path, "w") as file:
        json.dump(res_data, file)

parse(lines_from_file=sys.stdin)
get_data()
save_to_json(output_file_path="./Out/map.json")
show()