#clase base
class BankAccount:
    balance = 0

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount

#clase hija
class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance

    #se crea metodo para generar un error si con el retiro, balance queda por debajo de min_balance
    def generate_error_by_min_balance(self,amount):
        try:
            if self.balance - amount < self.min_balance:
                raise ValueError()
            return True
        except ValueError as ex:
            print("Retiro no permitido, balance quedaria debajo de min_balance")
            return False

#se inicializa valores de min_balace,  deposito y retiro
min_balance = 2000
deposit_money = 5000
withdraw_money = 3001
#se crea objeto
count_a = SavingsAccount(min_balance)
#se deposita
count_a.deposit_money(deposit_money)
#se hace el retiro pero se corrobora que balnce no quede debajo de min_balance
if count_a.generate_error_by_min_balance(withdraw_money):
    count_a.withdraw_money(withdraw_money)
print(f"balance = {count_a.balance}")