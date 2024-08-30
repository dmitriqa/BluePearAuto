from asyncio import timeout

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def test_authorization(driver):
    driver.get('https://app.bluepear.net/auth')
    field_email = driver.find_element(By.NAME, 'email')
    field_email.click()
    field_email.send_keys('dmitry.bovkunovich@bluepear.co')
    field_password = driver.find_element(By.NAME, 'password')
    field_password.click()
    field_password.send_keys('D9471166dklm')
    login_buttom = driver.find_element(By.XPATH, '//div[@class="mt-[16px] flex flex-col"]')
    login_buttom.click()
    logo = driver.find_element(By.XPATH, '//img[@class="cursor-pointer w-[111px]"]')
    assert logo.get_attribute('src') == 'https://app.bluepear.net/logo.svg'


def test_wrong_username(driver):
    driver.get('https://app.bluepear.net/auth')
    field_email = driver.find_element(By.NAME, 'email')
    field_email.click()
    field_email.send_keys('dmitry.bovkunovich@bluepear.c')
    field_password = driver.find_element(By.NAME, 'password')
    field_password.click()
    field_password.send_keys('D9471166dklm')
    login_buttom = driver.find_element(By.XPATH, '//div[@class="mt-[16px] flex flex-col"]')
    login_buttom.click()
    error_message = driver.find_element(By.XPATH, '//span[@class="flex-1 text-[13px] text-focus-500 leading-[24px]"]')
    assert error_message.is_displayed()

