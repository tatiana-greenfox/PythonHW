import psycopg2 as pg

def create_db(db_name, user_name, user_pass):
    with pg.connect(dbname = 'postgres', user = 'postgres', password = '1') as conn:
        with conn.cursor() as curs:
             curs.execute(
                 "CREATE USER %s WITH PASSWORD %s;", (user_name, user_pass)
             )

             curs.execute(
                 '''
                    CREATE DATABASE %s OWNER %s;
                 ''', (db_name, user_name)
             )

def drop_db(db_name):
    with pg.connect(dbname = 'postgres', user = 'postgres', password = '1') as conn:
        with conn.cursor() as curs:
            curs.execute(
                 '''
                    DROP DATABASE %s; 
                 ''', (db_name)
             )

if __name__ == "__main__":
    create_db('test_create_db', 'tatiana', '111')
    