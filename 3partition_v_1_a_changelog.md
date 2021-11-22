# 3partition_v_1_a

## file: 3partition_v_1_a.py: changelog v 1.a


## A. might cause error

### changed this lines of code starting at line 172 to 190:

	    smallest_number = new_set_numbers[index_smallest_num]
        new_set_numbers[index_smallest_num] = -1000000

        if difference_nums in new_set_numbers:
            new_set_numbers[index_smallest_num] = smallest_number
            new_set_numbers.remove(smallest_number)
        else:
            new_set_numbers[index_smallest_num] = smallest_number

### to this line of code starting at 184 to 203:

	    smallest_number = new_set_numbers[index_smallest_num]
        new_set_numbers.remove(smallest_number)

        if difference_nums in new_set_numbers:
            break
        else:
            print("no match found")
            new_set_numbers.append(smallest_number)
            new_set_numbers.sort()





## B. increase efficiency

### detect if the value of the previous small number is the same as the value of the current small number
### inserted at line 164 to 174:

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

### Example

Original Set: [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55, 35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, 
		20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55, 35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0, 
		20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 23, 18, 55, 35, 0, 89, 1, 0, 45, 40, 5, 0, -1, 91, -89, 179, 0]

The complete list: [[0, 179, -89], [0, 179, -89], [0, 179, -89], [0, 91, -1], [0, 91, -1], [0, 91, -1], 
			[1, 89, 0], [1, 89, 0], [1, 89, 0], [35, 55, 0], [35, 55, 0], [35, 55, 0], [23, 49, 18], 
			[23, 49, 18], [23, 49, 18], [40, 45, 5], [40, 45, 5], [40, 45, 5], [25, 45, 20], [25, 45, 20], 
			[25, 45, 20], [27, 40, 23], [27, 40, 23], [27, 40, 23], [30, 30, 30], [30, 30, 30], [30, 30, 30]]

The amount for each subset is: 90

Previous version: 3partition.py

	Total steps for all the functions to complete: 64
	Total steps for finding a match for all the subsets using the equation: 36

New version: 3partition_v_1_a.py

	Total steps for all the functions to complete: 58
	Total steps for finding a match for all the subsets using the equation: 30
```
Result: 
=====================
the difference: 36 = 90 - (49 + 5)
=====================
no match found
Skipped the number: 5 >>> 2 time(s)
because it's the same small number
=====================

=====================
the difference: 36 = 90 - (49 + 5)
=====================
no match found
Skipped the number: 5 >>> 2 time(s)
because it's the same small number
=====================

=====================
the difference: 36 = 90 - (49 + 5)
=====================
no match found
Skipped the number: 5 >>> 2 time(s)
because it's the same small number
=====================
            
```
