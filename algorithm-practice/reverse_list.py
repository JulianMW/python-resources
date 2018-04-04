def reverse_iter(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-1*(i+1)] = lst[-1*(i+1)], lst[i]
return lst
