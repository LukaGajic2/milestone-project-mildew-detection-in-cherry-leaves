import streamlit as st


def page_summary_body():

    st.title("Project Summary Overview")

    st.header("General Information: ")
    st.info(
        f" Powdery mildew is a fungal disease that affects a wide range of "
        f"plants. Powdery mildew diseases are caused by many different species"
        f" of ascomycete fungi in the order Erysiphales. Powdery mildew is one"
        f" of the easier plant diseases to identify, as its symptoms are quite"
        f" distinctive. Infected plants display white powdery spots on the "
        f"leaves and stems. The lower leaves are the most affected, but the "
        f"mildew can appear on any above-ground part of the plant. As the "
        f"disease progresses, the spots get larger and denser as large numbers"
        f" of asexual spores are formed, and the mildew may spread up and down"
        f" the length of the plant."
    )

    st.header("Problem Statement: ")
    st.info(
        f"Farmy and Foods agricultural plantation has recently discovered "
        f"Powdery Mildew infections in some of their Cherry Trees. The Cherry "
        f"Leaves production is one of their largest portfolio assets and there"
        f" can be a large financial short term and long term to a variety of "
        f"thier crops if the infection is not identified and prevented "
        f"quickly. With conventional means, there is a large labor cost in "
        f"time and resources to identify infected leaves. Farmy and Foods "
        f"requires a new method to quickly identify infected leaves from "
        f"healthy leaves in order to save time and labour to treat the trees, "
        f"save the harvest and protect the company's finances."
    )
    st.header("Project Dataset: ")
    st.info(
        f"The [Kaggle Cherry Leaves](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) dataset contains "
        f"4208 images of healthy and infected cherry leaves and was used as "
        f"the source to train the ML app.\n\n")

    st.header("Business Requirements: ")
    if st.checkbox("Requirement 1:"):
        st.info(
            f"The client is interested in conducting a study to visually "
            f"differentiate a healthy cherry leaf from one with powdery "
            f"mildew."
        )

    if st.checkbox("Requirement 2:"):
        st.info(
            f"The client is interested in predicting if a cherry leaf is "
            f"healthy or contains powdery mildew."
        )
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/LukaGajic2/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md).")
