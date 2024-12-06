def solve_part_one(input_list):
    depth = 0
    h_pos = 0

    for direction, value in input_list:
        if direction == "forward":
            h_pos+= value
        if direction == "down":
            depth+= value
        if direction == "up":
            depth-= value
        

    return depth*h_pos
    

def solve_part_two(input_list):
    depth = 0
    h_pos = 0
    aim = 0

    for direction, value in input_list:
        if direction == "forward":
            h_pos+= value
            depth+=aim*value
        if direction == "down":
            aim+= value
        if direction == "up":
            aim-= value

    return depth*h_pos

def main():
    input_list = []
    with open("input.txt") as input:
        for line in input.readlines():
            direction, value = line.split(" ")
            input_list.append((direction, int(value)))
        input.close()

    print(f"Part One Solution: {solve_part_one(input_list)}")


    print(f"Part Two Solution: {solve_part_two(input_list)}")

if __name__ == '__main__':
    main()