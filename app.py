from flask import Flask, request, render_template, redirect, url_for
import pyodbc

app = Flask(__name__)

#------------------------------------------- Login Data -----------------------------------------
class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-F82IRCQF;DATABASE=flaskapp;')
        self.cursor = self.conn.cursor()

    def set_items(self, arg1, arg2, arg3):
        self.cursor.execute("INSERT INTO user_info(email, name, password) VALUES (?, ?, ?)",(arg1, arg2, arg3))
        self.conn.commit()
        

    def check_credentials(self, email, password):
        self.cursor.execute("SELECT * FROM user_info WHERE email=? AND password=?", (email, password))
        return self.cursor.fetchone() is not None
    

#------------------------------------Appointment Data-------------------------------------------
class AppointmentDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-F82IRCQF;DATABASE=flaskapp;')
        self.cursor = self.conn.cursor()

    def set_items(self, name, email, mobile, date, timing, requested_by):
        self.cursor.execute("INSERT INTO appointment(name, email, mobile, date, timing, requested_by) VALUES (?, ?, ?, ?, ?, ?)", (name, email, mobile, date, timing, requested_by))
        self.conn.commit()


#------------------------------------Default Route----------------------------------------------
@app.route('/')
def temp_home():
    return render_template('temp_home.html')


#------------------------------------Login Route (login.html)--------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['password']

        db = ItemDatabase()
        if db.check_credentials(email, password):
            return render_template('index.html')
        else:
            message = "Incorrect email or password. Please try again."

    return render_template('login.html', message=message)


#------------------------------Register Page Route (register.html)--------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        try:
            db = ItemDatabase()
            db.set_items(email, name, password)
            return render_template('login.html')
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('register.html')


#------------------------------Home Page Route (index.html)--------------------------------
@app.route('/index')
def index():
    return render_template('index.html')


#------------------------------Doctors Page Route (doctors.html)--------------------------------
@app.route('/doctors')
def doctors():
    return render_template('/doctors.html')


#------------------------------Medicines Page Route (medicines.html)--------------------------------
@app.route('/medicines')
def medicines():
    return render_template('medicines.html')    #('medicines.html', medicines_data=medicines_data)


#------------------------------About Page Route (about.html)--------------------------------
@app.route('/about')
def about():
    return render_template('/about.html')


#------------------------------Appointment Page Route (appointment.html)--------------------------------
@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['phone']
        date = request.form['appointment_date']
        timing = request.form['timing']
        requested_by = request.form['requested_by']
        
        try:
            db = AppointmentDatabase()
            db.set_items(name, email, mobile, date, timing, requested_by)
            return render_template('index.html')
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
    return render_template('appointment.html')


#------------------------------Services Page Route (services.html)--------------------------------
# @app.route('/services')
# def services():
#     return "hello"


#------------------------------Contact Page Route (contact.html)--------------------------------
@app.route('/contact')
def contact():
    return render_template('contact.html')


#------------------------------Cart Page Route (cart.html)--------------------------------
@app.route('/cart')
def cart():
    total_price = sum(item["price"] * item["quantity"] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


#------------------------------Remeve Items from Cart--------------------------------
@app.route('/remove_item/<int:item_id>', methods=['POST'])
def remove_item(item_id):
    global cart_items
    cart_items = [item for item in cart_items if item["id"] != item_id]
    return redirect(url_for('cart'))



# Sample data for cart items
cart_items = [
    {"id": 1, "name": "Paracetamol", "price": 5.99, "quantity": 2, "image": "images/paracetamol.jpg"},
    {"id": 2, "name": "Ibuprofen", "price": 7.99, "quantity": 1, "image": "images/ibuprofen.jpg"},
    # Add more sample cart items as needed
]



#------------------------------Running App (app.py)--------------------------------
if __name__ == '__main__':
    app.run(debug=True)

