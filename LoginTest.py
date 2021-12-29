from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\leoka\PycharmProjects\Rokomari_Automation\drivers\chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://www.rokomari.com")

        signin = LoginPage(driver)
        signin.click_signin()
        signin.enter_username("alkafi000@gmail.com")
        signin.enter_password("kafi12345")
        signin.click_login()
        signin.click_profile()
        signin.click_mylist()
        signin.click_create()
        signin.enter_title("My list")
        signin.enter_description("Science fiction")
        signin.enter_product("Time-Machine")
        #signin.click_select()
        #signin.click_save()
        signin.click_profile()
        signin.click_signout()
        signin.click_electronics()
        signin.click_stationaries()
        signin.click_gifts()
        signin.click_corporate()
        signin.click_offers()
        signin.click_blogs()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.signin_button_path = '//*[@id="js--main-header"]/div/div/div[3]/div/div[2]/a'
        self.username_textbox_path = '//*[@id="j_username"]'
        self.password_textbox_path = '//*[@id="j_password"]'
        self.loginin_button_path = '//*[@id="loginForm"]/button'
        self.profile_button_path = '//*[@id="dropdownMenu2"]'
        self.mylist_button_path = '//*[@id="js--main-header"]/div/div/div[3]/div/div[3]/div/a[3]'
        self.create_list_button_path = '//*[@id="my-account"]/div/div/div[2]/main/section/div[1]/a/button'
        self.title_list_textbox_path = '//*[@id="list_title"]'
        self.list_description_textbox_path = '//*[@id="my-account"]/div/div/div[2]/main/section/div[2]/form/div[4]/textarea'
        self.add_product_textbox_path = '//*[@id="products"]'
        #self.select_product_text_path = '//*[@id="ui-id-73"]'
        #self.save_list_button_path = '//*[@id="submit"]'
        self.profile_button_path = '//*[@id="dropdownMenu2"]'
        self.signout_button_path = '/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[7]'
        self.electronics_button_path = '/html/body/header/div/nav/div/div/ul/li[2]/a'
        self.stationaries_button_path = '/html/body/header/div/nav/div/div/ul/li[3]/a'
        self.gifts_button_path = '/html/body/header/div/nav/div/div/ul/li[4]/a'
        self.corporate_order_button_path = '/html/body/header/div[6]/div/div/div/ul/li[5]/a'
        self.offers_button_path = '/html/body/header/div[6]/div/div/div/ul/li[6]/a'
        self.blogs_button_path = '/html/body/header/div/nav/div/div/ul/li[7]/a'

    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_button_path).click()

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_path).clear()
        self.driver.find_element_by_xpath(self.username_textbox_path).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_path).clear()
        self.driver.find_element_by_xpath(self.password_textbox_path).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.loginin_button_path).click()

    def click_profile(self):
        self.driver.find_element_by_xpath(self.profile_button_path).click()

    def click_mylist(self):
        self.driver.find_element_by_xpath(self.mylist_button_path).click()

    def click_create(self):
        self.driver.find_element_by_xpath(self.create_list_button_path).click()

    def enter_title(self, title):
        self.driver.find_element_by_xpath(self.title_list_textbox_path).clear()
        self.driver.find_element_by_xpath(self.title_list_textbox_path).send_keys(title)

    def enter_description(self, description):
        self.driver.find_element_by_xpath(self.list_description_textbox_path).clear()
        self.driver.find_element_by_xpath(self.list_description_textbox_path).send_keys(description)

    def enter_product(self, product):
        self.driver.find_element_by_xpath(self.add_product_textbox_path).clear()
        self.driver.find_element_by_xpath(self.add_product_textbox_path).send_keys(product)
    #def click_select(self):
        #self.driver.find_element_by_xpath(self.select_product_text_path).click()

    #def click_save(self):
        #self.driver.find_element_by_xpath(self.save_list_button_path).click()
    def click_profile(self):
        self.driver.find_element_by_xpath(self.profile_button_path).click()

    def click_signout(self):
        self.driver.find_element_by_xpath(self.signout_button_path).click()

    def click_electronics(self):
        self.driver.find_element_by_xpath(self.electronics_button_path).click()

    def click_stationaries(self):
        self.driver.find_element_by_xpath(self.stationaries_button_path).click()

    def click_gifts(self):
        self.driver.find_element_by_xpath(self.gifts_button_path).click()

    def click_corporate(self):
        self.driver.find_element_by_xpath(self.corporate_order_button_path).click()

    def click_offers(self):
        self.driver.find_element_by_xpath(self.offers_button_path).click()

    def click_blogs(self):
        self.driver.find_element_by_xpath(self.blogs_button_path).click()



