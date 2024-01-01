from munch import munchify
import psycopg as pg
import psycopg_binary as pg_binary
import yaml

with open("./config.yaml") as f:
  try:
    yamlfile=yaml.safe_load(f)
  except yaml.YAMLError as exc:
    print(exc)
config = munchify(yamlfile)


class database:
  conn = None

  def __init__(self, host:str=config.db.host, port:int=config.db.port, user:str=config.db.user, password:str=config.db.password, database:str=config.db.db):
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
        
        cursor.execute("""
          CREATE TABLE IF NOT EXISTS albums (
            id serial PRIMARY KEY,
            title text,
            url text UNIQUE,
            time date
          )             
          """)
        
        self.conn.commit()
    except pg.Error as e:
      print(f"Error creating tables: {e}")
  
  
  def write_to_videoDB(self, title, url, download_path, elapsed):
    self.db_create()
    with self.conn.cursor() as cursor:
      cursor.execute("""
        INSERT INTO downloaded (title, url, path, elapsed, time)
        VALUES (%s, %s, %s, %s, NOW());
        """, [title, url, download_path, elapsed])
      self.conn.commit()
      self.conn.close()
  
  def write_to_albumDB(self, title, url):
    self.db_create()
    with self.conn.cursor() as cursor:
      cursor.execute("""
        INSERT INTO albums (title, url, time)
        VALUES (%s, %s, NOW());
        """, [title, url])
      self.conn.commit()
      self.conn.close()
      
# db.db_create()