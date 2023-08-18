def makeGoodNumbers(input_string):
    def make_good_number(left_part, right_part):
        if 2 <= len(left_part) <= 4 and 2 <= len(right_part) <= 5:
            return f"{left_part.zfill(4)}/{right_part.zfill(5)}"
        else:
            return "Некорректный формат номера"

    good_numbers = []
    words = input_string.split()

    for word in words:
        if "/" in word:
            left_part, right_part = word.split("/")
            good_number = make_good_number(left_part, right_part)
            if good_number:
                good_numbers.append(good_number)

    return good_numbers


if __name__ == '__main__':

    input_string = "Адрес 5467/456. Номер 405/549"
    good_numbers = makeGoodNumbers(input_string)
    for number in good_numbers:
        print(number)