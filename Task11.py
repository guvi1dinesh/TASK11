## USING PYTHON SELENIUM AUTOMATION AND ACTIONS CHAINS VISIT THE URL:https://jqueryui.com/droppable/
# AND DO DRAG AND DROP OPERATION OF WHITE RECTANGULAR BOX INTO THE YELLOW RECTANGULAR BOX:-




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class ActionChainsDragExample:
    url = 'https://jqueryui.com/droppable/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)
    driver.get(url)

    stage_1 = 'draggable'
    stage_2 = 'droppable'

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def drag_drop(self):
        sleep(5)
        self.driver.switch_to.frame(self.driver.find_element(by=By.CLASS_NAME,value="demo-frame"))
        source_1_web = self.driver.find_element(by=By.ID, value=self.stage_1)
        target_1_web = self.driver.find_element(by=By.ID, value=self.stage_2)

        self.action.drag_and_drop(source_1_web, target_1_web).perform()
        sleep(9)


Output = ActionChainsDragExample()
Output.browsing()
Output.drag_drop()



