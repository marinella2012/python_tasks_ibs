# 1. Открыть страницу http://google.com/ncr
# 2. Выполнить поиск слова 'selenide'
# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
# 4. Перейти в раздел поиска изображений
# 5. Проверить, что первое изображение неким образом связано с сайтом
# selenide.org.
# 6. Вернуться в раздел поиска Все
# 7. Проверить, что первый результат такой же, как и на шаге 3.
# Если с гуглом будут проблемы, можно выбрать любой другой поисковик.
# Браузер - по своему выбору. Стандартно
# селениум разработан под Firefox, но также стабильно работает по Chrome.
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://google.com/ncr')

    def test_search(self):
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        elm = self.drv.find_element_by_css_selector(
            '#rso > div:first-child a cite').text
        assert elm in 'https://selenide.org'
        time.sleep(2)
        links = self.drv.find_elements_by_class_name('hdtb-mitem')
        for i in links:
            if i.text == 'Images':
                assert i.text == 'Images'
                i.click()
                break
        time.sleep(2)
        first_link_in_images = self.drv.find_elements_by_class_name(
            'fxgdke')[0].text
        assert 'selenide.org' in first_link_in_images
        time.sleep(2)
        all_link = self.drv.find_elements_by_class_name('NZmxZe')[0]
        assert all_link.text == 'Все'
        all_link.click()
        time.sleep(2)
        first_link = self.drv.find_element_by_css_selector(
            '#rso > div:first-child a cite').text
        assert 'selenide.org' in first_link
        assert 'No result found' not in self.drv.page_source

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
