from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.database import Base


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(20), nullable=False)
    debit_card_last_four = Column(String(4), nullable=False)
    verification_code = Column(String(6), nullable=True)
    verified = Column(Boolean, default=False, nullable=False)
    user = relationship("User", back_populates="bank_accounts")
