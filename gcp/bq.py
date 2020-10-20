from google.cloud import bigquery


def test_query():
    # Construct a BigQuery client object
    client = bigquery.Client()

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


def get_tables():
    """Returns currently available tables in GCP BQ"""
    tables = []
    return tables