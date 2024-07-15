import os
import pytest

PASSWORD = os.environ['PASSWORD']


@pytest.fixture()
def navigate_to_the_site(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    yield page
    page.close()
