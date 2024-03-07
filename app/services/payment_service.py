class PaymentService:
    @staticmethod
    def send_money(user_id, recipient_id, amount):
        # Logic to send money from user to recipient
        return {'message': 'Money sent successfully'}

    @staticmethod
    def request_money(user_id, requester_id, amount):
        # Logic to request money from another user
        return {'message': 'Money request sent successfully'}

    @staticmethod
    def pay_bill(user_id, bill_id, amount):
        # Logic to pay a bill
        return {'message': 'Bill paid successfully'}
