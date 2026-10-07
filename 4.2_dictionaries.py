"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed in. The product details are written straight into the
#    dictionary (one Maison Leon shirt).
# 2. Process: read a couple of fields, change the price, remove the fabric
#    field, then loop through whatever is left.
# 3. Out: the product's fields and values printed one per line, plus a
#    message when I ask for a field that isn't there.
# 4. My object, my five fields, and why those:
#    Object is one product from Maison Leon, an overcoat.
#    - name: so I know which product it is
#    - fabric: customers always ask what it's made of
#    - price: I need it for margins and for the listing
#    - sizes: needed so we know what can be ordered
#    - stock: tells me when to reorder from the supplier

# Your code below

product = {
    "name": "Paris Overcoat",
    "fabric": "wool blend",
    "price": 8999,
    "sizes": ["S", "M", "L", "XL"],
    "stock": 24,
}

# read it
print("Product:", product["name"])
print("Price:", product["price"])

# change it (price goes up a bit)
product["price"] = 9499
print("New price:", product["price"])

# remove one field
del product["fabric"]

# show everything that's left
print("\nAll fields now:")
for key, value in product.items():
    print(key, "->", value)

# check it yourself: asking for a field that doesn't exist
# product["colour"] crashes the program with a KeyError, because
# there's no "colour" key in the dictionary.
# .get() fixes it, it gives back a default instead of crashing.
colour = product.get("colour", "not listed")
print("\nColour:", colour)
