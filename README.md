# datasette-template-sql

[![PyPI](https://img.shields.io/pypi/v/datasette-template-sql.svg)](https://pypi.org/project/datasette-template-sql/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-template-sql.svg?style=svg)](https://circleci.com/gh/simonw/datasette-template-sql)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-template-sql/blob/master/LICENSE)

Datasette plugin for executing SQL queries from templates.

This plugin makes a new function, `sql(sql_query)`, available to your Datasette templates.

You can use it like this:

```html+jinja
{% for row in sql("select 1 + 1 as two, 2 * 4 as eight") %}
    {% for key in row.keys() %}
        {{ key }}: {{ row[key] }}<br>
    {% endfor %}
{% endfor %}
```

The plugin will execute SQL against the current database for the page in  `database.html`, `table.html` and `row.html` templates. If a template does not have a current database (`index.html` for example) the query will execute against the first attached database.

You can pass an optional second argument to specify a named database to use for the query. For example, if you have attached a `news.db` database you could use this:

```html+jinja
{% for article in sql(
    "select headline, date, summary from articles order by date desc limit 5",
    "news"
) %}
    <h3>{{ article.headline }}</h2>
    <p class="date">{{ article.date }}</p>
    <p>{{ article.summary }}</p>
{% endfor %}
```
