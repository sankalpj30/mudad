import pandas as pd
import random

data = pd.read_csv('data.csv')
lri = data.index[-1]

#Dictionary of the last users input
last_r = data.tail(1).to_dict()
name = last_r['First Name'][lri]
base_salary = last_r['Base Salary'][lri]

#Calculating Spending Marks
s_marks = random.randint(50,90)
if base_salary > 50000:
    s_marks -= 5
elif base_salary > 30000:
    s_marks -= 10
else:
    s_marks -= 15


#Calculating personality test
p_marks = 0

for i in range(1, 11):
    ans = last_r['Question ' + str(i)][lri]
    # case statement
    if(i==2 or i==3 or i==5):
        if ans == 'Strongly Agree':
            p_marks += 20 
        elif ans == 'Somewhat Agree':
            p_marks += 40
        elif ans == 'Neutral':
            p_marks += 60
        elif ans == 'Somewhat Disagree':
            p_marks += 80
        else:
            p_marks += 100
    else:
        if ans == 'Strongly Agree':
            p_marks += 100 
        elif ans == 'Somewhat Agree':
            p_marks += 80
        elif ans == 'Neutral':
            p_marks += 60
        elif ans == 'Somewhat Disagree':
            p_marks += 40
        else:
            p_marks += 20

p_marks = p_marks/10

#Credit Score Marks
c_marks = last_r['Credit Score'][lri]/10



score = (s_marks * 50/100)  + (p_marks * 30/100) + (c_marks * 20/100)

final_score = int(score * 5/100)



data.loc[lri, ["Credit Marks", "Personality Marks", "Spending Marks", "Final Marks"]] = [c_marks, p_marks, s_marks, final_score]
    
data.to_csv('data.csv', index=False)
