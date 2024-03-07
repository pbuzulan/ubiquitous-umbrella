from flask import Blueprint, request, jsonify

from app.services.payment_service import PaymentService
from app.services.user_service import UserService

bp = Blueprint('app', __name__, url_prefix='/v1')


@bp.route('/auth/login', methods=['POST'])
def sign_in():
    data = request.json
    username = data.get('username')
    civil_id_last_two = data.get('civil_id_last_two')
    result = UserService.sign_in(username, civil_id_last_two)
    return jsonify(result)


@bp.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    phone_number = data.get('phone_number')
    password = data.get('password')
    result = UserService.register_user(phone_number, password)
    return jsonify(result)


@bp.route('/notifications/onboarding/<int:user_id>', methods=['POST'])
def send_onboarding_notification(user_id):
    result = UserService.send_onboarding_notification(user_id)
    return jsonify(result)


@bp.route('/users/accept-terms/<int:user_id>', methods=['POST'])
def accept_terms(user_id):
    result = UserService.accept_terms(user_id)
    return jsonify(result)


@bp.route('/ba/link/<int:user_id>', methods=['POST'])
def link_bank_account(user_id):
    data = request.json
    account_number = data.get('account_number')
    debit_card_last_four = data.get('debit_card_last_four')
    result = UserService.link_bank_account(user_id, account_number, debit_card_last_four)
    return jsonify(result)


@bp.route('/ba/set-verification-code/<int:bank_account_id>', methods=['POST'])
def set_verification_code(bank_account_id):
    data = request.json
    code = data.get('code')
    result = UserService.set_verification_code(bank_account_id, code)
    return jsonify(result)


@bp.route('/ba/verify/<int:bank_account_id>', methods=['POST'])
def verify_bank_account(bank_account_id):
    data = request.json
    code = data.get('code')
    result = UserService.verify_bank_account(bank_account_id, code)
    return jsonify(result)


@bp.route('/auth/authenticate-with-civil-id/<int:user_id>', methods=['POST'])
def authenticate_with_civil_id(user_id):
    data = request.json
    civil_id_last_two = data.get('civil_id_last_two')
    result = UserService.authenticate_with_civil_id(user_id, civil_id_last_two)
    return jsonify(result)


@bp.route('/kyc/initiate-verification/<int:user_id>', methods=['POST'])
def initiate_kyc_verification(user_id):
    result = UserService.initiate_kyc_verification(user_id)
    return jsonify(result)


@bp.route('/complete-profile/<int:user_id>', methods=['POST'])
def complete_profile(user_id):
    data = request.json
    name = data.get('name')
    address = data.get('address')
    phone_number = data.get('phone_number')
    result = UserService.complete_profile(user_id, name, address, phone_number)
    return jsonify(result)


@bp.route('/retrieve-account', methods=['POST'])
def retrieve_account():
    data = request.json
    phone_number = data.get('phone_number')
    result = UserService.retrieve_account(phone_number)
    return jsonify(result)


@bp.route('/dashboard/total-balance/<int:user_id>', methods=['GET'])
def total_balance(user_id):
    result = UserService.get_total_account_balance(user_id)
    return jsonify(result)


@bp.route('/dashboard/send-money', methods=['POST'])
def send_money():
    data = request.json
    user_id = data.get('user_id')
    recipient_id = data.get('recipient_id')
    amount = data.get('amount')
    result = PaymentService.send_money(user_id, recipient_id, amount)
    return jsonify(result)


@bp.route('/dashboard/request-money', methods=['POST'])
def request_money():
    data = request.json
    user_id = data.get('user_id')
    requester_id = data.get('requester_id')
    amount = data.get('amount')
    result = PaymentService.request_money(user_id, requester_id, amount)
    return jsonify(result)


@bp.route('/dashboard/pay-bill', methods=['POST'])
def pay_bill():
    data = request.json
    user_id = data.get('user_id')
    bill_id = data.get('bill_id')
    amount = data.get('amount')
    result = PaymentService.pay_bill(user_id, bill_id, amount)
    return jsonify(result)
