import streamlit as st
from agents.ingestion_agent import IngestionAgent
from agents.cleaning_agent import CleaningAgent
from agents.eda_agent import EDAAgent
from agents.insight_agent import InsightAgent
from agents.viz_agent import VizAgent

st.title("Smart Data Analyst AI Agent")

st.write("Upload your dataset to begin analysis")

uploaded_file = st.file_uploader(
    "Choose CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:

    ingest = IngestionAgent()
    clean = CleaningAgent()
    eda = EDAAgent()
    insight = InsightAgent()
    viz = VizAgent()

    data = ingest.load_data(uploaded_file)

    st.subheader("Uploaded Dataset Preview")
    st.dataframe(data)

    cleaned_data, report = clean.analyze_and_clean(data)

    st.subheader("Data Cleaning Report")
    st.write("Missing Values:")
    st.write(report["missing_values"])
    st.write("Duplicate Rows:")
    st.write(report["duplicate_rows"])

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(cleaned_data)

    st.subheader("Exploratory Data Analysis")

    eda_report = eda.generate_eda_report(cleaned_data)

    st.write("Dataset Shape:")
    st.write(eda_report["shape"])

    st.write("Columns:")
    st.write(eda_report["columns"])

    st.write("Summary Statistics:")
    st.write(eda_report["summary"])

    st.subheader("AI Generated Insights")

    insights = insight.generate_insights(eda_report)
    st.write(insights)

    # --------- NEW VISUALIZATION PART ---------

    st.subheader("Data Visualizations")

    numeric_cols = viz.numeric_columns(cleaned_data)

    if len(numeric_cols) > 0:

        st.write("Correlation Heatmap")
        corr_fig = viz.correlation_chart(cleaned_data)

        if corr_fig:
            st.plotly_chart(corr_fig)

        selected_col = st.selectbox(
            "Select Column for Visualization",
            numeric_cols
        )

        st.write("Histogram")
        hist = viz.histogram(cleaned_data, selected_col)

        if hist:
            st.plotly_chart(hist)

    else:
        st.write("No numeric columns available for visualization.")
