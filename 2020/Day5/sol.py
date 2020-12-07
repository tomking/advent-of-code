import math

def calculate_seat_ID(ID_string):
    row_list = [*range(0,128)]
    col_list = [*range(0,8)]
    fb_string = ID_string[0:7]
    lr_string = ID_string[7:10]

    for char in fb_string:
        if char == "F":
            row_list = row_list[0:math.floor(len(row_list)/2)]
        else:
            row_list = row_list[math.ceil(len(row_list)/2):len(row_list)]

    row = row_list[0]

    for char in lr_string:
        if char == "L":
            col_list = col_list[0:math.floor((len(col_list))/2)]
        else:
            col_list = col_list[math.ceil((len(col_list))/2):len(col_list)]

    col = col_list[0]

    return row * 8 + col

def main():
    with open("input.txt") as input:
        input_list = input.readlines()
        input.close()

    seat_id_array = []

    for seat_code in input_list:
        seat_id_array.append(calculate_seat_ID(seat_code))

    seat_id_array.sort()

    part_one_sol = seat_id_array[-1]

    part_two_sol = 0
    last_seat_id = 0
    for seat_id in seat_id_array:
        if last_seat_id == 0 or seat_id == last_seat_id+1:
            last_seat_id = seat_id
        elif seat_id == last_seat_id+2:
            part_two_sol = seat_id-1


    print(f"Part One Solution: {part_one_sol}\nPart Two Solution: {part_two_sol}")

if __name__ == '__main__':
    main()