import pandas as pd
import joblib

# =========================
# Load model & encoders
# =========================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

visa_encoder = joblib.load("visa_encoder.pkl")
emp_state_encoder = joblib.load("emp_state_encoder.pkl")
work_state_encoder = joblib.load("work_state_encoder.pkl")


# =========================
# Preprocessing
# =========================
def preprocess_input(data):

    df = pd.DataFrame([data])

    # Feature Engineering
    df['wage_ratio'] = df['WAGE_RATE_OF_PAY_FROM'] / df['PREVAILING_WAGE']
    df['application_month'] = pd.to_datetime(df['application_date']).dt.month

    # Encoding
    df['VISA_CLASS'] = visa_encoder.transform(df['VISA_CLASS'])
    df['EMPLOYER_STATE'] = emp_state_encoder.transform(df['EMPLOYER_STATE'])
    df['WORKSITE_STATE'] = work_state_encoder.transform(df['WORKSITE_STATE'])

    # Convert FULL_TIME_POSITION
    df['FULL_TIME_POSITION'] = 1 if data.get('FULL_TIME_POSITION', 'Y') == "Y" else 0

    # Scaling
    df[['WAGE_RATE_OF_PAY_FROM', 'PREVAILING_WAGE']] = scaler.transform(
        df[['WAGE_RATE_OF_PAY_FROM', 'PREVAILING_WAGE']]
    )

    # Drop date
    df = df.drop(columns=['application_date'])

    # FINAL feature order (VERY IMPORTANT)
    df = df[['VISA_CLASS', 'FULL_TIME_POSITION',
             'EMPLOYER_STATE', 'WORKSITE_STATE',
             'WAGE_RATE_OF_PAY_FROM', 'PREVAILING_WAGE',
             'wage_ratio', 'application_month']]

    return df


# =========================
# Prediction
# =========================
def predict_processing_time(input_data):

    processed = preprocess_input(input_data)

    print("Processed Input:\n", processed)  # debug

    prediction = model.predict(processed)

    return round(prediction[0], 2)


# =========================

def validate_input(data):

    required_fields = [
        "VISA_CLASS", "FULL_TIME_POSITION",
        "EMPLOYER_STATE", "WORKSITE_STATE",
        "WAGE_RATE_OF_PAY_FROM", "PREVAILING_WAGE",
        "application_date"
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"{field} is missing")

    # Salary check
    if data["WAGE_RATE_OF_PAY_FROM"] <= 0 or data["PREVAILING_WAGE"] <= 0:
        raise ValueError("Salary values must be positive")

    return True


#================

def predict_processing_time(input_data):

    validate_input(input_data)

    processed = preprocess_input(input_data)
    prediction = model.predict(processed)

    return round(prediction[0], 2)


#====================
# Test Example
# =========================
if __name__ == "__main__":

    sample_input = {
        "VISA_CLASS": "E-3 Australian",
        "FULL_TIME_POSITION": "Y",
        "EMPLOYER_STATE": "CA",
        "WORKSITE_STATE": "CA",
        "WAGE_RATE_OF_PAY_FROM": 9000,
        "PREVAILING_WAGE": 85000,
        "application_date": "2023-05-10"
    }

    result = predict_processing_time(sample_input)

    print("\n✅ Predicted Processing Time (days):", result)