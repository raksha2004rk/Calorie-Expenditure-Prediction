# 🔥 Calorie Expenditure Prediction App

A full-stack Machine Learning project that predicts **calories burned** based on user fitness data such as age, gender, weight, height, duration, and heart rate.

The project follows an **end-to-end ML pipeline** with deployment using Flask, React, and Docker.

---

## 🚀 Features

* 📊 Data Cleaning & EDA (Jupyter Notebooks)
* 🧠 ML Model Training (Random Forest Regressor)
* ⚙️ Modular ML Pipeline (`src/` structure)
* 🌐 Flask Backend API for predictions
* 🎨 React + Tailwind Frontend UI
* 📄 PDF Report Generation
* 🐳 Dockerized Backend
* ☁️ Deployment (Render + Vercel)

---

## 🧠 Tech Stack

### Machine Learning

* Python
* Pandas, NumPy
* Scikit-learn

### Backend

* Flask
* Flask-CORS
* Gunicorn

### Frontend

* React
* Tailwind CSS
* Axios

### Deployment

* Docker
* Render (Backend)
* Vercel (Frontend)

---

## 📁 Project Structure

```
calorie_prediction_app/
│
├── data/
├── notebooks/
├── artifacts/
├── src/
├── backend/
├── frontend/
├── logs/
└── README.md
```

---

## 📊 ML Workflow

1. Data Collection
2. Data Cleaning (NaN handling, outliers)
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training & Evaluation
6. Model Saving (`model.pkl`, `preprocessor.pkl`)

---

## ⚙️ How to Run the Project

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/raksha2004rk/Calorie-Expenditure-Prediction
cd calorie_prediction_app
```

---

### 🔹 Step 2: Run ML Pipeline

```bash
python src/pipeline/train_pipeline.py
```

This will generate:

* `artifacts/model.pkl`
* `artifacts/preprocessor.pkl`

---

### 🔹 Step 3: Run Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### 🔹 Step 4: Run Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 🐳 Run with Docker

### Build Image

```bash
docker build -t calorie-backend ./backend
```

### Run Container

```bash
docker run -p 5000:5000 calorie-backend
```

---

## ☁️ Deployment

### Backend (Render)

* Deploy Docker-based Flask API
* Public API endpoint used by frontend

### Frontend (Vercel)

* Connect GitHub repo
* Update API URL in frontend

---

## 🔗 API Endpoint

### Predict Calories

```
POST /predict
```

#### Request Body:

```json
{
  "age": 25,
  "gender": "male",
  "height": 175,
  "weight": 70,
  "duration": 30,
  "heart_rate": 120
}
```

#### Response:

```json
{
  "calories": 210.45
}
```

---

## 📈 Model Performance

* Algorithm: Random Forest Regressor
* R² Score: ~0.95+
* MAE: Low error (dataset dependent)

---

## 📌 Future Improvements

* JWT Authentication
* User history tracking
* Graph-based insights
* Mobile responsiveness
* FastAPI migration

---

## 👨‍💻 Author

**RAKSHA KADAM**
BTech CSE (AI/ML)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
