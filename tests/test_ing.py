# from hello import app
# with app.test_client() as c:
#     response = c.get('/')
#     assert response.data == b'Hello World!'
#     assert response.status_code == 200

import pytest
#tgt = __import__("hello.py")
#import hello.py
import hello

def test_sum():
    assert hello.simpleSum(1,2) == 3
    #assert sum([1,2,3]) == 6, "should be 6"

def test_sqlite3_demo():
    hello.sqlDemoInit()
    hello.sqlDemoAddData()
    result = hello.sqlDemoReadback()
    assert result == 55, "equal"