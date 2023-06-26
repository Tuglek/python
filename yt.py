def get_avg_unigue(lst1,lst2):
    numbers = dict()
    numbers2 = dict()
    for num in lst:
        if num not in numbers:
            numbers[num] = 1
        else:
            numbers[num] +=1
    for num in lst2:
        if num not in numbers2:
            numbers2[num] = 1
        else:
            numbers2[num] +=1
    unigue = [key for key in numbers if numbers[key]==1]
    unigue2 = [key for key in numbers2 if numbers2[key]==1]
    if not unigue:
        return 0
    return round(sum(unigue+unigue2) / len(unigue+unigue2) , 1)
lst = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
print(get_avg_unigue(lst,lst2))
