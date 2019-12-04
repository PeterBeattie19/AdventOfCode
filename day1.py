def get_input():
    return [int(i) for i in open("day1_input.txt", "r")] 


def calc_fuel(mass):
    return int(mass/3) - 2 


def new_shite(mass):
    t = 0
    while True:
        mass = calc_fuel(mass)
        if mass <= 0:
            break
        t += mass
    return t


print(sum(list(map(new_shite, get_input()))))
