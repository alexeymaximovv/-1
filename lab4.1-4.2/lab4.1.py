import json

def calculate_sum_of_products(file_path) -> float:
    with open(file_path, 'r') as file:
        data = json.load(file)

    sum_values = sum([item["score"] * item["weight"] for item in data])

    return round(sum_values, 3)

file_path = 'input.json'
result = calculate_sum_of_products(file_path)
print(result)
