student = {
    "Lavanya": {"class": "B1", "height": 165, "weight": 55, "agility": 8, "speed": 7, "strength": 6},
    "Navya": {"class": "B2", "height": 175, "weight": 75, "agility": 6, "speed": 8, "strength": 7},
    "Nishtha": {"class": "B3", "height": 180, "weight": 85, "agility": 5, "speed": 6, "strength": 9},
}

def recommended_sport(student):
    if student['agility'] >= 7 and student['speed'] >= 7:
        return "Football"
    elif student['agility'] >= 6 and student['strength'] >= 7:
        return "Cricket"
    elif student['agility'] < 6 and student['strength'] >= 8:
        return "Javelin Throw"
    else:
        return "Chess"

def generated_diet_plan(student):
    if student['weight'] < 60:
        return "High-protein diet"
    elif student['weight'] <= 75:
        return "Balanced diet"
    else:
        return "Low-carb diet"

for name, details in student.items():
    sport = recommended_sport(details)
    diet_plan = generated_diet_plan(details)
    print(f"Student: {name}")
    print(f"Class: {details['class']}")
    print(f"Height: {details['height']} cm")
    print(f"Weight: {details['weight']} kg")
    print(f"Recommended Sport: {sport}")
    print(f"Diet Plan: {diet_plan}")
    print()
