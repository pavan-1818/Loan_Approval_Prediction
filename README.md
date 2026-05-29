# Loan Approval Prediction

## Overview

Loan Approval Prediction is a Machine Learning project that predicts whether a loan application will be approved or not based on applicant details such as income, education, employment status, loan amount, credit history, and other financial factors.

The main objective of this project is to automate the loan approval process and help financial institutions make faster and more accurate decisions.

---

## Problem Statement

Banks receive a large number of loan applications every day. Manually evaluating each application is time-consuming and may lead to errors.

This project uses Machine Learning algorithms to analyze applicant information and predict loan approval status.

---

## Dataset Features

The dataset contains various applicant details, including:

- Dependents
- Education
- Self Employed
- Applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area
- Loan Status

---

## Project Workflow

### 1. Data Collection
- Load dataset
- Understand data structure

### 2. Data Preprocessing
- Handle missing values
- Encode categorical variables
- Feature scaling

### 3. Exploratory Data Analysis (EDA)
- Data visualization
- Correlation analysis
- Distribution analysis

### 4. Model Building
- Split dataset into training and testing sets
- Train Machine Learning models

### 5. Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report

### 6. Prediction
- Predict loan approval for new applicants

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

## Machine Learning Algorithms

Some commonly used algorithms for loan prediction include:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pavan-1818/Loan_Approval_Prediction.git
```

Navigate to the project folder:

```bash
cd Loan_Approval_Prediction
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook file and execute all cells.

---

## Project Structure

```text
Loan_Approval_Prediction/
│
├── dataset/
│   └── loan_data.csv
│
├── notebooks/
│   └── Loan_Approval_Prediction.ipynb
│
├── images/
│
├── README.md
│
└── requirements.txt
```

---

## Sample Output

Input:

- Applicant Income: 5000
- Loan Amount: 120
- Credit History: 1

Prediction:

```text
Loan Approved
```

---

## Future Improvements

- Deploy using Streamlit
- Deploy using Flask/Django
- Hyperparameter tuning
- Improve model accuracy
- Real-time prediction system

---

## Results

The model successfully predicts loan approval status based on applicant information and can assist banks in making faster lending decisions.

---

## Conclusion

This project demonstrates the application of Machine Learning in the banking sector. By analyzing customer data and predicting loan eligibility, the system helps reduce manual effort and supports data-driven decision-making.

---

## Author

R Pall Pavan

GitHub:
https://github.com/pavan-1818
