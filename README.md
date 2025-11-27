# 🎓 Student Performance Prediction – End-to-End ML Project

## 🚀 Project Overview

This project predicts **student performance (Math Score)** based on features like gender, parental education, lunch type, test preparation, reading & writing scores.

It is built using **Modular Machine Learning Architecture** following real-world production practices including:

✔ Data ingestion  
✔ Data transformation (feature engineering, encoding, scaling)  
✔ Model training and selection  
✔ Hyperparameter tuning  
✔ Prediction pipeline with Flask  
✔ Dockerized deployment on AWS EC2 & Azure Web App  
✔ CI/CD using GitHub Actions  

---

## 📂 Project Architecture

```
MLProject/
│── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
│   ├── __init__.py
│
├── artifacts/           # model.pkl, preprocessor.pkl, train/test data
├── templates/           # HTML files for Flask UI
├── app.py              # Flask web application
├── Dockerfile          # For containerization
├── requirements.txt
├── .gitignore
├── README.md
```

---

## 🧠 ML Workflow

### 🔹 1. Data Ingestion

- Load dataset
- Split into train/test
- Store in `artifacts/`

```python
train.csv, test.csv, data.csv
```

### 🔹 2. Data Transformation

- Handle missing values
- Encoding categorical features
- Standard Scaling numerical features
- Save preprocessor as `.pkl`
- ColumnTransformer + Pipeline

### 🔹 3. Model Training & Evaluation

Multiple models trained:

| Model | Accuracy (R²) |
|-------|---------------|
| Linear Regression | 88% |
| RandomForest | 85% |
| XGBoost | 87% |
| CatBoost | 86% |

📌 **Best Model Selected** → Linear Regression

### 🔹 4. Hyperparameter Tuning

Used GridSearchCV to optimize best model parameters.

### 🔹 5. Prediction Pipeline (Flask App)

Flask app accepts user input ➝ processes with preprocessor ➝ outputs prediction.

🔗 **Local URL:**
```
http://127.0.0.1:5000
```

---

## 🌐 Deployment Options

### 🚀 AWS EC2 + Docker + ECR + GitHub Actions (CI/CD)

- Dockerize the app using Dockerfile
- Push to AWS ECR (private image)
- Deploy container on EC2
- Automate via GitHub Actions

### 🚀 Azure Web App (Container Deployment)

- Build Docker image locally
- Push to Azure ACR
- Deploy container on Azure Web App
- Enable Continuous Deployment via GitHub Actions

---

## 🐳 Docker Setup

### 👉 Build the Docker Image
```bash
docker build -t student-performance:latest .
```

### 👉 Run the Docker Container
```bash
docker run -p 8080:8080 student-performance:latest
```

---

## 📦 Requirements Installation

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project Locally

```bash
python app.py
```

Go to browser:
```
http://127.0.0.1:5000/
```

---

## 🧪 Test Prediction (Sample Input)

| Feature | Value |
|---------|-------|
| Gender | Female |
| Lunch | Standard |
| Reading Score | 92 |
| Writing Score | 90 |
| Parental Education | Master's |
| Test Preparation | Completed |

🔮 **Predicted Math Score** → 87.57

---

## 📌 Key Features

| Feature | Description |
|---------|-------------|
| Modular ML Pipeline | Easy to scale and maintain |
| Logging & Custom Exceptions | Debuggable & production ready |
| Hyperparameter Tuning | GridSearchCV-based optimization |
| Flask UI for Predictions | Web-based live predictions |
| Docker Support | Portable & OS-independent deployment |
| AWS & Azure Compatible | Multi-cloud deployment ready |
| CI/CD with GitHub Actions | Auto deploy on commit |

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| ML Libraries | Scikit-learn, Pandas, NumPy |
| Web Framework | Flask |
| Cloud | AWS EC2, Azure Web App |
| Container | Docker, Azure ACR, AWS ECR |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |

---

## 📜 Future Enhancements

🚀 Deploy using FastAPI instead of Flask  
🎯 Add Model Monitoring (Prometheus / MLFlow)  
📈 Use AutoML or MLOps (DVC / MLFlow)  
🎨 Add better UI using Streamlit or React  

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

---

## 💬 Contact

📌 **Author:** Saksham Agarwal 
📧 **Email:** agarwalsaksham11@gmail.com  
🌐 **LinkedIn / GitHub Portfolio Link**

---

⭐ **If you like this project, star this repo to support!**


# TextSummarizer USing Huggingface

### Workflows 

1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components- Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline-- Training Pipeline,PRediction Pipeline
7. Front end-- Api's, Training APi's, Batch Prtediction API's
