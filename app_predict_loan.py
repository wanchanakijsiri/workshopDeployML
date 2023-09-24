import streamlit as st
import urllib.request
import json

st.title('Loan Prediction App')

# Create a form for user input
st.subheader('Enter Customer Information:')
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income')
coapplicant_income = st.number_input('Coapplicant Income')
loan_amount = st.number_input('Loan Amount')
term = st.number_input('Term (in months)')
credit_history = st.selectbox('Credit History', ['0.0', '1.0'])
area = st.selectbox('Area', ['Urban', 'Rural', 'Semiurban'])

# When the user clicks the "Predict" button
if st.button('Predict'):
    # Create the data payload
    data = {
        "Inputs": {
            "data": [
                {
                    "Gender": gender,
                    "Married": married,
                    "Dependents": dependents,
                    "Education": education,
                    "Self_Employed": self_employed,
                    "Applicant_Income": applicant_income,
                    "Coapplicant_Income": coapplicant_income,
                    "Loan_Amount": loan_amount,
                    "Term": term,
                    "Credit_History": float(credit_history),
                    "Area": area
                }
            ]
        },
        "GlobalParameters": {
            "method": "predict"
        }
    }

    # Convert data to JSON
    json_data = json.dumps(data).encode('utf-8')

    # Send a POST request to the specified URL
    url = 'http://28132852-a923-4783-b934-0c91b8f04bfa.southeastasia.azurecontainer.io/score'
    headers = {'Content-Type': 'application/json'}
    try:
        response = urllib.request.urlopen(urllib.request.Request(url, json_data, headers))

        # Read and display the result
        result = response.read()
        st.subheader('Prediction Result:')
        st.json(json.loads(result))
    except urllib.error.HTTPError as error:
        st.error(f'The request failed with status code: {error.code}')
        st.error(error.read().decode("utf8", 'ignore'))
