# Efficient Algorithm for 3 partition problems
# research paper: Possibility of proving P = NP through 3 partition problems
# created by Glenn Patrick King Ang 10/21/2021 (edited 12/03/2021)
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985

# this program doesn't work if the amount for each subset is negative, a change in the equation is required
# this program was not thoroughly tested for bugs
# the main purpose of the program is to act as proof of concept

# Sample Sets:
set_of_numbers = [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
                  35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, ]
# set_of_numbers = [3, 1, 1, 3, 1, 1]
# set_of_numbers = [7, 2, 5, 1, 7, 8]
# set_of_numbers = [7, 2, 3, 1, 8, 5]
# set_of_numbers = [1, 1, 1]
# set_of_numbers = [0, 0, 0, 0, 0, 0, 2, 2, 2]
# set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# set_of_numbers = [0, 9, 1, 2, 8, 2, 1, 6, 1]

# anticipated bug:
# a. 2 combinations exists, but only 1 combination is correct
# b. the sum of each subset has the same value, but a number doesn't have a match
# c. the sum of each subset has the same value, two possible combinations, but only one can form a subset
# d. the sum of each subset has the same value, multiple possible combinations (based on section c)

# a. Special case A (Section 7): 2 combinations exists, but only 1 combination is correct
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1] # [9, 0, 3] [9, 2, 1], but only [9, 2, 1] is correct
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 9, 3]

# b. Special case B (Section 8): equal amount per subset, one of the large number has no match
# set_of_numbers = [1, 2, 3, 4, 5, 11] # 11 has no match
# set_of_numbers = [1, 1, 1, 9, 10, 12] # 12 has no match
# set_of_numbers = [13, 10, 1, 8, 1, 1] # 13 has no match
# set_of_numbers = [1, 2, 3, 10, 13, 21, 1, 2, 3, 4, 5, 15] # 21 has no match
# set_of_numbers = [0, 0, 0, 0, 0, 20, 20, 20, 30] # all of the 20 has no match

# c. Special case C (Section 9): equal amount per subset, two possible combinations, only one can form a subset
# set_of_numbers = [1, 2, 3, 0, 9, 7, 13, 18, 25] # 18 or 25 has no match because there is only one 1
# set_of_numbers = [0, 0, 2, 3, 5, 9, 20, 21, 30] # 21 or 30 has no match because there is only two 0

# d. Special case D (Section 10): multiple possible combinations
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1, ]

# possible combinations
# [9, 0, 3] [9, 0, 3] [0, 7, 5] [0, 7, 5] // [8, 1, 3] [8, 1, 3] [8, 2, 2] [9, 1, 2] [9, 1, 2]
# only two 0, perfect choice: [0, 7, 5] [0, 7, 5], instead of [9, 0, 3] [9, 0, 3]
# only two 2, perfect choice: [9, 1, 2] [9, 1, 2], instead of [8, 2, 2]
# only two 3, perfect choice: [8, 1, 3] [8, 1, 3], instead of [7, 2, 3] [7, 2, 3] [9, 0, 3] [9, 0, 3]

# d.2. Special case D (Section 10): multiple possible combinations
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1, ]

# no possible combinations
# set_of_numbers = [20, 5, 5, 5, 5, 10]
# set_of_numbers = [10, 10, 10, 10, 10, 40] # error
# set_of_numbers = [0, 0, 0, 0, 0, 90] # error
# set_of_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 1]
# set_of_numbers = [0, 7, 2, 3, 8, 5]

# Random set of numbers
# set_of_numbers = [0, 0, 1, 1, 1, 1]
# set_of_numbers = [0, 0, 22, 10, 10, 0, 16, 1, 1]
# set_of_numbers = [0, 18, 2, 0, 10, 10, 2, 16, 2]
# set_of_numbers = [5, 5, 2, 6, 4, 4, 7, 3, 0]
# set_of_numbers = [0, 5, 7, 2, 6, 6, 4, 1, 5]
# set_of_numbers = [1, 0, 3, 1, 1, 9, 9, 0, 0]
# set_of_numbers = [1, 0, 3, 1, 1, 9, 9, 0, 3]
# set_of_numbers = [1, 0, 3, 1, 1, 9, 9, 0, 6]
# set_of_numbers = [15, 3, 2, 14, 5, 1, 13, 0, 7]
# set_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# odd numbers
# set_of_numbers = [1, 3, 5, 7, 11, 13, 17, 19, 23]
# set_of_numbers = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# set_of_numbers = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
#                   59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 111 ]


# number of steps test sets (Section 14):

# section 14.a
# set_of_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# section 14.b
# set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# section 14.c
# set_of_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1,
#                   9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1,
#                   9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, ]

# section 14.d
# set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                   1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                   1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# section 14.e
# set_of_numbers = [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
#                   35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, ]

# section 14.f
# set_of_numbers = [13, 10, 8, 1, 1, 1] # 13 has no match

# section 14.g
# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1]

# section 14.h
# set_of_numbers = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
#                   9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
#                   8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
#                   7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5,
#                   5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3,
#                   3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2,
#                   2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#                   1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                   0, 0, 0, 0, 0, 0, 0, 0, 0]

# section 14.i
# set_of_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                   0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#                   1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#                   2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
#                   3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5,
#                   5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
#                   7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
#                   7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
#                   8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
#                   9, 9, 9, 9, 9, 9, 9, 9, 9]


complete_list = []
number_of_subsets = 0
amount_each_subset = -1000000
break_all_loops = False
loop_count = 0
index_largest_num = 1
restart_set_collected = []
restart_activated = False
restart_nums_collected = []

