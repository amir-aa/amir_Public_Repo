from peewee import *
db=SqliteDatabase('order.db')
class BaseModel(Model):
    class Meta:
        database=db

class Order(BaseModel):
    id=IntegerField(primary_key=True)
    status=CharField()

class Payment(BaseModel):
    id=IntegerField(primary_key=True)
    order=ForeignKeyField(Order)
    status=CharField()

db.connect()
db.create_tables([Order,Payment],safe=True)
