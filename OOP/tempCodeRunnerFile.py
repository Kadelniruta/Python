def odd(x):
    return True if x%2 == 0 else False

numbers= [ 1,2,3,4,5,6,7,8,9,10]
filtered_items = filter(odd, numbers)
print(list[filtered_items])
    