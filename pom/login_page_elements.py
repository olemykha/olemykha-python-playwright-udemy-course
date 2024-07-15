def navigate_to_email_login(page):
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()


def fill_login_credentials(page, email, password):
    page.fill('input:below(:text("Email"))', email)
    page.fill('input:below(:text("Password"))', password)


def navigate_to_forgot_password(page):
    page.get_by_test_id("forgotPasswordDesktop").click()
    page.get_by_test_id("siteMembers.container").get_by_label("Email").click()
