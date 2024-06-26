import psycopg2

pg_conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
pg_cursor = pg_conn.cursor()

# select first name, last name from all presidents
pg_cursor.execute('''
    select firstname, lastname from presidents order by termnum desc
''')

print(f"{pg_cursor.rowcount} rows in result set\n")

for row in pg_cursor.fetchall():
    print(' '.join(row))
print()

pg_conn.close()

