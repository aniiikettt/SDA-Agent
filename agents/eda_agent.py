class EDAAgent:

    def generate_eda_report(self, df):

        report = {}

        # Basic Info
        report["shape"] = df.shape

        report["columns"] = list(df.columns)

        report["data_types"] = df.dtypes.astype(str).to_dict()

        # Summary Statistics
        report["summary"] = df.describe().to_dict()

        # Null values
        report["null_values"] = df.isnull().sum().to_dict()

        return report
