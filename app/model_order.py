# Order Component
from app import mongo

class Order:

    @staticmethod
    def view_order():
        order_list =[]
        
        try:
            order_data = list(mongo.db.order_data.find({}))
            for order in order_data:
            
                order_dict = {
                "id": order ["id"],
                "orderdate": order["orderdate"],
                "webinardate": order["webinardate"],
                "topic": order["topic"],
                "session": order["session"], # Array
                "customername": order["customerName"],
                "customeremail": order["customerEmail"],
                "billingemail": order["billingEmail"],
                "orderamount": order["orderamount"],
                "paymentstatus": order["paymentstatus"],
                "country" : order["country"],
                "state" : order["state"],
                "city" : order["city"],
                "zipcode" : order["zipcode"],
                "address": order["address"],
                "document": order["document"],
                "website" : order["website"]

            }

            order_list.append(order_dict)
            
        
        except Exception as e:
            order_list = []
        
        return order_list
        

    @staticmethod
    def order_data(o_id):
        order_dict={}
        try:
            order = list(mongo.db.order_data.find({"id": o_id}))
            order_dict = {
                "id": order ["id"],
                "orderdate": order["orderdate"],
                "webinardate": order["webinardate"],
                "topic": order["topic"],
                "session": order["session"], # Array
                "customername": order["customerName"],
                "customeremail": order["customerEmail"],
                "billingemail": order["billingEmail"],
                "orderamount": order["orderamount"],
                "paymentstatus": order["paymentstatus"],
                "country" : order["country"],
                "state" : order["state"],
                "city" : order["city"],
                "zipcode" : order["zipcode"],
                "address": order["address"],
                "document": order["document"],
                "website" : order["website"]

            }

        except Exception as e:
            order_dict = {}
            
        return order_dict
        
