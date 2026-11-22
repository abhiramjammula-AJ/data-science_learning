import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# App title
st.title('Titanic Survival Prediction')
st.write('Enter the passenger details to predict survival:')

def user_input_features():
    pclass = st.selectbox('Passenger Class', [1, 2, 3])
    sex = st.selectbox('Sex', ['male', 'female'])
    age = st.number_input('Age', min_value=0.1, max_value=120.0, value=30.0)
    sibsp = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, max_value=10, value=0)
    parch = st.number_input('Number of Parents/Children Aboard', min_value=0, max_value=10, value=0)
    fare = st.number_input('Fare', min_value=0.0, max_value=1000.0, value=50.0)
    embarked = st.selectbox('Port of Embarkation', ['C', 'Q', 'S'])
    
    data = {'pclass': pclass,
            'sex': sex,
            'age': age,
            'sibsp': sibsp,
            'parch': parch,
            'fare': fare,
            'embarked': embarked}
    return pd.DataFrame(data, index=[0])

# Get user inputs
df = user_input_features()
st.subheader('User Input Parameters')
st.write(df)

# Load dataset
titanic = pd.read_csv("D:\\Data science\\Assignments\\Questions\\Logistic Regression\\Titanic_cleaned.csv")
X = titanic.drop(['Name', 'Ticket', 'Survived', 'PassengerId'], axis=1)
y = titanic['Survived']

# Show columns for debugging
st.write("Training feature columns:", list(X.columns))

# Train logistic regression
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X, y)

# Encode user input
sex_encoded = 1 if df['sex'][0] == 'male' else 0
embarked_value = df['embarked'][0]
embarked_encoded = {'C': 0, 'Q': 1, 'S': 2}[embarked_value]
pclass_encoded = {1: 0, 2: 1, 3: 2}[df['pclass'][0]]

# Build input_data aligned with X.columns
input_data = pd.DataFrame(0, index=[0], columns=X.columns)

# Fill values based on available columns
if 'Pclass' in X.columns:
    input_data.at[0, 'Pclass'] = pclass_encoded
if 'Sex' in X.columns:
    input_data.at[0, 'Sex'] = sex_encoded
if 'Age' in X.columns:
    input_data.at[0, 'Age'] = df['age'][0]
if 'SibSp' in X.columns:
    input_data.at[0, 'SibSp'] = df['sibsp'][0]
if 'Parch' in X.columns:
    input_data.at[0, 'Parch'] = df['parch'][0]
if 'Fare' in X.columns:
    input_data.at[0, 'Fare'] = df['fare'][0]

# Handle Embarked dynamically
if 'Embarked' in X.columns:
    input_data.at[0, 'Embarked'] = embarked_encoded
else:
    # One-hot encoding case
    col_name = f'Embarked_{embarked_value}'
    if col_name in X.columns:
        input_data.at[0, col_name] = 1

# Predict on button click
if st.button('Predict Survival'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)[:, 1]

    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.success(f'Survived! (Probability: {prediction_proba[0]:.2f})')
    else:
        st.error(f'Did not survive (Probability: {prediction_proba[0]:.2f})')
