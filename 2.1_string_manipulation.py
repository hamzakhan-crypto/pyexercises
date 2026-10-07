"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# A sentence entered by the user.
#
# 2. Process:
# The program changes the sentence in four different ways using string methods.
#
# 3. Out:
# Four transformed versions of the sentence.
# 
# 4. My four transformations, and when each is useful:
# strip() - removes extra spaces at the beginning and end of a sentence.
# lower() - makes all letters lowercase, useful for comparing text.
# upper() - makes all letters uppercase, useful when text needs to stand out.
# title() - makes the first letter of each word uppercase, useful for titles or headings.


sentence = input("Enter a sentence: ")

print("Without extra spaces:", sentence.strip())
print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())
print("Title case:", sentence.title())


# Check:
# I tested the program with spaces at both ends and a capital letter in the middle.
# strip() worked as expected because the spaces at the ends were removed.
# lower() worked as expected because all letters became lowercase.
# upper() worked as expected because all letters became uppercase.
# title() worked as expected because the first letter of each word became uppercase.
