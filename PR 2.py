GRAVITY_EARTH = 9.81
GRAVITY_MOON = 1.62

def calculate_weight(mass, gravity):
    weight = mass * gravity
    return weight

mass = float(input("Enter mass in kg: "))
layout = "Earth and Moon"

print("Earth weight:", calculate_weight(mass, GRAVITY_EARTH))
print("Moon weight:", calculate_weight(mass, GRAVITY_MOON))

# Answers:
# 1. Constant identifier: GRAVITY_EARTH
# 2. User-defined function: calculate_weight
# 3. Data type of layout: String (str)
# 4. Parameter: mass
# 5. Arithmetic operator: *