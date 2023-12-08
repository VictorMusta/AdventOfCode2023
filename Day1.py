calibration_values = "textFile.txt"


def get_first_and_last_numbers(list_of_numbers):
    return int("".join(str(list_of_numbers[0]) + str(list_of_numbers[-1])))


def get_numbers_in_line(line):
    return [n for n in line if n.isdigit()]


def day_1(file=calibration_values):
    with open(file, "r", encoding='utf_8') as calibration_values_rf:
        total = 0
        for line in calibration_values_rf.readlines():
            numbers_in_line = get_numbers_in_line(line)
            total += get_first_and_last_numbers(numbers_in_line)
        return total


if __name__ == "__main__":
    print(day_1(calibration_values))
