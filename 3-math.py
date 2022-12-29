# 8  +  2  =  16106
# 5  +  4  =  2091
# 9  +  6  =  54153
# 7  +  5  =  35122
# 20  +  3  =  ??????

def get_resultado(a, b):
    return str(a * b) + str(a + b) + str(a - b)

def print_resultado(a, b):
    print(a, " + ", b, " = ", get_resultado(a, b))

print_resultado(8, 2)
print_resultado(5, 4)
print_resultado(9, 6)
print_resultado(7, 5)
print_resultado(20, 3)

# 8  +  2  =  16106
# 5  +  4  =  2091
# 9  +  6  =  54153
# 7  +  5  =  35122
# 20  +  3  =  602317