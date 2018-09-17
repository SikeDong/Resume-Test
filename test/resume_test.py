import unittest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

class ResumeTestCase(unittest.TestCase):
    def setUp(self):
        driver.get("http://localhost:8000")

    def tearDown(self):
        driver.close()
        pass

    def xtest_name_should_exist(self):
        name_text = driver.find_element_by_css_selector('.title h1').text
        assert name_text == 'Sike Dong (Christina)', "can't find name text"

    def test__title_should_exist(self):
        education_text = driver.find_element_by_css_selector('.educations h3').text
        assert education_text == 'EDUCATION', "can't find education text"
        
        skill_text = driver.find_element_by_css_selector('.skills h3').text
        assert skill_text == 'SKILLS & ACTIVITIES', "can't find skill text"
            
        experience_text = driver.find_element_by_css_selector('.experience h3').text
        assert experience_text == 'EXPERIENCE', "can't find experience text"
               
        project_text = driver.find_element_by_css_selector('.projects h3').text
        assert project_text == 'ACADEMIC PROJECTS', "can't find project text"

    def xtest_education_number(self):
        education_number = len(driver.find_elements_by_css_selector('.educations h5'))
        assert education_number >= 2, "can't find all educations"

if __name__ == "__main__":
    unittest.main() # run all tests