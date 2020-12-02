def solve_part_one(input_list):
    for first_number in input_list:
        for second_number in input_list:
            if first_number + second_number == 2020:
                return first_number * second_number

def solve_part_two(input_list):
    for first_number in input_list:
        for second_number in input_list:
            for third_number in input_list:
                if (first_number + second_number + third_number) == 2020:
                    return first_number * second_number * third_number

def main():
    with open("input.txt") as input:
        input_list = [int(line) for line in input]
        input.close()

    print(f"Part One Solution: {solve_part_one(input_list)}")


    print(f"Part Two Solution: {solve_part_two(input_list)}")

if __name__ == '__main__':
    main()