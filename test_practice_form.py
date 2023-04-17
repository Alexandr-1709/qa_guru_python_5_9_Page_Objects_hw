import os
from selene.support.shared import browser
from selene import have


def test_practice_form(browser_management):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Aleksandr')

    browser.element('#lastName').type('Nikiforov')

    browser.element('#userEmail').type('nikiforov@mail.ru')

    browser.element('#gender-radio-1[value=Male]').double_click()

    browser.element('#userNumber').type('9009997733')

    browser.element('#dateOfBirthInput').press()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1982"]').click()
    browser.element('.react-datepicker__day--017').click()

    browser.element('#subjectsInput').type("Computer Science").press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()


    browser.element('#uploadPicture').send_keys(os.getcwd() + "/test_5_5.jpg")

    browser.element('#currentAddress').type('Moscow, Vernadsky avenue,19')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').press_enter()

    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Aleksandr Nikiforov', 'Student Email nikiforov@mail.ru', 'Gender Male', 'Mobile 9009997733',
        'Date of Birth 17 September,1982', 'Subjects Computer Science', 'Hobbies Sports, Music',
        'Picture test_5_5.jpg', 'Address Moscow, Vernadsky avenue,19',
        'State and City NCR Delhi'))

    browser.element('#closeLargeModal').click()
