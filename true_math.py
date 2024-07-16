from math import inf
def divide(first, second):
    if first > 0 and second == 0:
        return inf
    elif first < 0 and second == 0:
        return -inf
    else:
        result = first/second
        return result

# if __name__ == '__main__':
#     divide()