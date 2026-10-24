
# Predictive Pulse — Blood Pressure Analysis with Machine Learning

Predictive Pulse is a machine-learning project that classifies hypertension stages from patient-provided inputs through a Flask web application.

<p align="center">
  <a href="https://predictive-pulse-harnessing-machine-c75g.onrender.com"><strong>🚀 Try the Live Demo</strong></a>
  &nbsp; • &nbsp;
  <a href="https://github.com/Rtl-mdy/Predictive-Pulse-Harnessing-Machine-Learning-for-Blood-Pressure-Analysis"><strong>View Source Code</strong></a>
</p>

## 🚀 Live Demo

**Application:** https://predictive-pulse-harnessing-machine-c75g.onrender.com

The application is hosted on Render. On a free instance, the first request after inactivity may take longer while the service starts.

## ✨ Features

- Interactive web form for patient-related inputs.
- Hypertension category prediction using a saved machine-learning model.
- Flask-powered web interface.
- Data preprocessing and exploratory data analysis.
- Model training and evaluation materials included in the project.
- Notebook-based exploration, if `model.ipynb` is present.

## 📸 Screenshots

### Home Page

<img width="100%" alt="Predictive Pulse home page" src="https://github.com/user-attachments/assets/4a4cf3a9-a0ab-4a93-ae69-d6337fe6c8db" />

### Prediction Page

<img width="100%" alt="Predictive Pulse prediction page" src="https://github.com/user-attachments/assets/f772dfda-8ba8-4a35-a95a-2c76b7efe8c1" />

## 🧰 Tech Stack

- **Python** — programming language
- **Pandas and NumPy** — data handling
- **Scikit-learn and Feature-engine** — machine learning and preprocessing
- **Flask and Flask-WTF** — web application and forms
- **Joblib** — model persistence
- **Gunicorn** — production server
- **Render** — deployment

## 📁 Project Structure

```text
.
├── app.py
├── forms.py
├── model.joblib
├── requirements.txt
├── data/
│   └── patient_data.csv
├── templates/
├── static/
└── model.ipynb
```

The exact files may vary depending on what is present in the repository.

## 🛠️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rtl-mdy/Predictive-Pulse-Harnessing-Machine-Learning-for-Blood-Pressure-Analysis.git
cd Predictive-Pulse-Harnessing-Machine-Learning-for-Blood-Pressure-Analysis
```

### 2. Create a virtual environment (Ubuntu/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If `venv` is missing:

```bash
sudo apt update
sudo apt install python3-venv
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set a local secret key

```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
```

Keep secret keys private. Never commit them to GitHub.

### 5. Run the application

```bash
python app.py
```

Open the local address shown in your terminal. If the app uses port 10000, visit http://127.0.0.1:10000.

For a production-style local run:

```bash
gunicorn app:app
```

### Optional: Open the notebook

If `model.ipynb` exists:

```bash
jupyter notebook model.ipynb
```

## 🔎 How It Works

1. The user enters the requested patient-related values.
2. Flask processes the form inputs.
3. The saved model loaded from `model.joblib` generates a prediction.
4. The application displays the predicted category.

## ⚠️ Medical Disclaimer

This project is for educational and demonstration purposes only. It is not a clinically validated diagnostic tool and must not be used to diagnose or treat medical conditions. Predictions can be inaccurate. Consult a qualified healthcare professional for medical advice.

## 📄 License

See the repository's license file for the applicable terms.

---

Made by **Ratul Midya** · [GitHub](https://github.com/Rtl-mdy)
