from flask import Flask, render_template, redirect, url_for, flash
from app.config.Database import init_db # Import fungsi inisialisasi database
from app.controllers.staffcontroller import staff_bp # Impor Blueprint staff
from app.controllers.customercontroller import customer_bp # Impor Blueprint staff
from app.controllers.absensicontroller import absen_bp
from app.controllers.restockcontroller import restock_bp
from app.controllers.produkcontroller import produk_bp
from app.controllers.transaksi_layanancontroller import transaksi_bp
from app.controllers.layanancontroller import layanan_bp
from app.controllers.reservasicontroller import reservasi_bp
from app.controllers.viewjadwalcontroller import viewreservasi_bp

app = Flask(__name__)

app.secret_key = 'dear123'

# Inisialisasi database
init_db(app)

# Daftarkan Blueprint staff
app.register_blueprint(staff_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(absen_bp)
app.register_blueprint(produk_bp)
app.register_blueprint(restock_bp)
app.register_blueprint(transaksi_bp)
app.register_blueprint(layanan_bp)
app.register_blueprint(reservasi_bp)
app.register_blueprint(viewreservasi_bp)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)