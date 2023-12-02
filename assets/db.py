import asyncpg, asyncio

async def main():
  conn = await asyncpg.connect(host='localhost',
                               port=5432,
                               user='Kaleb',
                               password='',
                               database='youtube'
                               )
  
  await conn.execute('''
      CREATE TABLE downloaded(
          id serial PRIMARY KEY,
          url text,
          date_downloaded date
      )
  ''')


  await conn.close()


class database:
  conn = None
  async def __init__(self):
    self.conn = await asyncpg.connect('postgresql://Kaleb@localhost:5432/youtube')
    
  async def new_download(self, ):
    self.conn

asyncio.get_event_loop().run_until_complete(main())

