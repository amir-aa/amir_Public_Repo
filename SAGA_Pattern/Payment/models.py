from peewee import *
db=SqliteDatabase("payment.db")

class BaseModel(Model):
    class Meta:
        database=db
class Payment(BaseModel):
    id=IntegerField(primary_key=True)
    order_id=IntegerField()
    status=CharField()

db.connect()
db.create_tables([Payment],safe=True)
