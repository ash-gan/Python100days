
def calculate_life_in_weeks(current_age):
    max_age = 90
    remaining = {}
    remaining_years = max_age-current_age
    remaining["month"] = remaining_years*12
    remaining["week"] = remaining_years*52
    remaining["day"]=remaining_years*365
    return remaining

current_age = int(input("what's your current age?: "))
remaining = calculate_life_in_weeks(current_age)
remaining_days,remaining_weeks, remaining_months  = remaining['day'], remaining['week'], remaining['month']
print(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")


