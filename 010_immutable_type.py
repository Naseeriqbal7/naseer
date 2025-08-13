def double_the_number(value):
    value = value * 2
    return value

value1 = 25                         # global: value1
value2 = double_the_number(value1)  # global: value2
print("Value1:", value1)
print("Value2:", value2)
