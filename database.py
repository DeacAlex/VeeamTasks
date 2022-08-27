import sqlite3


def sql_database():
    conn = sqlite3.connect('Client_data.db')
    conn.execute(''' CREATE TABLE Client_db
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 user_uuid varchar(40) NOT NULL,
                 user_unique_code varchar(40) NOT NULL)''')
    conn.commit()
    conn.close()


def insert_data(user_uuid, user_unique_code):
    conn = sqlite3.connect('Client_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Client_db VALUES (?,?,?)", (None, user_uuid, user_unique_code))
    conn.commit()
    print("Data added succesfully")
    conn.close()


def check_data(user_uuid, user_unique_code):
    conn = sqlite3.connect('Client_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Client_db WHERE user_uuid =:NAME", {'NAME': user_uuid})
    if cursor.fetchone()[2] == user_unique_code:
        return True


def show_data():
    conn = sqlite3.connect('Client_data.db')
    cursor = conn.cursor()
    for row in cursor.execute('SELECT * FROM Client_db'):
        print (row)


def delete_data():
    conn = sqlite3.connect('Client_data.db')
    cursor = conn.cursor()
    delete_query = """DELETE FROM Client_db"""
    cursor.execute(delete_query)
    conn.commit()


if __name__ == '__main__':
    # sql_database()
    # insert_data('288d9ef36f6544da804a8f1a1211e161', 'b0ca429a251111ed94e7b4b6868ef913')
    # get_data('288d9ef36f6544da804a8f1a1211e161', 'b0ca429a251111ed94e7b4b6868ef913')
    # delete_data()
    get_data()
    show_data()
