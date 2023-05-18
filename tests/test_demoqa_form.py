import os
import allure
from selene import be, have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
 browser = setup_browser

 with allure.step("Open registrations form"):
     browser.open('https://demoqa.com/automation-practice-form')
     browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
     browser.driver.execute_script("$('#fixedban').remove()")

 with allure.step("Fill form"):
    browser.element("#firstName").type('Sherlock')
    browser.element("#lastName").type('Holmes')
    browser.element("#userEmail").type('HolmsTest@gmail.com')
    browser.element("[value=Male]").double_click()
    browser.element("#userNumber").type('8977777575')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker-popper').should(be.visible)
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1984"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="0"]').click()
    browser.element('.react-datepicker__day--006').should(
        have.attribute('aria-label', 'Choose Friday, January 6th, 1984')).click()
    browser.element('#dateOfBirthInput').should(have.value('06 Jan 1984'))
    browser.element("#subjectsInput").type('Maths').press_enter()
    browser.element("#subjectsInput").type('Eng').press_enter()
    browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
    #browser.element('#uploadPicture').send_keys(os.getcwd() + '/picture.jpg')
    browser.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.element('#currentAddress').type('221B Baker Street')
    browser.element('#state').click()
    browser.element('#react-select-3-input').set_value('NCR').press_tab()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.driver.execute_script("$('footer').remove()")
    browser.driver.execute_script("$('#submit').click()")

 with allure.step("Check form results"):
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts('Student Name Sherlock Holmes', 'Student Email HolmsTest@gmail.com',
                                                    'Gender Male', 'Mobile 8977777575',
                                                    'Date of Birth 06 January,1984', 'Subjects Maths, English',
                                                    'Hobbies Sports', 'Picture',
                                                    'Address 221B Baker Street', 'State and City NCR Delhi'))
    #browser.driver.execute_script("$('#closeLargeModal').click()")
