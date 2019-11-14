from datasette import hookimpl

import jinja2


@hookimpl
def extra_template_vars(datasette, database):
    async def execute_sql(sql, dbname=None):
        if dbname is None:
            dbname = database or next(iter(datasette.databases.keys()))
        return (await datasette.execute(dbname, sql)).rows

    return {"sql": execute_sql}
