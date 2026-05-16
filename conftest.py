import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(page):
    return LoginPage(page) # can just return since we don't need to clean up anything

@pytest.fixture
def dashboard_page(page):
    dashboard_page = DashboardPage(page)
    yield dashboard_page # yield in case we fail so that we can clean up

    #cleanup
    dashboard_page.navigate()
    if dashboard_page.user_dropdown.is_visible():
        dashboard_page.logout()
        print("Log: Teardown wylogował użytkownika.")