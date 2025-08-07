def binary_search(search_list:list,item:int)->int | None:
    low = 0
    high = len(search_list) -1

    while low <= high:
        half = int((low + high) / 2)
        bid = search_list[half]

        if bid == item:
            return half
        if bid > item:
            high = half - 1
        else:
            low = half +1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,3))
print(binary_search(my_list,-1))


