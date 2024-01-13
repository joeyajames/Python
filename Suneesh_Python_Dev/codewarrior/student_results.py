def possibly_perfect(key, answers):
    if len(key) != len(answers):
        return False

    correct_answer_list = []
    for answer, expected_answer in zip(answers, key):
        if expected_answer == '_':
            continue

        if answer == expected_answer:
            correct_answer_list.append(True)
        else:
            correct_answer_list.append(False)

    if (len(correct_answer_list) == correct_answer_list.count(True)
            or len(correct_answer_list) == correct_answer_list.count(False)):
        return True
    else:
        return False


print(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']))
print(possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C']))
print(possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T']))
