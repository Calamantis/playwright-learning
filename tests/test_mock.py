def get_user_status(user_id, db_connection):
    status = db_connection.query_status(user_id)
    return f"User is {status}"


def test_get_user_status(mocker):
    # mocking the db connection and response
    mock_db = mocker.Mock() #case-sensitive lol
    mock_db.query_status.return_value = "Active"

    result = get_user_status(1, mock_db)

    assert result == "User is Active"
    mock_db.query_status.assert_called_once_with(1)