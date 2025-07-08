from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import reservasi, customer, layanan, staff
import random
from datetime import datetime, timedelta

viewreservasi_bp = Blueprint('viewreservasi_bp', __name__, url_prefix='/viewreservasi')

# Tampil semua reservasi
@viewreservasi_bp.route('/')
def view_reservasi():
    reservasi_list = reservasi.get_all_reservasi()# Dummy ID for initial load
    customer_list = customer.get_all_customers()
    layanan_list = layanan.get_all_layanan()
    id_layanan_selected = request.args.get('id_layanan')
    return render_template('jadwalreservasi.html', reservasi=reservasi_list, customer=customer_list, layanan=layanan_list,
        id_layanan_selected=id_layanan_selected)

@viewreservasi_bp.route('/edit/<int:id_reservasi>', methods=['GET'])
def form_edit_reservasi(id_reservasi):
    reservasi_data = reservasi.get_reservasi_by_id(id_reservasi)
    if not reservasi_data:
        flash("Reservasi tidak ditemukan.", "danger")
        return redirect(url_for('reservasi_bp.manage_reservasi'))

    reservasi_list = reservasi.get_all_reservasi()
    customer_list = customer.get_all_customers()
    layanan_list = layanan.get_all_layanan()
    staff_list = staff.get_all_staffs()

    return render_template('reservasi.html', reservasi=reservasi_list, customer=customer_list, layanan=layanan_list, staff=staff_list, edit_mode_reservasi=reservasi_data)

@viewreservasi_bp.route('/hapus/<int:id_reservasi>', methods=['GET', 'POST'])
def hapus_reservasi(id_reservasi):
    reservasi.delete_reservasi(id_reservasi)
    return redirect(url_for('reservasi_bp.manage_reservasi'))

# Edit metadata reservasi (status, tanggal)
@viewreservasi_bp.route('/edit/<int:id_reservasi>', methods=['POST'])
def edit_reservasi(id_reservasi):
    # Ambil reservasi sekarang dari database
    reservasi_data = reservasi.get_reservasi_by_id(id_reservasi)
    if not reservasi_data:
        flash("Reservasi tidak ditemukan.", "danger")
        return redirect(url_for('reservasi_bp.manage_reservasi'))

    # Waktu reservasi saat ini
    tanggal = reservasi_data['tanggal_reservasi']
    jam = reservasi_data['jam_reservasi']
    waktu_reservasi = datetime.strptime(f"{tanggal} {jam}", "%Y-%m-%d %H:%M:%S")

    # Waktu sekarang
    waktu_sekarang = datetime.now()

    # Batas waktu minimal edit
    batas_waktu = waktu_reservasi - timedelta(hours=1)

    if waktu_sekarang >= batas_waktu:
        flash("Reservasi tidak bisa diubah karena sudah mendekati waktu pelaksanaan.", "danger")
        return redirect(url_for('reservasi_bp.manage_reservasi'))

    # Kalau masih boleh edit
    id_customer = request.form.get('id_customer')
    tanggal_reservasi = request.form.get('tanggal_reservasi')
    jam_reservasi = request.form.get('jam_reservasi')
    id_layanan = request.form.get('id_layanan')
    id_staff = request.form.get('id_staff')
    status = request.form.get('status')

    reservasi.update_reservasi(id_customer, tanggal_reservasi, jam_reservasi, id_layanan, id_staff, status, id_reservasi)
    flash("Reservasi berhasil diupdate.", "success")
    return redirect(url_for('reservasi_bp.manage_reservasi'))
