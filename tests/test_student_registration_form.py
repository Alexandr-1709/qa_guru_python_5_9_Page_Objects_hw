import os
from selene.support.shared import browser
from selene import have, command
from pages.registration_page import RegistrationFormPage


def test_practice_form(browser_management):
    registration_page = RegistrationFormPage()

    registration_page.open()

    # WHEN
    registration_page.fill_in_first_name('Aleksandr')
    registration_page.fill_in_last_name('Nikiforov')

    registration_page.fill_in_email('nikiforov@mail.ru')

    registration_page.select_gender('Male')

    browser.element('#userNumber').type('9009997733')

    registration_page.fill_in_date_of_birth('17', 'September', '1982')

    browser.element('#subjectsInput').type("Computer Science").press_enter()

    registration_page.select_hobby('Sports')
    registration_page.select_hobby('Music')

    registration_page.upload_picture_file('test_5_5.jpg')

    registration_page.fill_in_current_address('Moscow, Vernadsky avenue,19')

    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')

    registration_page.submit_form()

    # THEN
    registration_page.should_registered_user_with('Aleksandr Nikiforov',
                                                  'nikiforov@mail.ru',
                                                  'Male',
                                                  '9009997733',
                                                  '17 September,1982',
                                                  'Computer Science',
                                                  'Sports, Music',
                                                  'test_5_5.jpg',
                                                  'Moscow, Vernadsky avenue,19',
                                                  'NCR Delhi')

    registration_page.close_submit_form()
