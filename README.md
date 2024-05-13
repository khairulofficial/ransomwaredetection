# Ransomware Detection in Small & Medium Enterprises using Machine Learning

## Background
This project is regarding using machine learning for ransomware detection in Small & Medium Enterprises (SMEs). SMEs do not have the luxury of time, manpower and resources to collect, process and analyse all features of a ransomware. As such, this projects acts as triage where we utilise the minimum number of features possible while still maintaining an accuracy score of at least 90% for our top model. This project is inspired by Juan A. Herrera-Silva and Myriam Hernández-Álvarezhtt's paper titled Dynamic Feature Dataset for Ransomware Detection Using Machine Learning Algorithms (www.mdpi.com/1424-8220/23/3/1053)

## Project Structure
This project contains 4 main files:
1) Ransomware Training Dataset (under src/data)
2) Notebook for Analysis 
3) Code for Streamlit Web Application (under src)
4) Various sample files for prediction in the Streamlit Web Application

## Data and Instruction Details
Note:
- The training dataset collected by the reserachers above has 50 features
- Ensure that files are downloaded into the same folder as the notebook/web app that you are running. Many data source errors in data science projects arise due to dataset being downloaded directly into "Downloads" instead of the same folder as the notebook/web app.
- For Notebook for Anaylsis, ensure that you have installed the libraries shown in the import statement using "pip install -r requirements.txt"
- Section 12 of the notebook, Feature Reduction Using Principal Component Analysis, is miscelleanous. We will not recommend it as interpretability is limitied. You can interact with the scores and loadings plot to analyse potential relationships.
- For the Streamlit Web Application, ensure that you have installed streamlit. I will update by deploying it onto streamlit cloud in the future.
- Upload the sample files. Sample files refer to the files that users can upload into the web app. It does not refer to files for unit testing. For instance, we can experiment with a use case where the user wants to only determine the outcome of the file using only 2 features instead of 50 features. The ground truth of the file is denoted in the file name e.g. Sample Goodware 2 features means this is non-malicious file with 2 features.
- Next, based on analysis from the notebook, I recommend users to select Random Forest as the top performing model. However, users can play around and choose other models. This flexibility is offered to give users an experience of how users in SMEs can choose their model based on company requirements. For instance, so companies may not prioritise accuracy but rather low latency or computing costs. Hence simpler models such as Logistic Regression can be choosen. 
- This is how the web application interface looks like upon running the Streamlit app
![image](https://github.com/khairulofficial/ransomwaredetection/assets/59458479/9a2893b7-ec84-487a-b2b7-1db1a107b2f7)


- This is how the interface looks like once prediction is displayed
![image](https://github.com/khairulofficial/ransomwaredetection/assets/59458479/aadb929f-b128-448f-b9f4-4267799324a7)


- Video demo of web app

[![Video Title](https://img.youtube.com/vi/DOjKgGNEQ5A/0.jpg)](https://youtu.be/DOjKgGNEQ5A)

## Feedback and Extensions
- Feedback from professors who visited my project booth which can be a learning point for all of us: Higlight the prediction based on severity e.g. red for ransomware, green for goodware to help users notice easily. The dataset, obtained by paid researchers, may not be the best dataset as they have carried out encoding hence limiting interpretablity. (Note: I have incorporated the first feedback where colors are reflected based on predicted file category)
- To be updated: I will add in more explanation with regards to the paper by the researcher itself. 


