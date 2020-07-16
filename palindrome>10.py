"""
Author  : Vivek Shinde
Date    :07/06/2020
purpose : Practice problem solving
code    : To take size of list as input & make corresponding list.print list of those palindrome number which are
          greater than 10 or else print that number
"""

user_input_test_case = int(input('Enter your number of test cases : '))

# Create an empty list to store the elements in list one by one
mylist = []
"""
create an empty list to store the (palindrome number)number less than 10 & the value which is not palindrome comes from
that below while loop till it becomes palindrome
"""
new_list = []
for i in range(user_input_test_case):
    user_input_number = int(input('Enter number :'))

    # All the elements get added one by one as for loop gets repeated
    mylist.append(user_input_number)

for i in mylist:
    # convert int i to string for escaping from nonscriptable error
    reverse_str = str(i)[::-1]
    if str(i) == reverse_str:
        # To store current single digit value of i in single_digit_number
        single_digit_number = i
        # Adds the value of single_digit_number to print the new_list
        new_list.append(single_digit_number)
    else:
        while True:
            i = int(i) + 1
            reverse_str = str(i)[::-1]
            if str(i) == reverse_str:
                # Adds the value of i to new_list to print the new_list
                new_list.append(i)
                break
print(f'\nInput  : {mylist}')
print(f'Output : {new_list}')
