import unittest
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class iFrameTestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        #options.add_argument('--headless')
        options.add_argument('user-agent=User-Agent: Chrome/89.0.4389.114')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.close()

    def test_something(self):
        strd = 'https://www.bing.com'
        to_check_result = 'bing.com/travelguide?q=Redmond'

        driver = self.driver
        driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="iframeResult"]'))

        element = driver.find_element_by_xpath('//iframe')
        driver.execute_script("arguments[0].setAttribute('src', arguments[1])", element, strd)
        driver.execute_script("arguments[0].setAttribute('height', arguments[1])", element, 2000)
        element.send_keys(Keys.ENTER)

        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/iframe'))

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="bLogo"]')))
        driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('Redmond')
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="sw_as"]')))

        for i in driver.find_elements_by_xpath('//li[@class="sa_sg"]'):
            if (i.text == 'redmond washington'):
                i.click()
                break

        first_search_link = driver.find_element_by_xpath('//*[contains(@href, "travelguide") and contains(text(), "Redmond")]')
        self.assertIn(to_check_result, first_search_link.get_attribute("href"))


if __name__ == '__main__':
    unittest.main()
