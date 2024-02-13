class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number =phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {recipient} successfully")
        else:
            print("insufficient amount to Send Money")
class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_no):
        super().__init__(account_balance,phone_number)
        self.id_no = id_no
    def buyairtime(self,amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully")
class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_name):
        super().__init__(account_balance,phone_number)
        self.business_name = business_name
    def recieve_payment(self,amount):
        self.account_balance += amount
        print(f"{amount}KES received from a customer")
personal=PersonalMpesa(100,714704742,2435678)
personal.send_money(300,714704742)
personal.buyairtime(150)

business=BusinessMpesa(900,714704742,"Sean")
business.send_money(5000,78653987)
business.recieve_payment(2000)