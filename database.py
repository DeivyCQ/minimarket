from connection.conn import Conexion

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_editorial(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS editorial(
                editorial_id SERIAL PRIMARY KEY NOT NULL,
                nombres varchar(150) NOT NULL,
                direccion varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_autor(self):
    
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  autor(
                autor_id  SERIAL PRIMARY KEY NOT NULL,
                nombres varchar(150) NOT NULL,
                apellidos varchar(150) NOT NULL,
                fecha_nacimiento date NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
        
    def crear_genero(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  genero(
                genero_id  SERIAL  PRIMARY KEY NOT NULL,
                decripcion varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
        
    def crear_estado_libro(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS estado_libro(
                estado_libro_id SERIAL PRIMARY KEY NOT NULL,
                descripcion varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
    
    def crear_libro(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS libro(
                libro_id SERIAL PRIMARY KEY NOT NULL,
                editorial_id INTEGER NOT NULL,
                nombres varchar(150) NOT NULL,
                genero_id INTEGER NOT NULL,
                estado_libro_id INTEGER NOT NULL,
                CONSTRAINT fk_editorial FOREIGN KEY (editorial_id) REFERENCES editorial(editorial_id),
                CONSTRAINT fk_genero FOREIGN KEY (genero_id) REFERENCES genero(genero_id),
                CONSTRAINT fk_estado_libro FOREIGN KEY (estado_libro_id) REFERENCES estado_libro(estado_libro_id)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
    
    def crear_libro_autor(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS libro_autor(
                libro_autor_id SERIAL PRIMARY KEY NOT NULL,
                libro_id INTEGER NOT NULL,
                autor_id INTEGER NOT NULL,
                CONSTRAINT fk_libro FOREIGN KEY (libro_id) REFERENCES libro(libro_id),
                CONSTRAINT fk_autor FOREIGN KEY (autor_id) REFERENCES autor(autor_id)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
  
    def crear_libro_edicion(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS libro_edicion(
                libro_edicion_id SERIAL PRIMARY KEY NOT NULL,
                libro_id INT NOT NULL,
                descripcion varchar(150) NOT NULL,
                CONSTRAINT fk_edicion FOREIGN KEY (libro_id) REFERENCES libro(libro_id)
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_estado_lector(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS estado_lector(
                estado_lector_id SERIAL PRIMARY KEY NOT NULL,
                descripcion varchar(150) NOT NULL
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_lector(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS lector(
                lector_id SERIAL PRIMARY KEY NOT NULL,
                dni varchar(150) NOT NULL,
                nombres varchar(150) NOT NULL,
                apellidos varchar(150) NOT NULL,
                fecha_nacimiento date NOT NULL,
                estado_lector_id INT NOT NULL,
                CONSTRAINT fk_estado_lector FOREIGN KEY (estado_lector_id) REFERENCES estado_lector(estado_lector_id)
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_estado_alquiler(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS estado_alquiler(
                estado_alquiler_id SERIAL PRIMARY KEY NOT NULL,
                descripcion varchar(150) NOT NULL
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_alquiler(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS alquiler(
                alquiler_id SERIAL PRIMARY KEY NOT NULL,
                libro_id INT NOT NULL,
                lector_id INT NOT NULL,
                fecha_alquiler date NOT NULL,
                fecha_devolucion date NOT NULL,
                estado_alquiler_id INT NOT NULL,
                CONSTRAINT fk_libro FOREIGN KEY (libro_id) REFERENCES libro(libro_id),
                CONSTRAINT fk_lector FOREIGN KEY (lector_id) REFERENCES lector(lector_id),
                CONSTRAINT fk_estado_alquiler FOREIGN KEY (estado_alquiler_id) REFERENCES estado_alquiler(estado_alquiler_id)
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

conn = Conexion('sistema_biblioteca')
database= Database(conn)
database.crear_editorial()
database.crear_autor()
database.crear_genero()
database.crear_estado_libro()
database.crear_libro()
database.crear_libro_autor()
database.crear_libro_edicion()
database.crear_estado_lector()
database.crear_lector()
database.crear_estado_alquiler()
database.crear_alquiler()
conn.close_connection()