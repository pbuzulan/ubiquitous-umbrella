from app.dao.kyc_dao import KYCVerificationDAO
from app.dao.user_dao import UserDAO
from app.integrations.sms_service import send_sms_notification


class UserService:
    """
        Service class for user-related actions. Provides methods for signing in,
        registering, sending notifications, accepting terms, linking bank accounts,
        setting verification codes, verifying bank accounts, authenticating with civil ID,
        initiating KYC verification, completing user profile, retrieving accounts, and
        getting total account balance.
        """

    @staticmethod
    def sign_in(username, civil_id_last_two):
        """
        Signs in a user using their username and the last two digits of their civil ID.

        :param username: The username of the user.
        :param civil_id_last_two: The last two digits of the user's civil ID.
        :return: A success message with user ID if credentials are valid, otherwise an error message.
        """
        user = UserDAO.find_user_by_username_and_civil_id(username, civil_id_last_two)
        if user:
            return {'message': 'Sign in successful', 'user_id': user.id}
        else:
            return {'message': 'Invalid credentials'}, 401

    @staticmethod
    def register_user(phone_number, password):
        """
        Registers a new user with the given phone number and password.

        :param phone_number: The phone number of the new user.
        :param password: The password of the new user.
        :return: A success message with the new user's ID.
        """
        # Here you should add password hashing for security
        user = UserDAO.create_user(phone_number, password)
        return {'message': 'User registered successfully', 'user_id': user.id}

    @staticmethod
    def send_onboarding_notification(user_id):
        """
        Sends an onboarding notification to the user's phone number.

        :param user_id: The ID of the user to send the notification to.
        :return: A success message if the notification is sent, otherwise an error message.
        """
        user = UserDAO.find_user_by_id(user_id)
        if user:
            message = "Welcome back! Continue your onboarding process by signing in to the app."
            send_sms_notification(user.phone_number, message)
            return {'message': 'Notification sent successfully'}
        else:
            return {'message': 'User not found'}, 404

    @staticmethod
    def accept_terms(user_id):
        """
        Marks the terms and conditions as accepted for the user.

        :param user_id: The ID of the user accepting the terms.
        :return: A success message if the terms are accepted, otherwise an error message.
        """
        user = UserDAO.update_terms_accepted(user_id, True)
        if user:
            return {'message': 'Terms and conditions accepted'}
        else:
            return {'message': 'User not found'}, 404

    @staticmethod
    def link_bank_account(user_id, account_number, debit_card_last_four):
        """
        Links a bank account to the user's profile.

        :param user_id: The ID of the user.
        :param account_number: The account number of the bank account.
        :param debit_card_last_four: The last four digits of the debit card associated with the bank account.
        :return: A success message if the bank account is linked, otherwise an error message.
        """
        bank_account = UserDAO.add_bank_account(
            user_id, account_number, debit_card_last_four
        )
        if bank_account:
            return {'message': 'Bank account linked successfully'}
        else:
            return {'message': 'User not found'}, 404

    @staticmethod
    def set_verification_code(bank_account_id, code):
        """
        Sets a verification code for a bank account.

        :param bank_account_id: The ID of the bank account.
        :param code: The verification code to set.
        :return: A success message if the code is set, otherwise an error message.
        """
        bank_account = UserDAO.set_verification_code(bank_account_id, code)
        if bank_account:
            return {'message': 'Verification code set'}
        else:
            return {'message': 'Bank account not found'}, 404

    @staticmethod
    def verify_bank_account(bank_account_id, code):
        """
        Verifies a bank account with the given verification code.

        :param bank_account_id: The ID of the bank account.
        :param code: The verification code to verify the account.
        :return: A success message if the bank account is verified, otherwise an error message.
        """
        bank_account = UserDAO.verify_bank_account(bank_account_id, code)
        if bank_account:
            return {'message': 'Bank account verified'}
        else:
            return {'message': 'Invalid verification code'}, 400

    @staticmethod
    def authenticate_with_civil_id(user_id, civil_id_last_two):
        """
        Authenticates a user with their Civil ID's last two digits.

        :param user_id: The ID of the user.
        :param civil_id_last_two: The last two digits of the user's Civil ID.
        :return: A message indicating the result of the authentication.
        """
        user = UserDAO.find_user_by_id(user_id)
        if user and user.civil_id.endswith(civil_id_last_two):
            return {'message': 'Authentication successful'}
        else:
            return {'message': 'Authentication failed'}, 401

    @staticmethod
    def initiate_kyc_verification(user_id):
        """
        Initiates the KYC verification process for a user.

        :param user_id: The ID of the user.
        :return: A message indicating the result of the KYC verification initiation.
        """
        kyc_verification = KYCVerificationDAO.create_kyc_verification(user_id)
        if kyc_verification:
            return {'message': 'KYC verification initiated', 'verification_id': kyc_verification.id}
        else:
            return {'message': 'User not found'}, 404

    @staticmethod
    def complete_profile(user_id, name, address, phone_number):
        """
        Completes the profile of a user with personal details.

        :param user_id: The ID of the user.
        :param name: The name of the user.
        :param address: The address of the user.
        :param phone_number: The phone number of the user.
        :return: A message indicating the result of the profile update.
        """
        user = UserDAO.update_user_profile(user_id, name, address, phone_number)
        if user:
            return {'message': 'Profile updated successfully'}
        else:
            return {'message': 'User not found'}, 404

    @staticmethod
    def retrieve_account(phone_number):
        """
        Retrieves a user's account using their phone number.

        :param phone_number: The phone number of the user.
        :return: A message indicating the result of the account retrieval, including the username if found.
        """
        user = UserDAO.find_user_by_phone(phone_number)
        if user:
            return {'message': 'Account retrieved', 'username': user.username}
        else:
            return {'message': 'User not found'}, 404

    @staticmethod
    def get_total_account_balance(user_id):
        """
        Gets the total balance of all accounts for a user.

        :param user_id: The ID of the user.
        :return: A dictionary containing the total balance.
        """
        total_balance = UserDAO.get_total_balance(user_id)
        return {'total_balance': total_balance}
