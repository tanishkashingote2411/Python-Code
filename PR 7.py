def calculate_calories(carbs, fats, proteins):
    return carbs * 4 + fats * 9 + proteins * 4

carbs = float(input("Enter carbs (g): "))
fats = float(input("Enter fats (g): "))
proteins = float(input("Enter proteins (g): "))

total = calculate_calories(carbs, fats, proteins)

print("Total Calories:", total)