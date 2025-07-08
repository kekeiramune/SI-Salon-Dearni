from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import restock, detail_restock, produk
from datetime import date

restock_bp = Blueprint('restock_bp', __name__, url_prefix='/restock')

# FUNGSI 1: HANYA untuk menampilkan DAFTAR SEMUA restock.
# Dia memanggil 'restock.html'.
@restock_bp.route('/')
def manage_restock():
    restock_list = restock.get_all_restock()
    return render_template('restock.html', restock_list=restock_list)

# FUNGSI 2: Untuk MEMBUAT data restock baru, lalu redirect ke halaman detail.
@restock_bp.route('/tambah', methods=['POST'])
def tambah_restock():
    id_staff = 1  # Ganti dengan session jika sudah ada sistem login
    id_restock = restock.insert_restock(date.today(), 0, 'draft', id_staff)
    if id_restock:
        return redirect(url_for('restock_bp.detailrestock', id_restock=id_restock))
    else:
        flash("Gagal membuat data restock baru.", 'danger')
        return redirect(url_for('restock_bp.manage_restock'))

# FUNGSI 3: HANYA untuk menampilkan DETAIL SATU restock.
# Dia memanggil 'detail_restock.html'.
@restock_bp.route('/detail/<int:id_restock>')
def detailrestock(id_restock):
    restock_data = restock.get_restock_by_id(id_restock)
    detail_list = detail_restock.get_detail_by_restock(id_restock)
    produk_list = produk.get_all_produk()
    
    return render_template('detail_restock.html',
                           restock=restock_data,
                           detail=detail_list,
                           produk=produk_list,
                           id_restock=id_restock)

# FUNGSI 4: HANYA untuk MEMPROSES FORM tambah produk dari halaman detail.
@restock_bp.route('/detail/tambah', methods=['POST'])
def tambah_detail_restock():
    id_restock = request.form.get('id_restock')
    id_produk = request.form.get('id_produk')
    jumlah = request.form.get('jumlah')
    harga_satuan = request.form.get('harga_satuan')
    
    detail_restock.insert_detail(id_restock, id_produk, jumlah, harga_satuan)
    return redirect(url_for('restock_bp.detailrestock', id_restock=id_restock))

# (Fungsi hapus dan edit tidak perlu diubah)
@restock_bp.route('/detail/hapus/<int:id_detail_restock>/<int:id_restock>', methods=['POST'])
def hapus_detail_restock(id_detail_restock, id_restock):
    detail_restock.delete_detail(id_detail_restock)
    return redirect(url_for('restock_bp.detailrestock', id_restock=id_restock))

@restock_bp.route('/edit/<int:id_restock>', methods=['POST'])
def edit_restock(id_restock):
    tanggal_restock = request.form.get('tanggal_restock')
    total_biaya = request.form.get('total_biaya')
    status = request.form.get('status')
    restock.update_restock(id_restock, tanggal_restock, total_biaya, status)
    return redirect(url_for('restock_bp.manage_restock'))

# Tambahkan fungsi ini di restockcontroller.py

@restock_bp.route('/update_status/<int:id_restock>/<new_status>', methods=['POST'])
def update_status(id_restock, new_status):
    # Pastikan status yang dikirim valid untuk keamanan
    if new_status in ['draft', 'ordered', 'done']:
        restock.update_status(id_restock, new_status)
        flash(f"Status restock #{id_restock} berhasil diubah menjadi {new_status}.", 'success')
    else:
        flash("Status tidak valid.", 'danger')
    return redirect(url_for('restock_bp.manage_restock'))

    # Tambahkan fungsi ini di restockcontroller.py

@restock_bp.route('/selesai_detail/<int:id_restock>')
def selesai_detail(id_restock):
    # Cek jumlah item di dalam restock ini
    jumlah_item = detail_restock.count_items(id_restock)
    
    # Jika tidak ada item dan statusnya masih draft, hapus data restock utama
    if jumlah_item == 0:
        data_restock = restock.get_restock_by_id(id_restock)
        if data_restock and data_restock['status'] == 'draft':
            restock.delete_by_id(id_restock)
            flash(f"Restock #{id_restock} dibatalkan karena kosong.", 'info')

    return redirect(url_for('restock_bp.manage_restock'))
