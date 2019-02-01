
def add_two(v1,v2):
    p = v1+v2

    return p


def min_find(num_list):
    min = num_list[0]
    for i in num_list:
        if i <= min:
            min = i

    return min


def max_find(num_list):
    max = num_list[0]
    for i in num_list:
        if i >= max:
            max = i

    return max
