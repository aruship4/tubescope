import streamlit as st
import pandas as pd
import pickle
from pathlib import Path


st.set_page_config(
    page_title="Tubescope Dashboard",
    page_icon="📊",
    layout="wide"
)


#sidebar
st.sidebar.title("Tubescope Dashboard")
st.sidebar.write("Upload your dataset to begin.")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Load data if uploaded
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)

# Sidebar Page Navigation
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Models", "Plots", "Exploration", "Random Forest Model", "Survival Analysis"]
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

    st.header( "Most Common Video Tags")
    st.image("most_common_tags-2.png", width = 650, caption = (
            "This chart highlights the most frequently used tags among trending YouTube videos, "
            "revealing which themes, keywords, and topics creators use to optimize discoverability."
        )
    )

    st.header("Average Rank Trajectory")
    st.image("rank_trajectory.png",  width = 650, caption = "Average Rank Trajectory")

    st.header("Top Categories by Views")
    st.image("top_categories_by_views.png",  width = 650, caption = "Top Categories by Views")

    st.header( "Views Per Day vs. Days Since Posted")
    st.image("views_per_day_vs_age.png",  width = 650, caption = "Views Per Day vs. Days Since Posted")

    uploaded_file = st.file_uploader("Choose a .pkl file", type=["pkl"])


elif page == "Models":

    st.title("Models")

    # Path to your pickle files
    base_path = Path(__file__).parent  # ensures relative path works

    category_encoding_file = base_path / "category_encoder.pkl"
    model_columns_file = base_path / "model_columns.pkl"
    viral_prediction_file = base_path / "viral_prediction_model.pkl"

    # Load the pickle files safely
    try:
        with open(category_encoding_file, 'rb') as f:
            model1 = pickle.load(f)
        with open(model_columns_file, 'rb') as f:
            model2 = pickle.load(f)
        with open(viral_prediction_file, 'rb') as f:
            model3 = pickle.load(f)
        
        st.success("Models loaded successfully!")
        st.write("✅ Category Encoder:", model1)
        st.write("✅ Model Columns:", model2)
        st.write("✅ Viral Prediction Model:", model3)

    except ModuleNotFoundError as e:
        st.error(f"Cannot load model: missing module. {e}")
    except FileNotFoundError as e:
        st.error(f"Pickle file not found: {e}")
    except Exception as e:
        st.error(f"Failed to load models: {e}")
    '''
    st.title("Models")

    category_encoding_file = "category_encoder.pkl"

    model_columns_file = "model_columns.pkl"

    viral_prediction_file = "viral_prediction_model.pkl"

    with open("category_encoder.pkl", 'rb') as file1:
        model1 = pickle.load(file1)
    with open("model_columns.pkl", 'rb') as file2:
        model2 = pickle.load(file2)
    with open("viral_prediction_model.pkl", 'rb') as file3:
        model3 = pickle.load(file3)
    
    '''




elif page == "Exploration":
    st.title("🔎 Data Exploration")

    if df is None:
        st.warning("Please upload a dataset first.")
    else:
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Column Information")
        st.write(df.dtypes)

        st.subheader("Missing Values")
        st.write(df.isna().sum())

        st.info("Plots will be added later.")


elif page == "Random Forest Model":
    st.title(" Random Forest Classifier")

    if df is None:
        st.warning("Please upload a dataset to train or evaluate a model.")
    else:
        st.subheader("Model Inputs")
        st.write("Feature selection, training, and predictions will be added later.")

        with st.expander("Model Settings"):
            n_estimators = st.slider("Number of Trees", 10, 300, 100)
            max_depth = st.slider("Max Depth", 2, 30, 10)
            st.write("Model settings chosen.")

        st.info("The Random Forest implementation will be added later.")


elif page == "Survival Analysis":
    st.title("⏳ Survival Analysis (Kaplan-Meier)")

    if df is None:
        st.warning("Please upload a dataset to run survival models.")
    else:
        st.subheader("Survival Model Inputs")
        st.write("Specify the duration and event columns below.")

        duration_col = st.selectbox("Duration Column", options=df.columns)
        event_col = st.selectbox("Event Column", options=df.columns)

        st.info("Kaplan-Meier plots and model will be added later.")

