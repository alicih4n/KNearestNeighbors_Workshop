# 🧑‍💻 K-Nearest Neighbors (KNN) Workshop Solution

## 👨‍🎓 Student Information
**Name:** Ali Cihan Ozdemir  
**Student ID:** 9091405

**Name:** Danda, Lohith Reddy  
**Student ID:** 9054470   

## 📘 Summary of Work
This project implements a complete **Machine Learning Pipeline** for the Titanic dataset, meeting all workshop requirements:
1.  **Remote Database Pattern**: Uses a persistent SQLite database (`titanic.db`) to simulate a remote relational database service. The architecture allows for easy swapping to PostgreSQL/MySQL.
2.  **Data Streaming**: Simulates a live data feed by reading the Titanic CSV one record at a time and pushing it to the database with a 2-second delay.
3.  **Dynamic Dashboard**: A real-time Jupyter Notebook dashboard that connects to the streaming database, visualizes incoming data, and updates KNN model predictions live.

---

## 📂 Project Structure
- **`KNN_Workshop_Solution.ipynb`**: The main solution notebook containing the Dynamic Dashboard and ML Pipeline.
- **`stream_titanic.py`**: Python script to stream data into the database.
- **`db_setup.py`**: Python script to initialize the database schema.
- **`requirements.txt`**: List of Python dependencies.
- **`titanic.db`**: The SQLite database file (created after running `db_setup.py`).

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or VS Code with Python extension

### 2. Install Dependencies
Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Project

Follow these steps in order to see the full pipeline in action.

### Step 1: Initialize the Database
This creates the empty `titanic.db` file with the correct schema.

```bash
python3 db_setup.py
```
*Output: `Database setup complete.`*

### Step 2: Start the Data Stream
This script mimics an external data source feeding into your database. Keep this terminal window **OPEN** while running the dashboard.

```bash
python3 stream_titanic.py
```
*Output:*
```text
Starting data stream...
Loaded 891 records from CSV.
[1/891] Streamed Passenger 1: Braund, Mr. Owen Harris
[2/891] Streamed Passenger 2: Cumings, Mrs. John Bradley (Florence Briggs Thayer)
...
```

### Step 3: Launch the Dashboard
1.  Open **`KNN_Workshop_Solution.ipynb`** in Jupyter Notebook or VS Code.
2.  Click **"Run All"** or execute cells sequentially.
3.  Scroll down to the **"Dynamic Dashboard"** section.
4.  Watch as the graphs update automatically every 3 seconds as new data arrives from your streaming script!

---

## 🛠️ Troubleshooting

- **Database Locked Error**: If you see a "database is locked" error, it usually means the notebook and the stream are trying to write at the exact same millisecond. This is rare with SQLite but if it happens, simply restart the `stream_titanic.py` script.
- **No Data in Dashboard**: Ensure `stream_titanic.py` is running in a separate terminal window. The dashboard reads from the database file, which is populated by that script.
- **Stopping the Stream**: Press `Ctrl+C` in the terminal running `stream_titanic.py` to stop the data feed gracefully.

---

## 📦 Submission Details
- **PDF Report**: Generated from `KNN_Workshop_Solution.ipynb` after running the dashboard.
- **GitHub Repository**: Contains all source code and documentation.
