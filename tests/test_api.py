import pytest
from playwright.sync_api import Playwright, APIRequestContext, expect

# no token

def test_api_get(api_request_context: APIRequestContext):
    response = api_request_context.get("https://jsonplaceholder.typicode.com/posts/1")

    #assert response.ok
    assert response.status == 200
    response_body = response.json()
    assert response_body["id"] == 1
    print("Finished")

def test_api_delete(api_request_context: APIRequestContext):
    response = api_request_context.delete("https://jsonplaceholder.typicode.com/posts/1")

    #assert response.status == 204
    assert response.status == 200 # server returns 200
    response_body = response.json()
    print("RES_BODY:",response_body)

# with token

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "TOKEN",
        "X-api-key": "free_user_3DrbRdS9HQUTOAEk40o6LM2lpDY"
    }
    request_context = playwright.request.new_context(
        base_url="https://reqres.in", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()

def test_get_user_details(api_request_context: APIRequestContext):
    response = api_request_context.get("/api/users/2")

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    #print(response_body)
    assert response_body["data"]["email"] == "janet.weaver@reqres.in"

def test_create_user(api_request_context: APIRequestContext):
    user_data = {
        "name": "Yan",
        "job": "Engineer"
    }
    response = api_request_context.post("/api/users", data=user_data)

    assert response.status == 201
    assert response.json()["name"] == "Yan"
    assert response.json()["job"] == "Engineer"