import httpx
import pathlib
import pytest
import re
import sqlite_utils
from datasette.app import Datasette


@pytest.fixture
def app(tmpdir):
    dogs = str(pathlib.Path(tmpdir / "dogs.db"))
    news = str(pathlib.Path(tmpdir / "news.db"))
    sqlite_utils.Database(dogs)["dogs"].insert_all([{"name": "Cleo"}])
    sqlite_utils.Database(news)["articles"].insert_all(
        [
            {"date": "2018-01-01", "headline": "First post"},
            {"date": "2018-02-01", "headline": "Post the second"},
        ]
    )
    ds = Datasette(
        [dogs, news],
        immutables=[],
        template_dir=str(pathlib.Path(__file__).parent / "test_templates"),
    )
    return ds.app()


@pytest.mark.asyncio
async def test_sql_against_named_database(app):
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/news")
        stripped = re.sub(r"\s+", " ", response.text)
        assert (
            '<h3>Post the second</h2> <p class="date">2018-02-01</p> '
            '<h3>First post</h2> <p class="date">2018-01-01</p>'
        ) in stripped


@pytest.mark.asyncio
async def test_sql_against_default_database(app):
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/")
        stripped = re.sub(r"\s+", " ", response.text)
        assert "<pre> type: table<br> name: dogs<br> </pre>" in stripped
