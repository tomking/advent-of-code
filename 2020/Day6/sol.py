import re

def create_group_sets(input_list):
    """Creates sets of answers by group
        Parameters:
            input_list: 
                A list of lists of characters each of which represents all answers from a given group.
        
        Returns:
            A list of sets, each containing the answers from one group
    """
    group_sets = []
    for entry in input_list:
        new_set = set()
        for char in entry:
            new_set.add(char)
        group_sets.append(new_set)
    return group_sets

def count_shared_answers(input_list):
    """Count the number of shared answers across an entire group
        Parameters:
            input_list: 
                A list of lists of strings representing individual's answers by group

        Returns:
            The number of answers that everyone in the group gave
    """
    shared_answer_counter = 0
    for char in input_list[0]:
        if len(input_list) == 1:
            shared_answer_counter += 1
        else:
            answer_shared = True
            for individual in input_list[1:]:
                if individual.count(char) != 1:
                    answer_shared = False
            if answer_shared == True:
                shared_answer_counter += 1

    return shared_answer_counter

def main():
    with open("input.txt") as input:
        dirty_input = input.read()
        input.close()

    # Clean input lines
    input_group_strings = dirty_input.split("\n\n")
    input_group_strings = [elem.rstrip() for elem in input_group_strings]

    # Create list of lists of strings where each list is an individual and each string is an individual
    group_individual_lists = []
    for entry in input_group_strings:
        group_individual_lists.append(list(entry.split('\n')))

    # Create list of lists of characters where each list represents the collective answers of a group
    group_char_lists = []
    for entry in input_group_strings:
        group_char_lists.append(list(entry.replace('\n', '')))

    # Create group answer set list
    answer_set_list = create_group_sets(group_char_lists)

    # Calculate part one solution by totalling all group's unique answers
    part_one_sol = 0
    for group in answer_set_list:
        part_one_sol += len(group)

    # Calculate part two solution by totalling all group's shared answers
    part_two_sol = 0
    for group in group_individual_lists:
        part_two_sol += count_shared_answers(group)

    print(f"Part One Solution: {part_one_sol}\nPart Two Solution: {part_two_sol}")

if __name__ == '__main__':
    main()