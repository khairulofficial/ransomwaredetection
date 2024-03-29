This project is regarding using machine learning for ransomware detection in SMEs. SMEs do not have the luxury of time and resources to analyse all features of a ransomware. As such, this projects acts as triage where we utilise the minimum number of feature possible while still maintaining an accuracy score of at least 90% for our top model. More background context will be updated. This project contains 4 main files:
1) Ransomware Dataset
2) Notebook for Analysis 
3) Code for Streamlit Web Application (main.py)
4) Various Test use case files for Streamlit Web Application

Note:
- The dataset has 50 features
- Ensure that all 3 files are downloaded into the same folder. Many data source errors in data science projects arise due to dataset being downloaded directly into "Downloads" instead of the same folder as the notebook/web app.
- For No.2 Notebook for Anaylsis, ensure that you have installed the libraries shown in the import statement using "pip install -r requirements.txt"
- Section 12 of the notebook, Feature Reduction Using Principal Component Analysis, is miscelleanous. We will not recommend it as interpretability is limitied. You can interact with the scores and loadings plot to analyse potential relationships.
- For No.3 Code for Streamlit Web Application, ensure that you have installed streamlit. I will update by deploying it onto streamlit cloud in the future.
- Upload the text use case CSV file. Test use case files refer to the files that users can upload into the web app. It does not refet to files for unit testing. For instance, we can experiment with a use case where the user wants to only determine the outcome of the file using only 2 features instead of 50 features. The ground truth of the file is denoted by the letter in the file name e.g. Test Ransomware File E 2 features means this is an Encryptor Ransomware with 2 features.
- Next, based on analysis from the notebook, I recommend users to select Random Forest as the top performing model. However, users can play around and choose other models. This flexibility is offered to give users an experience of how users in SMEs can choose their model based on company requirements. For instance, so companies may not prioritise accuracy. Hence simpler models such as Logistic Regression can be choosen. 
- This is how the web application interface looks like upon running the Streamlit app
![image](https://github.com/khairulofficial/ransomwaredetection/assets/59458479/c951cf27-35ea-48cc-9540-8628aae919b2)
- This is how the interface looks like once prediction is displayed
![image](https://github.com/khairulofficial/ransomwaredetection/assets/59458479/41c34fae-8fcb-4405-80bd-fd3dafc99695)
- Feedback from professors who visited my project booth which can be a learning point for all of us: Higlight the prediction based on severity e.g. red for ransomware, green for goodware to help users notice easily. The dataset, obtained by paid researchers, may not be the best dataset as they have carried out encoding hence limiting interpretablity.


