
import os
from pathlib import Path

import pandas as pd
import joblib
from flask import Flask, render_template
from forms import InputForm

app = Flask(__name__)

# Set SECRET_KEY in your environment before starting the app.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")

BASE_DIR = Path(__file__).resolve().parent
model = joblib.load(BASE_DIR / "model.joblib")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    message = "Please provide valid input details!"

    if form.validate_on_submit():
        x_new = pd.DataFrame({
            "Gender": [form.Gender.data],
            "Age": [form.Age.data],
            "History": [form.History.data],
            "Patient": [form.Patient.data],
            "TakeMedication": [form.TakeMedication.data],
            "Severity": [form.Severity.data],
            "BreathShortness": [form.BreathShortness.data],
            "VisualChanges": [form.VisualChanges.data],
            "NoseBleeding": [form.NoseBleeding.data],
            "Whendiagnoused": [form.Whendiagnoused.data],
            "Systolic": [form.Systolic.data],
            "Diastolic": [form.Diastolic.data],
            "ControlledDiet": [form.ControlledDiet.data],
        })

        prediction = model.predict(x_new)[0]

        stage_map = {
            0: "NORMAL",
            1: "HYPERTENSION (Stage-1)",
            2: "HYPERTENSION (Stage-2)",
            3: "HYPERTENSIVE CRISIS",
        }

        stage_label = stage_map.get(prediction, "Unknown")
        message = (
            f"Model prediction: {stage_label}. "
            "This is an educational demonstration, not a medical diagnosis."
        )

    return render_template(
        "predict.html",
        title="Predict",
        form=form,
        output=message,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        debug=False,
    )
