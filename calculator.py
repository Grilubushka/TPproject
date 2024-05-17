# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# класс блюда
class Meal:
    def __init__(self, name, calories, protein, fat, carbohydrates, vitamins):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.vitamins = vitamins

    def __str__(self):
        return f"{self.name}: {self.calories} ккал, Белки: {self.protein} г, Жиры: {self.fat} г, Углеводы: {self.carbohydrates} г, Витамины: {', '.join(self.vitamins)}"

# функция расчета дневного потребления каллорий
def calculate_bmr(weight, age, gender, height):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Please specify 'male' or 'female'.")
    return bmr
#функция учитывает уровень физических нагрузок в виде к коэфцентов к БМР (дневное потребление каллорий)
def calculate_daily_calories(bmr, activity_level):
    activity_levels = {
        'сидячий': 1.2,
        'редкие физические нагрузки': 1.375,
        'постоянные тренировки': 1.55
    }
    if activity_level not in activity_levels:
        raise ValueError("Invalid activity level. Please choose from: 'сидячий', 'редкие физические нагрузки', 'постоянные тренировки'")
    return bmr * activity_levels[activity_level]

def distribute_calories(meal_calories):
    breakfast_ratio = 0.25  # Процент калорий, приходящийся на завтрак
    lunch_ratio = 0.35      # Процент калорий, приходящийся на обед
    dinner_ratio = 0.40     # Процент калорий, приходящийся на ужин

    breakfast_calories = meal_calories * breakfast_ratio
    lunch_calories = meal_calories * lunch_ratio
    dinner_calories = meal_calories * dinner_ratio

    return breakfast_calories, lunch_calories, dinner_calories

def select_meals(breakfast_calories, lunch_calories, dinner_calories, breakfast_meals, lunch_meals, dinner_meals, drink_meals):
    # Выбираем блюдо для завтрака
    selected_breakfast = None
    for meal in breakfast_meals:
        if meal.calories <= breakfast_calories:
            selected_breakfast = meal
            break

    # Выбираем блюдо для обеда
    selected_lunch = None
    for meal in lunch_meals:
        if meal.calories <= lunch_calories:
            selected_lunch = meal
            break

    # Выбираем блюдо для ужина
    selected_dinner = None
    for meal in dinner_meals:
        if meal.calories <= dinner_calories:
            selected_dinner = meal
            break

    # Выбираем напиток
    selected_drink = None
    for drink in drink_meals:
        if drink.calories <= 100:  # Предположим, что максимальная калорийность напитка 100 ккал
            selected_drink = drink
            break

    return selected_breakfast, selected_lunch, selected_dinner, selected_drink

def main():
    #набиваем базу блюдами (пока для примера)
    # Создаем экземпляры блюд
    breakfast1 = Meal("Яичница с помидорами", 150, 15, 25, 10, ["A", "B6", "C"])
    breakfast2 = Meal("Овсянка с фруктами", 200, 10, 10, 50, ["B1", "B2", "E"])
    lunch1 = Meal("Куриный салат", 250, 30, 20, 15, ["A", "C", "K"])
    lunch2 = Meal("Паста с тунцом", 150, 20, 15, 60, ["B3", "E", "K"])
    dinner1 = Meal("Рыбный тефтели", 380, 25, 18, 20, ["D", "B12", "K"])
    dinner2 = Meal("Тушеные овощи", 250, 5, 10, 40, ["C", "E"])

    # Создаем экземпляры напитков
    drink1 = Meal("Зеленый чай", 20, 0, 0, 5, ["C", "E"])
    drink2 = Meal("Смузи с молоком", 150, 5, 5, 30, ["A", "B6"])

    # Создаем списки для каждого приема пищи
    breakfast = [breakfast1, breakfast2]
    lunch = [lunch1, lunch2]
    dinner = [dinner1, dinner2]
    drinks = [drink1, drink2]


    weight = float(input("Введите ваш вес в кг: "))
    age = int(input("Введите ваш возраст в годах: "))
    gender = input("Введите ваш пол ('male' или 'female'): ").lower()
    height = float(input("Введите ваш рост в см: ")) / 100  # конвертируем в метры
    activity_level = input("Введите ваш уровень физической активности ('сидячий', 'редкие физические нагрузки', 'постоянные тренировки'): ").lower()

    bmr = calculate_bmr(weight, age, gender, height)
    daily_calories = calculate_daily_calories(bmr, activity_level)
    print("Ваша суточная норма калорий:", daily_calories)

    breakfast_calories, lunch_calories, dinner_calories = distribute_calories(daily_calories)
    print("Завтрак:", breakfast_calories, "ккал")
    print("Обед:", lunch_calories, "ккал")
    print("Ужин:", dinner_calories, "ккал")

    selected_breakfast, selected_lunch, selected_dinner, selected_drink = select_meals(breakfast_calories,
                                                                                       lunch_calories, dinner_calories,
                                                                                       breakfast, lunch,
                                                                                       dinner, drinks)

    # Выводим выбранные блюда и напиток
    print("Завтрак:", selected_breakfast)
    print("Обед:", selected_lunch)
    print("Ужин:", selected_dinner)
    print("Напиток:", selected_drink)

if __name__ == "__main__":
    main()
