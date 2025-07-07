from flask import Blueprint, render_template, url_for
from app.models import layanan

layanan_bp = Blueprint('layanan_bp', __name__, url_prefix='/layanan')

@layanan_bp.route('/')
def daftar_layanan():
    data_layanan = layanan.get_all_layanan()

    # ini buat mapping gambar sesuai layanan nya
    gambar_map = {
    'Creambath': url_for('static', filename='images/creambath.jpg'),
    'Hair Spa': url_for('static', filename='images/hairspa.jpg'),
    'Manicure & Pedicure Spa': url_for('static', filename='images/manipedi.jpg'),
    'Pedicure Spa': url_for('static', filename='images/pedicure.jpg'),
    'Refleksiologi Kaki': url_for('static', filename='images/refkaki.jpg'),
    'Balinese Massage': url_for('static', filename='images/balimes.jpg'),
    }


    return render_template('layanan.html', data_layanan=data_layanan, gambar_map=gambar_map)