import streamlit as st
from test import test_model
import pandas as pd

def main():

    # instructions
    st.title("Ransomware Detection Web App")
    st.markdown("""
    1. Click "Browse File" to upload the generated csv file. You can download the sample files from [Github](https://github.com/khairulofficial/ransomwaredetection/tree/main/sample%20files) 
    2. Select machine learning model. If unsure, please use recommended model.
    3. Click "Predict"
    """)
    
    
    st.sidebar.image(r"C:\Users\khair\Pictures\LogAIAP.png", use_column_width=True) [image]
    
    # upload file
    test_file = st.sidebar.file_uploader(label="Upload Generated CSV File", type="csv", accept_multiple_files=False)
    
        
    if test_file:
        test_file = pd.read_csv(test_file)
        
        try:
            model = st.sidebar.selectbox(label="Select Machine Learning model", options=['Random Forest (Recommended)','SVM','Logistic Regression','Naive Bayes','KNN','XGBoost','Neural Network'])
            
            if st.sidebar.button('Predict'):
            
                family, cvscore = test_model(model, test_file)
                
                
                
                st.markdown("""---""")
                # display prediction
                if family == 0:
                    st.header(f'\nResult: This file is predicted to be a :green[Goodware]')
                
                if family == 1:
                    # display further instructions
                    st.header(f'\nResult: This file is predicted to be a :red[Encryptor Ransomware]')
                    st.write(f'\n:red[WARNING:] Please delete the file if you have accidentally download it on any machine and inform your admin')

                if family == 2:
                    # display further instructions
                    st.header(f'\nResult: This file is predicted to be a :red[Locker Ransomware]')
                    st.write(f'\n:red[WARNING:] Please delete the file if you have accidentally download it on any machine and inform your admin')
                # model and file details
                st.write(f"Model: {model}")
                st.write("Accuracy: ",f"{cvscore:.2%}")
                
            
        except:
            st.warning("Invalid File. Please try another file.")
    

if __name__ == "__main__":
    main()
