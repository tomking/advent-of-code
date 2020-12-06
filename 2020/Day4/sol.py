import re

def generate_passport_array(input_list):
    passport_array = []
    for entry in input_list:
        current_passport_dict = {}
        seperated_passport_string = re.split(r':|\s', entry)

        # Range only to len-1 to eliminate odd number of hanging empty strings at end of file
        for index in range(0, len(seperated_passport_string)-1, 2):
            current_passport_dict[seperated_passport_string[index]] = seperated_passport_string[index+1]
        passport_array.append(current_passport_dict)

    return passport_array

def count_part1_valid_passports(passport_array):
    valid_passport_count = 0
    for passport in passport_array:
        valid_key_count = 0
        if 'byr' in passport:
            valid_key_count += 1
        if 'iyr' in passport:
            valid_key_count += 1
        if 'eyr' in passport:
            valid_key_count += 1
        if 'hgt' in passport:
            valid_key_count += 1
        if 'hcl' in passport:
            valid_key_count += 1
        if 'ecl' in passport:
            valid_key_count += 1
        if 'pid' in passport:
            valid_key_count += 1

        if valid_key_count == 7:
            valid_passport_count += 1

    return valid_passport_count

def count_part2_valid_passports(passport_array):
    valid_passport_count = 0
    for passport in passport_array:
        valid_key_count = 0
        if 'byr' in passport:
            if re.match(r'^\d{4}$', passport['byr']) and 1920 <= int(passport['byr']) <= 2002:
                print(int(passport['byr']))
                valid_key_count += 1
        if 'iyr' in passport:
            if re.match(r'^\d{4}$', passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020:
                valid_key_count += 1
        if 'eyr' in passport:
            if re.match(r'^\d{4}$', passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030:
                valid_key_count += 1
        if 'hgt' in passport:
            if re.match(r'^((1[5-8][0-9])cm|(19[0-3])cm)|((59|6[0-9]|7[0-6])in)$', passport['hgt']):
                valid_key_count += 1
        if 'hcl' in passport:
            if re.match(r'^#([0-9]|[a-f]){6}$', passport['hcl']):
                valid_key_count += 1
        if 'ecl' in passport:
            if re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', passport['ecl']):
                valid_key_count += 1
        if 'pid' in passport:
            if re.match(r'^\d{9}$', passport['pid']):
                valid_key_count += 1

        if valid_key_count == 7:
            valid_passport_count += 1

    return valid_passport_count

def main():
    with open("input.txt") as input:
        input_list = input.read()
        input.close()

    input_list = input_list.split("\n\n")
    passport_array = generate_passport_array(input_list)

    part_one_sol = count_part1_valid_passports(passport_array)
    part_two_sol = count_part2_valid_passports(passport_array)

    print(f"Part One Solution: {part_one_sol}\nPart Two Solution: {part_two_sol}")

if __name__ == '__main__':
    main()