# count total steps for each function and loop
count_steps = 0
# count total steps for finding a match for each subset only
count_only_when_finding_match = 0
# count total steps for sorting
count_steps_sorting = 0


def sorting_algorithm():
    global count_steps_sorting
    global set_of_numbers

    loop = 0

    print("\n>>>>>>>>>> Step: Sorting Algorithm <<<<<<<<<<")

    while loop != len(set_of_numbers):
        loop += 1
        set_complete = -1

        for x in range(1, len(set_of_numbers)):

            # ========= count total steps for the sorting function
            count_steps_sorting += 1
            # ============================

            # print(f"is {set_of_numbers[x - 1]} > {set_of_numbers[x]}")

            if set_of_numbers[x - 1] > set_of_numbers[x]:
                switch_numbers = set_of_numbers[x - 1]
                set_of_numbers[x - 1] = set_of_numbers[x]
                set_of_numbers[x] = switch_numbers
                set_complete += 1

        if set_complete == -1:
            break

    print("\n*************************************** Sorting Sets Results ******************************************")
    print(f"Total steps for sorting the set (ascending) = {count_steps_sorting}")
    print(f"Original Set = {original_set}")
    print(f"\nSorted Set = {set_of_numbers}")
    print("*******************************************************************************************************")


def restart_match(number):
    global new_set_numbers
    global loop_count
    global break_all_loops
    global complete_list
    global restart_activated
    global restart_nums_collected

    restart_activated = True

    print("\n>>>>>>>>>> No match found <<<<<<<<<<")
    print(">>>>>>>>>> restart everything <<<<<<<<<<")

    complete_list = []
    break_all_loops = False

    loop_count = 0

    new_set_numbers = set_of_numbers.copy()

    if len(restart_set_collected) > 0:
        for nums_collected in restart_nums_collected:

            new_set_numbers.remove(nums_collected)

            # ========= count total steps for each function and loop
            count_total_steps()
            print(">>>>>>>>>> Step: Restart match <<<<<<<<<<")
            # ============================

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

    if len(set_of_numbers) % 3 == 0:
        global number_of_subsets
        number_of_subsets = len(set_of_numbers) // 3

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

    global restart_activated
    global restart_set_collected
    global restart_nums_collected

    index_smallest_num = 0

    while len(new_set_numbers) > 0:

        if index_smallest_num >= 1:
            previous_num = new_set_numbers[index_smallest_num - 1]
            skipped_nums = 0

            if new_set_numbers[index_smallest_num] == previous_num:

                while new_set_numbers[index_smallest_num] == previous_num:

                    # ========= count total steps for each function and loop
                    count_total_steps()
                    print(">>>>>>>>>> Step: Restart match <<<<<<<<<<")
                    # ============================

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
        # ========= count only this function

        print("\n>>>>>>>>>> Step: Find match <<<<<<<<<<")

        global count_only_when_finding_match
        count_only_when_finding_match += 1
        # ============================

        smallest_number = new_set_numbers[index_smallest_num]
        new_set_numbers[index_smallest_num] = "small_num"
        difference_nums = amount_each_subset - (largest_num + smallest_number)
        print("\n=====================")
        print(f"the difference: {difference_nums} = {amount_each_subset} - ({largest_num} + {smallest_number})")
        print("=====================")

        if difference_nums in new_set_numbers:
            collect_numbers = [smallest_number, difference_nums, largest_num, ]
            new_set_numbers[index_smallest_num] = smallest_number

            if restart_activated:
                restart_activated = False

                if len(restart_set_collected) > 0:
                    for sets_inside_rsc in restart_set_collected:
                        complete_list.append(sets_inside_rsc)

                restart_set_collected.append(collect_numbers)
                restart_nums_collected.append(smallest_number)
                restart_nums_collected.append(difference_nums)
                restart_nums_collected.append(largest_num)

            print(f"new set nums before deletion = {new_set_numbers}")
            print(f"collected numbers: {collect_numbers}")
            new_set_numbers.remove(smallest_number)
            new_set_numbers.remove(difference_nums)
            complete_list.append(collect_numbers)
            print(f"new set nums after deletion = {new_set_numbers}")
            break
        else:
            print("there is no match found")
            new_set_numbers[index_smallest_num] = smallest_number
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

    original_set = set_of_numbers.copy()
    sorting_algorithm()
    new_set_numbers = set_of_numbers.copy()
    print(f"\nset start: {original_set}")
    print(f"set sorted: {new_set_numbers}\n")

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
                new_set_numbers = []

            else:
                if len(new_set_numbers) > 0:
                    output_error()
                else:
                    # print(f"the number of subsets: {number_of_subsets} and the loop count is: {loop_count}")
                    loop_count = number_of_subsets + 1

        loop_count += 1

    if not break_all_loops:
        print(f"\n>>>>>>>>>>>>>>> Output <<<<<<<<<<<<<<<")
        print(f"\nOriginal Set: {original_set}")
        print(f"Total number of elements inside the set: {len(original_set)}")
        print(f"\nNumber of subsets: {number_of_subsets}")
        print(f"Total sum of the entire set: {amount_each_subset * number_of_subsets}")
        print(f"The amount for each subset is: {amount_each_subset}")
        print(f"\nThe complete list of subsets: {complete_list}")
        print(f"Total steps for only finding a match for all the subsets: {count_only_when_finding_match}")
    else:
        output_error()

    print(f"\nTotal steps for sorting the set (ascending): {count_steps_sorting}")
    print(f"Total steps for all the functions to complete: {count_steps}")
    print(f"\nTotal steps for all the functions to complete + sorting: {count_steps + count_steps_sorting}")
else:
    print("================ Error =================")
