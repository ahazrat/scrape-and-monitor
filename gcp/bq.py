from google.cloud import bigquery

client = bigquery.Client()


def test_query():
    # Construct a BigQuery client object


    query = """
    select
        name,
        sum(number) as total_people
    from
        `bigquery-public-data.usa_names.usa_1910_2013`
    where
        state = 'TX'
    group by
        name, state
    order by
        total_people desc
    limit
        20
    """
    query_results = client.query(query)  # Make an API request

    print('Query results:')
    for row in query_results:
        # Row values can be accessed by field name or index
        print(f'name={row[0]}, count={row["total_people"]}')


def get_projects():
    projects = client.list_projects()
    for project in projects:
        print(project.__dict__)
    return projects


def get_tables():
    """Returns currently available tables in GCP BQ"""
    tables = []
    return tables


def insert_records(project_name: str, dataset_name: str, table_name: str, insert_rows: list):
    table_id = f'{project_name}.{dataset_name}.{table_name}'
    print(f'Inserting {len(insert_rows)} into {table_id}')

    # todo use pandas.DataFrame -> dict records
    if table_id == 'crypto-frontend.coinbase.test_table':
        rows_to_insert = [{
            'time': r[0],
            'low': r[1],
            'high': r[2],
            'open': r[3],
            'close': r[4],
            'volume': r[5],
        } for r in insert_rows]
        for r in rows_to_insert[:5]:
            print(r)
        errors = client.insert_rows_json(table_id, rows_to_insert)
        if not errors:
            print('New rows have been added.')
        else:
            print(f'Encountered errors while inserting rows: {errors}')
