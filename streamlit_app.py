import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model_data = pickle.load(open('employee_performance_prediction_model.pkl', 'rb'))
model = model_data['model']
model_accuracy = model_data['accuracy']
# Assuming 'logo.png' is the path to your logo image file
st.sidebar.image('logo.png', use_column_width=True)

# Using columns to create a layout for logo next to the title
col1, col2 = st.beta_columns([1, 8])

with col1:
    # Display logo in the first column
    st.image('logo.png', width=100)

with col2:
    # Display the title in the second column
    st.title('Employee Performance Prediction Form')

# Replace selectbox with st.radio
department = st.selectbox('Select your department', ['Sales & Marketing', 'Operations', 'Procurement', 'Technology', 'Analytics', 'Finance', 'HR', 'R&D', 'Legal'])

# Rest of your st.radio widgets replacing selectbox...
education = st.selectbox('Select your education status', ["Bachelor's", "Master's & above", "Below Secondary", "Others"])
gender = st.radio('Gender', ['Male', 'Female'])
recruitment_channel = st.selectbox('Select your recruitment channel', ['Other', 'Sourcing', 'Referred'])
awards_won = st.radio('Awards Won', [0, 1])

# Replace number_input with st.slider
no_of_trainings = st.slider('Number of Trainings', 1, 5, 1)

region_options = [f'region_{i}' for i in range(1, 35)]
region = st.selectbox('Region', options=region_options)

education = st.selectbox('Education', ["Bachelor's", "Master's & above", "Below Secondary", "Others"])

age = st.slider('Age', 20, 60, 20)
previous_year_rating = st.slider('Previous Year Rating', 1, 5, 1)
length_of_service = st.slider('Length of Service', 1, 32, 1)
avg_training_score = st.slider('Average Training Score', 1, 100, 1)

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
    # Show a loading animation using an animated GIF
    with st.spinner('Predicting...'):
        # Simulate a time-consuming task
        time.sleep(2)
        prediction = model.predict(input_df)
    
    # After prediction, display the result with a color theme
    output = 'High Performance' if prediction[0] == 1 else 'Low Performance'
    if output == 'High Performance':
        st.markdown(f"<h1 style='color:green;'>{output}</h1>", unsafe_allow_html=True)
        st.write(f'Model Accuracy: {model_accuracy*100:.2f}%')
    else:
        st.markdown(f"<h1 style='color:red;'>{output}</h1>", unsafe_allow_html=True)
        st.write(f'Model Accuracy: {model_accuracy*100:.2f}%')