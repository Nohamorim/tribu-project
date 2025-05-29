import psycopg2

try:
    conn = psycopg2.connect(
        dbname="cadastro",
        user="noemy",
        password="umaSenhaSegura",  # troque pela sua senha real
        host="localhost",
        port="5432",
    )
    print("✅ Conexão com o banco estabelecida com sucesso!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar com o banco:", e)
