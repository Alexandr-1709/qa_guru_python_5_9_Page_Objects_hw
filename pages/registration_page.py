import os
from selene.support.shared import browser
from selene import have, command
from data.users import User


class RegistrationFormPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_form(self, student: User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)

        browser.element('#userEmail').type(student.email)

        browser.all('[name=gender]').element_by(have.value(f'{student.gender.Male.value}')).double_click()

        browser.element('#userNumber').type(student.phone_number)

        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__month-select').send_keys(student.birth_month)
        browser.element('.react-datepicker__year-select').send_keys(student.birth_year)
        browser.element(f'.react-datepicker__day--0{student.birth_day}').click()

        for subject in student.subjects:
            browser.element('#subjectsInput').type(subject.value).press_enter()

        for hobby in student.hobbies:
            browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(hobby.value)).click()

        browser.element('#uploadPicture').send_keys(os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.path.pardir, f'resourсes/{student.picture_file}')))

        browser.element('#currentAddress').type(student.address)

        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()

        browser.element('#react-select-4-input').type(student.city).press_enter()

        browser.element('#submit').press_enter()

    def should_registered_user_with(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        day_of_birth = f'{student.birth_day} {student.birth_month},{student.birth_year}'
        state_and_city = f'{student.state} {student.city}'
        subjects = ', '.join([subject.value for subject in student.subjects])
        hobbies = ', '.join([hobby.value for hobby in student.hobbies])
        browser.element('.table').all('td').even.should(have.texts(full_name,
                                                                   student.email,
                                                                   student.gender.Male.value,
                                                                   student.phone_number,
                                                                   day_of_birth,
                                                                   subjects,
                                                                   hobbies,
                                                                   student.picture_file,
                                                                   student.address,
                                                                   state_and_city
                                                                   )
                                                        )

    def close_submit_form(self):
        browser.element('#closeLargeModal').press_enter()
