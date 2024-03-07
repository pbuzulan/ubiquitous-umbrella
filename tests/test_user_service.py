import unittest
from app.dao.user_dao import UserDAO
from app.database.database import Base, engine, Session
from app.models.account import Account
from app.models.user import User
from app.services.user_service import UserService
from app.models.bank_account import BankAccount


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create the database tables
        Base.metadata.create_all(engine)

    @classmethod
    def tearDownClass(cls):
        # Drop the database tables
        Base.metadata.drop_all(engine)

    def setUp(self):
        # Create a new session for each test
        self.session = Session()

    def tearDown(self):
        # Rollback and close the session after each test
        self.session.rollback()
        self.session.close()

    def test_sign_in(self):
        user = UserDAO.create_user(phone_number='123456789055', password='password')
        result = UserService.sign_in('testuser', '12')
        self.assertEqual(result[0]['message'], 'Sign in successful')

    def test_register_user(self):
        result = UserService.register_user('123456789000', 'password')
        self.assertEqual(result['message'], 'User registered successfully')

    def test_send_onboarding_notification(self):
        user = UserDAO.create_user(phone_number='1234567891', password='password')
        result = UserService.send_onboarding_notification(user.id)
        self.assertEqual(result['message'], 'Notification sent successfully')

    def test_accept_terms(self):
        user = UserDAO.create_user(phone_number='1234567892', password='password')
        result = UserService.accept_terms(user.id)
        self.assertEqual(result['message'], 'Terms and conditions accepted')

    def test_link_bank_account(self):
        user = UserDAO.create_user(phone_number='1234567893', password='password')
        result = UserService.link_bank_account(user.id, '123456789', '1234')
        self.assertEqual(result['message'], 'Bank account linked successfully')

    def test_set_verification_code(self):
        user = UserDAO.create_user(phone_number='1234567894', password='password')
        bank_account = UserDAO.add_bank_account(user.id, '123456789', '1234')
        result = UserService.set_verification_code(bank_account.id, '123456')
        self.assertEqual(result['message'], 'Verification code set')

    def test_verify_bank_account(self):
        user = UserDAO.create_user(phone_number='1234567895', password='password')
        bank_account = UserDAO.add_bank_account(user.id, '123456789', '1234')
        UserDAO.set_verification_code(bank_account.id, '123456')
        result = UserService.verify_bank_account(bank_account.id, '123456')
        self.assertEqual(result['message'], 'Bank account verified')

    def test_authenticate_with_civil_id(self):
        user = UserDAO.create_user(phone_number='1234567896', password='password')
        result = UserService.authenticate_with_civil_id(user.id, '12')
        self.assertEqual(result['message'], 'Authentication successful')

    def test_initiate_kyc_verification(self):
        user = UserDAO.create_user(phone_number='1234567897', password='password')
        result = UserService.initiate_kyc_verification(user.id)
        self.assertEqual(result['message'], 'KYC verification initiated')

    def test_complete_profile(self):
        user = UserDAO.create_user(phone_number='1234567898', password='password')
        result = UserService.complete_profile(user.id, 'New Name', 'New Address', '1234567890')
        self.assertEqual(result['message'], 'Profile updated successfully')

    def test_retrieve_account(self):
        user = UserDAO.create_user(phone_number='1234567899', password='password')
        result = UserService.retrieve_account('1234567899')
        self.assertEqual(result['message'], 'Account retrieved')

    def test_get_total_account_balance(self):
        user = UserDAO.create_user(phone_number='1234567800', password='password')
        account1 = Account(user_id=user.id, balance=100.0)
        account2 = Account(user_id=user.id, balance=200.0)
        self.session.add_all([account1, account2])
        self.session.commit()
        result = UserService.get_total_account_balance(user.id)
        self.assertEqual(result['total_balance'], 300.0)


if __name__ == '__main__':
    unittest.main()
