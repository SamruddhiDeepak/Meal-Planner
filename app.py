from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS  
import random

app = Flask(__name__)

CORS(app)

@app.route('/generate-plan')

def generate_plan():
    file_path = "nutri2.csv"
    data = pd.read_csv(file_path)

    calorie_limit = 2000
    days = 7

    def knapsack(data, calorie_limit):
        breakfast_items = data[data['Type'] == 'Breakfast']
        other_items = data[data['Type'] == 'Other']

        selected_meals = []
        unique_meals = set()

        for _, breakfast in breakfast_items.iterrows():
            for i, dish1 in other_items.iterrows():
                for j, dish2 in other_items.iterrows():
                    if i != j:
                        dishes = [breakfast['Meal'], dish1['Meal'], dish2['Meal']]
                        if len(set(dishes)) < 3:
                            continue

                        total_calories = breakfast['Calories (kcal)'] + dish1['Calories (kcal)'] + dish2['Calories (kcal)']
                        total_score = breakfast['Score'] + dish1['Score'] + dish2['Score']

                        if total_calories <= calorie_limit or total_score >= 15:
                            meal_key = tuple(sorted(dishes))
                            if meal_key not in unique_meals:
                                unique_meals.add(meal_key)
                                selected_meals.append(dishes)

        return selected_meals
    


    def apply_nqueens(dishes, days):
        """
        Select unique dishes for a meal type (e.g. breakfasts) across given days
        """
        unique_dishes = list(set(dishes))
        if len(unique_dishes) < days:
            raise ValueError("Not enough unique dishes to arrange for the given number of days.")
        return unique_dishes[:days]


    def arrange_meals(meals, days):
        random.shuffle(meals)
        arranged = []

        for meal in meals:
            b, l, d = meal

        # If this is the first day, just add it
            if not arranged:
                arranged.append([b, l, d])
                continue

        # Get previous day's lunch and dinner
            prev_lunch = arranged[-1][1]
            prev_dinner = arranged[-1][2]

        # Ensure current day's meals do not repeat previous day's lunch/dinner
            if b not in [prev_lunch, prev_dinner] and l not in [prev_lunch, prev_dinner] and d not in [prev_lunch, prev_dinner]:
                arranged.append([b, l, d])

            if len(arranged) == days:
                break

        if len(arranged) < days:
            raise ValueError("Couldn't find enough non-repeating meals for all days.")

        return arranged


    selected_meals = knapsack(data, calorie_limit)

    if len(selected_meals) < days:
        return jsonify({"error": "Not enough unique meals to plan for 7 days."}), 400

    arranged_meals = arrange_meals(selected_meals, days)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    response = [{"day": weekdays[i], "breakfast": m[0], "lunch": m[1], "dinner": m[2]} for i, m in enumerate(arranged_meals)]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)