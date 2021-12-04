USE_TEST_INPUT = False

def solve_part_one(bingo_num_list, bingo_board_list):
    winning_board_idx = 0

    found = False
    last_bingo_number = 0

    for bingo_num in bingo_num_list:
        if found == True:
            break

        last_bingo_number = int(bingo_num)

        for board_idx, board in enumerate(bingo_board_list):
            for line_idx, line in enumerate(board):
                for e_idx, e in enumerate(line):
                    if e==bingo_num:
                        bingo_board_list[board_idx][line_idx][e_idx] += "B"
    
        # Check for win condition in rows
        for board_idx, board in enumerate(bingo_board_list):
            for line_idx, line in enumerate(board):
                total_in_row = 0
                for e_idx, e in enumerate(line):
                    if e[len(e)-1]=="B":
                        total_in_row+=1

                if total_in_row == 5:
                    winning_board_idx = board_idx
                    found = True

        # Check for win condition in cols
        for board_idx, board in enumerate(bingo_board_list):
                for col_idx in range(0,len(board[0])):
                    total_in_col = 0
                    for line in board:
                        if line[col_idx][len(line[col_idx])-1] == "B":
                            total_in_col+=1

                    if total_in_col == 5:
                        winning_board_idx = board_idx
                        found = True

    winning_board_score = 0
    for line in bingo_board_list[winning_board_idx]:
        for e in line:
            if e[len(e)-1] != "B":
                winning_board_score += int(e)

    return (winning_board_score * last_bingo_number)

def solve_part_two(bingo_num_list, bingo_board_list):
    won_boards = []

    found = False
    last_bingo_number = 0

    for bingo_num in bingo_num_list:
        if found == True:
            break

        last_bingo_number = int(bingo_num)

        for board_idx, board in enumerate(bingo_board_list):
            for line_idx, line in enumerate(board):
                for e_idx, e in enumerate(line):
                    if e==bingo_num:
                        bingo_board_list[board_idx][line_idx][e_idx] += "B"
    
        # Check for win condition in rows
        for board_idx, board in enumerate(bingo_board_list):
            if board_idx not in won_boards:
                for line_idx, line in enumerate(board):
                    total_in_row = 0
                    for e_idx, e in enumerate(line):
                        if e[len(e)-1]=="B":
                            total_in_row+=1

                    if total_in_row == 5:
                        won_boards.append(board_idx)
                        if len(bingo_board_list) == len(won_boards):
                            found = True

        # Check for win condition in cols
        for board_idx, board in enumerate(bingo_board_list):
            if board_idx not in won_boards:
                for col_idx in range(0,len(board[0])):
                    total_in_col = 0
                    for line in board:
                        if line[col_idx][len(line[col_idx])-1] == "B":
                            total_in_col+=1

                    if total_in_col == 5:
                        won_boards.append(board_idx)
                        if len(bingo_board_list) == len(won_boards):
                            found = True

    winning_board_idx = won_boards[len(won_boards)-1]

    winning_board_score = 0
    for line in bingo_board_list[winning_board_idx]:
        for e in line:
            if e[len(e)-1] != "B":
                winning_board_score += int(e)

    return (winning_board_score * last_bingo_number)
    
def main():
    bingo_num_list = []
    bingo_board_list = []
    with open("test_input.txt" if USE_TEST_INPUT else "input.txt") as input:
        input_list = input.readlines()
        for idx, line in enumerate(input_list):
            if idx == 0:
                # These are the bingo numbers
                bingo_num_list = line.strip().split(",")
            if line == "\n":
                pass
            else:
                if input_list[idx-1] == "\n":
                    new_board = []
                    for i in range (idx, idx+5):
                        new_board.append([e for e in input_list[i].strip().split()])

                    bingo_board_list.append(new_board)
                else:
                    pass

        input.close()


    print(f"Part One Solution: {solve_part_one(bingo_num_list, bingo_board_list)}")


    print(f"Part Two Solution: {solve_part_two(bingo_num_list, bingo_board_list)}")

if __name__ == '__main__':
    main()