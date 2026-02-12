import plotly.express as px
import pandas as pd


class VizAgent:

    def correlation_chart(self, df):
        try:
            corr = df.corr(numeric_only=True)
            fig = px.imshow(corr, title="Correlation Heatmap")
            return fig
        except:
            return None

    def bar_chart(self, df, column):
        try:
            fig = px.bar(df[column].value_counts(),
                         title=f"Distribution of {column}")
            return fig
        except:
            return None

    def histogram(self, df, column):
        try:
            fig = px.histogram(df, x=column,
                               title=f"Histogram of {column}")
            return fig
        except:
            return None

    def numeric_columns(self, df):
        return df.select_dtypes(include=['int64', 'float64']).columns.tolist()
