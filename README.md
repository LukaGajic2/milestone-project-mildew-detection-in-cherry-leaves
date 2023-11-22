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
  - [Bugs](#bugs)
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

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

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
  - We will display an image montage for either infected or uninfected leaves.

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

The Dashboard contains five app pages in Streamlit App User Interface style.

1. Page Summary Overview

- General information  

Powdery mildew is a fungal disease that affects a wide range of plants. Powdery mildew diseases are caused by many different species of ascomycete fungi in the order Erysiphales. Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. Infected plants display white powdery spots on the leaves and stems. The lower leaves are the most affected, but the mildew can appear on any above-ground part of the plant. As the disease progresses, the spots get larger and denser as large numbers of asexual spores are formed, and the mildew may spread up and down the length of the plant.

- Problem Statement

Farmy and Foods agricultural plantation has recently discovered Powdery Mildew infections in some of their Cherry Trees. The Cherry Leaves production is one of their largest portfolio assets and there can be a large financial short term and long term to a variety of thier crops if the infection is not identified and prevented quickly. With conventional means, there is a large labor cost in time and resources to identify infected leaves. Farmy and Foods requires a new method to quickly identify infected leaves from healthy leaves in order to save time and labour to treat the trees, save the harvest and protect the company's finances.

- Project Dataset

The Kaggle Cherry Leaves dataset contains 4208 images of healthy and infected cherry leaves and was used as the source to train the ML app.

- Business Requirements

- The client is interested to have a study to visually differentiate between infected and uninfected cherry leaves.
- The client is interested in positively identifying whether a particular cherry leaf is infected with mold or not.

2. Leaf Visualizer

On this page we answer the first business requirement: 
The client is interested to have a study to visually differentiate between infected and uninfected cherry leaves.

- Checkbox 1 shows Difference between Average and Variability image.
- Checkbox 2 shows Differences between a Healthy and an Infected Cherry Leaf
- Checkbox 3 shows Image Montage where user can self make collage of 24 images of infected or healthy leaves to see the difference.

3. Mildew Detector

The Mildew Detector page is, with no doubt, the most important page in the dashboard.
It answers the second business requirement: The client is interested in positively identifying whether a particular cherry leaf is infected with mold or not.
On the page the client/user can interact with the ML app by uploading images and having the app predict if the leaf is infected or healthy.

![Screenshot of the Mildew Detector page](/assets/detector.png)

4. Project Hypothesis

On this page it is explained project hypothesis and how it is validated.

![Screenshot of the Project Hypothesis page](/assets/hypothesis.png)

5. ML Performance

On this page it is represented:

- Train, Validation and Test set(bar graph shows a visual breakdown on the amount of images, for each category label).
- Model History(graph provide a visual representation of the learning cycle for the ML model used for this project).
- Generalised Performance on Test Set(graph provides a numerical explanation of the line graphs above)

## Bugs

1. fixed bugs 

- AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

(ANTIALIAS was removed in Pillow 10.0.0. I used LANCZOS as recommended "Reference: Pillow 10.0.0 release notes (with table of removed constants)")

- pylint(import_error)

![Screenshot of the import_error issue](/assets/import_error.png)

fixed by adding comment "# pylint: disable=import-error" next to import (thanks to Neil McEwen for support!)

2. unfixed bugs

- no unfixed bugs

## Deployment

### Heroku

- The App live link is: <https://mildew-detector-live-02cdc32ebba0.herokuapp.com/>
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. Had to change Heroku stack from Heroku-22 to Heroku-20.

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

- [Codeanywhere](https://app.codeanywhere.com/) is the workspace that hosted all facets of the project.

- [Heroku](https://heroku.com) was used for deployment of the project.

## Credits

### Acknowledgements

- Walkthrough Project 1: Malaria Detector was followed and replicated to conduct the study, build the ML model and construct the Streamlit site.  Much of the code was replicated from the project and tailored as required.
- (<https://github.com/ericjonesdev/milestone-project-cherry-leaves-mildew-detection/tree/main>) used as inspiration during building notebooks and streamlit app

### Content

- General information about powdery mildew in the "Project Summary Overview" was sourced from [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew)

### Media

- The images used for the dataset were sourced from this [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves) site.
