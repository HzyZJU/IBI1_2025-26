#Practical8 Task2

class Food_Item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_totals(food_list):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    print("Daily Nutrition Report")
    print(f"Total calories: {total_calories:.1f} kcal")
    print(f"Total protein: {total_protein:.1f} g")
    print(f"Total carbohydrates: {total_carbs:.1f} g")
    print(f"Total fat: {total_fat:.1f} g")

    #Warnings
    if total_calories > 2500:
        print(f"Warning: Calorie intake ({total_calories:.1f} kcal) exceeds 2500 kcal ")
    else: 
        print(f"Your calorie intake are within healthy limits.")

    if total_fat > 90:
        print(f"Warning: Fat intake ({total_fat:.1f} g) exceeds 90 g")
    else:
        print("Your fat intake are within healthy limits.")
        
    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbs": total_carbs,
        "fat": total_fat
    }

# Example shown
if __name__ == "__main__":
    apple = Food_Item("Apples", 60, 0.3, 15, 0.5)
    chicken = Food_Item("Chicken", 165, 31, 0, 3.6)
    rice = Food_Item("Rice", 130, 2.7, 28, 0.3)
    cake = Food_Item("Cake", 350, 4, 45, 15)
    cheeseburger = Food_Item("Cheeseburger", 500, 30, 40, 25)
    milk = Food_Item("Whole Milk (250ml)", 150, 8, 12, 8)
    medium_fries = Food_Item("French Fries (medium)", 365, 4, 48, 17)
    daily_meals = [apple, chicken, rice, apple, cake, chicken, cheeseburger, milk, medium_fries]
    totals = calculate_daily_totals(daily_meals)