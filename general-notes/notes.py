# Comparisons
# ------------------------------------------------ #

# check if a list is empty
if not my_list:
    #actionA
    pass
else:
    #actionB
    pass
    
    
# check type (ex. is it a list or a dict)
my_list = [1,2,3]
non_list = {'a':1}
if isinstance(my_list, (list,)):
    ## This code will execute
if isinstance(non_list, (list,)):
    ## This code will NOT execute




# Built-ins
# ------------------------------------------------ #

# enumerate()
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_start_value = 1
for counter, value in enumerate(my_list, counter_start_value):
    print(counter, value)
# Output:
# 1 apple
# 2 banana etc...




# Lists
# ------------------------------------------------ #

# 'mylist.remove(value)' removes the first matching value, not a specific index:
# 'del mylist[index]' removes the item by index
