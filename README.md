# 🏏 IPL Win Predictor using Machine Learning

---

## 🔍 1. Introduction
The Indian Premier League (IPL) is one of the most competitive and unpredictable T20 cricket tournaments in the world. With match dynamics changing every over, fans and analysts are always eager to predict the likely winner. 

The **IPL Win Predictor** is a machine learning-powered web application that provides **real-time, data-driven win probability predictions** based on the current match scenario. By processing historical match and ball-by-ball data, it estimates the winning chance of the batting team during a live match.

This project demonstrates how machine learning can bridge sports and data analytics, turning complex match scenarios into actionable insights for fans, analysts, and broadcasters.

---

## 🎯 2. Objective
- Develop a machine learning model that uses live match features to estimate win probability.
- Create an intuitive web-based interface for users to input real-time match situations and get predictions.
- Help analysts and fans understand match outcomes using statistical probability instead of pure intuition.
- Demonstrate end-to-end deployment of an ML pipeline — from data preprocessing to web deployment.

---

## 📦 3. Dataset Description

### A. `matches.csv`
Contains high-level match metadata:
- `id`: Unique match identifier
- `season`: Year of the match
- `city`: Venue city
- `team1`, `team2`: Competing teams
- `winner`: Winning team
- `toss_winner`, `toss_decision`: Toss information
- `result`: Match result status
- `dl_applied`: Was DLS method used

### B. `deliveries.csv`
Contains granular, ball-by-ball delivery data:
- `match_id`: Foreign key linking to `matches.csv`
- `inning`: Inning number (1 or 2)
- `batting_team`, `bowling_team`: Teams involved in delivery
- `over`, `ball`: Over and ball number
- `batsman`, `bowler`: Player names
- `total_runs`: Runs scored in the delivery
- `player_dismissed`: Player dismissed (if any)

---

## 🧹 4. Data Cleaning and Preprocessing
1. Filtered out rain-affected matches (DLS applied).
2. Standardized team names (e.g., "Delhi Daredevils" to "Delhi Capitals").
3. Removed irrelevant columns and handled missing values.
4. Selected only 2nd innings for training (since the label is known).
5. Engineered features such as runs left, balls left, wickets left, current run rate (CRR), and required run rate (RRR).

---

## 🧠 5. Feature Engineering
Features used for modeling:
- `batting_team`
- `bowling_team`
- `city`
- `runs_left`
- `balls_left`
- `wickets` (wickets remaining)
- `total_runs_x` (target)
- `crr` (Current Run Rate)
- `rrr` (Required Run Rate)

**Label:**
- `1` if batting team wins, else `0`.

---

## 📊 6. Exploratory Data Analysis (EDA)
- Analyzed win probability vs overs left.
- Studied the impact of wickets remaining on match outcome.
- Explored how target score affects win likelihood.
- Investigated stadium/city bias.
- Visualized data using heatmaps, bar charts, and line plots.

---

## 🔧 7. Model Development

- **Model:** Logistic Regression (for interpretability and speed)
- **Pipeline:**
  - OneHotEncoding for categorical features (`batting_team`, `bowling_team`, `city`)
  - Numerical features passed directly
- **Evaluation Metrics:**
  - Accuracy: ~80%
  - Precision: ~78%
  - Recall: ~81%
  - ROC-AUC: 0.86

---

## 🏗️ 8. Model Architecture

- **Preprocessing:** ColumnTransformer for encoding categorical variables and passing through numerical ones.
- **Classifier:** Logistic Regression (can be swapped for Random Forest or other models).
- **Pipeline Serialization:** Model pipeline is serialized using `pickle` for deployment.

---

## 🛠️ 9. Libraries and Tools Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning modeling and pipeline creation
- **Streamlit**: Web application framework for deployment
- **Matplotlib/Seaborn**: Data visualization
- **Pickle**: Model serialization

---

## 🌐 10. Model Deployment

- **Framework:** Streamlit
- **User Inputs:** Batting team, bowling team, city, target, current score, wickets fallen, overs completed
- **Feature Calculation:** Computes runs left, balls left, wickets left, CRR, RRR
- **Prediction:** Uses the trained pipeline to predict win probability
- **Output:** Displays win chances for both teams in a user-friendly format

---

## 🧾 11. Sample Output

**Input:**
- Batting Team: Chennai Super Kings
- Bowling Team: Mumbai Indians
- City: Mumbai
- Target: 180
- Score: 100
- Overs: 12.0
- Wickets: 4

**Output:**  
- CSK Win Probability: `62.3%`  
- MI Win Probability: `37.7%`

---

## 🧩 12. Challenges Faced

- Handling class imbalance in the dataset.
- Ensuring consistent encoding of categorical variables between training and inference.
- Dealing with missing or inconsistent data (e.g., city names).
- Deployment issues related to package versions and dependencies.

---

## 🔮 13. Future Scope

- Integrate live data feeds via APIs (e.g., Cricbuzz, ESPNcricinfo).
- Experiment with advanced models (Random Forest, XGBoost, Deep Learning).
- Incorporate player, pitch, and weather data for richer predictions.
- Deploy as a REST API using Flask or FastAPI.
- Add visualizations for match progression and win probability over time.

---

## 📚 14. References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Kaggle IPL Datasets](https://www.kaggle.com/datasets)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Sports Analytics Research Papers](https://www.journals.elsevier.com/international-journal-of-sports-science-and-coaching)

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ipl-win-predictor.git
   cd ipl-win-predictor
