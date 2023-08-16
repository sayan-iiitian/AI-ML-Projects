
#The final code
import streamlit as st
import joblib

# Load Model from .pkl or .sav file
model1_path = 'diabetes_model.sav'
model2_path = 'heart_disease_model.sav' 
model3_path = 'parkinson_model.sav'
def load_model(model1_path):
    return joblib.load(model1_path)
def load_model(model2_path):
    return joblib.load(model2_path)
def load_model(model3_path):
    return joblib.load(model3_path)
# Prediction function

def predict('1'):
    
    model1 = load_model(model1_path)
    prediction = predict(model1, ['1'])  # Assuming a single input
    return prediction

def predict('2'):
    
    model2 = load_model(model2_path)
    prediction = predict(model2, ['2'])  # Assuming a single input
    return prediction

def predict('3'):
    
    model3 = load_model(model3_path)
    prediction = predict(model3, ['3'])  # Assuming a single input
    return prediction



# Define the Streamlit app
def main():
    st.title("Disease Model Deployment")

    # Dropdown menu to select a disease model
    selected_model = st.selectbox('Select a Disease Model', ['Model 1', 'Model 2', 'Model 3'])

    # User input
    user_input = st.text_input('Enter input data:')

    # Load the selected model
    if selected_model == 'Model 1':
        model = load_model('model1.pkl')  # Replace with the actual path to your .pkl or .sav file
    elif selected_model == 'Model 2':
        model = load_model('model2.sav')  # Replace with the actual path to your .pkl or .sav file
    else:
        model = load_model('model3.pkl')  # Replace with the actual path to your .pkl or .sav file

    # Make predictions and display results
    if user_input:
        prediction = predict(model, [user_input])
        st.write('Model Prediction:', prediction)

if __name__ == "__main__":
    main()
