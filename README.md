# Smart Data Analyst AI Agent (SDA-Agent)

An AI-powered automated data analytics system that acts like a virtual data analyst.  
This project allows users to upload datasets and automatically performs data cleaning, exploratory data analysis, insight generation, and visualization.

---

## 🚀 Project Overview

The Smart Data Analyst AI Agent (SDA-Agent) is designed to automate common data analysis tasks using a modular AI-agent-based architecture.

It enables users to:

- Upload CSV or Excel datasets  
- Automatically clean and preprocess data  
- Perform Exploratory Data Analysis (EDA)  
- Generate human-readable insights  
- Visualize data through interactive charts  

This project simulates the workflow of a real data analyst in an automated and user-friendly manner.

---

## 🧠 Key Features

- 📂 **Dataset Upload:** Supports CSV and Excel files  
- 🧹 **Data Cleaning:** Detects missing values and duplicates  
- 📊 **Exploratory Data Analysis:** Generates dataset summary and statistics  
- 💡 **Insight Generation:** Produces automatic insights from data  
- 📈 **Visualization:** Creates histograms and correlation heatmaps  
- 🌐 **Interactive Dashboard:** Built using Streamlit  

---

## 🏗 System Architecture

The project follows a modular multi-agent design:
User Input  
↓  
Ingestion Agent → Cleaning Agent → EDA Agent → Insight Agent → Visualization Agent  
↓  
Final Analytics Dashboard Output


Each agent performs a specific task to complete the end-to-end analytics workflow.

---

## 🛠 Technologies Used

| Component | Technology |
|---------|-----------|
| Programming Language | Python |
| Frontend Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Insights Engine | Rule-based AI |
| Environment | Python Virtual Environment |

---

## 📁 Project Structure

SDA-Agent/
│
├── agents/
│ ├── ingestion_agent.py
│ ├── cleaning_agent.py
│ ├── eda_agent.py
│ ├── insight_agent.py
│ └── viz_agent.py
│
├── utils/
│ └── prompts.py
│
├── app.py
├── requirements.txt
└── README.md


---

## ⚙ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone <repository_url>
cd SDA-Agent
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
---

