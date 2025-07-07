from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import staff # Impor modul model staff kita
from app.models import absen # Impor modul model absen kita

staff_bp = Blueprint('staff_bp', __name__, url_prefix='/staffs')


@staff_bp.route('/', methods=['GET', 'POST'])
def manage_staffs():
    if request.method == 'POST':
        # --- Logika untuk MENAMBAH Staff Baru ---
        if 'action' in request.form and request.form['action'] == 'add_staff':
            nama_staff = request.form.get('nama_staff')
            alamat = request.form.get('alamat')
            no_telp = request.form.get('no_telp')
            email = request.form.get('email')
            posisi = request.form.get('posisi')

            if not all([nama_staff, alamat, no_telp, email, posisi]):
                flash("Semua kolom harus diisi!", "warning")
            else:
                new_id = staff.create_staff(nama_staff, alamat, no_telp, email, posisi)
                if new_id:
                    flash(f"Staff '{nama_staff}' berhasil ditambahkan dengan ID: {new_id}.", "success")
                else:
                    flash("Gagal menambahkan staff. Silakan coba lagi.", "danger")
            # Setelah POST, kita akan redirect untuk menghindari resubmission form
            return redirect(url_for('staff_bp.manage_staffs'))

        # --- Logika untuk MENGEDIT Staff ---
        elif 'action' in request.form and request.form['action'] == 'edit_staff':
            id_staff_to_edit = request.form.get('id_staff_edit') # Ambil ID dari hidden field
            nama_staff = request.form.get('nama_staff')
            alamat = request.form.get('alamat')
            no_telp = request.form.get('no_telp')
            email = request.form.get('email')
            posisi = request.form.get('posisi')


            if not all([nama_staff, alamat, no_telp, email, posisi, id_staff_to_edit]):
                flash("Semua kolom harus diisi untuk edit!", "warning")
            else:
                success = staff.update_staff(int(id_staff_to_edit), nama_staff, alamat, no_telp, email, posisi)
                if success:
                    flash(f"Data staff '{nama_staff}' berhasil diperbarui.", "success")
                else:
                    flash("Gagal memperbarui data staff. Silakan coba lagi.", "danger")
            return redirect(url_for('staff_bp.manage_staffs'))

        # --- Logika untuk MENGHAPUS Staff ---
        elif 'action' in request.form and request.form['action'] == 'delete_staff':
            id_staff_to_delete = request.form.get('id_staff_delete')
            if id_staff_to_delete:
                success = staff.delete_staff(int(id_staff_to_delete))
                if success:
                    flash("Staff berhasil dihapus.", "success")
                else:
                    flash("Gagal menghapus staff.", "danger")
            return redirect(url_for('staff_bp.manage_staffs'))

        # --- Logika untuk MEMUAT DATA Staff ke Form Edit (via GET dari tabel) ---
        elif 'action' in request.form and request.form['action'] == 'load_for_edit':
            id_staff_to_load = request.form.get('id_staff_load')
            if id_staff_to_load:
                staff_to_edit = staff.get_staff_by_id(int(id_staff_to_load))  # ← Tambahkan ini!
                if staff_to_edit:
                    staffs = staff.get_all_staffs()
                    return render_template('staff_management.html',
                                           staffs=staffs,
                                           edit_mode_staff=staff_to_edit)
        else:
            flash("Staff yang ingin diedit tidak ditemukan.", "danger")


    # --- Untuk permintaan GET (atau setelah POST yang tidak ditangani) ---
    staffs = staff.get_all_staffs() # Selalu ambil daftar staff untuk tabel
    if staffs is None:
        flash("Terjadi kesalahan saat mengambil daftar staff.", "danger")
        staffs = []
    return render_template('staff_management.html', staffs=staffs, edit_mode_staff=None)
    # edit_mode_staff akan berisi data staff jika mode edit, atau None jika mode tambah

@staff_bp.route('/login', methods=['GET', 'POST'])
def login_staff():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if '@' not in email:
            flash("Format email tidak valid. Harus mengandung '@'", 'danger')
            return redirect(url_for('staff_bp.login_staff'))
        
        if len(password) > 14:
            flash("Password tidak boleh lebih dari 14 karakter", 'danger')
            return redirect(url_for('staff_bp.login_staff'))
        print(f"Email: {email}, Password: {password}")  # ✅ Debug
        staff_data = staff.get_staff_by_email(email)
        print("Staff Data:", staff_data)  # ✅ Debug

        if staff_data:
            if staff_data['password'] == password:
                session['logged_in'] = True
                session['staff_name'] = staff_data['nama_staff']
                flash('Berhasil login!', 'success')
                return redirect(url_for('staff_bp.view_staffs'))
            else:
                flash('Password salah!', 'danger')
        else:
            flash('Email tidak ditemukan!', 'danger')

    return render_template('loginstaff.html')

@staff_bp.route('/view', methods=['GET'] )
def view_staffs():
    return render_template('tampilanstaff.html')