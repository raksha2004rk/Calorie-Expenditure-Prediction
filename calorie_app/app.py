from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
app.secret_key = "super_secret_random_key"

# --- LOAD ML ARTIFACTS ---
# Using os.path to correctly find the artifacts folder relative to this file
base_path = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(base_path, '..', 'artifacts', 'model.pkl')
PREPROCESSOR_PATH = os.path.join(base_path, '..', 'artifacts', 'preprocessor.pkl')

try:
    model = pickle.load(open(MODEL_PATH, 'rb'))
    preprocessor = pickle.load(open(PREPROCESSOR_PATH, 'rb'))
except Exception as e:
    print(f"CRITICAL ERROR: Could not load ML artifacts. Check paths. {e}")

# --- MOCK USER DATABASE ---
users_db = {"admin": "password123"}

# --- ROUTES ---

@app.route('/')
def login_page():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users_db and users_db[username] == password:
        session['user'] = username
        return redirect(url_for('dashboard'))
    flash("Invalid credentials. Use admin / password123")
    return redirect(url_for('login_page'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login_page'))
    
    result = None
    if request.method == 'POST':
        try:
            # 1. Capture data from the form
            gender = request.form.get('sex')
            age = float(request.form.get('age'))
            height = float(request.form.get('height'))
            weight = float(request.form.get('weight'))
            duration = float(request.form.get('duration'))
            heart_rate = float(request.form.get('heart_rate'))
            body_temp = float(request.form.get('body_temp'))

            # 2. Construct DataFrame matching the Training Data Headers exactly
            # We include a dummy 'id' since it was present in your CSV structure
            input_df = pd.DataFrame([[0, gender, age, height, weight, duration, heart_rate, body_temp]],
                                     columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])

            # 3. Apply the Preprocessor (Handling One-Hot Encoding/Scaling)
            transformed_features = preprocessor.transform(input_df)

            # 4. Generate Prediction using the Model
            prediction = model.predict(transformed_features)
            
            # 5. Round the prediction for a clean UI output
            result = f"{round(prediction[0], 2)}"
            
        except Exception as e:
            print(f"PREDICTION ERROR: {e}")
            result = "Invalid Input"

    return render_template('dashboard.html', username=session['user'], result=result)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)