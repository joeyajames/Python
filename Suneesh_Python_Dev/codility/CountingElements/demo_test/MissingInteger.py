import os

def solution(A):
    A.sort()

    lowest_number = 1

    for num in A:
        if num >= 1_000_000 or num <= -1_000_000:
            continue
        if num == lowest_number:
            lowest_number += 1

    return lowest_number


def get_file_data(file_name):
    # Check if the file exists
    if os.path.exists(file_name):
        # Read input from the file
        with open(file_name, 'r') as file:
            return list(map(int, file.readline().strip().split(',')))
    else:
        raise FileNotFoundError(f"File {file_name} not found")


try:
    input_array = get_file_data('test-input.txt')

    if len(input_array) > 0:
        print(input_array)
        # Call the solution function with the input array
        result = solution(input_array)

        # Print the result
        print(result)

except Exception as e:
    print(e)
