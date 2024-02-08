from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters
    Performs a query on the input data by applying column selection and
    filtering based on the specified criteria.

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data based on the applied selection and filters.
    """
    result = selector(data)
    for f in filters:
        result = f(result)
    return result


def select(*columns: str) -> ModifierFunc:
    """
    Return function that selects only specific columns from the dataset.

    :param columns: Columns to be selected
    :return: A function (modifier_func) that, when applied to data,
             returns a new dataset with only the specified columns for each row.
    """
    def modifier_func(data: DataType) -> DataType:
        return [{col: row[col] for col in columns} for row in data]
    return modifier_func


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return function that filters a specific column to be one of the provided values.

    :param column: Column to be filtered
    :param values: Values to filter the column
    :return: A function (modifier_func) that, when applied to data,
             returns a new dataset with only the rows where the specified
             column matches one of the provided values.
    """
    def modifier_func(data: DataType) -> DataType:
        return [row for row in data if row[column] in values]
    return modifier_func


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value

    value2 = query(
        friends,
        select('name', 'sport'),
        field_filter('sport', *('Volleyball',)),
    )
    assert [{'name': 'Emily', 'sport': 'Volleyball'}] == value2


if __name__ == "__main__":
    test_query()
