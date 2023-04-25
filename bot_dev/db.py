import os
import mysql.connector
from dotenv import load_dotenv, find_dotenv


def on_startup():
    pass


def create_connection(host_name, database, user_name, user_password):
    try:
        connection = mysql.connector.connect(host=host_name,
                                             database=database,
                                             user=user_name,
                                             password=user_password)
        print(f"Connection to MySQL DB '{database}' successful.")
    except mysql.connector.Error as err:
        return print(f"The error '{err}' occurred")
    return connection


# data_user = [tg_username, nickname, phone, adress]
def create_or_get_user(connection: mysql.connector,
                       data_user: list) -> int | None:
    tg_username = data_user[1]
    cursor = connection.cursor()
    try:
        get_user_id = ("SELECT user_id FROM user "
                       "WHERE tg_username = %s")
        cursor.execute(get_user_id, (tg_username, ))
        user_id = cursor.fetchall()[0][0]
        return user_id
    except mysql.connector.Error:
        add_user = ("INSERT INTO user "
                    "(tg_username, nickname, phone, adress) "
                    "VALUES (%s, %s, %s, %s)")
        cursor.execute(add_user, data_user)
        connection.commit()


# data_box = [box_name, created_at, finished_at, items_size, items_weight, salt, encrypted_key]
def create_box(connection: mysql.connector, data_user: list, data_box: list):
    user_id = create_or_get_user(connection, data_user)
    data_box.insert(1, user_id)
    add_box_for_user = ("INSERT INTO box "
                        "(box_name, user_id, created_at, finished_at, items_size, items_weight, salt, encrypted_key) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    cursor = connection.cursor()
    cursor.execute(add_box_for_user, data_box)
    connection.commit()


def get_user_boxes(connection: mysql.connector, user_id: int) -> list[tuple]:
    cursor = connection.cursor()
    user_boxes = ("SELECT * FROM box "
                  "WHERE user_id = %s")
    cursor.execute(user_boxes, (user_id, ))
    boxes = cursor.fetchall()
    return boxes


def get_box(connection: mysql.connector, box_id: int) -> tuple:
    cursor = connection.cursor()
    user_box = ("SELECT * FROM box "
                "WHERE box_id = %s")
    cursor.execute(user_box, (box_id, ))
    box = cursor.fetchall()[0]
    return box


def delete_box(connection: mysql.connector, box_id: int) -> None:
    cursor = connection.cursor()
    cursor.execute(("DELETE FROM box WHERE box_id = %s"), (box_id, ))
    connection.commit()


# Возвращает пустой список, если нет просроченных
def get_overdue_boxes(connection: mysql.connector) -> list[tuple]:
    overdue = "SELECT \
        tg_username, nickname, box_id, finished_at, phone, adress, \
        DATEDIFF(CURDATE(), finished_at) AS overdue_days \
        FROM user INNER JOIN box ON user.user_id = box.user_id \
        WHERE DATEDIFF(CURDATE(), finished_at) > 0"
    cursor = connection.cursor()
    cursor.execute(overdue)
    return cursor.fetchall()


def get_overdue_box(connection: mysql.connector, box_id: int) -> tuple:
    overdue = "SELECT \
        tg_username, nickname, box_id, finished_at, phone, adress, \
        DATEDIFF(CURDATE(), finished_at) AS overdue_days \
        FROM user INNER JOIN box ON user.user_id = box.user_id \
        WHERE DATEDIFF(CURDATE(), finished_at) > 0 AND box_id = %s"
    cursor = connection.cursor()
    cursor.execute(overdue, (box_id, ))
    return cursor.fetchall()[0]


def get_all_boxes(connection: mysql.connector) -> list[tuple]:
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM box"))
    return cursor.fetchall()


def main():
    load_dotenv(find_dotenv())
    conn = create_connection(
        host_name="localhost", 
        database="self_storage",
        user_name="root",
        user_password='michael')
    return conn


if __name__ == "__main__":
    conn = main()
    data_user = ['@myname', '', '+9048383', 'NYC']
    user_id = create_or_get_user(conn, data_user)
