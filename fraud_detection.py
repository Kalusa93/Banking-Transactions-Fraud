import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("App de Predicción de Fraudes")

st.markdown("Por favor ingrese los detalles de la transacción")

st.divider()

transaction_type = st.selectbox("Tipo de transacción", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Monto", min_value = 0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Balance viejo origen", min_value = 0.0, value = 10000.0)
newbalanceOrig = st.number_input("Balance nuevo origen", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Balance viejo destino", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("Balance nuevo destino", min_value=0.0, value=0.0)

if st.button("Predecir"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("Esta transacción puede ser un fraude")
    else:
        st.success("Esta transacción no parece ser un fraude")