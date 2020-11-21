import pytest

from handlers.code_format import CodeFormatReminder
from tests.utils import create_message


@pytest.fixture
def handler():
    return CodeFormatReminder()


def test_python_function(handler):
    response = handler.handle(create_message("Here is a function(a, b)"), intent={})
    assert response is not None


def test_sql_query(handler):
    response = handler.handle(create_message("My solution is SELECT * FROM table;"), intent={})
    assert response is not None


def test_r_assignment(handler):
    response = handler.handle(create_message("my.var <- c(123,456)"), intent={})
    assert response is not None


def test_ignore_parens(handler):
    response = handler.handle(create_message("This is ok (i think)"), intent={})
    assert response is None

