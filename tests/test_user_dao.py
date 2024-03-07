import unittest

from app.database.database import Base, engine, Session
from app.models.user import User
from app.dao.user_dao import UserDAO
from app.models.bank_account import BankAccount
from app.models.account import Account


class TestUserDAO(unittest.TestCase):

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

    def test_find_user_by_username_and_civil_id(self):
        self.user = User(username='testuser2', civil_id='12', phone_number='12345678911230', password='password')
        self.session.add(self.user)
        self.session.commit()
        found_user = UserDAO.find_user_by_username_and_civil_id('testuser2', '12')
        self.assertEqual(found_user.id, self.user.id)

    def test_create_user(self):
        user = UserDAO.create_user(phone_number='1234567891', password='password')
        self.assertIsInstance(user, User)

    def test_find_user_by_id(self):
        user = UserDAO.create_user(phone_number='123456789112', password='password')
        found_user = UserDAO.find_user_by_id(1)
        self.assertEqual(found_user.id, 1)

    def test_update_terms_accepted(self):
        user = UserDAO.create_user(phone_number='1234567898', password='password')
        updated_user = UserDAO.update_terms_accepted(user.id, True)
        self.assertTrue(updated_user.terms_accepted)

    def test_add_bank_account(self):
        user = UserDAO.create_user(phone_number='1234567899', password='password')
        bank_account = UserDAO.add_bank_account(user.id, '123456789', '1234')
        self.assertIsInstance(bank_account, BankAccount)

    def test_set_verification_code(self):
        user = UserDAO.create_user(phone_number='12345678412', password='password')
        bank_account = UserDAO.add_bank_account(user.id, '123456789', '1234')
        updated_account = UserDAO.set_verification_code(bank_account.id, '123456')
        self.assertEqual(updated_account.verification_code, '123456')

    def test_verify_bank_account(self):
        user = UserDAO.create_user(phone_number='12345678412', password='password')
        bank_account = UserDAO.add_bank_account(user.id, '123456789', '1234')
        UserDAO.set_verification_code(bank_account.id, '123456')
        verified_account = UserDAO.verify_bank_account(bank_account.id, '123456')
        self.assertTrue(verified_account.verified)

    def test_update_user_profile(self):
        user = UserDAO.create_user(phone_number='1234567891555', password='password')
        updated_user = UserDAO.update_user_profile(user.id, 'New Name', 'New Address', '12345678905')
        self.assertEqual(updated_user.name, 'New Name')
        self.assertEqual(updated_user.address, 'New Address')
        self.assertEqual(updated_user.phone_number, '12345678905')

    def test_find_user_by_phone(self):
        user = UserDAO.create_user(phone_number='1234567893', password='password')
        found_user = UserDAO.find_user_by_phone('1234567893')
        self.assertEqual(found_user.id, user.id)

    def test_get_total_balance(self):
        user = UserDAO.create_user(phone_number='1234567894', password='password')
        account1 = Account(user_id=user.id, balance=100.0)
        account2 = Account(user_id=user.id, balance=200.0)
        self.session.add_all([account1, account2])
        self.session.commit()
        total_balance = UserDAO.get_total_balance(user.id)
        self.assertEqual(total_balance, 300.0)


if __name__ == '__main__':
    unittest.main()
