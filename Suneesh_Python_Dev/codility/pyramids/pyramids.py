def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


def decode(message_file):
    # Read the File
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create Dictionary for the message decoding
    dictionary = {}
    for line in lines:
        parts = line.split()
        dictionary[int(parts[0])] = parts[1]

    sorted_items = sorted(dictionary.items(), key=lambda x: x[0])
    sorted_numbers = [x[0] for x in sorted_items]
    staircase_list = create_staircase(sorted_numbers)

    # Create a decoding string
    decoded_message_string = ''

    # Variable to keep track of the line number
    line_number = 1

    # Iterate through each line of the Staircase/pyramid
    for line in staircase_list:
        # Get the last Element of the line
        element = line[-1]

        # Extract words corresponding to the selected numbers
        words_to_add = dictionary[element]

        # Add to the resultant String
        decoded_message_string += ' ' + words_to_add

        # Increment the line number for the next iteration
        line_number += 1

    return decoded_message_string


# Example usage:
message_file = "message.txt"
decoded_message = decode(message_file)
print(decoded_message)
