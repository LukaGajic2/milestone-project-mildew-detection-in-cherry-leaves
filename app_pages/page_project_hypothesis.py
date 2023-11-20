import streamlit as st


def page_project_hypothesis_body():

    st.title("Mildew Detection Project Hypothesis")

    st.success(
        f"* We believe that Cherry leaves infected with powdery mildew shows "
        f"a distinct difference in color and appearance than purely green "
        f"healthy cherry leaves, making the differences markedly apparent. \n"

        f"* An Image Montage shows the clear difference between both kinds of"
        f" leaves. Powdery mildew being white and discolored and healthy "
        f"cherry leaves showing their normal dark green coloring.\n"

        f"* Average Image, Variability Image and Difference confirmed ours "
        f"hypothesis showing color difference between healthy and infected "
        f"leaves, however, there were no clear identifications via leaf shape."
        f"\n"

        f"* ML pipeline performance was evaluated and it differentiates a "
        f"healthy leaf from an infected leaf with at least of 97% accuracy.\n"
    )
