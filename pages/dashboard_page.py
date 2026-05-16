class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-name")
        self.logout_link = page.get_by_role("menuitem", name="Logout")
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def logout(self):
        self.user_dropdown.click()
        self.logout_link.click()