from pages.registration_page import RegistrationFormPage
from data.users import Hobby, Gender, User, Subject



def test_practice_form(browser_management):
    registration_page = RegistrationFormPage()

    student = User(
        first_name='Aleksandr',
        last_name='Nikiforov',
        email='nikiforov@mail.ru',
        gender=Gender.Male,
        phone_number='9009997733',
        birth_day= '17',
        birth_month='September',
        birth_year='1982',
        subjects=[Subject.computer_science],
        hobbies=[Hobby.sports, Hobby.music],
        picture_file='test_5_5.jpg',
        address='Moscow, Vernadsky avenue,19',
        state='NCR',
        city='Delhi',
    )

    registration_page.open()

    # WHEN
    registration_page.fill_form(student)

    # THEN
    registration_page.should_registered_user_with(student)

    registration_page.close_submit_form()
