import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation  # pylint: disable=import-error


def page_ml_performance_body():

    version = 'v1'

    st.title("ML Performance")

    st.header("Train, Validation and Test Set: Labels Frequencies")
    st.info(
        f"This bar graph shows a visual breakdown on the amount of images, for"
        f" each category label, that were used as dataset for the train, "
        f"validate and test data groupings."
    )

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.header("Model History")
    st.info(
        f"The graph below provide a visual representation of the learning "
        f" cycle for the ML model used for this project. The two graphs show "
        f"the accuracy and loss plots as a result of the training process.\n\n"
        f"These two graphs provide visual proof of a normal learning curve of "
        f"the ML pipeline as both graphs show a similar path and are close to "
        f"each other. These graphs prove that the model is neither overfitting"
        f" or underfitting; it is a normal learning curve."
    )

    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.header("Generalised Performance on Test Set")
    st.info(
        f"This table graph provides a numerical explanation of the line graphs"
        f" above, a normal learning curve and a 99% accurate ML model."
    )
    # load_test_evaluation(version)
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))
