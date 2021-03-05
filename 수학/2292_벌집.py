# 브론즈 2레벨      벌집

N = int(input())
cross = 1
flag = 1
add_flag = 0
while flag < N:
    add_flag += 6
    flag += add_flag
    cross += 1

print(cross)