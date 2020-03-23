##### IMPORTS ######
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Main Class
class LinkedinBot:

    # COnstructor Method
    def __init__(self, username, password):

        
        # Initialise : ChromeDriver , Base_Url , Login_Url and Feed_Url
        self.driver = webdriver.Chrome('chromedriver')
        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        # initialis credentials
        self.username = username
        self.password = password

    # Private Navigation Method
    def _nav(self, url):

        self.driver.get(url)
        time.sleep(3)

    # Login Methiod
    def login(self, username, password):

        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

        print("Logged In Successfully")

    # Posts Method
    def post(self, text):

        self.driver.find_element_by_class_name('share-box__open').click()
        self.driver.find_element_by_class_name('mentions-texteditor__content').send_keys(text)
        self.driver.find_element_by_class_name('share-actions__primary-action').click()

        print("Posted Successfully")
    
    # Connection Search Method
    def search(self, text, connect=False):

        self._nav(self.feed_url)

        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        
       
        time.sleep(3)

        print("Here Are The Search Results")

        if connect:

            self._send_invite()


    # Private methid to send invites to all on page
    def _send_invite(self):

        connect = self.driver.find_element_by_class_name('search-result__action-button')
        connect.click()
        time.sleep(2)

        self.driver.find_element_by_class_name('ml1').click()

        print("Invites Sent")


if __name__ == '__main__':

    username = ''
    password = ''
    post_text = ''
    search_text = ''

    linked_in_bot = LinkedinBot(username, password)
    linked_in_bot.login(username, password)
    linked_in_bot.post(post_text)
    linked_in_bot.search(search_text, connect=True)