USE_TEST_INPUT = False

def solve_part_one(input_list):
    gamma_rate = ""
    epsilon_rate = ""

    for index in range(0,len(input_list[0])):
        total_ones = 0
        total_zeros = 0
        for entry in input_list:
            if entry[index] == "0":
                total_zeros+=1
            else:
                total_ones+=1


        if total_ones > total_zeros:
            gamma_rate+="1"
            epsilon_rate+="0"
        else:
            gamma_rate+="0"
            epsilon_rate+="1"
            

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def solve_part_two(input_list):
    o2_gen_list = input_list.copy()
    co2_scrub_list = input_list.copy()

    print(o2_gen_list)

    for index in range(0,len(input_list[0])):
        total_o2_ones = 0
        total_o2_zeros = 0

        total_co2_ones = 0
        total_co2_zeros = 0

        for entry in o2_gen_list:
            if entry[index] == "0":
                total_o2_zeros+=1
            else:
                total_o2_ones+=1

        for entry in co2_scrub_list:
            if entry[index] == "0":
                total_co2_zeros+=1
            else:
                total_co2_ones+=1

        if len(o2_gen_list)>1:
            if total_o2_ones > total_o2_zeros:
                o2_gen_list = list(filter(lambda entry: entry[index] == "1", o2_gen_list))
            elif total_o2_zeros > total_o2_ones:
                o2_gen_list = list(filter(lambda entry: entry[index] == "0", o2_gen_list))
            else:
                o2_gen_list = list(filter(lambda entry: entry[index] == "1", o2_gen_list))
        
        if len(co2_scrub_list)>1:
            if total_co2_ones > total_co2_zeros:
                co2_scrub_list = list(filter(lambda entry: entry[index] == "0", co2_scrub_list))
            elif total_co2_zeros > total_co2_ones:
                co2_scrub_list = list(filter(lambda entry: entry[index] == "1", co2_scrub_list))
            else:
                co2_scrub_list = list(filter(lambda entry: entry[index] == "0", co2_scrub_list))

    return int(o2_gen_list[0], 2) * int(co2_scrub_list[0], 2)

def main():
    input_list = []
    with open("test_input.txt" if USE_TEST_INPUT else "input.txt") as input:
        input_list = [line.rstrip("\n") for line in input]
        input.close()

    print(f"Part One Solution: {solve_part_one(input_list)}")


    print(f"Part Two Solution: {solve_part_two(input_list)}")

if __name__ == '__main__':
    main()