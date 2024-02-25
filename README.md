This project is regarding using machine learning for ransomware detection in SMEs. SMEs do not have the luxury of time and resources to analyse all features of a ransomware. As such, this projects acts as triage where we utilise the minimum number of feature possible while still maintaining an accuracy score of at least 90% for our top model. More background context will be updated. This project contains 3 files:
1) Ransomware Dataset
2) Notebook for Analysis
3) Code for Streamlit Web Application
4) Test use case files for Streamlit Web Application

Note:
- The dataset has 50 features
- Ensure that all 3 files are downloaded into the same folder. Many data source errors in data science projects arise due to dataset being downloaded directly into "Downloads" instead of the same folder as the notebook/web app.
- For No.2 Notebook for Anaylsis, ensure that you have installed the libraries shown in the import statement. I will update this repo in the future with a requirements.txt file to ease installation.
- Section 12 of the notebook, Feature Reduction Using Principal Component Analysis, is miscelleanous. We will not recommend it as interpretability is limitied. You can interact with the scores and loadings plot to analyse potential relationships.
- For No.3 Code for Streamlit Web Application, ensure that you have installed streamlit. I will update by deploying it onto streamlit cloud in the future.
- Test use case files refer to the files that users can upload into the web app. It does not refet to files for unit testing. For instance, we can experiment with a use case where the user wants to only determine the outcome of the file using only 2 features instead of 50 features.

