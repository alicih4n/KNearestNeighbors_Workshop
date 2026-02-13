from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Define database file
DB_FILE = "titanic.db"
engine = create_engine(f"sqlite:///{DB_FILE}")
Base = declarative_base()

# Define the table schema corresponding to the Titanic CSV
class Passenger(Base):
    __tablename__ = 'passengers'
    
    PassengerId = Column(Integer, primary_key=True)
    Survived = Column(Integer)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Float, nullable=True) # Age can be fractional and null
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String, nullable=True)
    Embarked = Column(String, nullable=True)

    def __repr__(self):
        return f"<Passenger(name='{self.Name}', survived={self.Survived})>"

# Create the table
if __name__ == "__main__":
    print(f"Creating database {DB_FILE} with table 'passengers'...")
    Base.metadata.create_all(engine)
    print("Database setup complete.")
