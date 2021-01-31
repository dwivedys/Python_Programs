'''A Simple Sorting Program - sorts in ascending order'''

my_list = [1,3,2,9,7,22]
l = len(my_list)
for i in range(0, l):
    for j in range(i+1, l):
        if my_list[j] >= my_list[i]:
            continue
        else:
            swap_var = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = swap_var
print(my_list)

            
