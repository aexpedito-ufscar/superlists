from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_assert_new_priority_item(self):
        # Inicia nova lista
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Comprar anzol')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Comprar anzol - Prioridade Alta')

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Comprar cola instantanea')
        priority = self.browser.find_element(By.ID, 'priority')
        priority.send_keys('Baixa')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('2: Comprar cola instantanea - Prioridade Baixa')



    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if ((time.time() - start_time) > MAX_WAIT):
                    raise e
                time.sleep(0.5)