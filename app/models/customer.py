from app.config.Database import mysql

# --- READ All Customer ---
def get_all_customers():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_customer, nama_customer, alamat, no_telp, email, password FROM customer")
        customers = cursor.fetchall() 
        cursor.close()
        return customers
    except Exception as e:
        print("Error fetching all customers:", str(e))
        return None



# --- READ customer by ID ---
def get_customer_by_id(id_customer: int):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_customer, nama_customer, alamat, no_telp, email, password FROM customer WHERE id_customer = %s", (id_customer,))
        customer = cursor.fetchone()  # <-- langsung dict kalau config-nya benar
        cursor.close()
        return customer
    except Exception as e:
        print(f"Error fetching customer by ID {id_customer}: {e}")
        return None

def get_customer_by_email(email):
    try:
        cursor = mysql.connection.cursor() 
        cursor.execute("SELECT * FROM customer WHERE email = %s", (email,))
        customer_data = cursor.fetchone()
        cursor.close()
        return customer_data
    except Exception as e:
        print(f"Error fetching customer by email: {e}")
        return None


    
def get_customer_by_password(password):
    try:
        cursor = mysql.connection.cursor() 
        cursor.execute("SELECT * FROM customer WHERE password = %s", (password,))
        customer_data = cursor.fetchone()
        if customer_data:
            column_names = [desc[0] for desc in cursor.description]
            customer_dict = dict(zip(column_names, customer_data))
            cursor.close()
            return customer_dict
        cursor.close()
        return None
    except Exception as e:
        print(f"Error fetching customer by password: {e}")
        return None