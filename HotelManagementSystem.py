import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='****',
            database='hotel_management'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def add_booking(connection, guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode):
    cursor = connection.cursor()
    query = """INSERT INTO bookings (guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode)
    cursor.execute(query, values)
    connection.commit()
    print("Booking added successfully")

def view_bookings(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_booking(connection, booking_id, guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode):
    cursor = connection.cursor()
    query = """UPDATE bookings SET guest_name=%s, room_number=%s, check_in_date=%s, check_out_date=%s, mobile_number=%s, payment_mode=%s
               WHERE id=%s"""
    values = (guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode, booking_id)
    cursor.execute(query, values)
    connection.commit()
    print("Booking updated successfully")

def delete_booking(connection, booking_id):
    cursor = connection.cursor()
    query = "DELETE FROM bookings WHERE id=%s"
    values = (booking_id,)
    cursor.execute(query, values)
    connection.commit()
    print("Booking deleted successfully")

def main():
    connection = create_connection()
    if connection:
        while True:
            print("\nHotel Management System")
            print("1. Add Booking")
            print("2. View Bookings")
            print("3. Update Booking")
            print("4. Delete Booking")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                guest_name = input("Enter guest name: ")
                room_number = int(input("Enter room number: "))
                check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
                check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
                mobile_number = input("Enter mobile number: ")
                payment_mode = input("Enter payment status: ")
                add_booking(connection, guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode)
            
            elif choice == '2':
                view_bookings(connection)
            
            elif choice == '3':
                booking_id = int(input("Enter booking ID: "))
                guest_name = input("Enter new guest name: ")
                room_number = int(input("Enter new room number: "))
                check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
                check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
                mobile_number = input("Enter new mobile number: ")
                payment_mode = input("Enter new payment status: ")
                update_booking(connection, booking_id, guest_name, room_number, check_in_date, check_out_date, mobile_number, payment_mode)
            
            elif choice == '4':
                booking_id = int(input("Enter booking ID: "))
                delete_booking(connection, booking_id)
            
            elif choice == '5':
                break
            
            else:
                print("Invalid choice! Please try again.")

        connection.close()

if __name__ == "__main__":
    main()
