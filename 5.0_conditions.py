"""Exercise 5.0 — Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the order value in rupees, typed by the user.
# 2. Process: check which range the value falls in, starting from the
#    lowest, and pick the matching discount tier.
# 3. Out: one message saying what the customer gets on that order.
# 4. My ranges, my boundaries, my messages:
#    Below 5000      -> no offer, just nudge them to add something
#    5000 to 9999    -> free shipping
#    10000 to 19999  -> free shipping + 10% off
#    20000 and above -> free shipping + 15% off
#    Why these cut-offs: 5000 is about one shirt plus an accessory,
#    10000 is roughly two pieces, 20000 is an overcoat plus something
#    else, so each tier pushes the customer to add one more item.
#    A value exactly on the boundary goes to the HIGHER range
#    (5000 gets free shipping, 10000 gets the 10%, 20000 gets the 15%),
#    because the customer has reached that amount, so they get the reward.

# Your code below

order = float(input("Enter the order value in rupees: "))

if order < 0:
    print("An order value can't be negative, check the number.")
elif order < 5000:
    print("No offer on this one. Add a little more to get free shipping.")
elif order < 10000:
    print("Free shipping on your order.")
elif order < 20000:
    print("Free shipping and 10% off your order.")
else:
    print("Free shipping and 15% off your order.")

# Boundary check (ran each of these):
# 4999  -> no offer, as intended (just under 5000)
# 5000  -> free shipping, as intended (boundary goes up)
# 9999  -> free shipping, as intended
# 10000 -> 10% off, as intended
# 19999 -> 10% off, as intended
# 20000 -> 15% off, as intended
