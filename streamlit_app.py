import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open('employee_performance_prediction_model.pkl', 'rb'))

st.title('Employee Performance Prediction Form')

# Creating input widgets
department = st.selectbox('Department', ['Sales & Marketing', 'Operations', 'Procurement', 'Technology', 'Analytics', 'Finance', 'HR', 'R&D', 'Legal'])
no_of_trainings = st.number_input('Number of Trainings', min_value=1, max_value=5, value=1, step=1)
region_options = [f'region_{i}' for i in range(1, 35)]
region = st.selectbox('Region', options=region_options)
education = st.selectbox('Education', ["Bachelor's", "Master's & above", "Below Secondary", "Others"])
gender = st.selectbox('Gender', ['Male', 'Female'])
recruitment_channel = st.selectbox('Recruitment Channel', ['Other', 'Sourcing', 'Referred'])
age = st.number_input('Age', min_value=20, max_value=60, value=20, step=1)
previous_year_rating = st.number_input('Previous Year Rating', min_value=1, max_value=5, value=1, step=1)
length_of_service = st.number_input('Length of Service', min_value=1, max_value=32, value=1, step=1)
awards_won = st.selectbox('Awards Won', [0, 1])
avg_training_score = st.number_input('Average Training Score', min_value=1, max_value=100, value=1, step=1)

# Processing the prediction when the user changes any input
input_data = {
    'no_of_trainings': [no_of_trainings],
    'age': [age],
    'previous_year_rating': [previous_year_rating],
    'length_of_service': [length_of_service],
    'awards_won': [awards_won],
    'avg_training_score': [avg_training_score],
    'department': [department],
    'region': [region],
    'education': [education],
    'gender': [gender],
    'recruitment_channel': [recruitment_channel]
}

input_df = pd.DataFrame.from_dict(input_data)

# Display button and make prediction
if st.button('Predict Performance'):
    prediction = model.predict(input_df)
    output = 'High Performance' if prediction[0] == 1 else 'Low Performance'
    st.write('Employee Performance Prediction: ', output)
