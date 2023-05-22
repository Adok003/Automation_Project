from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time


driver = webdriver.Chrome()
driver.get('https://evrika.com/catalog/smartfon-iphone-14-plus-128gb-starlight/p34697')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/div[10]/div/div[3]/button[1]').click()
driver.implicitly_wait(10)


def test_choose_color():
    choose_color = driver.find_element(By.XPATH,
                                       '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div[4]/div[1]/div[1]/ul/li[5]/label/img')
    choose_color.click()
    time.sleep(5)

    assert 'Purple' in driver.title


def test_memory_type():
    choose_memory_type = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div[4]/div[1]/div[2]/ul/li[2]/label/span')
    choose_memory_type.click()
    time.sleep(5)

    assert '256gb' in driver.current_url


def test_click_review():
    ActionChains(driver).scroll_by_amount(0, 600).perform()
    driver.implicitly_wait(10)

    review = driver.find_element(By.XPATH, '//*[@id="product-tabs"]/div[1]/div/ul/li[3]/div/span')
    review.click()
    time.sleep(5)

    assert 'reviews' in driver.current_url


def test_put_stars():
    driver.find_element(By.XPATH, '//*[@id="product-tabs"]/div[5]/div/div/div[2]/div[1]/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/form/div[1]/div/div/div[2]/label[1]').click()
    time.sleep(5)

    assert True


def test_write_data():
    name = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/form/div[2]/div[1]/input')
    name.send_keys("qwerty", Keys.TAB)
    driver.implicitly_wait(10)

    email = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/form/div[2]/div[2]/input')
    email.send_keys("qwerty@qwe.qwe", Keys.TAB)
    driver.implicitly_wait(10)

    assert True


def test_provide_feedback():
    message = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/form/div[3]/textarea')
    message.send_keys('qwerty')
    time.sleep(5)

    button = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/form/div[5]/button')
    test_text = button.text
    button.click()
    time.sleep(6)

    assert test_text == 'Оставить отзыв'


def test_add_to_basket():
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div[1]/button').click()
    basket = driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div[1]/button/span').text
    time.sleep(5)

    assert basket == 'Купить'


def test_go_to_basket():
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div[1]/button').click()
    time.sleep(5)

    assert 'Корзина' in driver.title


def test_place_an_order():
    place_an_order = driver.find_element(By.LINK_TEXT, 'Оформить заказ')
    place_an_order.click()
    time.sleep(5)

    assert 'checkout' in driver.current_url


def test_write_name():
    ActionChains(driver).scroll_by_amount(0, 200).perform()
    time.sleep(5)

    write_name = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div/input')
    write_name.send_keys("qwerty", Keys.TAB)
    driver.implicitly_wait(10)

    write_surname = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/div/input')
    write_surname.send_keys("asdfgh", Keys.TAB)
    driver.implicitly_wait(10)

    write_phone = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[3]/div/input')
    write_phone.send_keys("7087777777", Keys.TAB)
    driver.implicitly_wait(10)

    write_email = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[4]/div/input')
    write_email.send_keys("qwerty@qwe.qwe")
    time.sleep(5)

    assert True


def test_choose_courier():
    ActionChains(driver).scroll_by_amount(0, 300).perform()
    time.sleep(5)

    shipping = driver.find_element(By.XPATH,
                                   '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/label/span[1]/span[1]')
    shipping.click()
    time.sleep(5)

    assert shipping.text == 'Доставка курьером'


def test_choose_city():
    ActionChains(driver).scroll_by_amount(0, 300).perform()
    time.sleep(5)

    driver.find_element(By.XPATH,
                        '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]').click()
    choose_city = driver.find_element(By.XPATH,
                                      '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/ul/li[2]')
    test_text = choose_city.text
    choose_city.click()
    time.sleep(5)

    assert test_text == 'Алматы, Каскелен'


def test_choose_address():
    address = "Алтын ауыл"
    home = "2"
    home_number = "24"
    choose_address = driver.find_element(By.XPATH,
                                         '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/input')
    choose_address.send_keys(address)
    driver.implicitly_wait(10)

    choose_home = driver.find_element(By.XPATH,
                                      '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/input')
    choose_home.send_keys(home)
    driver.implicitly_wait(10)

    choose_home_number = driver.find_element(By.XPATH,
                                             '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/input')
    choose_home_number.send_keys(home_number)
    time.sleep(5)

    test_text = f"{address} {home}/{home_number}"

    assert test_text == 'Алтын ауыл 2/24'


def test_choose_time():
    driver.find_element(By.XPATH,
                        '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div/div/div[1]/div/div/input').click()
    choose_date = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div/span[23]')
    choose_date.click()
    time.sleep(5)

    choose_time = driver.find_element(By.XPATH,
                                      '//*[@id="checkout-form"]/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[1]/button')
    times = choose_time.text
    choose_time.click()
    time.sleep(5)

    assert f'{times}' == '12:00 - 18:00'


def test_choose_payments():
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    time.sleep(5)

    choose_payments = driver.find_element(By.XPATH,
                                          '//*[@id="checkout-form"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/label/span[1]/span[1]')
    choose_payments.click()
    time.sleep(5)

    assert choose_payments.text == 'Наличными или картой'


def test_add_comment():
    driver.find_element(By.XPATH, '//*[@id="checkout-form"]/div/div[2]/div[3]/div[2]/button').click()
    comment = "Thanks for service"
    add_comment = driver.find_element(By.XPATH, '//*[@id="checkout-form"]/div/div[2]/div[3]/div[2]/div[2]/textarea')
    add_comment.send_keys(comment)
    time.sleep(5)

    assert True
