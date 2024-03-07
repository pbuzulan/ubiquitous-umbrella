from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure your database URI here
DATABASE_URI = 'sqlite:///:memory:'

Base = declarative_base()

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

from app.models.user import User
from app.models.bank_account import BankAccount
from app.models.kyc_verification import KYCVerification

Base.metadata.create_all(engine)
