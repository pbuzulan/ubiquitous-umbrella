from app.models.kyc_verification import KYCVerification
from app.database.database import Session


class KYCVerificationDAO:
    @staticmethod
    def create_kyc_verification(user_id):
        session = Session()
        kyc_verification = KYCVerification(user_id=user_id)
        session.add(kyc_verification)
        session.commit()
        session.refresh(kyc_verification)
        session.close()
        return kyc_verification
