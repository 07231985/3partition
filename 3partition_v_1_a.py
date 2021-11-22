# Efficient Algorithm for 3 partition to prove P = NP
# research paper: Proving P = NP through 3 partition problems
# created by Glenn Patrick King Ang 10/21/2021

# this program doesn't work if the amount for each subset is negative, a change in the equation is required
# this program was not thoroughly tested for bugs
# anticipated bug:
# a. 2 combinations exists, but only 1 combination is correct
# b. the sum of each subset has the same value, but a number doesn't have a match
# c. the sum of each subset has the same value, two possible combinations, but only one can form a subset
# the main purpose of the program is to act as proof of concept

# Perfect sets

set_of_numbers = [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
                  35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, ]

# set_of_numbers = [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
#                   35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0,
#                   20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
#                   35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0,
#                   20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
#                   35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, ]

# set_of_numbers = [3, 1, 1, 3, 1, 1]
# set_of_numbers = [7, 2, 5, 1, 7, 8]
# set_of_numbers = [1, 1, 1]
# set_of_numbers = [0, 0, 0, 0, 0, 0, 2, 2, 2]
# set_of_numbers = [1, 5, 0, 0, 3, 5, ]

# a. special case: 2 combinations exists, but only 1 combination is correct
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1]
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 9, 3]

# b. special case: equal amount per subset, one of the large number has no match
# set_of_numbers = [1, 2, 3, 4, 5, 11] # 11 has no match
# set_of_numbers = [1, 1, 1, 9, 10, 12] # 12 has no match
# set_of_numbers = [13, 10, 1, 8, 1, 1] # 13 has no match
# set_of_numbers = [1, 2, 3, 10, 13, 21, 1, 2, 3, 4, 5, 15] # 21 has no match
# set_of_numbers = [0, 0, 0, 0, 0, 20, 20, 20, 30] # all of the 20 has no match

# c. special case: equal amount per subset, two possible combinations, only one can form a subset
# set_of_numbers = [1, 2, 3, 0, 9, 7, 13, 18, 25] # 18 or 25 has no match because there is only one 1
# set_of_numbers = [0, 0, 2, 3, 5, 9, 20, 21, 30] # 21 or 30 has no match because there is only two 0

# no possible combinations
# set_of_numbers = [20, 5, 5, 5, 5, 10]
# set_of_numbers = [10, 10, 10, 10, 10, 40] # error
# set_of_numbers = [0, 0, 0, 0, 0, 90] # error
# set_of_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 1]
# set_of_numbers = [0, 7, 2, 3, 8, 5]

complete_list = []
number_of_subsets = 0
amount_each_subset = -1000000
original_set = set_of_numbers.copy()
set_of_numbers.sort()
new_set_numbers = set_of_numbers.copy()
break_all_loops = False
# count total steps for each function and loop
count_steps = 0
# count total steps for finding a match for each subset only
count_only_when_finding_match = 0
loop_count = 0

print(f"\nset start: {original_set}")
print(f"set sorted: {new_set_numbers}\n")


def restart_match(number):
    global new_set_numbers
    global loop_count
    global break_all_loops
    global complete_list

    print("\n>>>>>>>>>> No match found <<<<<<<<<<")
    print(">>>>>>>>>> restart everything <<<<<<<<<<")

    # ========= count total steps for each function and loop
    count_total_steps()
    print(">>>>>>>>>> Step: Restart match <<<<<<<<<<")
    # ============================

    complete_list = []
    break_all_loops = False

    loop_count = 0

    new_set_numbers = set_of_numbers.copy()
    index_item = new_set_numbers.index(number)
    start_with_this_num = index_item
    index_middle_restart = (len(new_set_numbers) + 1) / 2 - 1
    if start_with_this_num > index_middle_restart:
        print(f"restart set: {new_set_numbers} \nstart with previous number: {new_set_numbers[start_with_this_num]}")
        find_match(start_with_this_num)
    else:
        break_all_loops = True
        no_match_found()


def count_total_steps():
    global count_steps
    count_steps += 1


def sum_of_set():

    # ========= count total steps for each function and loop
    count_total_steps()
    print(">>>>>>>>>> Step: Sum of sets <<<<<<<<<<\n")
    # ============================

    sum_nums = sum(set_of_numbers)
    print(f"Number of subsets: {number_of_subsets}")

    if sum_nums % number_of_subsets == 0:

        global amount_each_subset
        amount_each_subset = sum_nums // number_of_subsets
        print(f"Total sum = {sum_nums}")
        print(f"Amount each subset = {amount_each_subset}")

    else:

        print(f"{sum_nums} is not divisible by {number_of_subsets}")



