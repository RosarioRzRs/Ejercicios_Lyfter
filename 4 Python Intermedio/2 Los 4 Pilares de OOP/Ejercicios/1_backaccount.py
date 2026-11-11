#clase base
class BankAccount:
    balance = 0

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self):
        pass

#clase hija
class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance

    #se crea metodo para generar un error si con el retiro, balance queda por debajo de min_balance
    def withdraw_money(self,amount):
        try:
            if self.balance - amount < self.min_balance:
                raise ValueError("Retiro no permitido, balance quedaria debajo de min_balance")
            self.balance -= amount
        except ValueError as ex:
            print(ex)
            

#se inicializa valores de min_balace,  deposito y retiro
min_balance = 2000
deposit_val = 5000
withdraw_val = 3000
#se crea objeto
count_a = SavingsAccount(min_balance)
#se deposita
count_a.deposit_money(deposit_val)
#se  retira
count_a.withdraw_money(withdraw_val)
print(f"balance = {count_a.balance}")