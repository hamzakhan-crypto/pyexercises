"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a size typed by the user (S, M, L or XL), asked again if it's wrong.
# 2. Process: clean up the answer (remove spaces, make it capitals), check
#    it against the list of sizes, count each try, keep the wrong ones.
# 3. Out: a message after each wrong answer, then a summary at the end.
# 4. My stop condition, my attempt limit, my summary:
#    Stop condition: the user enters a size that is in the list (S, M, L, XL).
#    Attempt limit: 5. After 5 wrong answers the program gives up so it
#    can't run forever, and tells the user to contact support.
#    Summary: whether a size was picked, which size, how many attempts it
#    took, and the wrong answers they typed.
#    Cleaning the answer: " xl ", "Xl" and "XL" all count as the same size,
#    because a customer shouldn't get rejected over a space or a capital.

# Your code below

valid_sizes = ["S", "M", "L", "XL"]
max_attempts = 5

attempts = 0
wrong_answers = []
chosen_size = None

while attempts < max_attempts and chosen_size is None:
    answer = input("Enter your size (S, M, L, XL): ")
    attempts += 1

    cleaned = answer.strip().upper()

    if cleaned in valid_sizes:
        chosen_size = cleaned
    else:
        wrong_answers.append(answer)
        print("That's not a size we stock, try again.")

print("\n--- Summary ---")
if chosen_size is not None:
    print("Size chosen:", chosen_size)
else:
    print("No valid size after", max_attempts, "tries. Please contact support.")
print("Attempts used:", attempts)
print("Wrong answers:", wrong_answers)

# Checked it two ways:
# - gave 5 wrong answers in a row: it stopped at attempt 5, as intended
# - typed "  xl " with spaces and lowercase: it accepted it as XL
