from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login("Admin", "admin123")

    expect(dashboard_page.dashboard_header).to_be_visible()

def test_logout_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login("Admin", "admin123")

    dashboard_page.logout()

    expect(login_page.login_button).to_be_visible()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")