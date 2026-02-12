class InsightAgent:

    def generate_insights(self, eda_report):

        insights = []

        shape = eda_report["shape"]
        columns = eda_report["columns"]
        summary = eda_report["summary"]

        insights.append(
            f"The dataset contains {shape[0]} rows and {shape[1]} columns.")

        insights.append(
            f"The dataset has the following columns: {', '.join(columns)}")

        for col, stats in summary.items():
            try:
                insights.append(
                    f"For column '{col}', the average value is {round(stats['mean'], 2)} "
                    f"with minimum {stats['min']} and maximum {stats['max']}."
                )
            except:
                continue

        insights.append(
            "No AI API was used. These insights are generated locally.")

        return "\n\n".join(insights)
