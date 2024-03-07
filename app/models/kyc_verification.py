from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base


class KYCVerification(Base):
    __tablename__ = 'kyc_verifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    verification_status = Column(String(50), nullable=False, default='pending')
    document_url = Column(String(255), nullable=True)
    biometric_data = Column(String(255), nullable=True)
    user = relationship("User", back_populates="kyc_verification")
