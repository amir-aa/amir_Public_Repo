from peewee import *
import datetime
db=SqliteDatabase("wallet.db")
class BaseClass(Model):
    class Meta:
        database=db
class User(BaseClass):
    username=CharField(primary_key=True,max_length=60)
    password=CharField(max_length=50)
    registered_at=DateTimeField(default=datetime.datetime.now())
    email=CharField(max_length=150,unique=True)

class Wallet(BaseClass):
    id=AutoField()
    owner=ForeignKeyField(User)
    currency=CharField(max_length=4,default="IRR")
    amount=IntegerField(default=0)
    @classmethod
    def new_wallet(self,owner:str,currency:str="IRR"):
        return Wallet.create(owner=owner,currency=currency)
    def increase_wallet_amount(self,amount:int):
        self.amount+=amount
        self.save()
    def decrease_wallet(self,amount:int):
        self.amount-=amount
        self.save()
    
class Transaction(BaseClass):
    id=AutoField()
    wallet=ForeignKeyField(Wallet)
    created_at=DateTimeField(default=datetime.datetime.now())
    is_credit=BooleanField()
    description=CharField()
    amount=IntegerField()
    @classmethod
    def new_transaction(self,walletid:int,is_credit:bool,amount:int,description:str):
        _wallet=Wallet.get_by_id(walletid)
        if is_credit:
            _wallet.decrease_wallet(amount)
        else:
            _wallet.increase_wallet_amount(amount)
        return Transaction.create(wallet=walletid,is_credit=is_credit,amount=amount,description=description)

def init():
    from hashlib import sha1
    db.create_tables([User,Wallet,Transaction],safe=True)
    #User.insert(username="amir",password=sha1(b"021").hexdigest(),email="a@a.com").execute()
init()
