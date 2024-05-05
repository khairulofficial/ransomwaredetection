import streamlit as st
from test import test_model
import pandas as pd

def main():

    # page config
    st.get_option("theme.primaryColor")
    st.get_option("theme.textColor")
    st.get_option("theme.backgroundColor")
    st.get_option("theme.secondaryBackgroundColor")
    st.get_option("theme.font")
    image_url = "data:image/jpeg;base64,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"
    st.set_page_config(layout="wide", page_icon=image_url, page_title = "Ransomware Detection App")
    st.title("Ransomware Detection Web App")
    
    # instructions
    st.markdown("""
    1. Click "Browse File" to upload the generated csv file. You can download the sample files from [Github](https://github.com/khairulofficial/ransomwaredetection/tree/main/sample%20files) 
    2. Select machine learning model. If unsure, please use recommended model.
    3. Click "Predict"
    """)
    
    # Load image
    st.sidebar.image(image_url,use_column_width=True)
    st.markdown("""
    
    
    """)
    
    # upload file
    test_file = st.sidebar.file_uploader(label="Upload Generated CSV File", type="csv", accept_multiple_files=False)
            
    if test_file:
        test_file = pd.read_csv(test_file)
        
        try:
            model = st.sidebar.selectbox(label="Select Machine Learning model", options=['Random Forest (Recommended)','SVM','Logistic Regression','Naive Bayes','KNN','XGBoost','Neural Network'])
            
            if st.sidebar.button('Predict'):
                # feed data through pipeline
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
