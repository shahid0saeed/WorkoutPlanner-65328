def calculate_bmi(weight, height_cm):
    """Calculates BMI from weight (kg) and height (cm)."""
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_workout_recommendation(bmi):
    """Returns workout duration and diet recommendation based on BMI."""
    if bmi < 18.5:
        return "30 mins light workout", "High-calorie diet with protein"
    elif 18.5 <= bmi < 25:
        return "45 mins moderate workout", "Balanced diet with all nutrients"
    elif 25 <= bmi < 30:
        return "60 mins cardio workout", "Low-carb, high-fiber diet"
    else:
        return "75 mins intense workout", "Strict low-fat, high-protein diet"

def main():
    try:
        weight = float(input("Enter your weight (kg): ").strip())
        height = float(input("Enter your height (cm): ").strip())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        workout, diet = get_workout_recommendation(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Recommended Workout: {workout}")
        print(f"Suggested Diet Plan: {diet}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
