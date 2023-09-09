from rest_framework.test import APISimpleTestCase


class TestFindSimilarApi(APISimpleTestCase):
    def setUp(self):
        self.valid_data = {
            "text_to_check": "one two",
            "texts": ["one", "two", "one two"],
            "language": "russian",
            "count": 10,
            # 'dictionary': {'some': 'analog'} https://github.com/findsimilar/find-similar/issues/7
        }
        self.response = self.client.post("/api/", data=self.valid_data)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response(self):
        expected_result = [
            {"text": "one two", "cos": "1.00"},
            {"text": "one", "cos": "0.71"},
            {"text": "two", "cos": "0.71"},
        ]
        self.assertEqual(self.response.json(), expected_result)


class TestDocsViews(APISimpleTestCase):
    def setUp(self) -> None:
        self.urls = ["/", "/swagger/", "/redoc/", "/swagger.json/", "/swagger.yaml/"]

    def test_health(self):
        for url in self.urls:
            with self.subTest(f"health: {url}"):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
