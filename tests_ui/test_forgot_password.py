import pytest
from playwright.sync_api import expect

from pom.login_page_elements import login_navigate_to_email_login, login_navigate_to_forgot_password


@pytest.mark.smoke
@pytest.mark.regression
def test_reset_password_positive_scenario(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    login_navigate_to_forgot_password(page)
    expect(page.get_by_text("Enter your login email and we’ll send you a link to reset your password.")).to_be_visible()
    page.get_by_test_id("siteMembers.container").get_by_label("Email").click()
    page.get_by_test_id("siteMembers.container").get_by_label("Email").fill("test.mkhlk@gmail.com")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    expect(page.get_by_text("Reset password link was sent")).to_be_visible()


@pytest.mark.regression
def test_reset_password_empty_filed(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    login_navigate_to_forgot_password(page)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    expect(page.get_by_text("Email cannot be blank")).to_be_visible()


@pytest.mark.regression
def test_reset_password_without_domen(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    login_navigate_to_forgot_password(page)
    page.get_by_test_id("siteMembers.container").get_by_label("Email").fill("test.mkhlk@gmail")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    expect(page.get_by_text("Double check your email and try again.")).to_be_visible()


@pytest.mark.regression
def test_reset_password_non_existent_account(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    login_navigate_to_forgot_password(page)
    page.get_by_test_id("siteMembers.container").get_by_label("Email").fill("qweqweqfcvs123123dv@gmail.com")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    expect(page.get_by_text("This email doesn't match any account. Try again.")).to_be_visible()
