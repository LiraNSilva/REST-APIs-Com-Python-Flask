import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, \
    nome text, estrela real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha hotel', 4.3, 345.30, 'Rio De Janeiro')"

cursor.execute(criar_tabela)
cursor.execute(cria_hotel)

connection.commit
connection.close()