import streamlit as st
import pandas as pd
import pickle
import time

# Load your trained model
model_data = pickle.load(open('employee_performance_prediction_model.pkl', 'rb'))
model = model_data['model']
model_accuracy = model_data['accuracy']
# Assuming 'logo.png' is the path to your logo image file
st.sidebar.image('logo.png', use_column_width=True)

# Add formatted text below the logo in the sidebar
st.sidebar.markdown("""
    **About the Company**  
    *Teach for India* is a fellowship program for young professionals who want to solve the education crisis in the country. It is reported that the TFI alumni community is responsible for starting 150+ organisations in the field of social impact.

    **Bridging the gap**  
    *Teach for India* has approximately 900+ fellows who are deployed across 7 cities and are working with 28000 students. Many of these students do not have the reading and numeracy skills required at their grade level. The ability to predict employee performance will enable TFI to implement learning and development measures to empower their fellows to improve the reading levels of their students.
""", unsafe_allow_html=True)

st.title('Employee Performance Prediction Form')

st.image('logo.png')

st.write("""
This is a Python created an HR analytics tool that can help a talent management team in Teach For India predict employee performance and plan for their growth.
""")
         
# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Department
""")
# Replace selectbox with st.radio
department = st.selectbox('Select your department', ['Sales & Marketing', 'Operations', 'Procurement', 'Technology', 'Analytics', 'Finance', 'HR', 'R&D', 'Legal'])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Education
""")
# Rest of your st.radio widgets replacing selectbox...
education = st.selectbox('Select your education status', ["Bachelor's", "Master's & above", "Below Secondary", "Others"])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Gender
""")
gender = st.radio('Gender', ['Male', 'Female'])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Recruitment Channel
""")
recruitment_channel = st.selectbox('Select your recruitment channel', ['Other', 'Sourcing', 'Referred'])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Awards Won
0 means have not received an award. 1 means have received an award.
""")
awards_won = st.radio('Awards Won', [0, 1])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Number of Trainigs
""")
no_of_trainings = st.slider('Number of Trainings', 1, 5, 1)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Region
""")
region_options = [f'region_{i}' for i in range(1, 35)]
region = st.selectbox('Region', options=region_options)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Age
""")
age = st.slider('Age', 20, 60, 20)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Previous year rating 
Rating is between 1 and 5. 1 meaning low, 5 meaning high.
""")
previous_year_rating = st.slider('Previous Year Rating', 1, 5, 1)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Length of Service
Time period is in years.
""")
length_of_service = st.slider('Length of Service', 1, 32, 1)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Average Training Score
Training score is between 1 and 100. 1 meaning low, 100 meaning high.
""")
avg_training_score = st.slider('Average Training Score', 1, 100, 1)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

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

        st.balloons()

    else:
        st.markdown(f"<h1 style='color:red;'>{output}</h1>", unsafe_allow_html=True)
        st.write(f'Model Accuracy: {model_accuracy*100:.2f}%')

        st.balloons()