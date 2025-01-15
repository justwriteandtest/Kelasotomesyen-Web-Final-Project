from selenium.webdriver.common.by import By
from selenium import webdriver

class Component:
    def __init__(self, driver : webdriver.Chrome | webdriver.Firefox | webdriver.Edge | webdriver.Safari):
        self.driver = driver
    