# https://www.acmicpc.net/problem/1427

num_element_list = list(map(int, list(input())))

sorted_string_num_list = list(map(str, sorted(num_element_list, reverse=True)))
print("".join(sorted_string_num_list))
