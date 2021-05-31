from selenium import webdriver
from selenium.webdriver.common.keys import keys


deriver_path = r'/home/gilas/selenium'

options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

deriver = webdriver.Chrome(deriver_path, chrome_options=options)
deriver.get('https://google.com')