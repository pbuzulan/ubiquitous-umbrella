import unittest
from app.dao.user_dao import UserDAO
from app.models.user import User
from app.models.bank_account import BankAccount
from app.models.account import Account
from app.database.database import Session


class TestUserDAO(unittest.TestCase):

    def test_find_user_by_username_and_civil_id(self):
        # Assuming you have a user with these credentials in your test database
        user = UserDAO.find_user_by_username_and_civil_id('testuser', '12')
        self.assertIsInstance(user, User)

    def test_create_user(self):
        user = UserDAO.create_user('1234567890', 'password')
        self.assertIsInstance(user, User)
        # Clean up
        session = Session()
        session.delete(user)
        session.commit()

    def test_find_user_by_id(self):
        # Assuming you have a user with ID 1 in your test database
        user = UserDAO.find_user_by_id(1)
        self.assertIsInstance(user, User)

    def test_update_terms_accepted(self):
        # Assuming you have a user with ID 1 in your test database
        user = UserDAO.update_terms_accepted(1, True)
        self.assertTrue(user.terms_accepted)
        # Reset for future tests
        UserDAO.update_terms_accepted(1, False)

    def test_add_bank_account(self):
        # Assuming you have a user with ID 1 in your test database
        bank_account = UserDAO.add_bank_account(1, '123456789', '1234')
        self.assertIsInstance(bank_account, BankAccount)
        # Clean up
        session = Session()
        session.delete(bank_account)
        session.commit()

    def test_set_verification_code(self):
        # Assuming you have a bank account with ID 1 in your test database
        bank_account = UserDAO.set_verification_code(1, '123456')
        self.assertEqual(bank_account.verification_code, '123456')
        # Reset for future tests
        UserDAO.set_verification_code(1, None)

    def test_verify_bank_account(self):
        # Assuming you have a bank account with ID 1 and verification code '123456' in your test database
        bank_account = UserDAO.verify_bank_account(1, '123456')
        self.assertTrue(bank_account.verified)
        # Reset for future tests
        UserDAO.set_verification_code(1, None)
        UserDAO.verify_bank_account(1, None)

    def test_update_user_profile(self):
        # Assuming you have a user with ID 1 in your test database
        user = UserDAO.update_user_profile(1, 'New Name', 'New Address', '1234567890')
        self.assertEqual(user.name, 'New Name')
        self.assertEqual(user.address, 'New Address')
        self.assertEqual(user.phone_number, '1234567890')
        # Reset for future tests
        UserDAO.update_user_profile(1, None, None, None)

    def test_find_user_by_phone(self):
        # Assuming you have a user with phone number '1234567890' in your test database
        user = UserDAO.find_user_by_phone('1234567890')
        self.assertIsInstance(user, User)

    def test_get_total_balance(self):
        # Assuming you have accounts for user ID 1 with balances in your test database
        total_balance = UserDAO.get_total_balance(1)
        self.assertIsInstance(total_balance, float)


if __name__ == '__main__':
    unittest.main()
