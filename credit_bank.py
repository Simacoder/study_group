class CreditCard:
    """ A consumer credit card """

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance
         
         The initial balance is Zero.

         customer: the name of the customer  (e.g Simanga Mchunu)
         bank: the name of the bank (e.g  FNB bank)
         acnt: account number (eg 3267 238)
         limit: credit limit (measured in Rand) 
           """
        
        self._customer = customer
        self._bank = bank
        self._account = acnt 
        self._limit = limit 
        self.balance = 0

    def get_customer(self):
        """ Return the of the customer """
        return self._customer
    
    def get_bank(self):
        """" Return te bank's name """
        return self._bank
    
    def get_account(self):
        """ Return the account number """
        return self._account 
    
    def get_limit(self):
        """ Return current credit limit """
        return self._limit
    
    def get_balance(self):
        """ Return current balance """
        return self._balance
    
    def charge(self, price):
        """ Charge given price to the card, assuming sufiecient credit
         return true if card was processed, false if card was denied
        """
        if price + self.get_balance > self._limit: # if charge are exceeding the charge
            return False                           # cannot accept the charge
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        """ Process payment of the customerwich deduct from the her/him """
        self._balance -= amount


if __name__ == '__name__':
    wallet = []
    wallet.append(CreditCard('Simanga Mchunu', 'TymeBank', '6218362 2568', 2500))
    wallet.append(CreditCard('Sami Ahmed', 'FNB Bank', '37292 3272 223', 3500))
    wallet.append(CreditCard('Gonste Motloung', 'Standards bank', '32781 292327 22332',5000))
    wallet.append(CreditCard('Taiwo shakuro', 'Naira bank', '544 28329', 6500))


    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        wallet[3].charge(4*val)

    for c in range(4):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()

    




