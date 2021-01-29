from setuptools import setup
import os

VERSION = "1.0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-template-sql",
    description="Datasette plugin for executing SQL queries from templates",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-template-sql",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-template-sql/issues",
        "CI": "https://github.com/simonw/datasette-template-sql/actions",
        "Changelog": "https://github.com/simonw/datasette-template-sql/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_template_sql"],
    entry_points={"datasette": ["template-sql = datasette_template_sql"]},
    install_requires=["datasette>=0.54"],
    extras_require={"test": ["pytest", "pytest-asyncio", "sqlite-utils"]},
    tests_require=["datasette-template-sql[test]"],
    python_requires=">=3.6",
)
