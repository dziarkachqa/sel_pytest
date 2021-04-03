import pytest
from selenium import webdriver

@pytest.fixture
def open_browser():
    return webdriver.Chrome(executable_path='C:\\selenium\\chromedriver.exe')

@pytest.fixture
def open_browser2():
    return webdriver.Firefox(executable_path='C:\\selenium\\geckodriver.exe')

@pytest.fixture
def open_browser3():
    return webdriver.Edge(executable_path='C:\\selenium\\msedgedriver.exe')