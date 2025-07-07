from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import transaksi_layanan
from datetime import date

transaksi_bp = Blueprint('transaksi_bp', __name__, url_prefix='/transaksi')

# Tampil semua transaksi
@transaksi_bp.route('/')
def manage_transaksi():
    transaksi_list = transaksi_layanan.get_all_transaksi()
    reservasi_list = transaksi_layanan.get_reservasi_selesai()
    return render_template('prosestransaksi.html', transaksi=transaksi_list, reservasi=reservasi_list)

# Tambah transaksi
@transaksi_bp.route('/tambah', methods=['POST'])
def tambah_transaksi():
    id_reservasi = request.form.get('id_reservasi')
    tanggal_transaksi = request.form.get('tanggal_transaksi')
    total_bayar = request.form.get('total_bayar')
    metode_pembayaran = request.form.get('metode_pembayaran')
    status_pembayaran = request.form.get('status_pembayaran')

    transaksi_layanan.insert_transaksi(id_reservasi, tanggal_transaksi, total_bayar, metode_pembayaran, status_pembayaran)
    flash("Transaksi berhasil ditambahkan.", 'success')
    return redirect(url_for('transaksi_bp.manage_transaksi'))

# Ubah status pembayaran
@transaksi_bp.route('/ubah_status/<int:id_transaksi>', methods=['POST'])
def ubah_status(id_transaksi):
    status_baru = request.form.get('status_pembayaran')

    # Cek status transaksi via model
    status_saat_ini = transaksi_layanan.get_status_transaksi(id_transaksi)

    if status_saat_ini is None:
        flash('Data transaksi tidak ditemukan.', 'danger')
    elif status_saat_ini == 'Lunas':
        flash('Status transaksi ini sudah Lunas dan tidak bisa diubah.', 'warning')
    else:
        transaksi_layanan.update_status_pembayaran(id_transaksi, status_baru)
        flash('Status pembayaran berhasil diupdate.', 'success')

    return redirect(url_for('transaksi_bp.manage_transaksi'))
