import pickle
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('employee_performance_prediction_model.pkl', 'rb'))

@app.route('/')
def home():
    # Render the home page with the form on it
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve numerical input data from form and convert to float
    numerical_input_data = {
        'no_of_trainings': float(request.form['no_of_trainings']),
        'age': float(request.form['age']),
        'previous_year_rating': float(request.form['previous_year_rating']),
        'length_of_service': float(request.form['length_of_service']),
        'awards_won': float(request.form['awards_won']),
        'avg_training_score': float(request.form['avg_training_score'])
    }
    
    # Retrieve categorical input data from form
    categorical_input_data = {
        'department': request.form['department'],
        'region': request.form['region'],
        'education': request.form['education'],
        'gender': request.form['gender'],
        'recruitment_channel': request.form['recruitment_channel']
    }
    
    # Combine numerical and categorical data into a single dictionary
    input_data = {**numerical_input_data, **categorical_input_data}
    
    # Convert input data to DataFrame to match training data format
    input_df = pd.DataFrame([input_data])
    
    # Make prediction with the entire pipeline (preprocessing + classifier)
    prediction = model.predict(input_df)
    
    # Customize the output
    output = 'High Performance' if prediction[0] == 1 else 'Low Performance'

    return render_template('index.html', prediction_text='Employee Performance Prediction: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

