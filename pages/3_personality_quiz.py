import pandas as pd
import streamlit as st


result = pd.read_csv('data.csv')
lr = result.index[-1]
last_row = result.tail(1)
# st.dataframe(last_row)


# Question 1
question_1 = "Have you paid your all yours bills on time (conscientiousness)"
options_1 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 2
question_2 = "How often do you neglect others needs and spend more on yourself? (agreeableness)"
options_2 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 3
question_3 = "Do you shop or buy so much that it negatively effects your daily obligations (like loan repayments)? (Extraversion)"
options_3 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 4
question_4 = "How often do you anxious about your repayments? (Neuroticism)"
options_4 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 5
question_5 = "Most of the time, I avoid taking responsibilities? (Neuroticism)"
options_5 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 6
question_6 = "Making repayments is my first priority? (Conscientiousness)"
options_6 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 7
question_7 = "I am willing to repay my loan on time, in order to reduce my debt. (Agreeableness)"
options_7 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 8
question_8 = "If you have a car breakdown and at the same time, your loan repayment arrive!! What will you do? (Openness)"
options_8 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 9
question_9 = "I am good at handling social situations. (Extraversion)"
options_9 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]

# Question 10
question_10 = "How do you adjust to new changes when you have no control over them? (Openness)"
options_10 = ["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"]



# Personality Test
st.title(":red[Personality Test]")
st.header("Hi " + result.iloc[-1,0])


q1_answer = st.selectbox(question_1, options_1)
q2_answer = st.selectbox(question_2, options_2)
q3_answer = st.selectbox(question_3, options_3)
q4_answer = st.selectbox(question_4, options_4)
q5_answer = st.selectbox(question_5, options_5)
q6_answer = st.selectbox(question_6, options_6)
q7_answer = st.selectbox(question_7, options_7)
q8_answer = st.selectbox(question_8, options_8)
q9_answer = st.selectbox(question_9, options_9)
q10_answer = st.selectbox(question_10, options_10)


if st.button('Submit'):
    result.loc[lr, ["Question 1", "Question 2" , "Question 3" , "Question 4", "Question 5",
                    "Question 6", "Question 7","Question 8", "Question 9", "Question 10"]] = [q1_answer
                    , q2_answer , q3_answer,q4_answer, q5_answer, q6_answer, q7_answer, q8_answer, q9_answer, q10_answer]
    
    result.to_csv('data.csv', index=False)

    st.write("Your Response has been submitted")
