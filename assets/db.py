import psycopg as pg

class database:
  conn = None

  def __init__(self, host:str=None, port:int=5432, user:str=None, password:str=None, database:str=None):
    self.conn = pg.connect(f"host={host} port={port} dbname={database} user={user} password={password}")

  def db_create(self):
    try:
      with self.conn.cursor() as cursor:
        cursor.execute("""
          CREATE TABLE IF NOT EXISTS downloaded (
            id serial PRIMARY KEY,
            title text,
            url text,
            path text,
            elapsed text,
            time date
          )             
          """)
        self.conn.commit()
    except pg.Error as e:
      print(f"Error creating table: {e}")
  def write_to_db(self, title, url, download_path, elapsed):
    self.db_create()
    with self.conn.cursor() as cursor:
      cursor.execute("""
        INSERT INTO downloaded (title, url, path, elapsed, time)
        VALUES (%s, %s, %s, %s, NOW());
        """, [title, url, download_path, elapsed])
      self.conn.commit()
      
# db.db_create()
