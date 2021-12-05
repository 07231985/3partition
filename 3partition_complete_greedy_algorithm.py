# Complete Greedy Algorithm for 3 partition problems
# research paper: Possibility of Proving P = NP through 3 partition problems
# created by Glenn Patrick King Ang 12/03/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985

# sample sets:

set_of_numbers = [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55,
                  35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, ]

# set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# set_of_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# set_of_numbers = [13, 10, 8, 1, 1, 1] # 13 has no match

# set_of_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1,
#                   9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1,
#                   9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, ]

# set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                   1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                   1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# set_of_numbers = [9, 5, 3, 6, 7, 1, 2, 4, 8]

# set_of_numbers = [0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1,
#                   0, 7, 2, 3, 1, 9, 8, 5, 1, 0, 7, 2, 3, 1, 9, 8, 5, 1, ]


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


original_set_numbers = set_of_numbers.copy()
new_set_numbers = set_of_numbers.copy()
amount_each_subset = -1
break_all_loops = False
count_steps = 0
number_of_subsets = 0
collect_subsets = []


def count_total_steps():
    global count_steps
    count_steps += 1

def sum_of_set():

    # ========= count total steps for each function and loop
    count_total_steps()
    # ============================

    print(">>>>>>>>>> Step: Sum of sets <<<<<<<<<<\n")

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
    # ============================

    print(">>>>>>>>>> Step: Split into three <<<<<<<<<<")

    if len(new_set_numbers) % 3 == 0:
        global number_of_subsets
        number_of_subsets = len(new_set_numbers) // 3
        # ========== function sum of sets
        sum_of_set()
        # =======================
    else:
        print("================ Error =================")
        print("The total number of items can't be divided into 3")


# ***********************************************************************************************
# *************************************** Start . Program ***************************************
# ***********************************************************************************************

can_be_split_into_three()

if amount_each_subset > -1:
    print(f"\noriginal set: {original_set_numbers}")
    print(f"original set length is {len(original_set_numbers)}")
    new_set_numbers_x = new_set_numbers.copy()

    for x_index in range(len(new_set_numbers) - 2):
        x = new_set_numbers[x_index]
        new_set_numbers_x.remove(new_set_numbers[x_index])
        new_set_numbers_y = new_set_numbers_x.copy()
        print(f"\n=========================== start program with x: {x}")

        while len(new_set_numbers_y) > 1:
            print(f"\ny subset length is {len(new_set_numbers_y)}")
            print(f"y subset = {new_set_numbers_y}")
            y = new_set_numbers_y[0]
            print(f"\n=========================== start program with x: {x} and y: {y}")
            new_set_numbers_y.remove(new_set_numbers_y[0])

            for z in new_set_numbers_y:

                # ========= count total steps
                count_total_steps()
                # ============================

                print(f"combination: x: {x} y:{y} z:{z}")
                combination_sum = x + y + z

                if combination_sum == amount_each_subset:
                    collect_combination = [x, y, z]
                    print("\n**************************** ")
                    print(f"match found: sum of combination {collect_combination} = {amount_each_subset}")
                    print("**************************** \n")

                    collect_subsets.append(collect_combination)


print("\n*************************************** Results ***************************************")
print(f"original set: {original_set_numbers}")
print(f"total number of elements inside the set: {len(original_set_numbers)}")
print(f"\nnumber of subsets: {number_of_subsets}")
print(f"Total sum of the entire set: {amount_each_subset * number_of_subsets}")
print(f"The amount for each subset is: {amount_each_subset}")

print(f"\ncollected list of all possible subsets: {collect_subsets}")
print(f"Total number of all possible subsets collected: {len(collect_subsets)}")
print(f"\nTotal steps for finding all possible subsets: {count_steps}")
print("***************************************************************************************")


# ***********************************************************************************************
# *************************************** Finding Subsets ***************************************
# ***********************************************************************************************

print("\n\n=================== start looking for subsets")

set_numbers_complete = set_of_numbers.copy()
loop_count_for = 0
collect_sets = []
count_steps_finding_subset = 0

set_x = collect_subsets.copy()

for x in collect_subsets:

    loop_count_for += 1

    print(f"\n=================== starting subsets program with the for loop: {loop_count_for}")

    find_subsets = x.copy()

    set_x.remove(find_subsets)

    set_numbers_complete = set_of_numbers.copy()
    set_numbers_complete.remove(find_subsets[0])
    set_numbers_complete.remove(find_subsets[1])
    set_numbers_complete.remove(find_subsets[2])

    collect_sets.append(find_subsets)

    for y in set_x:

        find_y_subsets = y.copy()

        if len(set_numbers_complete) > 0:

            count_total_steps()
            count_steps_finding_subset += 1

            # print(f"available subset: {find_y_subsets} and the remaining set = {set_numbers_complete}")

            if find_y_subsets[0] in set_numbers_complete:

                set_numbers_complete.remove(find_y_subsets[0])

                if find_y_subsets[1] in set_numbers_complete:

                    set_numbers_complete.remove(find_y_subsets[1])

                    if find_y_subsets[2] in set_numbers_complete:
                        set_numbers_complete.remove(find_y_subsets[2])
                        collect_sets.append(find_y_subsets)

                        # print("\n**************************** ")
                        # print(f"match found: removing combination {find_y_subsets} new set: {set_numbers_complete}")
                        # print("**************************** \n")

                    else:
                        set_numbers_complete.append(find_y_subsets[0])
                        set_numbers_complete.append(find_y_subsets[1])
                else:
                    set_numbers_complete.append(find_y_subsets[0])
        else:
            break

    if len(set_numbers_complete) == 0:
        break
    else:
        collect_sets = []

        # print("\n**************************** ")
        # print(f"resetting collected sets: {collect_sets}")
        # print("**************************** \n")



print("\n*************************************** Finding Subsets Output ****************************************")
print(f"found possible subsets: {collect_subsets}")
print(f"\nThe complete list of subsets: {collect_sets}")
print(f"total steps for finding the complete list of subsets only: {count_steps_finding_subset}")

print(f"\ntotal steps for finding all possible subsets: {count_steps - count_steps_finding_subset}")
print(f"total steps for finding all possible subsets + finding the {number_of_subsets} subset(s): {count_steps}")
print("*******************************************************************************************************")














