"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# My list of customer support problems and the number of cases.

# 2. Process:
# I make different versions of the list without changing the first one.

# 3. Out:
# The list in four different orders and the original list at the end.

# 4. My four orders, and which ones modify the original:
# I used reverse order, alphabetical order, highest number first,
# and lowest number first. I used copies so the original stays the same.


cases = [
    ("Delivery problems", 42),
    ("Returns", 38),
    ("Refund requests", 35),
    ("Account issues", 31),
    ("General questions", 30),
    ("Payment issues", 28),
    ("Order changes", 25),
    ("Technical problems", 22)
]

print("Original list:")
print(cases)

# Reverse the list
reverse_list = cases.copy()
reverse_list.reverse()
print("\nReverse order:")
print(reverse_list)

# Put the names in alphabetical order
alphabetical_list = sorted(cases)
print("\nAlphabetical order:")
print(alphabetical_list)

highest_list = sorted(cases, key=lambda x: x[1], reverse=True)
print("\nHighest number first:")
print(highest_list)

lowest_list = sorted(cases, key=lambda x: x[1])
print("\nLowest number first:")
print(lowest_list)

print("\nOriginal list at the end:")
print(cases)
