import pyrebase
import time


config={
   "apiKey": "AIzaSyBMjuS7yAjgHWUY-VxX7y6TSYDzu6C2E3c",
  "authDomain": "sigin-a0a4b.firebaseapp.com",
  "databaseURL": "https://sigin-a0a4b-default-rtdb.firebaseio.com",
  "projectId": "sigin-a0a4b",
  "storageBucket": "sigin-a0a4b.appspot.com",
  "messagingSenderId": "139412624194",
  "appId": "1:139412624194:web:39fb80ba1b0dc4cef2aedb"
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()

auth=firebase.auth()

storage = firebase.storage()

def initialize_machine(email, password):
    try:
        machine = auth.sign_in_with_email_and_password(email, password)
        #db.child('machines').child(machine['localId']).child('state').set(1)
        return VendingMachine(machine)
    except Exception as e:

        print("Error logging in ")
        # Catch the exception and return the error message
        return None

class VendingMachine:
    def __init__(self,machine_info):
        self.machine_id=machine_info['localId']
        self.id_token=machine_info['idToken'] 
        self.machine=None 
        try:
            self.machine=Machine(self.machine_id)
        except:
            raise ValueError("Error intializing machine") 
         

    def get_products(self):
        
       return self.machine.get_products()

    
    def get_product_by_slot(self,slot):
        for product in self.machine.get_products():
            if product.postion==slot:
                return product 
        return None    
    
    #returns a list of all products information
    #show products


class Machine:
    def __init__(self,machine_id):
        self.machine_id=machine_id
        self._machine_info=self.get_machine_data()
        self.products=None
        if self._machine_info!=None:
            self.name=self._machine_info["name"] 
            self.slots=self._machine_info["slots"]
        else:
            raise ValueError("Error retrieving machine")   
        
        self._products=self.get_products()    
        if self._products!=None:
            self.products=self._products    
        else:
            raise ValueError("Error retrieving products")                       
    #state function
    def set_available(self):
        if len(self.products) == 0:
            print("Erro:Machine doesn't have products")
        try:
            db.child("machines").child(self.machine_id).child("state").set(1)
            self.state = 1
            return True
        except:
            print("Error setting machine state")    
             
            
    def set_unavailable(self):
        try:
            db.child("machines").child(self.machine_id).child("state").set(0)    
            self.state = 0
            return True
        except:
            print("Error setting machine state")
   
    def get_state(self):
        try:
            self.state = db.child("machines").child(self.machine_id).child("state").get().val()
            return self.state
        except:
            print("Error getting machine state")
            return None  

    def get_machine_data(self):
        try:
            machine_info=db.child("machines").child(self.machine_id).get().val() 
            return machine_info 
        except:
            print("Error retriveing data")    
            return None
    def get_products(self):
            products=[]
            try:
                productref=db.child('machine-products').child(self.machine_id).get().each()
            except:
                print("Error getting products")
                return None
            
            for product in productref:
                products.append(Product(self.machine_id,product.key()))
                
            products.sort(key=lambda p: p.postion)  
            return products    
     
#move to machine class
   
         
       


class Product:
    def __init__(self,machine_id,product_id):
        self.machine_id=machine_id
        self.product_id=product_id
        product=self.get_product_data()
        self.name=product['name']
        self.imgUrl=product['img']
        self.price=product['price']
        self.amount=product['amount'] 
        self.postion=product['postion'] 
    def get_product_data(self):
        product=db.child('machine-products').child(self.machine_id).child(self.product_id).get().val()
        return product
    def set_product_amount(self,newAmount):
        if newAmount not in range(1,11):
           print("incorrect amount")
           return None
        try:
            db.child('machine-products').child(self.machine_id).child(self.product_id).child("amount").set(newAmount)
            self.amount = db.child('machine-products').child(self.machine_id).child(self.product_id).child("amount").get().val()
            return True
        except:
            return None 
    
    def set_product_price(self,new_price):
        try:
            new_price = float(new_price)
            if new_price <= 0:
                print("Invalid price amount: {}".format(new_price))
                return None
        except ValueError:
            print("Invalid price input: {}".format(new_price))
            return None  
        # Set the instance variable
        self.price = new_price

        try:
            db.child('machine-products').child(self.machine_id).child(self.product_id).child("price").set(new_price)
            return True
        except:
            print("Error updating database")   
            return None 
  
      
        
    
#order class
class Order:
    def __init__(self):
        self.items = []  # List to store the items in the order
        self.total=0

    def add_item(self, product, quantity=1):
        if product.amount<quantity:
            raise ValueError("Not enough inventory")
       
        self.items.append({
            'product': product,
            'quantity': quantity,
            'subtotal':product.price*quantity
        })
        self.total+=product.price*quantity

        print(f"{quantity} {product.name}(s) added to the order.")
    def view_order(self):
        if self.items:
            print("Items in the order:")
            for item in self.items:
                
                print(f"{item['product'].name}: {item['quantity']} x ${item['product'].price} = ${item['subtotal']}")
            print(f"Total: ${self.total}")
        else:
            print("The order is empty.")

    # def process_payment(self):
    #     if self.items:
    #         total = 0
    #         for item in self.items:
    #             subtotal = item['product'].price * item['quantity']
    #             total += subtotal
    #             # Perform any payment processing operations here, such as charging the customer, updating sales, etc.
    #         print(f"Payment processed successfully. Total amount: ${total}")
    #         self.items = []  # Clear the items in the order after processing the payment
    #     else:
    #         print("Cannot process an empty order.")



#Payment


















signin_info=auth.sign_in_with_email_and_password("machine@mail.com",123456)

machine=initialize_machine("machine@mail.com","123456")





#tests

# # Print the name and number of slots of machine_1
# print(machine_1.name)
# print(machine_1.slots)

# # Set the state of machine_1 to available and print the state
# machine_1.set_available()
# print(machine_1.get_state())

# # Set the state of machine_1 to unavailable and print the state
# machine_1.set_unavailable()
# print(machine_1.get_state())

# # Get the list of products of machine_1 and print their names and positions
# products = machine_1.get_products()
# for product in products:
#     print(vars(product))

# # Get the product at slot 1 of machine_1 and print its name
# product_1 = machine_1.get_product_by_slot(1)
# product_1.set_product_price(10)
# product_1.set_product_amount(7)
# print(vars(product_1))





