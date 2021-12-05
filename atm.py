class Atm(object):
    def __init__(self, atm_card_num, pin_num):
        self.atm_card_num = atm_card_num
        self.pin_num = pin_num

    def cash_withdrawl(self):
        print("Cash taken out of your account!")
    
    def balance_enquiry(self):
        print("The balance on you account is very low!")
    
    def add_cash(self):
        print("Cash added")

aravs_account = Atm(1234, 6789)
print(aravs_account.add_cash())