# Football (EPL) Win Prediction Model
This repository contains the code and resources for a machine learning project that aims to predict the chance of winning a match for a given football team. 

### Project Overview
The Football Winning Percentage Prediction project utilizes machine learning techniques to forecast the likelihood of a football team winning a match. The project leverages historical data from the past three seasons (2020-21, 2021-22, and 2022-23) to train and evaluate the prediction models.

### Data Collection
The dataset used for training the machine learning models was obtained by scraping data from FBref.com. The scraping process is documented in the *scraping.ipynb* file, which provides details about how the data was collected using the Beautiful Soup library.

### Machine Learning Models
The prediction models are implemented in the *prediction_model.ipynb* notebook. Three different models were trained and evaluated for this project: **Random Forest**, **XGBoost**, and **Logistic Regression**. The notebook contains the code for each model, including data preprocessing, feature selection, and model training.

### Web Application
To provide easy accessibility and user interaction, a web application was created using the Streamlit library. The application is implemented in the *app.py* file. Users can input the relevant features, and the trained models will predict the winning percentage of a football team in a match.

To access the web application, follow these steps:
1. Clone this repository to your local machine using the following command:
`git clone https://github.com/2spi/pl-predictor.git`
2. Install the required dependencies by running the following command:
`pip install -r requirements.txt`
3. Run the web application using the following command:
`streamlit run app.py`
