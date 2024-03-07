from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=True)
    civil_id = Column(String(12), nullable=True)
    phone_number = Column(String(15), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    terms_accepted = Column(Boolean, default=False, nullable=False)
    bank_accounts = relationship("BankAccount", back_populates="user")
    kyc_verification = relationship("KYCVerification", back_populates="user", uselist=False)
    accounts = relationship("Account", back_populates="user")
    name = Column(String(100), nullable=True)
    address = Column(String(255), nullable=True)
