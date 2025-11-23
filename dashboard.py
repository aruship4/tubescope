import streamlit as st
import pandas as pd
import pickle
from pathlib import Path


st.set_page_config(
    page_title="Tubescope Dashboard",
    page_icon="📊",
    layout="wide"
)


# Sidebar Page Navigation
page = st.sidebar.radio(
    "Navigation", 
    ["Home", "Models", "Plots", "Findings"]
)

if page == "Home":
    st.header("DS3 Projects Fall 2025")
    st.write("Project Members: Yra Climaco, Vivek Moorkoth, Arushi Patra, Nathaniel Trueba, Project Mentor: Vedant Vardhaan")
    st.title("📺 Tubescope Overview")
    st.write("TubeScope explores what makes YouTube videos go viral — and how long that virality lasts. " \
    "By tracking daily trending videos using the YouTube Data API, we analyze how long videos from different content categories "
    "(like Music, Gaming, or News) stay on the trending list, visualize their popularity curves, and even predict how long new videos might trend..")

    st.subheader("Look through our findings, data, and models through the Navigation section!")
    

elif page == "Plots":
    st.title("📊 Plots")


    st.subheader("Kaplan-Meier Category Survival Curve")
    st.image("KM_category_survival_curve.png", width = 650, caption = (
            "This chart uses Kaplan-Meier (explain what it is and purpose)"
            "to predict how long a video lasts"
        )
    )

    st.subheader("Kaplan-Meier Survival Curve")
    st.image("KM_survival_curve.png", width = 650, caption = (
        "This chart uses Kaplan-Meier (explain what it is and purpose)"
        "to predict how long a video lasts"
        )
    )

    st.subheader("Confusion Matrix")
    st.image("confusion_matrix.png", width = 650, caption = (
        "x"
        )
    )

    st.subheader("Top 15 Features")
    st.image("feature_importance.png", width = 650, caption = (
        "This predicts ___"
        )
    )



    st.subheader( "Most Common Video Tags")
    st.image("most_common_tags-2.png", width = 650, caption = (
            "This chart highlights the most frequently used tags among trending YouTube videos, "
            "revealing which themes, keywords, and topics creators use to optimize discoverability."
        )
    )

    st.subheader("Average Rank Trajectory")
    st.image("rank_trajectory.png",  width = 650, caption = "Average Rank Trajectory")

    st.subheader("Top Categories by Views")
    st.image("top_categories_by_views.png",  width = 650, caption = "Top Categories by Views")

    st.subheader( "Views Per Day vs. Days Since Posted")
    st.image("views_per_day_vs_age.png",  width = 650, caption = "Views Per Day vs. Days Since Posted")



elif page == "Models":

    st.title("Models")

    with open("category_encoder.pkl", 'rb') as file1:
        model1 = pickle.load(file1)
    with open("model_columns.pkl", 'rb') as file2:
        model2 = pickle.load(file2)
    with open("viral_prediction_model.pkl", 'rb') as file3:
        model3 = pickle.load(file3)

    st.success("Models loaded successfully!")
    st.write(model1)
    st.write(model2)
    st.write(model3)
    
    




elif page == "Findings":
    st.title("🔎 Inferences and Conclusions")

    




