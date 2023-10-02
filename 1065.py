def namechi(num) :
    namechi_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            namechi_cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            namechi_cnt += 1
    return namechi_cnt

num = int(input())
print(namechi(num))