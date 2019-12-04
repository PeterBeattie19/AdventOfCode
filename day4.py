import collections


def read_input():
    return list(map(int, open("day4_input.txt", "r").read().split(",")))


def verify(value):
    if len(str(value)) != 6:
        return False
    if sorted(list(str(value))) != list(str(value)):
        return False
    st = set()
    for i in str(value):
        if i in st:
            return True
        else:
            st.add(i)
    return False


def check_consec(lst):
    cntr = 1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            cntr += 1
        if lst[i] != lst[i+1]:
            if cntr == 2:
                return True
            cntr = 1
    return False if cntr != 2 else True


def verify_2(value):
    if len(str(value)) != 6:
        return False
    if sorted(list(str(value))) != list(str(value)):
        return False
    return check_consec(list(str(value)))


cnt = 0
for i in range(*read_input()):
    cnt += 1 if verify_2(i) else 0

print(cnt)
