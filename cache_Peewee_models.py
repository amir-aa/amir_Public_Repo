import memcache
from peewee import *
from playhouse.shortcuts import model_to_dict
cache=memcache.Client(['127.0.0.1:11211'])
db=SqliteDatabase('mydb.db')
class BaseModel(Model):
    class Meta:
        database=db
    @classmethod
    def selectcached(self,use_cache=True,*query):
        if not use_cache:
            return super().select(*query)
        cache_key=f"{self.__name__}:{str(query)}"
        cached_data=cache.get(cache_key)
        if cached_data:
            print("fetched from cache")
            return [self(**item) for item in cached_data]
        
        print("fetched from DB")
        instance=list(super().select(*query))
        cache.set(cache_key,[model_to_dict(i) for i in instance],10)
        return instance
class Order(BaseModel):
    customer_name = CharField()
    total_amount = FloatField()

class OrderItem(BaseModel):
    order = ForeignKeyField(Order, backref='items')
    product_name = CharField()
    quantity = IntegerField()
    price = FloatField()
db.create_tables([Order,OrderItem])

from flask import Flask , jsonify
app= Flask(__name__)
@app.route('/order')
def orders():
    return jsonify([i.__data__ for i in Order.selectcached()])
app.run()
