from flask import Flask, request, jsonify

app = Flask(__name__)

numbers = []


@app.route('/add', methods=['POST', 'PUT'])
def add_number():
    global numbers
    number = request.json
    if not isinstance(number, int):
        return "Invalid number provided", 400
    numbers.append(number)
    return f"Number {number} added successfully", 201


@app.route('/get', methods=['GET'])
def get_numbers():
    global numbers
    sorted_numbers = sort_ascending_without_comparators(numbers)
    return jsonify(sorted_numbers)


def sort_ascending_without_comparators(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


if __name__ == '__main__':
    app.run(debug=True)
