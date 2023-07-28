import streamlit as st
import pickle as pkl
# Load the trained model
with open('C:/Users/HP/Desktop/ML_modes_vscode/advertising/Advertising_model_selection.pkl', 'rb') as file:
    model= pkl.load(file)
def main():
    st.title('Advertising model prediction')
    #Create input features of advertising

Dstp= st.number_input('Daily Time Spent on Site')
Age= st.number_input('Age')
AI= st.number_input('Area Income')
Diu= st.number_input('Daily Internet Usage')
male= st.selectbox('Male', [0,1], format_func= lambda x: 'No' if x==0 else 'Yes')

if st.button('predict'):
    #Make prediction
    input_data= [[Dstp, Age, AI, Diu, male]]

    #Convert input data to a dataframe and make predictions
    prediction= model.predict(input_data)

    #Display prediction
    if prediction[0] == 0:
        st.write('Prediction: The user will click the Ad')
    else:
        st.write('Prediction: The user will not click the Ad')

#Run the App
    if __name__ == '__main__':
        main()