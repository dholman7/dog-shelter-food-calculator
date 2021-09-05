# Dog Shelter Food Calculator
You are the owner of a dog shelter that can hold at most 30 dogs. You want a
programmatic way to order the necessary amount of food for next month based on how
many dogs you currently have and the remaining food from last month.

Sizes of dogs and food needs:
- Small - 10lbs.,
- Medium - 20lbs.,
- Large - 30lbs.

When ordering food you always want to order at least 20% more than the minimum needed
to feed all dogs currently in your shelter for that month.

**Example:**
If at the end of the month I have 5 small dogs, 3 medium dogs, 7 large dogs, and a leftover
food supply of 17lbs. I should expect the function would tell me to order 363.6 lbs.

### Dependencies
- Clone repository `git clone git@github.com:dholman7/dog-shelter-food-calculator.git`
- Install Python 3.8 or above
- Install dependencies `pip install -r requirements.txt`

### Run Program
From the root project directory: `python3 food_calculator.py`

### Running Tests
From the root project directory: `pytest -v tests`

### Test Cases Not Covered in AC
- Possible shortages due to variances in average amount of dogs the previous month
- Variances in the monthly order cycle due to months having more or less days.
- Assumption: The 20% additional food covers for the slight variances mentioned above. 
- Assumption: In the case of food excess we will order no food.

### Questions
see [QUESTIONS.md](QUESTIONS.md)