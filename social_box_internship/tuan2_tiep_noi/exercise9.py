# F(0) = 1
# F(x) = F(x-1) + 3
def F(x):
    if x == 0:
        return 1
    return F(x - 1) + 3


print(F(10))


# convert to binary

def cvt_to_binary(number):
    if number <= 1:
        return str(number)
    return cvt_to_binary(int(number/2)) + str(number%2)

print(cvt_to_binary(12))