def this_fails():
    x = 1 / 0


def sum_number():
    result = 'a' + b


# exception 1
try:
    this_fails()
except:
    print("error! Division by zero! (this_fails method)")

# exception 2
try:
    sum_number()
except:
    print("error! Has an element of different type! (sum_number method)")

# exception 3
try:
    open('duc.txt')
except:
    print("file duc.txt does not exist!")
