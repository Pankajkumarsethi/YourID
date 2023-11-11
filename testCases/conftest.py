import pytest
from selenium import webdriver



@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    # options = Options()
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--ignore-certificate-errors')
    #
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver.implicitly_wait(10)

    return driver
