from flask import send_file
from flask import make_response, flash
from flask import Flask
from functools import wraps
from flask import render_template, redirect, request
from flask import session
from flask import url_for
from nocache import nocache
from billing_portal.models.invoice import GenerateInvoice
from billing_portal.common.databasesql import Database
from billing_portal.models.user import User
from billing_portal.models.allfields import Allfields
import time


#from billing_portal.models.forms import UserAddForm
#import billing_portal.app


app = Flask(__name__)
app.secret_key = "somerandomstringisrequired"


@app.before_first_request
def initialize_database():
    Database.initialize()



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login_template'))

    return wrap

@app.route('/')
def home_template():
    return redirect(url_for('login_template'))



@app.route('/login')
def login_template():
    return render_template('login.html')




@app.route('/auth/login',methods=['POST'])
@nocache
def login_user():

    username = request.form['username']
    password = request.form['password']

    newuser = User(username, password)

    if newuser.login_valid(username, password):
        newuser.login(username)
        return redirect(url_for('dashboard'))
    else:
        session['name']= None
        return render_template("login.html")

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    datafields=Allfields.fetchallfields()
    if request.method == 'POST':

        return render_template('dashboard.html', datafields=datafields)

    else:

        return render_template('dashboard.html', datafields=datafields)



@app.route('/data_entry')
@login_required
def data_entry():
    return render_template('fields.html')


@app.route('/handle_data', methods=['POST'])
@login_required
def handle_data():
    date = request.form['Date']
    grno = request.form['GrNo']
    pkgs = request.form['Pkgs']
    awt = request.form['Awt']
    cwt = request.form['Cwt']
    invoiceno = request.form['Invoice']
    sender = request.form['Sender']
    receiver = request.form['Receiver']
    origin = request.form['Origin']
    destination = request.form['Destination']
    mode = request.form['Mode']
    freight = request.form['Freight']
    li = [date,grno,pkgs,awt,cwt,invoiceno,sender,receiver,origin,destination,mode,freight]
    Allfields.saveallfields(li)
    return redirect(url_for('data_entry'))




@app.route('/logout')
@nocache
@login_required
def logout():
     User.logout()
     flash("You have been logged out!")
     return redirect(url_for('home_template'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")




@app.route('/New_Entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    if request.method == 'POST':
        datafields = []
        date = request.form['date']
        #date = time.strftime(date)
        datafields.append(date)
        prdct = request.form['prdct']
        datafields.append(prdct)
        rate = int(request.form['rate'])
        datafields.append(rate)
        qty = int(request.form['qty'])
        datafields.append(qty)
        gst = int(request.form['gst'])
        datafields.append(gst)
        stax = int(request.form['stax'])
        datafields.append(stax)


        subtotal = int(rate*qty);
        datafields.append(subtotal)
        total = int(subtotal + (gst*subtotal)/100 + (stax*subtotal)/100)
        datafields.append(total)

        Allfields.saveallfields(datafields)

    #datafields=Allfields.fetchallfields()
    return render_template('newentry.html')


@app.route('/Invoice')
@login_required
def Invoice():
    datafields=Allfields.fetchallfields()
    GenerateInvoice.createInvoice(datafields)
    time.sleep(1)
    return send_file('/home/madmax/projects/gst-billing-and-Invoice/invoice.pdf')


@app.route('/auth/add_user',methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']

    if(User.add_user(username, password)):
        return render_template("profile.html")

    else:
        flash("That username already exists.!")
        return render_template("add_user.html")



@app.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if(User.add_user(username, password)):
            return redirect('dashboard')
        else:
            return render_template('addnewuser.html')
    else:
        return render_template('addnewuser.html')


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if(User.update_user(username, password)):
            return redirect('dashboard')
        else:
            return render_template('changepassword.html')
    else:
        return render_template('changepassword.html')


@app.route('/delete_user', methods=['GET', 'POST'])

@login_required
def delete_user():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if(User.delete_user(username, password)):
            return redirect('dashboard')
        else:
            return render_template('deleteuser.html')
    else:
        return render_template('deleteuser.html')


app.run(port=5002, debug=True)
