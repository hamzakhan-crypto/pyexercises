"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a message and the number 5 (how many times to show it)
# 2. Process: count from 1 to 5 and print the number next to the message each time
# 3. Out: 5 lines on the screen, numbered 1 to 5
# 4. My message, and why:"Start the work now".
#    I chose it because  I often wait too long before starting something.
# so this is what I'd want my program to tell me.

message = "Start the work now."
times = 5
for i in range(1, times+1):
    print(f"{i}. {message}")
