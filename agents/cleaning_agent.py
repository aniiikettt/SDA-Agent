import pandas as pd


class CleaningAgent:

    def analyze_and_clean(self, df):

        report = {}

        # Missing values info
        report["missing_values"] = df.isnull().sum().to_dict()

        # Duplicate rows count
        report["duplicate_rows"] = int(df.duplicated().sum())

        # Basic column types
        report["data_types"] = df.dtypes.astype(str).to_dict()

        # Clean dataset
        cleaned_df = df.drop_duplicates()
        cleaned_df = cleaned_df.fillna(method="ffill")

        return cleaned_df, report
