# Mildew Detection in Cherry Leaves

********************

## Table of Contents

- [Mildew Detection in Cherry Leaves](#mildew-detection-in-cherry-leaves)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate](#hypothesis-and-how-to-validate)
    - [Hypothesis](#hypothesis)
    - [Validation](#validation)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Acknowledgements](#acknowledgements)
    - [Content](#content)
    - [Media](#media)

## Introduction

The customer is in search of a more efficient way of determining if their crop (Cherry Leaves) has been infected with a powdery mildew fungus or if it is healthy. Their current method of crop analysis is to manually inspect the leaves on every tree in their plantation, which is both time consuming and resource expensive. At its core, this application embodies the principles of supervised machine learning. It is single-label, binary classification model characterized by its ability to describe two distinct categories.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.

- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate

### Hypothesis

- We suspect that leaves infected by mildew shows white, powdery patches of fungus that spread on either the upper or lower surfaces of the leaf. These distinct indicators will be adequate for training a machine learning model as they effectively distinguish between infected leaves and those that are fungus-free.
- Conducting an average image analysis can assist in further investigating the matter.
- We propose that employing binary classification would be the most suitable approach for discerning the distinction between infected and healthy leaves.

### Validation

- Business Requirement 1: The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
  - "Mean" and "standard deviation" images will be displayed for healthy leaves and those infected with powdery mildew.
  - The difference between an average healthy leaf and the average mildew-infected leaf will be displayed.
  - An image montage will follow for the selected label: healthy and powdery_mildew.
- Business Requirement 2: The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
  - We want to predict whether a random sample leaf image is Infected or Uninfected with powdery mildew desease.
  - We want to build an ML model with binary classification and generate report on the results.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- **Business Requirement 1**: Data Visualization

  - We will display the "mean" and "standard deviation" images for infected and uninfected leaves.
  - We will display the difference between an average infected leaf and an average uninfected leaf.
  - We will display an image montage for either infected or uninfected cells.

- **Business Requirement 2**: Classification
  - We want to predict if a choosen cherry leaf is infected, or not, by powdery mildew.
  - We want to build a binary classifier and generate reports.

## ML Business Case

- We want to build an ML model that can accurately predict whether a random sample leaf image is presenting infected or unifected cherry leaf.
- We suggest a supervised ML model, a binary class, single label, classification model.
- Our ideal outcome is to provide the Farmy & Foods team a faster and more reliable diagnostic for the detection of the fungal disease on cherry tree crops.
- The model success metrics are 97% or above on the test set.
- The model's output will be binary: "infected" or "unifected" will be displayed to the application user.
- Heuristics: Today the client spends an average of 30 minutes manually assessing whether a tree is infected with powdery mildew. This procedure require staff with certain knowledge of the disease to accurately categorize the trees. By implementing a predictive analytics application, there would be a significant reduction in both need of educated staff as well ass reducing the time needed to categorize results.
- The training data is sourced from Kaggle.

## Dashboard Design

## Unfixed Bugs

## Deployment

### Heroku

* The App live link is: https://
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 

## Main Data Analysis and Machine Learning Libraries

- [Jupyter notebooks](https://jupyter.org/) was the main source used for running and executing the ML pipelines.

- [Streamlit](https://streamlit.io/) is used to host the interactive dashboard.

- [Pandas](https://pandas.pydata.org/) is used for data analysis, especially for structuring the data.

- [Numpy](https://numpy.org/) is used to handle and manipulate multi-dimensional arrays, including providing a wide set of mathematical functions to operate on those arrays.

- [Matplotlib](https://matplotlib.org/) is used for data visualization including embedding plots in Jupyter notebooks.

- [Plotly](https://plotly.com/) is used for plotting data, functions, and to add animation to data visualization.

- [Scikit-learn](https://scikit-learn.org/stable/) contains tools used for data processing, predictive analysis, specifically used in this case to train the machine learning models for classification.

- [Seaborn](https://seaborn.pydata.org/) is a high-level interface for statistical graphics and it offers numerous built-in themes for styling Matplot graphics.

- [Tensorflow](https://www.tensorflow.org/) is used to filter out corrupt images or missing data during image processing.

- [Keras](https://keras.io/) was used for the CNN model for the ML pipeline.

- [Joblib](https://joblib.readthedocs.io/en/latest/) was used for loading and saving the images shapes.

- [Github](https://github.com/) is used for hosting the project and accepting all of the pushed code.

- [Gitpod](https://github.com/) is the workspace that hosted all facets of the project.

- [Heroku](https://heroku.com) was used for deployment of the project.

## Credits

### Acknowledgements

- Walkthrough Project 1: Malaria Detector was followed and replicated to conduct the study, build the ML model and construct the Streamlit site.  Much of the code was replicated from the project and tailored as required.

### Content

- General information about powdery mildew in the Executive Summary was sourced from [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew)

### Media

- The images used for the dataset were sourced from this [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves) site.
