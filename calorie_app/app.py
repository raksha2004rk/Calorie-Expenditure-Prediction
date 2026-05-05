from flask import Flask, render_template, request, redirect, url_for, session
import pickle, os
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret"

BASE = os.path.dirname(__file__)

# Simple in-memory users (for demo)
users = {}

@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# 🔐 LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")


# 🆕 SIGNUP
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users[username] = password
        session["user"] = username
        return redirect("/dashboard")

    return render_template("signup.html")


# 📊 DASHBOARD + PREDICTION
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        try:
            # 🔥 Load model + preprocessor ONLY when needed
            model = pickle.load(open(os.path.join(BASE, "artifacts/model.pkl"), "rb"))
            preprocessor = pickle.load(open(os.path.join(BASE, "artifacts/preprocessor.pkl"), "rb"))

            # 📥 Get input
            data = {
                "Age": float(request.form["age"]),
                "Sex": request.form["sex"],
                "Height": float(request.form["height"]),
                "Weight": float(request.form["weight"]),
                "Duration": float(request.form["duration"]),
                "Heart_Rate": float(request.form["heart_rate"]),
                "Body_Temp": float(request.form["body_temp"])
            }

            # 🧠 Transform + predict
            df = pd.DataFrame([data])
            X = preprocessor.transform(df)
            result = round(float(model.predict(X)[0]), 2)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("dashboard.html", result=result)


# 🚪 LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)