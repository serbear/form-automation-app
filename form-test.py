from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

use_step_matcher("re")

# todo: check if an element not found.
# todo: wait for page loading.


@given("Users launch the browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver = webdriver.Firefox()


@when("Users open form webpage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = (
        f"https://www.tutorialspoint.com/selenium/practice/"
        f"selenium_automation_practice.php"
    )

    context.driver.get(url)


@then("User enter Name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    name_field = context.driver.find_element(By.NAME, "name")
    name_field.clear()
    name_field.send_keys("Sergei Markov")


@step("User enter Email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email_field = context.driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys("markov@emai.com")


@step("User choose a gender")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    xpath_male = "//input[@type='radio' and following-sibling::label[text()='Male']]"

    # Select male gender.
    context.driver.find_element(By.XPATH, xpath_male).click()


@step("User enter Mobile phone number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    mobile_field = context.driver.find_element(By.NAME, "mobile")
    mobile_field.clear()
    mobile_field.send_keys("1234567890")


@step("User enter date of birth")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    dob_field = context.driver.find_element(By.NAME, "dob")
    dob_field.clear()
    dob_field.send_keys("1982-01-22")


@step("User enter subjects")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    subjects_field = context.driver.find_element(By.NAME, "subjects")
    subjects_field.clear()
    subjects_field.send_keys("Math, Programming, Literature")


@step("User choose hobbies")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sports_xpath = "/html/body/main/div/div/div[2]/form/div[7]/div/div/div[1]/input"
    reading_xpath = "/html/body/main/div/div/div[2]/form/div[7]/div/div/div[2]/input"
    music_xpath = "/html/body/main/div/div/div[2]/form/div[7]/div/div/div[3]/input"

    context.driver.find_element(By.XPATH, sports_xpath).click()
    context.driver.find_element(By.XPATH, reading_xpath).click()
    context.driver.find_element(By.XPATH, music_xpath).click()


@step("User enters current address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    address_xpath = "//*[@placeholder='Currend Address']"
    address_field = context.driver.find_element(By.XPATH, address_xpath)
    address_field.clear()
    address_field.send_keys("My current address")


@step("User choose a state")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    state_field = Select(context.driver.find_element(By.NAME, "state"))
    state_field.select_by_value("Rajasthan")


@step("User choose a city")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    state_field = Select(context.driver.find_element(By.NAME, "city"))
    state_field.select_by_value("Lucknow")


@step("User click the button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    xpath = "//input[@type='submit']"
    submit_button = context.driver.find_element(By.XPATH, xpath)
    submit_button.click()

    context.driver.quit()


@step("User choose picture")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    picture_field = context.driver.find_element(By.NAME, "picture")
    picture_field.clear()
    picture_field.send_keys("/home/sergei/Pictures/Icons/tux.png")
