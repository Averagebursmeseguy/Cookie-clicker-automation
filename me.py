# from pynput.mouse import Button, Controller
# import time
#
# mouse = Controller()
#
# time.sleep(3)
#
# for i in range(100000):
#     mouse.click(Button.left, 1)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
#
# driver.get(url="https://orteil.dashnet.org/cookieclicker/")
# time.sleep(5)
#
# got_it_button = driver.find_element(by=By.CSS_SELECTOR, value=".cc_btn.cc_btn_accept_all")
# got_it_button.click()
#
# lang_choice_eng_button = driver.find_element(by=By.CSS_SELECTOR, value=".langSelectButton.title")
# lang_choice_eng_button.click()
# time.sleep(3)
#
#
# def find_price(id):
#     raw_price = driver.find_element(by=By.ID, value=id).text.split(" ")
#     print(raw_price)
# find_price("productPrice0")
#
# magnitudes = {
#     "million": 10 ** 6,
#     "billion": 10 ** 9,
#     "trillion": 10 ** 12,
#     "quadrillion": 10 ** 15,
#     "quintillion": 10 ** 18,
#     "sextillion": 10 ** 21,
#     "septillion": 10 ** 24,
#     "octillion": 10 ** 27,
#     "nonillion": 10 ** 30,
#     "undecillion": 10 ** 33,
#     "duodecillion": 10 ** 36,
#     "Tredecillion": 10 ** 42,
#     "quattuordecillion": 10 ** 45,
#     "quindecillion": 10 ** 48,
#     "sexdecillion": 10 ** 51
#
# }
#
# bob = [10, "trillion"]
#
# if bob[-1] in magnitudes:
#     print(bob[0]*magnitudes[bob[-1]])


import time

start = time.time()

while True:

    print(f"{int(time.time())-start}")
    start = int(time.time())
    time.sleep(2)

