def get_input():
    return [int(i) for i in open("day1_input.txt", "r")] 

def calc_fuel(mass):
    return int(mass/3) - 2 


print(sum(list(map(calc_fuel, get_input()))))