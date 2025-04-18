# 🥗 7-Day Meal Planner

A smart, deterministic weekly meal planning web app that generates a diverse and nutritionally balanced 7-day meal plan using classic algorithms!

## 📌 Features

- Creates a **7-day meal plan** (breakfast, lunch, dinner)
- Uses **Knapsack algorithm** to ensure meals stay within a calorie limit
- Applies an **N-Queens-inspired variety constraint** to prevent meal repetition
- Fully offline-capable once deployed

## 🧠 Algorithms Used

- **Knapsack Algorithm**: Selects meals that optimize for nutritional score while staying under a daily calorie limit.
- **N-Queens-Inspired Logic**: Ensures no meal type is repeated consecutively across days.

## ⚙️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Data Handling**: `pandas`, `random`
- **Cross-Origin Requests**: Handled using `Flask-CORS`

## Folder Structure

```
📁 project-root
├── nutri2.csv               # Dataset of meals with calorie and score info
├── app.py                   # Flask backend with algorithm logic
├── index.html               # Front page with "Generate Plan" button
├── meal-plan.html            # Result page that shows the generated meal plan
├── requirements.txt         # Python dependencies
```

## How to Run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask backend**  
   ```bash
   python app.py
   ```

3. **Open `index.html`** in your browser and click “Generate Plan”.
