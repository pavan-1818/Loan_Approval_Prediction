import pandas as pd
import pickle as pk
import streamlit as st

# Load model
model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('Scalar.pkl','rb'))

# Page config
st.set_page_config(page_title="Loan Prediction", layout="centered")

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #4facfe, #ad2d96);
}

.main-card {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}

.stButton>button {
    background-color: #ad2d96;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.result-success {
    color: green;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

.result-fail {
    color: red;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center; color:white;'> Loan Prediction App</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
        no_of_dep = st.number_input('No. of Dependents', min_value=0, max_value=5, step=1)
        grad = st.selectbox('Education', ['Graduated', 'Not Graduated'])
        self_emp = st.selectbox('Self Employed', ['Yes', 'No'])
        annual_income = st.number_input('Annual Income', min_value=0)

with col2:
        loan_amount = st.number_input('Loan Amount', min_value=0)
        loan_dur = st.number_input('Loan Duration (Years)', min_value=0, max_value=30)
        cibil = st.number_input('CIBIL Score', min_value=0, max_value=900)
        asset = st.number_input('Total Assets Value', min_value=0)

    # Encoding
grad_s = 0 if grad == 'Graduated' else 1
emp_s = 1 if self_emp == 'Yes' else 0
st.write("")  # spacing

if st.button("Predict Loan Status"):
        pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, annual_income,
                                   loan_amount, loan_dur, cibil, asset]],
                                 columns=['no_of_dependents','education','self_employed',
                                          'income_annum','loan_amount','loan_term',
                                          'cibil_score','Asset'])

        pred_data = scaler.transform(pred_data)
        prediction = model.predict(pred_data)

        st.write("")

        if prediction[0] == 1:
            st.markdown('<p class="result-success"> Loan Approved</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="result-fail"> Loan Rejected</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)