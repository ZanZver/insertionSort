import timeit
def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            # swap the current value one space left
            tmp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = tmp
            j -= 1

lis = [4,1,7,5,2]
print(lis)
start_time = timeit.default_timer()
elapsed = timeit.default_timer() - start_time
insertion_sort(lis)
print(elapsed)
print(lis)