def solve_part_one(input_list):
    counter = 0

    for idx, line in enumerate(input_list):
        if idx > 0:
            if line > input_list[idx-1]:
                counter+=1

    return counter

def solve_part_two(input_list):
    counter = 0

    for idx, line in enumerate(input_list):
        if idx>0 and idx<len(input_list)-1:
            if line+input_list[idx-1]+input_list[idx+1] > line+input_list[idx-1]+input_list[idx-2]:
                counter+=1

    return counter

def main():
    with open("input.txt") as input:
        input_list = [int(line) for line in input]
        input.close()

    print(f"Part One Solution: {solve_part_one(input_list)}")


    print(f"Part Two Solution: {solve_part_two(input_list)}")

if __name__ == '__main__':
    main()