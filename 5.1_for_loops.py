"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# My list of customer support problems and the number of cases.

# 2. Process:
# I go through each item in the list and calculate its percentage of the total.

# 3. Out:
# One line for each problem with its position, number of cases and percentage.

# 4. What I compute for each item, and why it is worth showing:
# I show the position and the percentage of the total cases.
# This makes it easier to see which problems happen more often.


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

total = sum(item[1] for item in cases)

for position, item in enumerate(cases, 1):
    name = item[0]
    number = item[1]
    percentage = number / total * 100

    print(position, name, number, round(percentage, 1), "%")
