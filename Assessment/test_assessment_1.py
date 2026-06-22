from pytest_bdd import given, scenario, then, when

from registration_page import RegistrationPage


@scenario("features/register.feature", "Registering with valid details")
def test_registering_with_valid_details():
    pass


@given("I am on the ParaBank registration page", target_fixture="registration_page")
def registration_page(browser_page):
    page = RegistrationPage(browser_page)
    page.open()
    return page


@when("I fill the registration form with valid details")
def fill_form(registration_page):
    registration_page.fill_valid_details()


@when("I submit the registration form")
def submit_form(registration_page):
    registration_page.submit()


@then("the registration page should not display validation errors")
def assert_no_validation_errors(registration_page):
    assert registration_page.has_validation_errors() is False


