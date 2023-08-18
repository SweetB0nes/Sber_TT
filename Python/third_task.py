def max_concatenated_number(strings):

    strings.sort(key=lambda x: x * 10, reverse=True)

    return int(''.join(strings))


if __name__ == '__main__':

    string_list = ["11", "234", "005", "89"]

    result = max_concatenated_number(string_list)
    print(result)
