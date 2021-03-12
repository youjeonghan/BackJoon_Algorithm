# def solution(name):
#     string = name
#     list_str = []
#     ch_cnt = 0
#     for i in range(len(string)):
#         list_str.append("A")

#     min = 15 * 20

#     # 알파벳 최소 변환 횟수
#     alphabet_min = 0
#     for i in range(len(string)):
#         up = ord(string[i]) - ord("A")
#         down = ord("Z") - ord(string[i]) + 1
#         alphabet_min = alphabet_min + (up if up < down else down)

#     # 커서 최소 이동 횟수
#     cursor_min = 0
#     check_list = ["A"] * len(string)
#     cnt = 0
#     temp_list = list(string[:])
#     temp_list[0] = "A"
#     for i in range(0, len(string)):
#         cnt += 1
#         if temp_list[i] != "A":
#             temp_list[i] = "A"

#         if temp_list == check_list:
#             # print(cnt)
#             cursor_min = cnt
#             cnt = 0
#             break

#     temp_list = list(string[:])
#     temp_list[0] = "A"
#     for i in range(len(string) - 1, -1, -1):
#         cnt += 1
#         if temp_list[i] != "A":
#             temp_list[i] = "A"

#         if temp_list == check_list:
#             # print(cnt)
#             cursor_min = (cnt) if (cnt) < cursor_min else cursor_min
#             break

#     # print("alphabet_min", alphabet_min)
#     # print("cursor_min", cursor_min)

#     for i in string:
#         if i != "A":
#             ch_cnt += 1

#     if ch_cnt == 0:
#         alphabet_min = 0
#         cursor_min = 0

#     print(alphabet_min + cursor_min)
#     return alphabet_min + cursor_min


# string = str(input())
# solution(string)


def solution(name):
    name = list(name)
    total = 0
    i = 0
    while True:
        # 상하 조작
        total += min(ord(name[i]) - 65, 91 - ord(name[i]))
        name[i] = "A"

        if name.count("A") == len(name):
            return print(total)

        # 좌우 조작
        right, left = 1, 1
        for m in range(1, len(name)):
            if name[i + m] == "A":
                right += 1
            else:
                break
        for m in range(1, len(name)):
            if name[i - m] == "A":
                left += 1
            else:
                break

        if left < right:
            i -= left
            total += left
        else:
            i += right
            total += right


string = str(input())
solution(string)