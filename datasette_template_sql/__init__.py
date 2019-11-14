from datasette import hookimpl


@hookimpl
def extra_template_vars(datasette, database):
    async def execute_sql(sql, dbname=None):
        dbname = dbname or database or next(iter(datasette.databases.keys()))
        return (await datasette.execute(dbname, sql)).rows

    return {"sql": execute_sql}
