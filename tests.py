# from hello import app
# with app.test_client() as c:
#     response = c.get('/')
#     assert response.data == b'Hello World!'
#     assert response.status_code == 200
    
def test_sum(self):
    assert self.simpleSum(1,2) == 3
    #assert sum([1,2,3]) == 6, "should be 6"

def test_sqlite3_demo(self):
    self.sqlDemoInit()
    self.sqlDemoAddData()
    assert self.sqlDemoReadback() == 2    