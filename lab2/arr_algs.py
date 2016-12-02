def min_1(list):
    result = list[0]
    for i in range(1, len(list)):
        if list[i] < result:
            result = list[i]
    return result


print(min_1([3, 5, 6, 2, 60, 23, 547, 12, 2]))