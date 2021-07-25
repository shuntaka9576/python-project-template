import src.main


class TestClass(object):
    def test_get_articles(self, mocker) -> None:
        mock_get_articles_from_db = mocker.patch.object(
            src.main, "get_articles_from_db"
        )
        mock_get_articles_from_db.return_value = [
            {
                "title": "blog title",
                "user_id": "test_user_id",
                "extra_field1": "extra_field1_value",
                "extra_field2": "extra_field2_value",
            }
        ]

        article_list = src.main.get_articles("test_user_id")

        mock_get_articles_from_db.assert_called_once_with("test_user_id")
        assert article_list == [
            {
                "title": "blog title",
                "user_id": "test_user_id",
            }
        ]
