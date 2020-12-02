def parse_password_line(input_line):
    parsed_dict = {
    }

    line_list = line.split("-", 1)
    parsed_dict["first_num"] = int(line_list[0])
    line_list = line_list[1].split(" ", 1)
    parsed_dict["second_num"] = int(line_list[0])
    line_list = line_list[1].split(": ", 1)
    parsed_dict["char"] = line_list[0]
    parsed_dict["password"] = line_list[1]

    return parsed_dict

def eval_parsed_password_policy1(parsed_dict):
    occurances_of_char = parsed_dict["password"].count(parsed_dict["char"])
    
    if occurances_of_char >= parsed_dict["first_num"] and occurances_of_char <= parsed_dict["second_num"]:
        return True

def eval_parsed_password_policy2(parsed_dict):
    first_position = False
    second_position = False

    if len(parsed_dict["password"]) >= parsed_dict["first_num"]:
        if parsed_dict["password"][parsed_dict["first_num"]-1] == parsed_dict["char"]:
            first_position = True

    if len(parsed_dict["password"]) >= parsed_dict["second_num"]:
        if parsed_dict["password"][parsed_dict["second_num"]-1] == parsed_dict["char"]:
            second_position = True
    
    return (first_position != second_position)
        


### DRIVER CODE

with open("input.txt") as input:
    input_list = input.readlines()
    input.close()

number_of_valid_passwords_policy1 = 0
number_of_valid_passwords_policy2 = 0

for line in input_list:
    parsed_dict = parse_password_line(line)
    if eval_parsed_password_policy1(parsed_dict):
        number_of_valid_passwords_policy1 += 1
    if eval_parsed_password_policy2(parsed_dict):
        number_of_valid_passwords_policy2 += 1

print(f"Part One Solution: {number_of_valid_passwords_policy1}\nPart Two Solution: {number_of_valid_passwords_policy2}")