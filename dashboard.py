import streamlit as st
import pandas as pd
import pickle


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
    st.title("📺 Tubescope Overview")
    st.write("TubeScope explores what makes YouTube videos go viral — and how long that virality lasts. " \
    "By tracking daily trending videos using the YouTube Data API, we analyze how long videos from different content categories "
    "(like Music, Gaming, or News) stay on the trending list, visualize their popularity curves, and even predict how long new videos might trend..")

    st.subheader("Current Dataset Status")
    if df is None:
        st.info("No dataset uploaded yet.")
    else:
        st.success("Dataset loaded!")
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])
        st.dataframe(df.head())


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

    category_encoding_file = "category_encoder.pkl"

    model_columns_file = "model_columns.pkl"

    viral_prediction_file = "viral_prediction_model.pkl"

    with open("category_encoder.pkl", 'rb') as file1:
        model1 = pickle.load(file1)
    with open("model_columns.pkl", 'rb') as file2:
        model2 = pickle.load(file2)
    with open("viral_prediction_model.pkl", 'rb') as file3:
        model3 = pickle.load(file3)
    




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

