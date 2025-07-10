from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import absen, staff
from datetime import date

absen_bp = Blueprint('absen_bp', __name__, url_prefix='/absensi')

# --- TAMPILKAN SEMUA DATA ABSENSI ---
@absen_bp.route('/', methods=['GET', 'POST'])
def manage_absensi():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add_absen':
            id_staff = request.form.get('id_staff')
            tanggal = request.form.get('tanggal')
            jam_masuk = request.form.get('jam_masuk')
            jam_keluar = request.form.get('jam_keluar')
            status = request.form.get('status')
            keterangan = request.form.get('keterangan')
            

            if not all([id_staff, tanggal, jam_masuk, jam_keluar, status]):
                flash('Semua field wajib diisi.', 'danger')
            else:
                result = absen.create_absensi(id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan)
                if result:
                    flash('Absensi berhasil ditambahkan.', 'success')
                else:
                    flash('Gagal menambahkan absensi.', 'danger')
            return redirect(url_for('absen_bp.manage_absensi'))

    is_owner = session['role'] == 'owner'
    absensi = absen.get_all_absensi(
        id_staff=session['id_staff'],
        is_owner=is_owner
    )
    staffs = staff.get_all_staffs()
    return render_template('absen.html', absensi=absensi, staffs=staffs, date=date)


# --- EDIT DATA ABSENSI ---
@absen_bp.route('/edit/<int:id_absensi>', methods=['GET', 'POST'])
def edit_absensi(id_absensi):
    absensi_data = absen.get_absensi_by_id(id_absensi)
    if not absensi_data:
        flash("Data absensi tidak ditemukan.", "danger")
        return redirect(url_for('absen_bp.manage_absensi'))

    if session['role'] != 'owner' and absensi_data['id_staff'] != session['id_staff']:
        flash("Kamu tidak boleh mengedit absensi staff lain.", "danger")
        return redirect(url_for('absen_bp.manage_absensi'))

    if absensi_data['tanggal'] != date.today():
        flash("Absensi hanya bisa diedit di hari yang sama.", "warning")
        return redirect(url_for('absen_bp.manage_absensi'))

    if request.method == 'POST':
        id_staff = request.form.get('id_staff')
        tanggal = request.form.get('tanggal')
        jam_masuk = request.form.get('jam_masuk')
        jam_keluar = request.form.get('jam_keluar')
        status = request.form.get('status')
        keterangan = request.form.get('keterangan')
        absen.update_absensi(id_absensi, id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan)
        flash("Absensi berhasil diupdate.", "success")
        return redirect(url_for('absen_bp.manage_absensi'))

    return render_template('absen.html', edit_mode_absensi=absensi_data, absensi=absen.get_all_absensi(session['id_staff'], session['role'] == 'owner'), staffs=staff.get_all_staffs(), date=date)



# --- HAPUS DATA ABSENSI ---
@absen_bp.route('/hapus/<int:id_absensi>', methods=['POST'])
def hapus_absensi(id_absensi):
    absensi_data = absen.get_absensi_by_id(id_absensi)
    if not absensi_data:
        flash("Data absensi tidak ditemukan.", "danger")
        return redirect(url_for('absen_bp.manage_absensi'))

    # Batasi hapus hanya milik sendiri kecuali admin
    if session['role'] != 'owner' and absensi_data['id_staff'] != session['id_staff']:
        flash("Kamu tidak boleh menghapus absensi staff lain.", "danger")
        return redirect(url_for('absen_bp.manage_absensi'))


    success = absen.delete_absensi(id_absensi)
    if success:
        flash("Data absensi berhasil dihapus.", "success")
    else:
        flash("Gagal menghapus data absensi.", "danger")
    return redirect(url_for('absen_bp.manage_absensi'))