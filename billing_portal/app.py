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
            flash("You need to login first.", 'error')
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
        flash("Invalid Credentials", 'error')
        return redirect(url_for("login_template"))


@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    datafields=Allfields.fetchallfields()
    return render_template('dashboard.html', datafields=datafields)


@app.route('/dashboard/<entryID>/')
def dashboard_delete(entryID):
    Allfields.deleteentry(entryID)
    flash('Entry Deleted Successfully', 'success')
    return redirect(url_for('dashboard'))


@app.route('/New_Entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    totallist = [0,0,0,0]
    if request.method == 'POST':
        datafields = []
        date = request.form['date']
        # date = time.strftime(date)
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

        subtotal = int(rate * qty);
        datafields.append(subtotal)
        total = int(subtotal + (gst * subtotal) / 100 + (stax * subtotal) / 100)
        datafields.append(total)

        if request.form.get('Submit') == 'Add New Entry':

            if Allfields.saveallfields(datafields):
                totallist[0] = datafields[6]
                totallist[1] = datafields[4]
                totallist[2] = datafields[5]
                totallist[3] = datafields[7]
                flash("Entry added successfully", 'success')

            else:
                flash("Something went wrong", 'error')
        #datafields=Allfields.fetchallfields()
        if request.form.get('Submit') == 'Generate Invoice':
            dicdatafields = {}
            dicdatafields['date'] = datafields[0]
            dicdatafields['product'] = datafields[1]
            dicdatafields['rate'] = datafields[2]
            dicdatafields['quantity'] = datafields[3]
            dicdatafields['gstrate'] = datafields[4]
            dicdatafields['stax'] = datafields[5]
            dicdatafields['subtotal'] = datafields[6]
            dicdatafields['total'] = datafields[7]
            GenerateInvoice.createInvoice([dicdatafields])
            time.sleep(1)
            return send_file('/home/madmax/projects/gst-billing-and-Invoice/invoice.pdf')

    return render_template('newentry.html', totallist = totallist)


@app.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if(User.add_user(username, password)):
            flash('User added succefully', 'success')
        else:
            flash('User already exists.', 'error')
    return render_template('addnewuser.html')


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if(User.update_user(username, password)):
            flash('password changed successfully.', 'success')
        else:
            flash('Username do not exists.', 'error')

    return render_template('changepassword.html')


@app.route('/delete_user',methods=['GET', 'POST'])
@login_required
def delete_user():
    userlist = Allfields.fetchallusers()
    return render_template('deleteuser.html', userlist = userlist)



@app.route('/delete_user/<username>', methods=['GET', 'POST'])
@login_required
def deletinguser(username):
    if User.delete_user(username):
        flash('user deleted successfully', 'success')
        return redirect(url_for('delete_user'))
    else:
        flash('error occured', 'error')
        return redirect(url_for('delete_user'))



@app.route('/Invoice')
@login_required
def Invoice():
    datafields=Allfields.fetchallfields()
    GenerateInvoice.createInvoice(datafields)
    time.sleep(1)
    return send_file('/home/madmax/projects/gst-billing-and-Invoice/invoice.pdf')



@app.route('/logout')
@nocache
@login_required
def logout():
     User.logout()
     flash("You have been logged out!", 'success')
     return redirect(url_for('home_template'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


app.run(port=5002, debug=True)
