from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import customer

customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')


@customer_bp.route('/login', methods=['GET', 'POST'])
def login_customer():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if '@' not in email:
            flash("Format email tidak valid. Harus mengandung '@'", 'danger')
            return redirect(url_for('customer_bp.login_customer'))
        
        if len(password) > 14:
            flash("Password tidak boleh lebih dari 14 karakter", 'danger')
            return redirect(url_for('customer_bp.login_customer'))
        print(f"Email: {email}, Password: {password}")  # ✅ Debug
        customer_data = customer.get_customer_by_email(email)
        print("Customer Data:", customer_data)  # ✅ Debug

        if customer_data:
            if customer_data['password'] == password:
                session['logged_in'] = True
                session['customer_name'] = customer_data['nama_customer']
                flash('Berhasil login!', 'success')
                return redirect(url_for('customer_bp.view_customer'))
            else:
                flash('Password salah!', 'danger')
        else:
            flash('Email tidak ditemukan!', 'danger')

    return render_template('logincustomer.html')

@customer_bp.route('/view', methods=['GET'] )
def view_customer():
    return render_template('tampilancustomer.html')