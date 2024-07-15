import os

import pytest
from playwright.sync_api import expect

from pom.login_page_elements import login_navigate_to_email_login, fill_login_credentials


@pytest.mark.smoke
@pytest.mark.regression
def test_login_positive_scenario(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    fill_login_credentials(page, "test.mkhlk@gmail.com", os.environ['PASSWORD'])
    page.get_by_test_id("submit").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()


@pytest.mark.regression
def test_login_negative_scenario_email(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    fill_login_credentials(page, "test.mkhlk@gmail", os.environ['PASSWORD'])
    page.get_by_test_id("submit").click()
    expect(page.get_by_test_id("siteMembers.inlineErrorMsg")).to_be_visible()


@pytest.mark.regression
def test_login_negative_scenario_password(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    fill_login_credentials(page, "test.mkhlk@gmail.com", "qwerty")
    page.get_by_test_id("submit").click()
    expect(page.get_by_test_id("siteMembers.inlineErrorMsg")).to_be_visible()


@pytest.mark.regression
def test_login_negative_scenario_short_password(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    fill_login_credentials(page, "test.mkhlk@gmail.com", "qwe")
    page.get_by_test_id("submit").click()
    expect(page.get_by_text("Passwords must be at least 4 characters long. Try again.")).to_be_visible()


@pytest.mark.regression
def test_login_negative_scenario_email_and_password(navigate_to_the_site):
    page = navigate_to_the_site
    login_navigate_to_email_login(page)
    fill_login_credentials(page, "test.mkhlkgmail.com", "qwe")
    page.get_by_test_id("submit").click()
    expect(page.get_by_text("Double check your email and try again.")).to_be_visible()
    expect(page.get_by_text("Passwords must be at least 4 characters long. Try again.")).to_be_visible()
