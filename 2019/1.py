from math import floor

class Module():
    def __init__(self, mass):
        self.mass = mass
        
    def get_required_fuel(self):
        return floor(self.mass/3.) - 2
    
assert Module(12).get_required_fuel() == 2
assert Module(14).get_required_fuel() == 2
assert Module(1969).get_required_fuel() == 654
assert Module(100756).get_required_fuel() == 33583



# second part

masses = []

def total_fuel(mass):
    fuel = floor(mass/3.) - 2
    if fuel > 0 :
        fuel += total_fuel(more_fuel)
        return fuel
    return 0

assert total_fuel(14) == 2
assert total_fuel(1969) == 966
assert total_fuel(100756) == 50346

print(sum(total_fuel(m) for m in masses))