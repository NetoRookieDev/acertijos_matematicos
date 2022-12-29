# 2  +  3  =  10
# 6  +  5  =  66
# 8  +  4  =  96
# 7  +  2  =  63
# 9  +  7  =  ??

def get_octava(a, b):
    return a * (a + b)

def print_octava(a, b):
    print(a, " + ", b, " = ", get_octava(a, b))

print_octava(2, 3)
print_octava(6, 5)
print_octava(8, 4)
print_octava(7, 2)
print_octava(9, 7)

# 2  +  3  =  10
# 6  +  5  =  66
# 8  +  4  =  96
# 7  +  2  =  63
# 9  +  7  =  144