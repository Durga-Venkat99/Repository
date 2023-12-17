class banking:
    def __init__(self):
        self.pin = None
        self.bal = 0.0
        self.menu()
    def menu(self):
        while True:
            print("1.Set_PIN")
            print("2.DEPOSITE")
            print("3.WITHDRAW")
            print("4.BALANCE")
            print("5.EXIT")
            choice = input("select option(1/2/3/4/5): ")
            if choice == "1":
                self.Set_PIN()
            elif choice == "2":
                self.deposite()
            elif choice == "3":
                self.WITHDRAW()
            elif choice == "4":
                self.balance()
            elif choice == "5":
                print("EXITING THE PROGRAM")
            else:
                print("invalid check again")
    def Set_PIN(self):
        self.pin = input("enter PIN: ")
        print("PIN SET SUCCESSFULLY ")
    def deposite(self):
        pin_attempt = input("enter a pin: ")
        if pin_attempt == self.pin:
            amount = float(input("deposite amount: "))
            if amount > 0:
                self.bal += amount
                print(f"your balance is deposited {amount:.2f}")
            else:
                print("invalid deposite amount")
        else:
            print("invalid pin")
    def WITHDRAW(self):
        pin_attempt = input("enter a pin: ")
        if pin_attempt == self.pin:
            amount = float(input("withdraw amount: "))
            if 0 < amount <= self.bal:
                self.bal -= amount
                print(f"your withdraw {amount:.2f}")
            else:
                print("insufficient amount")
        else:
            print("invalid pin")
    def balance(self):
        pin_attempt = input("enter the pin: ")
        if pin_attempt == self.pin:
            print("your balance : ",self.bal)
        else:
            print("invalid pin")

if __name__ == "__main__":
    atm = banking()