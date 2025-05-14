import pytest
from workout_planner import calculate_bmi, get_workout_recommendation

# ---------- Test for BMI calculation ----------
def test_calculate_bmi_normal_case():
    assert calculate_bmi(70, 175) == 22.86

def test_calculate_bmi_underweight():
    assert calculate_bmi(45, 165) == 16.53

def test_calculate_bmi_overweight():
    assert calculate_bmi(85, 165) == 31.22

# ---------- Test for workout and diet recommendation ----------
@pytest.mark.parametrize("bmi, expected_workout, expected_diet", [
    (16.5, "30 mins light workout", "High-calorie diet with protein"),
    (22.0, "45 mins moderate workout", "Balanced diet with all nutrients"),
    (27.0, "60 mins cardio workout", "Low-carb, high-fiber diet"),
    (32.0, "75 mins intense workout", "Strict low-fat, high-protein diet"),
])
def test_get_workout_recommendation(bmi, expected_workout, expected_diet):
    workout, diet = get_workout_recommendation(bmi)
    assert workout == expected_workout
    assert diet == expected_diet