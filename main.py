from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

buildings = []

driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

got_it_button = driver.find_element(by=By.CSS_SELECTOR, value=".cc_btn.cc_btn_accept_all")
got_it_button.click()

lang_choice_eng_button = driver.find_element(by=By.CSS_SELECTOR, value=".langSelectButton.title")
lang_choice_eng_button.click()
time.sleep(3)


class Building():
    def __init__(self, button, price, count):
        self.button = self.button(button)
        self.price = self.find_price(price)
        self.count = self.find_count(count)

    def find_price(self, target_id):
        raw_price = driver.find_element(by=By.ID, value=target_id).text.split(" ")
        prefix = int(raw_price[0].replace(",", ""))
        suffix = raw_price[-1]
        actual_price = 0

        magnitudes = {
            "million": 10 ** 6,
            "billion": 10 ** 9,
            "trillion": 10 ** 12,
            "quadrillion": 10 ** 15,
            "quintillion": 10 ** 18,
            "sextillion": 10 ** 21,
            "septillion": 10 ** 24,
            "octillion": 10 ** 27,
            "nonillion": 10 ** 30,
            "undecillion": 10 ** 33,
            "duodecillion": 10 ** 36,
            "Tredecillion": 10 ** 42,
            "quattuordecillion": 10 ** 45,
            "quindecillion": 10 ** 48,
            "sexdecillion": 10 ** 51

        }

        if suffix in magnitudes:
            actual_price = prefix * magnitudes[suffix]
        elif suffix not in magnitudes:
            actual_price = prefix
        return actual_price

    def find_count(self, target_id):
        raw_count = driver.find_element(by=By.ID, value=target_id).text

        if raw_count == "":
            actual_count = 0
        else:
            actual_count = int(raw_count)

        return actual_count

    def button(self, target_id):
        button = driver.find_element(by=By.ID, value=target_id)
        return button


def load():
    for i in range(0, 19):

        try:
            new_building = Building(f"product{str(i)}", f"productPrice{str(i)}", f"productOwned{str(i)}")
            buildings.append(new_building)
            print(f"price = {new_building.price}")

        except:
            print(Exception)

for i in range(150):
    cookie = driver.find_element(by=By.CSS_SELECTOR, value="#bigCookie")
    cookie.click()
    cookie_count = int(driver.find_element(by=By.ID, value="cookies").text.split(" ")[0])
    print(cookie_count)
    if cookie_count > 100:
        load()

# while True:
#     cookie = driver.find_element(by=By.CSS_SELECTOR, value="#bigCookie")
#     cookie.click()
#     cookie_count = int(driver.find_element(By.ID, value="cookies").text.split()[0].replace(",", ""))
#
#     cursor = driver.find_element(by=By.ID, value="product0")
#     cursor.click()
#
#     building = Building("product0", "productPrice0", "productOwned0")
#     print(f"price:{building.price}, count:{building.count}")
