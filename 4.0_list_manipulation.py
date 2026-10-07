"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of customer service tasks and the number of cases handled.
# 2. Process: Sort the list by the number of cases and calculate the total.
# 3. Out: The sorted list, one selected task, and the total number of cases.
# 4. What my list is about, and what I computed from it:
# My list is about customer service tasks. I calculated the total number
# of cases because I want to know how many cases were handled in total.

tasks = [
    ("Refund requests", 35),
    ("Payment issues", 28),
    ("Delivery problems", 42),
    ("Account issues", 31),
    ("Order changes", 25),
    ("Returns", 38),
    ("Technical problems", 22),
    ("General questions", 30)
]

tasks.sort(key=lambda task: task[1], reverse=True)

print("Sorted list:")
for task in tasks:
    print(task)

print("Selected task:", tasks[0])

total_cases = sum(task[1] for task in tasks)
print("Total cases:", total_cases)
