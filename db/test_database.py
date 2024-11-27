import pytest
from unittest.mock import MagicMock, patch
from db.database import Database

class TestDatabase:
    @pytest.fixture
    def mock_db_connection(self, mocker):
        # Mock the connection
        mock_connection = mocker.patch("mysql.connector.connect", autospec=True)
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{"id": 1, "name": "John Doe"}]
        mock_connection.return_value.cursor.return_value = mock_cursor
        return mock_connection

    def test_execute_query(self, mock_db_connection):
        # Initialize the Database with mocked connection
        db = Database("localhost", "root", "password", "test_db")

        # Test execute_query
        result = db.execute_query("SELECT * FROM students WHERE id = %s", (1,))
        assert result == [{"id": 1, "name": "John Doe"}]

        # Verify connection and cursor usage
        mock_db_connection.assert_called_once_with(
            host="localhost",
            user="root",
            password="password",
            database="test_db"
        )
        mock_db_connection.return_value.cursor.return_value.execute.assert_called_once_with(
            "SELECT * FROM students WHERE id = %s", (1,)
        )
        mock_db_connection.return_value.cursor.return_value.fetchall.assert_called_once()

    def test_close_connection(self, mock_db_connection):
        db = Database("localhost", "root", "password", "test_db")
        db.close_connection()
        mock_db_connection.return_value.close.assert_called_once()
