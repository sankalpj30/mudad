import pandas as pd
import streamlit as st
import plotly.graph_objects as go


result = pd.read_csv('data.csv')
lr = result.index[-1]
last_row = result.tail(1)
# st.dataframe(last_row)

credit_score = last_row['Final Marks'][lr]



# Create a new page
st.title(":red[Mala Credit Score]")

# Display the credit score
st.write("Your mala credit score is:", credit_score)



fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = credit_score,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Risk-O-Meter", 'font': {'size': 24, 'color':'white'}},
    # delta = {'reference': 4, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 5], 'tickwidth': 1, 'tickcolor': "Red"},
        'bar': {'color': "black"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 1], 'color': '#5ec214'},
            {'range': [1, 2], 'color': '#bdd527'},
            {'range': [2, 3], 'color': '#ffd507'},
            {'range': [3, 4], 'color': '#fe5502'},
            {'range': [4, 5], 'color': '#df0003'}],
        'threshold': {
            'line': {'color': "white", 'width': 4},
            'thickness': 0.75,
            'value': 490}}))

fig.update_layout(paper_bgcolor = "#0e1117", font = {'color': "white", 'family': "Arial"})

# fig.show()

st.plotly_chart(fig)



# Add some congratulations
if credit_score >= 3:
    st.success("Congratulations! Your credit score is excellent.")
    st.write("🎉 🎉 🎉")
    st.snow()
else:
    st.warning("Your credit score is good but you may want to improve it.")
    

