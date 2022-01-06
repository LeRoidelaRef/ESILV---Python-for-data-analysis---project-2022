# ESILV---Python-for-data-analysis---project-2022

-------------------------------------------------------------------------------
The goal is to identify the copiyst of the Avila Bible with Machine Learning
This is a classification Machine Learning.

The Dataset is divided in two parts, avila_tr and avila_ts

We train many classification methods:
-Logisical Regression
-Logistical Regression with PCA Method
-K Neighbors Classifier
-Random Forest
-Random Forest with PCA Method
-Random Forest with Grid Search Method

To evaluate each Method we use Accuracy, Precision, Recall, f1_Score, Confusion_Matrix and Cross Validation from sklearn

-------------------------------------------------------------------------------------

Flask API

In order to use the API you need to install flask (pip install flask).

Then you need to go into the directory of the Flask application and write "flask run" from the command line.

This API allows the use of the Machine Learning model, using pickle, and can also show specific rows of the dataset.
