import sqlite3

# Функция, создающая структуру БД (таблицы)


def create_database():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Создание таблицы клиентов
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 email TEXT,
                 phone TEXT)''')

    conn.commit()
    conn.close()

# Функция, позволяющая добавить нового клиента


def add_client(first_name, last_name, email=None, phone=None):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Добавление записи о клиенте в таблицу clients
    c.execute("INSERT INTO clients (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)",
              (first_name, last_name, email, phone))

    conn.commit()
    conn.close()

# Функция, позволяющая добавить телефон для существующего клиента


def add_phone(client_id, phone):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Поиск клиента по ID и обновление поля phone
    c.execute("UPDATE clients SET phone = ? WHERE id = ?", (phone, client_id))

    conn.commit()
    conn.close()

# Функция, позволяющая изменить данные о клиенте


def update_client(client_id, first_name=None, last_name=None, email=None):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Поиск клиента по ID и обновление соответствующих полей
    if first_name:
        c.execute("UPDATE clients SET first_name = ? WHERE id = ?",
                  (first_name, client_id))
    if last_name:
        c.execute("UPDATE clients SET last_name = ? WHERE id = ?",
                  (last_name, client_id))
    if email:
        c.execute("UPDATE clients SET email = ? WHERE id = ?",
                  (email, client_id))

    conn.commit()
    conn.close()

# Функция, позволяющая удалить телефон для существующего клиента


def delete_phone(client_id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Поиск клиента по ID и удаление поля phone
    c.execute("UPDATE clients SET phone = NULL WHERE id = ?", (client_id,))

    conn.commit()
    conn.close()

# Функция, позволяющая удалить существующего клиента


def delete_client(client_id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Удаление клиента по ID
    c.execute("DELETE FROM clients WHERE id = ?", (client_id,))

    conn.commit()
    conn.close()

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону


def find_client(keyword):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Поиск клиента по имени, фамилии, email или телефону
    c.execute("SELECT * FROM clients WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR phone LIKE ?",
              ("%" + keyword + "%", "%" + keyword + "%", "%" + keyword + "%", "%" + keyword + "%"))
    clients = c.fetchall()

    conn.close()

    return clients


# Пример использования функций
create_database()
add_client('Kirill', 'Leschenko', 'Unlimi.net@mail.ru', '123456789')
add_phone(1, '987654321')
update_client(1, email='john.doe@example.com')
delete_phone(1)
delete_client(1)
clients = find_client('Kirill')
print(clients)
