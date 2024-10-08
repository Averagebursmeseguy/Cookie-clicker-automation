from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

buildings = {}
cookie_count = 0

driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

got_it_button = driver.find_element(by=By.CSS_SELECTOR, value=".cc_btn.cc_btn_accept_all")
got_it_button.click()

lang_choice_eng_button = driver.find_element(by=By.CSS_SELECTOR, value=".langSelectButton.title")
lang_choice_eng_button.click()
time.sleep(3)


class Building():  # class used to represent each purchased building
    def __init__(self, button, price, count, achievable, name):
        self.button = self.find_button(button)
        self.price = self.find_price(price)
        self.count = self.find_count(count)
        self.achievable = achievable
        self.name = self.find_name(name)

    def find_name(self, id_name):
        name = driver.find_element(by=By.ID, value=id_name)
        return name.text.lower()

    def find_price(self, target_id):
        raw_price = driver.find_element(by=By.ID, value=target_id).text.split(" ")
        try:
            prefix = int(raw_price[0].replace(",", ""))
        except:
            prefix = 0
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

    def find_button(self, target_id):
        button = driver.find_element(by=By.ID, value=target_id)
        return button


def refresh():  # makes building objects for iterating and to make automation easier
    for p in range(0, 19):

        new_building = Building(f"product{str(p)}", f"productPrice{str(p)}", f"productOwned{str(p)}", False,
                                f"productName{str(p)}")

        if new_building.button.get_attribute("class") == "product unlocked enabled":
            new_building.achievable = True

            if new_building.name not in buildings:
                buildings[f"{new_building.name}"] = new_building  # checks if name is already used as a dict key
            else:
                pass

        elif new_building.button.get_attribute("class") == "product unlocked disabled":
            new_building.achievable = False

        # print(f"{new_building.price}, {new_building.achievable}, {new_building.count}, {new_building.button}")

        # print(f"price = {new_building.price}")


def purchase(money):
    for name, building in buildings.items():

        if money > building.price:
            building.button.click()

        else:
            pass

        print(f"Purchased buildings:"
              f"{building.name}: {building.count}\n")



timer = time.time()

while True:
    cookie = driver.find_element(by=By.CSS_SELECTOR, value="#bigCookie")
    cookie.click()
    cookie_count = int(driver.find_element(by=By.ID, value="cookies").text.split(" ")[0])

    if int(time.time() - timer) == 5:
        refresh()
        purchase(cookie_count)

        timer = time.time()



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
