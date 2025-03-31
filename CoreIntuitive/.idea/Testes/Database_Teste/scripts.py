import mysql.connector

def connect_db():
    
    print("starting")
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ocaosperfeito1#",
        database="database_teste" 
    )
    
    print("succeed.")
    
    return conn

# Conectar ao banco de dados
connect_db()
