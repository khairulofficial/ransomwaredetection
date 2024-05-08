import streamlit as st
import pandas as pd
from test import test_model
import hydralit_components as hc
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

def plot_accuracy():
    # accuracy scores 
    st.set_option('deprecation.showPyplotGlobalUse', False)
    accuracy_scores = [70, 83, 98, 74,99,99,100]
    
    model_names = ["SVM", "Logistic Regression", "KNN", "Naive Bayes", "Neural Network", "XGBoost", "Random Forest"]
    
    # Create the bar chart
    plt.figure(figsize=(8, 6))  # Adjust figure size as desired
    plt.bar(model_names, accuracy_scores)
    
    # Add labels and title
    plt.xlabel("Model")
    plt.ylabel("Accuracy (%)")
    plt.title("Model Accuracy Comparison")
    
    # Customize the plot 
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    for i, v in enumerate(accuracy_scores):
        plt.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom')
    
    # Display the plot
    plt.tight_layout()
    st.pyplot()

def plot_recall():
    # recall scores
    st.set_option('deprecation.showPyplotGlobalUse', False)
    recall_scores = [71, 83, 96, 73,97,100,100]
    
    model_names = ["SVM", "Logistic Regression", "KNN", "Naive Bayes", "Neural Network", "XGBoost", "Random Forest"]
    
    # Create the bar chart
    plt.figure(figsize=(8, 6))  # Adjust figure size as desired
    plt.bar(model_names, recall_scores)
    
    # Add labels and title
    plt.xlabel("Model")
    plt.ylabel("Recall (%)")
    plt.title("Model Recall Comparison")
    
    # Customize the plot 
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    for i, v in enumerate(recall_scores):
        plt.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom')
    
    # Display the plot
    plt.tight_layout()
    st.pyplot()

def plot_latency():
    # latency duration
    st.set_option('deprecation.showPyplotGlobalUse', False)
    latency = [39, 1.43, 26.89, 1.69,10.88,3.38,2.18]
    
    
    model_names = ["SVM", "Logistic Regression", "KNN", "Naive Bayes", "Neural Network", "XGBoost", "Random Forest"]
    
    # Create the bar chart
    plt.figure(figsize=(8, 6))  # Adjust figure size as desired
    plt.bar(model_names, latency)
    
    # Add labels and title
    plt.xlabel("Model")
    plt.ylabel("Duration (ms)")
    plt.title("Model Latency Comparison")
    
    # Customize the plot
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    for i, v in enumerate(latency):
        plt.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom')
    
    # Display the plot
    plt.tight_layout()
    st.pyplot()
    
def show_home_page():
    st.title("Ransomware Detection App")
        
    st.text("")
    st.text("")
    st.text("")

    # instructions
    st.markdown("""
    1. Click "Browse File" to upload the csv file. You can use sample files from [Github](https://github.com/khairulofficial/ransomwaredetection/tree/main/sample%20files) 
    2. Select machine learning model. If unsure, please use recommended model.
    3. Click "Predict"
    """)
    
    # Load logo in sidebar
    html_img = """
    <div style="text-align: center;">
    <img src="data:image/jpeg;base64,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" alt="My Image" style="border-radius: 50%; width: 100px; height: 100px;">
    </div>
    """

    # Display the HTML in the sidebar with unsafe_allow_html
    st.sidebar.markdown(html_img, unsafe_allow_html=True)
    
    st.sidebar.text("")
    st.sidebar.text("")
    
    
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

                
                theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
                theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}
                theme_model = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-database'}
                theme_accuracy = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-percent'}
                            
                # display prediction
                if family == 0:
                    hc.info_card(title='This file is predicted to be a: \nGOODWARE', sentiment='good',theme_override=theme_good)
                
                elif family == 1:
                    # display further instructions
                    hc.info_card(title='This file is predicted to be an: \nENCRYPTOR RANSOMWARE', content='Please delete the original file if you have downloaded it on any machine & inform your admin', sentiment='bad',theme_override=theme_bad)
                
                elif family == 2:
                    # display further instructions
                    hc.info_card(title='This file is predicted to be a: \nLOCKER RANSOMWARE', content='Please delete the original file if you have downloaded it on any machine & inform your admin', sentiment='bad',theme_override=theme_bad)
            
                # model and file details
                cc = st.columns(2)

                with cc[0]:
                    hc.info_card(title='Model:', content=f'{model}', sentiment='neutral', theme_override=theme_model)
                
                with cc[1]:
                    hc.info_card(title='Accuracy:', content=f'{cvscore:.2%}', sentiment='neutral', theme_override=theme_accuracy)
                
                
        except:
            st.warning("Invalid File. Please try another file.")
    
        
def show_demo_page():
    st.title("Sample Goodware Demo")
    st.video("https://youtu.be/DOjKgGNEQ5A")

def show_vis_page():
    st.title("Model Comparison")
    st.text("(when all features are used for training)")
    st.text("")
    st.text("")
    col1, col2, col3 = st.columns(3)
    col1.metric("Best Accuracy: :blue[Random Forest]", "100%", "Slightly better than XGBoost & Neural Network")
    col2.metric("Best Recall: :blue[Random Forest, XGBoost]", "100%", "3% better than Neural Network")
    col3.metric("Lowest Latency: :blue[Logistic Regression]", "1.43ms", "~1.5x faster than Random Forest")

    col1, col2 = st.columns(2)
    with col1:
        selection = st.selectbox(
        "Plot Bar Chart of",
        ("Accuracy (10-fold cross-validation average)", "Recall", "Latency (10 prediction average)"))

    with col2:
        if selection == "Accuracy (10-fold cross-validation average)":
            plot_accuracy()
        elif selection == "Recall":
            plot_recall()
        else:
            plot_latency()

    
def main():

    # page config
    st.get_option("theme.primaryColor")
    st.get_option("theme.textColor")
    st.get_option("theme.backgroundColor")
    st.get_option("theme.secondaryBackgroundColor")
    st.get_option("theme.font")
    image_url = "data:image/jpeg;base64,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"
    st.set_page_config(layout="wide", page_icon=image_url, page_title = "Ransomware Detection App")
    
    selected = option_menu(
            menu_title=None,  
            options=["Home", "Visualisation", "Demo"], 
            icons=["house", "bar-chart", "play"],  
            menu_icon="cast", 
            default_index=0, 
            orientation="horizontal",)
    
    if selected == "Home":
        show_home_page()
        
    elif selected == "Visualisation":
        show_vis_page()
        
    else:
        show_demo_page()
        

if __name__ == "__main__":
    main()
