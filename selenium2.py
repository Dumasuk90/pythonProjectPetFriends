import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()

def test_selenium2(driver):
        driver.find_element(By.ID, 'email').send_keys('dimasiks5700@gmail.com')
        driver.find_element(By.ID, 'pass').send_keys('Dumasuk0209')
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        assert driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'

        images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        names = driver.find_elements(By.CSS_SELECTOR, '.card-desk .card-title')
        descriptions = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-text')

        for i in range(len(names)):
            assert images[i].get_attribute('src') is not None and images[i].get_attribute('src') != ''
            assert names[i].text !=''
            assert descriptions[i].text !=''
            assert ', ' in descriptions[i]
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
