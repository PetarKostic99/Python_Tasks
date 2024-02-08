def test_table_data(table_cursor):
    # Test data for comparison
    expected_data = [(1, "books")]

    # Execute a query to fetch data from the 'items' table
    table_cursor.execute('select id, name from items')

    # Fetch all rows from the result set
    actual_data = table_cursor.fetchall()

    # Compare the expected data with the actual data
    assert actual_data == expected_data
