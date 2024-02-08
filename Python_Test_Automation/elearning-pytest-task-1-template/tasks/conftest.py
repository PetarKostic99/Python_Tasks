import pytest
import sqlite3

table_data = [(1, "books")]


# Part 1
@pytest.fixture(scope='session')
def connection(request):
    # Setup: Create a connection to the database
    conn = sqlite3.connect('example.db')

    # Teardown: Close the connection after all tests in the session
    def close_connection():
        conn.close()

    request.addfinalizer(close_connection)
    yield conn


@pytest.fixture(scope='session')
def cursor(connection):
    # Return cursor object from the connection
    return connection.cursor()


# Part 2
@pytest.fixture(scope='function', params=[(1, "books")])
def table_cursor(request, cursor):
    # Setup: Prepare 'items' table and insert data
    cursor.execute('drop table if exists items')
    cursor.execute('create table items (id int, name text)')
    data = request.param
    cursor.execute(f"insert into items values {data}")
    cursor.connection.commit()

    # Teardown: Drop the 'items' table
    def drop_table():
        cursor.execute('drop table if exists items')

    request.addfinalizer(drop_table)
    return cursor
