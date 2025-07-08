from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import restock, detail_restock, produk
from datetime import date
from flask import jsonify

restock_bp = Blueprint('restock_bp', __name__, url_prefix='/restock')

# Tampil semua restock
@restock_bp.route('/')
def manage_restock():
    restock_list = restock.get_all_restock()
    produk_list = produk.get_all_produk()
    detail_list = detail_restock.get_detail_by_restock(id_restock=1)  # Dummy ID for initial load
    return render_template('restock.html', restock=restock_list, produk=produk_list, detail=detail_list)

# Tambah restock
@restock_bp.route('/tambah', methods=['POST'])
def tambah_restock():
    tanggal_restock = date.today()
    total_biaya = 0
    status = 'draft'
    id_staff = 1  # sementara dummy
    id_restock = restock.insert_restock(tanggal_restock, total_biaya, status, id_staff)
    if id_restock:
        return redirect(url_for('restock_bp.detail_restock', id_restock=id_restock))
    else:
        flash("Gagal buat restock.", 'danger')
        return redirect(url_for('restock_bp.manage_restock'))

# Tampil detail restock
@restock_bp.route('/detail/<int:id_restock>')
def detailrestock(id_restock):
    restock_data = restock.get_restock_by_id(id_restock)
    restock_list = restock.get_all_restock()
    detail_list = detail_restock.get_detail_by_restock(id_restock)
    produk_list = produk.get_all_produk()
    return render_template('restock.html',
                           restock=restock_data,
                           restock_list=restock_list,
                           detail=detail_list,
                           produk=produk_list,
                           id_restock=id_restock)


# Tambah produk ke restock
@restock_bp.route('/detail/tambah', methods=['POST'])
def tambah_detail_restock():
    id_restock = request.form.get('id_restock')
    id_produk = request.form.get('id_produk')
    jumlah = request.form.get('jumlah')
    harga_satuan = request.form.get('harga_satuan')
    
    detail_restock.insert_detail(id_restock, id_produk, jumlah, harga_satuan)
    return redirect(url_for('restock_bp.detailrestock', id_restock=id_restock))



# Hapus produk dari detail restock
@restock_bp.route('/detail/hapus/<int:id_detail_restock>/<int:id_restock>', methods=['POST'])
def hapus_detail_restock(id_detail_restock, id_restock):
    detail_restock.delete_detail(id_detail_restock)
    return redirect(url_for('restock_bp.detail_restock', id_restock=id_restock))

# Edit metadata restock (status, tanggal)
@restock_bp.route('/edit/<int:id_restock>', methods=['POST'])
def edit_restock(id_restock):
    tanggal_restock = request.form.get('tanggal_restock')
    total_biaya = request.form.get('total_biaya')
    status = request.form.get('status')
    restock.update_restock(id_restock, tanggal_restock, total_biaya, status)
    return redirect(url_for('restock_bp.manage_restock'))

@restock_bp.route('/get_produk/<int:id_restock>')
def get_produk_by_restock_route(id_restock):
    produk_list = restock.get_produk_by_restock(id_restock)
    if produk_list:
        return jsonify([p['id_produk'] for p in produk_list])
    else:
        return jsonify([])