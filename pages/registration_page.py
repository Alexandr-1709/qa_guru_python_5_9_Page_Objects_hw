import os
from selene.support.shared import browser
from selene import have, command


class RegistrationFormPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_in_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_in_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_in_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(f'{value}')).double_click()

    def fill_in_phone_number(self, value):
        browser.element('#userNumber').type('9009997733')

    def fill_in_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_in_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    def upload_picture_file(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.path.pardir, f'resourсes/{value}')))

    def fill_in_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit_form(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))

    def close_submit_form(self):
        browser.element('#closeLargeModal').press_enter()

