def count_obstacles(map, slope_x_comp, slope_y_comp):
    obstacle_count = 0
    x_idx = 0

    for line_idx, line in enumerate(map):
        # This handles skipping vertical rows for our y component
        if (line_idx == 0) or (line_idx % slope_y_comp == 0):
            if line_idx != 0:
                # Increase our horizontal component
                x_idx += slope_x_comp
                if x_idx >= len(line):
                    x_idx -= len(line)

            # Check if we hit an obstacle
            if line[x_idx] == '#':
                obstacle_count += 1

        # Check if we are at the bottom
        if line_idx+1 == len(map):
            return obstacle_count

def main():
    with open("input.txt") as input:
        input_list = input.readlines()
        input_list = [line.rstrip() for line in input_list]
        input.close()
    
    part_one_sol = count_obstacles(input_list, 3, 1)
    part_two_sol = (count_obstacles(input_list, 1, 1) * count_obstacles(input_list, 3, 1)
                    * count_obstacles(input_list, 5, 1) * count_obstacles(input_list, 7, 1)
                    * count_obstacles(input_list, 1, 2))

    print(f"Part One Solution: {part_one_sol}\nPart Two Solution: {part_two_sol}")

if __name__ == '__main__':
    main()