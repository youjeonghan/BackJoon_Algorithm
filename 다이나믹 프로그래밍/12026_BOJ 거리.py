# 실버 1레벨
# 다시 풀기

n = int(input())
st = input()
len_st = len(st)

idx_list = [[-1, -1, -1] for _ in range(len_st)]
value_list = [[0, 0, 0] for _ in range(len_st)]

idx_list[0][0] = 0
dic = {"B": 0, "O": 1, "J": 2}
for i in range(1, len_st):
    char_num = dic[st[i]]
    if idx_list[i - 1][(char_num + 2) % 3] == -1:
        pass
    else:
        width = i - idx_list[i - 1][(char_num + 2) % 3]
        idx_list[i][char_num] = i
        value_list[i][char_num] = value_list[i - 1][(char_num + 2) % 3] + width ** 2

    for j in range(3):
        idx_list[i][j] = max(idx_list[i - 1][j], idx_list[i][j])
        value_list[i][j] = max(value_list[i - 1][j], value_list[i][j])
print(idx_list)
print(value_list)
print(max(value_list[-1]))