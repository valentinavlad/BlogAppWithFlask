import pytest

class TestFlaskr():
    """description of class"""
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