def can_be_split_into_three():

    # ========= count total steps for each function and loop
    count_total_steps()
    print(">>>>>>>>>> Step: Split into three <<<<<<<<<<")
    # ============================

    if len(new_set_numbers) % 3 == 0:
        global number_of_subsets
        number_of_subsets = len(new_set_numbers) // 3
        # ========== function sum of sets
        sum_of_set()
        # =======================
    else:
        print("================ Error =================")
        print("The total number of items can't be divided into 3")



def no_match_found():
    global break_all_loops
    break_all_loops = True
    print("\n================ Error =================")
    print("Break this loop")
    print("================ Error =================")


def find_match(start_with_this_num=-1):
    largest_num = new_set_numbers[start_with_this_num]
    new_set_numbers.remove(largest_num)

    index_smallest_num = 0

    while len(new_set_numbers) > 0:

        if index_smallest_num >= 1:
            previous_num = new_set_numbers[index_smallest_num - 1]
            skipped_nums = 0

            if new_set_numbers[index_smallest_num] == previous_num:

                while new_set_numbers[index_smallest_num] == previous_num:
                    skipped_nums += 1
                    if index_smallest_num < len(new_set_numbers) - 1:
                        index_smallest_num += 1
                    else:
                        break

                print(f"Skipped the number: {previous_num} >>> {skipped_nums} time(s)")
                print("because it's the same small number")
                print("=====================")

        # ========= count total steps for each function and loop
        count_total_steps()
        print("\n>>>>>>>>>> Step: Find match <<<<<<<<<<")
        # ========= count only this function
        global count_only_when_finding_match
        count_only_when_finding_match += 1
        # ============================

        smallest_number = new_set_numbers[index_smallest_num]
        new_set_numbers.remove(smallest_number)

        difference_nums = amount_each_subset - (largest_num + smallest_number)
        print("\n=====================")
        print(f"the difference: {difference_nums} = {amount_each_subset} - ({largest_num} + {smallest_number})")
        print("=====================")

        if difference_nums in new_set_numbers:
            collect_numbers = [difference_nums, largest_num, smallest_number]
            print(f"new set nums before deletion = {new_set_numbers}")
            print(f"collected numbers: {collect_numbers}")
            new_set_numbers.remove(difference_nums)
            complete_list.append(collect_numbers)
            print(f"new set nums after deletion = {new_set_numbers}")
            break
        else:
            print("no match found")
            new_set_numbers.append(smallest_number)
            new_set_numbers.sort()
            index_middle_restart = (len(new_set_numbers) + 1) / 2 - 1


            if index_smallest_num > int(index_middle_restart) - 1:
                if set_of_numbers[start_with_this_num] == largest_num:
                    global break_all_loops
                    break_all_loops = True
                    new_set_numbers.append(largest_num)
                    break
                else:
                    print("activate restart match")
                    no_match_found()
                    restart_match(largest_num)

                    break

        index_smallest_num += 1


def output_error():
    print("\n================ Error =================")
    print(f"Remaining set doesn't match the sum for each subset: {amount_each_subset}")
    print(f"The sets are: {new_set_numbers}")
    print("================ Error =================")


# ================= Start program


can_be_split_into_three()

if amount_each_subset > -1:

    loop_count = 0

    while number_of_subsets > loop_count and not break_all_loops:

        # ========= count total steps for each function and loop
        count_total_steps()
        # ============================

        if len(new_set_numbers) > 3:
            find_match()
        else:
            if sum(new_set_numbers) == amount_each_subset:

                # ========= count only this function
                count_only_when_finding_match += 1
                # ============================

                print("\n=====================")
                print(f"Sum of Remaining subset: {new_set_numbers} = {amount_each_subset}")
                print("Collecting set")
                print("=====================")

                complete_list.append(new_set_numbers)

            else:
                output_error()

        loop_count += 1

    if not break_all_loops:
        print(f"\n>>>>>>>>>>>>>>> Output <<<<<<<<<<<<<<<")
        print(f"\nOriginal Set: {original_set}")
        print(f"The complete list: {complete_list}")
        print(f"The amount for each subset is: {amount_each_subset}")
    else:
        output_error()

    print(f"\nTotal steps for all the functions to complete: {count_steps}")
    print(f"\nTotal steps for finding a match for all the subsets using the equation: {count_only_when_finding_match}")
else:
    print("================ Error =================")
