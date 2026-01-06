import mysql.connector
import json

# CONFIGURACION DEL WAMSERVER
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',          
    'password': '',           
    'database': 'peliculas_db'
}

print("="*60)
print("IMPORTANDO DATOS A MYSQL")
print("="*60)

try:
    # Conectar a MySQL 
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    cursor = conn.cursor()
    
    # Crear la base de datos si no existe
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cursor.execute(f"USE {DB_CONFIG['database']}")
    
    
    # Eliminar tablas si existen 
    cursor.execute("DROP TABLE IF EXISTS casting")
    cursor.execute("DROP TABLE IF EXISTS actores")
    cursor.execute("DROP TABLE IF EXISTS peliculas")
    
    
    # Crear tabla peliculas
    cursor.execute('''
        CREATE TABLE peliculas (
            id INT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            año INT NOT NULL,
            puntaje DECIMAL(3,1),
            votos INT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ''')
   
    
    # Crear tabla actores
    cursor.execute('''
        CREATE TABLE actores (
            id INT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellidos VARCHAR(100) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ''')
    
    # Crear tabla casting
    cursor.execute('''
        CREATE TABLE casting (
            pelicula_id INT,
            actor_id INT,
            FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
            FOREIGN KEY (actor_id) REFERENCES actores(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ''')
    
    # Leer datos del JSON
    with open('datos_peliculas.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    # Insertar películas
    for pelicula in datos['peliculas']:
        cursor.execute('''
            INSERT INTO peliculas (id, titulo, año, puntaje, votos)
            VALUES (%s, %s, %s, %s, %s)
        ''', (pelicula['id'], pelicula['titulo'], pelicula['año'], 
              pelicula['puntaje'], pelicula['votos']))
    
    # Insertar actores
    for actor in datos['actores']:
        cursor.execute('''
            INSERT INTO actores (id, nombre, apellidos)
            VALUES (%s, %s, %s)
        ''', (actor['id'], actor['nombre'], actor['apellidos']))
    
    # Insertar casting
    for casting in datos['casting']:
        cursor.execute('''
            INSERT INTO casting (pelicula_id, actor_id)
            VALUES (%s, %s)
        ''', (casting['pelicula_id'], casting['actor_id']))
    
    # Confirmar cambios
    conn.commit()
    print("\n" + "="*60)
    print("¡IMPORTACIÓN COMPLETADA EXITOSAMENTE")
    print("="*60)
    print(f"Base de datos: {DB_CONFIG['database']}")
    print(f"Películas: {len(datos['peliculas'])}")
    print(f"Actores: {len(datos['actores'])}")
    print(f"Relaciones casting: {len(datos['casting'])}")
    print("="*60)
    
    
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
        print("\n Conexión cerrada")