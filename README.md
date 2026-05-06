Calorie Expenditure Prediction

Overview

This project predicts the number of calories burned by an individual based on physical and workout-related parameters such as age, gender, height, weight, exercise duration, heart rate, and body temperature.

The project follows a modular Machine Learning pipeline architecture including data ingestion, data transformation, model training, and evaluation.



Project Objectives

- Analyze calories expenditure dataset
- Build a robust ML pipeline
- Perform feature engineering and preprocessing
- Train and evaluate regression models
- Deploy a reusable and scalable project structure



Problem Statement

Given user health and exercise-related attributes, predict the number of calories burned during physical activity.



Project Structure


Calories-Expenditure-Prediction/
│
├── artifacts/                # Generated files (datasets, models, preprocessor)
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── preprocessor.pkl
│   └── model.pkl
│
├── notebooks/                # Jupyter notebooks (EDA & experiments)
│   ├── data/
│   │   └── calories.csv
│   ├── 1. EDA.ipynb
│   └── 2. model_training.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── venv/                     # Virtual environment
├── requirements.txt
├── setup.py
└── README.md




Tech Stack

- Python 3.10
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle (Model Serialization)



ML Pipeline Workflow

 1. Data Ingestion

- Reads dataset from source
- Splits into train & test datasets
- Saves raw and processed files

 2. Data Transformation

- Handles missing values
- Applies encoding to categorical features
- Scales numerical features
- Saves preprocessing pipeline (`preprocessor.pkl`)

 3. Model Training

- Trains regression models
- Evaluates performance
- Saves best model (`model.pkl`)



 Features Used

 Numerical Features

- Age
- Height
- Weight
- Duration
- Heart_Rate
- Body_Temp

Categorical Features

- Gender



How to Run the Project

Step 1: Clone the Repository


git clone <your-repo-link>
cd Calories-Expenditure-Prediction


Step 2: Create & Activate Virtual Environment


python -m venv venv


Activate Environment (Windows)


venv\Scripts\activate


Step 3: Install Dependencies


pip install -r requirements.txt


Step 4: Run the Pipeline


python -m src.components.data_ingestion




Sample Output

After running the pipeline, the following files are generated:


artifacts/
├── data.csv
├── train.csv
├── test.csv
├── preprocessor.pkl
└── model.pkl




Key Highlights

- Modular and scalable ML architecture
- Production-level folder structure
- Custom logging and exception handling
- Reusable preprocessing pipeline
- Clean separation of concerns



Common Issues & Fixes

| Issue | Solution |
|-------|-----------|
| File not found error | Ensure correct working directory |
| Kernel crash | Install ipykernel in venv |
| Model not saving | Check artifacts path |
| Import errors | Run using `python -m` |



Future Improvements

- Add Flask/FastAPI deployment
- Integrate CI/CD pipeline
- Add model monitoring
- Hyperparameter tuning
- Docker containerization



Authors

- Raksha Kadam
- Dishant Phandyal
- Vivek Chauhan
- Aditya Gupta
- Merajudaula Shekh



Dataset Source

The dataset used in this project is collected from Kaggle.  
It contains various health and workout-related attributes used to predict calorie expenditure.

Dataset: Kaggle Calories Burnt Prediction Dataset



Acknowledgements

- Scikit-learn Documentation
- Kaggle Dataset for Calories Expenditure Prediction
- ML Pipeline Best Practices



Contact

Feel free to connect for collaboration or project-related queries.
