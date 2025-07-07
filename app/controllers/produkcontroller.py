from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import produk, supplier

produk_bp = Blueprint('produk_bp', __name__, url_prefix='/produk')

@produk_bp.route('/', methods=['GET'])
def manage_produk():
    produk_list = produk.get_all_produk()
    supplier_list = supplier.get_all_supplier()
    return render_template('produk.html', produk=produk_list, supplier=supplier_list)

@produk_bp.route('/tambah', methods=['POST'])
def tambah_produk():
    id_supplier = request.form.get('id_supplier')
    nama_produk = request.form.get('nama_produk')
    deskripsi = request.form.get('deskripsi')
    harga_beli = request.form.get('harga_beli')
    stok = request.form.get('stok')
    satuan = request.form.get('satuan')

    success = produk.insert_produk(id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan)
    if success:
        flash("Produk berhasil ditambahkan!", 'success')
    else:
        flash("Gagal menambahkan produk.", 'danger')

    return redirect(url_for('produk_bp.manage_produk'))

@produk_bp.route('/edit/<int:id_produk>', methods=['GET', 'POST'])
def edit_produk(id_produk):
    produk_data = produk.get_produk_by_id(id_produk)
    if not produk_data:
        flash("Data produk tidak ditemukan.", "danger")
        return redirect(url_for('produk_bp.manage_produk'))

    if request.method == 'POST':
        try:
            id_supplier = request.form.get('id_supplier')
            nama_produk = request.form.get('nama_produk')
            deskripsi = request.form.get('deskripsi')
            harga_beli = request.form.get('harga_beli')
            stok = request.form.get('stok')
            satuan = request.form.get('satuan')

            success = produk.update_produk(id_produk, id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan)
            if success:
                flash("Produk berhasil diperbarui.", "success")
            else:
                flash("Gagal memperbarui list produk.", "danger")
            return redirect(url_for('produk_bp.manage_produk'))
        except Exception as e:
            flash(f"Terjadi kesalahan: {e}", "danger")

    daftar_produk = produk.get_all_produk()
    return render_template('produk.html',
                       produk=produk.get_all_produk(),
                       supplier=supplier.get_all_supplier(),
                       edit_mode_produk=produk_data)

@produk_bp.route('/hapus/<int:id_produk>', methods=['POST'])
def hapus_produk(id_produk):
    success = produk.delete_produk(id_produk)
    if success:
        flash("Data produk berhasil dihapus.", "success")
    else:
        flash("Gagal menghapus data produk.", "danger")
    return redirect(url_for('produk_bp.manage_produk'))
