def test_check_uniqueness_of_pk(cursor):
    """ TC1.Verify if the primary key  in [hr].[employees]  table is unique"""

    query = 'SELECT employee_id, count(*) FROM [TRN].[hr].[employees] GROUP BY employee_id HAVING COUNT(*) > 1'
    cursor.execute(query)
    result = cursor.fetchall()
    assert result == []


def test_check_not_null_columns(cursor):
    """TC2.Verify if  not nullable columns in [hr].[employees]  table doesn't contain NULL"""

    query = 'SELECT * FROM [TRN].[hr].[employees] WHERE employee_id IS NULL OR last_name IS NULL OR email IS NULL OR hire_date IS NULL OR job_id IS NULL OR salary IS NULL'
    cursor.execute(query)
    result = cursor.fetchall()
    assert result == []


def test_check_full_duplicates(cursor):
    """TC3.Verify if there are any duplicated rows  in [hr].[countries]  table"""

    query = 'SELECT country_id, country_name, region_id, count(*) FROM [TRN].[hr].[countries] GROUP BY country_id, country_name, region_id HAVING count(*) > 1'
    cursor.execute(query)
    result = cursor.fetchall()
    assert result == []


def test_check_length_of_country_id(cursor):
    """TC4. Verify if all country_id values in [hr].[countries]  have appropriate length"""

    query = 'SELECT country_id, country_name, region_id, len(country_id) AS length_id FROM [TRN].[hr].[countries] WHERE len(country_id) <> 2'
    cursor.execute(query)
    result = cursor.fetchall()
    assert result == []


def test_check_row_count(cursor):
    """TC5. Verify if the row count of a table [hr].[jobs]  matches an expected value"""

    query = 'SELECT count(*) FROM [TRN].[hr].[jobs]'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 19


def test_check_validity_of_min_and_max_salary(cursor):
    """TC6. Verify if min_salary is less than max_salary for table [hr].[jobs]"""

    query = 'SELECT * FROM [TRN].[hr].[jobs] WHERE min_salary > max_salary'
    cursor.execute(query)
    result = cursor.fetchall()
    assert result == []

