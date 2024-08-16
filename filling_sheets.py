from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

class FillingForms:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Firefox(service=self.service)
        
    def sending_data(self, home_links:list, home_prices:list, home_addresses:list):
        for n in range(len(home_links)):
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSft3x6h0EcM75wzH9lOXP9URfn4g6BIXu7jf3HCzWscE8Vi8g/viewform")

            time.sleep(3)

            first_input = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")


            second_input = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

            third_input = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

            submit_btn = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
            
            first_input.send_keys(home_addresses[n])
            second_input.send_keys(home_prices[n])
            third_input.send_keys(home_links[n])
            submit_btn.click()
            