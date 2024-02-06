import mysql.connector


def get_db_connection():

    config = {
        'user': 'root',
        'password': '765795',
        'host': 'localhost',
        'database': 'omsdb'
    }

    try:
        connection = mysql.connector.connect(**config)

        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def get_ids(table_name, id_column_name):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT ' + id_column_name + ' FROM ' + table_name + ' ORDER BY ' + id_column_name + ' DESC LIMIT 1'
    # print(sql)
    my_cursor.execute(sql)
    x = list(my_cursor.fetchone())[0]
    return int(x) + 1
