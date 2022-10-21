# from hello import app
# with app.test_client() as c:
#     response = c.get('/')
#     assert response.data == b'Hello World!'
#     assert response.status_code == 200

import pytest
import python-flask/hello  

def test_sum(self):
    assert self.simpleSum(1,2) == 4
    #assert sum([1,2,3]) == 6, "should be 6"

def test_sqlite3_demo(self):
    hello.sqlDemoInit()
    hello.sqlDemoAddData()
    result = hello.sqlDemoReadback()
    assert result == 6, "equal"