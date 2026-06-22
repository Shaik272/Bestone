from playwright.sync_api import Page, expect


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://parabank.parasoft.com/parabank/register.htm"
        self.first_name_input = page.locator('[id="customer.firstName"]')
        self.last_name_input = page.locator('[id="customer.lastName"]')
        self.address_input = page.locator('[id="customer.address.street"]')
        self.city_input = page.locator('[id="customer.address.city"]')
        self.state_input = page.locator('[id="customer.address.state"]')
        self.zip_code_input = page.locator('[id="customer.address.zipCode"]')
        self.phone_input = page.locator('[id="customer.phoneNumber"]')
        self.ssn_input = page.locator('[id="customer.ssn"]')
        self.username_input = page.locator('[id="customer.username"]')
        self.password_input = page.locator('[id="customer.password"]')
        self.confirm_password_input = page.locator('#repeatedPassword')
        self.register_button = page.get_by_role("button", name="Register")

    def open(self) -> None:
        self.page.goto(self.url)
        expect(self.page).to_have_url(self.url)

    def fill_valid_details(self) -> None:
        self.first_name_input.fill("shaik")
        self.last_name_input.fill("gouse")
        self.address_input.fill("LB NAGAR")
        self.city_input.fill("HYDERABAD")
        self.state_input.fill("TELANGANA")
        self.zip_code_input.fill("500026")
        self.phone_input.fill("9182611745")
        self.ssn_input.fill("258975621")
        self.username_input.fill("SHAIK")
        self.password_input.fill("Shaikgouse7225@")
        self.confirm_password_input.fill("Shaikgouse7225@")

    def submit(self) -> None:
        self.register_button.click()

    def has_validation_errors(self) -> bool:
        return self.page.locator('.error').count() > 0

