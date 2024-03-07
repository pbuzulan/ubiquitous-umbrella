from sqlalchemy import func
from app.models.account import Account
from app.models.bank_account import BankAccount
from app.models.user import User
from app.database.database import Session


class UserDAO:
    """
    Data Access Object (DAO) class for interacting with User, BankAccount, and Account models.
    Provides methods to perform CRUD operations and other actions on these models.
    """

    @staticmethod
    def find_user_by_username_and_civil_id(username, civil_id_last_two):
        """
        Finds a user by their username and the last two digits of their civil ID.

        :param username: The username of the user.
        :param civil_id_last_two: The last two digits of the user's civil ID.
        :return: The User object if found, None otherwise.
        """
        session = Session()
        user = session.query(User).filter(
            User.username == username,
            User.civil_id.endswith(civil_id_last_two)
        ).first()
        session.close()
        return user

    @staticmethod
    def create_user(phone_number, password):
        """
        Creates a new user with the given phone number and password.

        :param phone_number: The phone number of the new user.
        :param password: The password of the new user.
        :return: The newly created User object.
        """
        session = Session()
        user = User(phone_number=phone_number, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user

    @staticmethod
    def find_user_by_id(user_id):
        """
        Finds a user by their ID.

        :param user_id: The ID of the user.
        :return: The User object if found, None otherwise.
        """
        session = Session()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    @staticmethod
    def update_terms_accepted(user_id, accepted):
        """
        Updates the terms acceptance status for a user.

        :param user_id: The ID of the user.
        :param accepted: The new terms acceptance status (True or False).
        :return: The updated User object.
        """
        session = Session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.terms_accepted = accepted
            session.commit()
        session.close()
        return user

    @staticmethod
    def add_bank_account(user_id, account_number, debit_card_last_four):
        """
        Adds a bank account to a user with the given account number and last four digits of the debit card.

        :param user_id: The ID of the user.
        :param account_number: The account number of the bank account.
        :param debit_card_last_four: The last four digits of the debit card associated with the bank account.
        :return: The newly created BankAccount object, None if the user is not found.
        """
        session = Session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            bank_account = BankAccount(
                user_id=user_id,
                account_number=account_number,
                debit_card_last_four=debit_card_last_four
            )
            session.add(bank_account)
            session.commit()
            session.refresh(bank_account)
            return bank_account
        session.close()
        return None

    @staticmethod
    def set_verification_code(bank_account_id, code):
        """
        Sets a verification code for a bank account.

        :param bank_account_id: The ID of the bank account.
        :param code: The verification code to set.
        :return: The updated BankAccount object.
        """
        session = Session()
        bank_account = session.query(BankAccount).filter(BankAccount.id == bank_account_id).first()
        if bank_account:
            bank_account.verification_code = code
            session.commit()
        session.close()
        return bank_account

    @staticmethod
    def verify_bank_account(bank_account_id, code):
        """
        Verifies a bank account with the given verification code.

        :param bank_account_id: The ID of the bank account.
        :param code: The verification code to verify.
        :return: The updated BankAccount object if verification is successful, None otherwise.
        """
        session = Session()
        bank_account = session.query(BankAccount).filter(
            BankAccount.id == bank_account_id,
            BankAccount.verification_code == code
        ).first()
        if bank_account:
            bank_account.verified = True
            session.commit()
        session.close()
        return bank_account

    @staticmethod
    def update_user_profile(user_id, name, address, phone_number):
        """
        Updates the profile information for a user.

        :param user_id: The ID of the user.
        :param name: The new name of the user.
        :param address: The new address of the user.
        :param phone_number: The new phone number of the user.
        :return: The updated User object.
        """
        session = Session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            user.address = address
            user.phone_number = phone_number
            session.commit()
        session.close()
        return user

    @staticmethod
    def find_user_by_phone(phone_number):
        """
        Finds a user by their phone number.

        :param phone_number: The phone number of the user.
        :return: The User object if found, None otherwise.
        """
        session = Session()
        user = session.query(User).filter(User.phone_number == phone_number).first()
        session.close()
        return user

    @staticmethod
    def get_total_balance(user_id):
        """
        Gets the total balance of all accounts for a user.

        :param user_id: The ID of the user.
        :return: The total balance as a float.
        """
        session = Session()
        total_balance = session.query(Account).filter(Account.user_id == user_id).with_entities(
            func.sum(Account.balance)).scalar()
        session.close()
        return total_balance if total_balance else 0.0
