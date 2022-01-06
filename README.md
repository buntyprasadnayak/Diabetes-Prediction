# Diabetes-Prediction
Machine Learning "Diabetes prediction" project which predicts the diabetes for female person only.
The aim of this project is to know about health of the person by predicting whether the are diabetes or not.

The requirements.txt file has listed all Python libraries that your notebooks depend on, and they will be installed using:

pip install -r requirements.txt

## Work Flow of this project is 

1. We Analysis the Diabetes Data 
2. Some pre-processing with the data 
3. Training and testing split 
4. We use Support Vector machine Classifier 
5. New data given to the model 
6. Trained Support Vector Machine Classifier 
7. Prediction


## Technologies
1. Anaconda 
2. Pycharm
3. Google Colab 


The data in this project is taken from **Kaggle** where there are 9 rows:
Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
BloodPressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skin fold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml)
BMI: Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction: Diabetes pedigree function
Age: Age (years)

Outcome: Class variable (0 or 1) where 0 represent 'the person is not diabetes' and 1 represent 'The person is diabetes '

## How to Launch 
Make sure all the files are in the same folder and install all the dependencies 


Install streamlit to your folder 
```
pip install streamlit
```

**Change to current Path of the loaded_model variable in **  "Predictive System.py" and "Diabetes Prediction Web App.py" file **

Run the Launch command
```
streamlit run " 'your folder Location'/Diabetes Prediction Web App.py"

