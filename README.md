# 🧑‍💻 K-Nearest Neighbors (KNN) Workshop Solution

**Student Name:** Ali Cihan Ozdemir
**Student ID:** [Insert ID Here]

## 📘 Summary of Work
This project implements a complete Machine Learning Pipeline for the Titanic dataset, meeting the workshop requirements for a "Remote Database", "Data Streaming", and "Dynamic Dashboard".

### Key Components:
1.  **Remote Database Integration**:
    - Implemented using a persistent SQLite database (`titanic.db`) managed via SQLAlchemy (`db_setup.py`).
    - Stores historical passenger data and supports concurrent reading/writing.

2.  **Data Collection & Streaming**:
    - `stream_titanic.py` reads the raw Titanic CSV and streams records into the database one by one with a 2-second delay, simulating a real-time data feed.

3.  **Dynamic Dashboard**:
    - The `KNN_Workshop_Solution.ipynb` notebook implements the ML pipeline (Acquisition -> Preprocessing -> Training -> Evaluation).
    - It features a real-time dashboard loop that polls the database, updates visualizations (Survival Counts, Fare Distribution), and retrains/evaluates the KNN model as new data arrives.

## 🚀 How to Run
1.  **Initialize Database**:
    ```bash
    python3 db_setup.py
    ```
2.  **Start Data Stream**:
    ```bash
    python3 stream_titanic.py
    ```
3.  **Running the Dashboard**:
    - Open `KNN_Workshop_Solution.ipynb` in multiple Jupyter environment or VS Code.
    - Run all cells.
    - Watch the dashboard update automatically!

## 🤖 Requirements
See `requirements.txt` for dependencies.
