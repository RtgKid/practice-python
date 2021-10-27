class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Crete a new credit card instance"""

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return ("Customer : " + self._customer +
                "\nBank : " + self._bank +
                "\nAccount : " + self._account +
                "\nLimit : " + str(self._limit) +
                "\nBalance : " + str(self._balance))


cc = CreditCard('John Doe', '1st Bank', '5381 9000 0000 3412', 1000)
print(cc)