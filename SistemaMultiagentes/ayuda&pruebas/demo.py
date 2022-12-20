import psycopg2

#conecta con la base de datos existente en docker
try:
    conn = psycopg2.connect(
        database="AGROdb",
        user="docker",
        password="docker",
        host="localhost"
    )
    print("conectado")
    #objeto cursor para operar con la BD
    cur =conn.cursor()

    cur.execute("SELECT * FROM prueba")
    rows = cur.fetchone()

    if not len(rows):
        print("Empty")
    else:
        for row in rows:
            print(row)
        
    cur.close()
    conn.close
except Exception as ex:
    print(ex)