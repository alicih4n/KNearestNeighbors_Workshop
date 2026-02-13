import pandas as pd
import time
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Passenger

# Database connection
DB_FILE = "titanic.db"
engine = create_engine(f"sqlite:///{DB_FILE}")
Session = sessionmaker(bind=engine)
session = Session()

CSV_FILE = "data/Titanic-Dataset.csv"

def stream_data():
    print("Starting data stream...")
    
    # Load the dataset
    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        return

    total_rows = len(df)
    print(f"Loaded {total_rows} records from CSV.")

    for index, row in df.iterrows():
        # Check if record already exists to avoid duplicates if re-run
        passenger_id = int(row['PassengerId'])
        existing_passenger = session.query(Passenger).filter_by(PassengerId=passenger_id).first()
        
        if existing_passenger:
            # Skip if already in DB
            continue

        # Create Passenger object
        # Using .get for safe access and handling NaN for Age/Cabin/Embarked if necessary
        # SQLite handles simple types well, but pandas NaNs are floats. 
        # SQLAlchemy might need None for NULL.
        
        age = row['Age'] if pd.notna(row['Age']) else None
        cabin = row['Cabin'] if pd.notna(row['Cabin']) else None
        embarked = row['Embarked'] if pd.notna(row['Embarked']) else None

        new_passenger = Passenger(
            PassengerId=passenger_id,
            Survived=int(row['Survived']),
            Pclass=int(row['Pclass']),
            Name=row['Name'],
            Sex=row['Sex'],
            Age=age,
            SibSp=int(row['SibSp']),
            Parch=int(row['Parch']),
            Ticket=row['Ticket'],
            Fare=float(row['Fare']),
            Cabin=cabin,
            Embarked=embarked
        )

        session.add(new_passenger)
        session.commit()

        print(f"[{index+1}/{total_rows}] Streamed Passenger {passenger_id}: {row['Name']}")
        
        # 2-second delay as per requirement
        time.sleep(2)

if __name__ == "__main__":
    try:
        stream_data()
    except KeyboardInterrupt:
        print("\nStreaming stopped by user.")
