def solution(num_list):
    print(num_list)
    list.sort(num_list, key=int)
    print(num_list)
    lis_size = len(num_list)
    try:
        for x in range(lis_size)[::2]:
            if num_list[x] != num_list[x+1]:
                return num_list[x]
    except IndexError as e:
        return num_list[x]

print(solution([1,2,3,"4",5,4,3,2,1]))
