from flask import Flask,request,jsonify
from models import db,Payment
app= Flask(__name__)
@app.route('/createpayment',methods=['POST'])
def createpayment():
    data=request.get_json()
    orderid=data.get('order_id')
    with db.atomic():
        payment=Payment.create(order_id=orderid,status='pending')
        # PaymentProcess

        payment.status='completed'
        payment.save()
        return jsonify({'message':'payment successfull'}),200
app.run(port=5001)
