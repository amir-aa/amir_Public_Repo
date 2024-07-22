from flask import Flask, request, jsonify
from models import db,Order,Payment
import requests
app= Flask(__name__)

@app.route('/create_order',methods=['POST'])
def createorder():
    with db.atomic():
        order=Order.create(status='pending')
        resp=requests.post('http://127.0.0.1:5001/createpayment',json={'order_id':order.id})
        if resp.status_code==200:
            order.status='Completed'
            order.save()
            return jsonify({'message':'Payment was successful','order_id':order.id})
        else:
            order.status='failed'
            order.save()
            return jsonify({"message":f"Orderid {order.id} is failed","order_id":order.id})

app.run(port=5000)
