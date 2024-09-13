import models
from hashlib import sha1
loggedin_users={}
def securepass(pswd:str):
    return sha1(pswd.encode()).hexdigest()
def is_authorized(username:str,walletid:int):
    w=models.Wallet.get_by_id(walletid)
    if str(w.owner)==str(username):
        return True
    return False
def prompt_menu():
    print("""[*] Please choose action? \n
           [*] 1 to open a new wallet\n
           [*] 2 to make a new user\n
           [*] 3 to make new transaction\n
          [*] 4 to logout\n
          [*] exit to close the app""")
    user_choice=input("your choice")
    return user_choice
def login_user():
    username=input("please enter your username:\t")
    passw=input("please enter password:\t")
    userdata=models.User.get_or_none(models.User.username==username)
    if userdata is None:
        return "Wrong credential"
    if userdata.password==securepass(passw):
        loggedin_users[username]=userdata
        print(f"successfully logged in as {username}")
        return userdata
    else:
        print("wrong password. App will be closed")
        exit()
def register():
    try:
        username=input("username? ")
        password=input("password? ")
        email=input("email ?")
        models.User.insert(username=username,password=securepass(password),email=email).execute()
        print("Registered successfully")
    except:
        print("an error occured while registering please try another username/email")
def logout(username:str):
    del loggedin_users[username]
    
def transaction(currentuser):
    _type=input("what are you going to do ? [deposit,withdraw,transfer]").lower()
    walletid=int(input("please give me wallet id?"))
    if not is_authorized(currentuser,walletid):
        print("App is going to exit! you are not Authorized")
        exit()
    wallet=models.Wallet.get_by_id(walletid)
    amount=int(input("please Enter amount? \t"))
    desc=input("Enter Transaction Description please? \t ")
    if _type=="deposit":
        models.Transaction.new_transaction(walletid,False,amount,desc)
        wallet.increase_wallet_amount(amount)
        print(f"increased! new balance is {wallet.amount}")
    if _type=="withdraw":
        models.Transaction.new_transaction(walletid,False,amount,desc)
        wallet.decrease_wallet(amount)
        print(f"decreased! new balance is {wallet.amount}")
    if _type=="transfer":
        pass
    
def newWallet(currentuser):
    models.Wallet.new_wallet(currentuser)

def app_loop():
    userdata=login_user()
    while True:
        
        choice=prompt_menu()
        if choice=="1":
            newWallet(userdata.username)
        if choice=="2":
            register()
        if choice=="3":
            transaction(userdata.username)

app_loop()
