accounts=dict()
class BankAccount:
    def __init__(self, owner, id2, balance=0):
        self.owner = owner
        self.id2 = id2
        self.balance = balance
    def is_valid_amount(self,amount):
        if not isinstance(amount(int,float)):
            print('lotfan meqdar addi vared konid')
            return False
        if amount <= 0:
            print('meqdar bayad bozorg tar az 0 bashad')
            return False
        return True
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}  in meqdar  {self.owner}  ezafe shod")
        else:
            print("The deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount}  in meqdar   {self.owner}   bardasht shod ")
            else:
                print("mojod kafi nist")
        else:
            print("The deposit amount must be positive")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"{amount} in meqdar {target_account.owner} montaqel shod")
        else:
            print("mojodi kafi nist")

    def show_balance(self):
        print(f"mojodi{self.owner}: {self.balance}")
def exists_account(acc_id)->bool:
    if acc_id not in accounts.keys():
        return False
    return True
def new_account_prompt():
    owner=input("name of owner: ")
    initial_amount=input("initial amount: ")
    _id=input("Account ID: ")
    return owner,_id,int(initial_amount)

def transfer_prompt()->tuple:
    _from=input("source account number? ")
    _to=input("target account id ? ")
    if not exists_account(_from) or not exists_account(_to):
        print("Unknown account")
        return None
    return accounts[_from],accounts[_to]
    
def app_loop():
    while 1:
        prompt=input("choose your request? \n 1.withdraw 2.deposit 3.transfer 4.open Account \n")
        prompt=int(prompt)
        if prompt==4:
            acc_instance=BankAccount(*new_account_prompt())
            accounts[acc_instance.id2]=acc_instance
            #print(accounts[0].id2)
        if prompt==3:
            acc=transfer_prompt() # source & dest
            if acc:
                amount=int(input("enter amount to transfer $? "))
                acc[0].transfer(acc[1],amount)
            

            
app_loop()
