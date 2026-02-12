import pandas as pd


class IngestionAgent:

    def load_data(self, file):
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            return df

        except Exception as e:
            return str(e)
