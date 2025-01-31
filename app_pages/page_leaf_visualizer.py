import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_leaf_visualizer_body():

    st.title("Leaf Visualizer")

    st.info(
        f"The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one with powdery mildew."
    )

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        st.image(avg_powdery_mildew,
                 caption='Cherry Leaf infected with powdery mildew - Average and Variability')
        st.image(avg_healthy,
                 caption='Healthy Cherry Leaf - Average and Variability')
        st.write("---")

        st.success(
            f"Upon inspection, a significant visual difference in consistent "
            f"colouring is present: "
            f"a healthy leaf presents more greenish uniform coloring.\n"
            f"where as an infected leaf presents a fuzzy white surface, "
            f"inconsistent colour patterns and white blotches.\n"
        )
        st.write("---")

    if st.checkbox("Differences between a Healthy and an Infected Cherry Leaf"):
        diff_between_avg = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"The comparison image between the two averages is the dark image "
            f"in the following checkbox, a further montage of both the healthy"
            f" and infected leaves will be shown.\n "
            f"These average images do show similarities for each grouping: "
            f"the healthy images are greener and the "
            f"infected images show a lighter more blotchy leaf.\n\n"
        )

        st.image(diff_between_avg, caption='Difference between average images')

    if st.checkbox("Image Montage"):
        st.write("* Click the 'Create Montage' button to refresh images")
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces"
            )
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
