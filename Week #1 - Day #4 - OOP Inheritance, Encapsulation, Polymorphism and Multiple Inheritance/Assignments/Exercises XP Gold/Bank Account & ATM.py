# Part I: BankAccount class

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        """Authenticate user"""
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"User {self.username} authenticated successfully.")
        else:
            self.authenticated = False
            print("Authentication failed.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated. Cannot deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated. Cannot withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

# Part II: MinimumBalanceAccount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated. Cannot withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw {amount}. Minimum balance requirement: {self.minimum_balance}")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

# Part IV: ATM class

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must be a list of BankAccount or MinimumBalanceAccount instances.")
        if try_limit <= 0:
            print("Invalid try_limit, setting to default 2")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == '2':
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                self.show_account_menu(account)
                return
        self.current_tries += 1
        print(f"Login failed. Attempt {self.current_tries}/{self.try_limit}")
        if self.current_tries >= self.try_limit:
            print("Reached maximum login attempts. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu ({account.username}) ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                amount = int(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = int(input("Enter withdrawal amount: "))
                try:
                    account.withdraw(amount)
                except Exception as e:
                    print(e)
            elif choice == '3':
                print(f"Current balance: {account.balance}")
            elif choice == '4':
                print("Logging out...")
                account.authenticated = False
                break
            else:
                print("Invalid choice. Try again.")


acc1 = BankAccount("user1", "pass1", 1000)
acc2 = MinimumBalanceAccount("user2", "pass2", 2000, minimum_balance=500)

atm = ATM([acc1, acc2], try_limit=3)
