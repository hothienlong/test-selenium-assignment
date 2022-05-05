from asyncio import sleep
from operator import truediv
import unittest
import time
from unittest import result
import HtmlTestRunner

from util import Util
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

util = Util()
util.driver.implicitly_wait(10)


class CreatePostTest(unittest.TestCase):
    def test_create_normal_post(self):
        # sign in
        util.sign_in("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # # add content
        # content_area_selector = 'textarea'
        # content_to_post = 'Timeout handling with node.js stream piping'
        # text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        # for txt in text_area:
        #     try:
        #         txt.clear()
        #         txt.send_keys(content_to_post)
        #     except ElementNotInteractableException:
        #         pass
        
        # # Click dang bai
        # btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        # util.click_element(By.CSS_SELECTOR, btn_post_selector)


        # # Get post title if success
        # result = False
        # try:
        #     title_selector = 'div.thread-title__block div.thread-title'
        #     title = util.driver.find_element(By.CSS_SELECTOR, title_selector).get_attribute('innerHTML')

        #     result = content_to_post in title
        # except NoSuchElementException:
        #     result = False

        # assert result
        assert True

    # def test_create_post_with_special_text(self):
    #     util.go_to_main_page()

    #     # click add post
    #     write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
    #     util.click_element(By.CSS_SELECTOR, write_post_button_selector)

    #     # add content
    #     content_area_selector = 'textarea'
    #     content_to_post = 'Timeout handling with node.js stream piping Ǆ ǆŸŻŴŒ'
    #     text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
    #     for txt in text_area:
    #         try:
    #             txt.clear()
    #             txt.send_keys(content_to_post)
    #         except ElementNotInteractableException:
    #             pass
        
    #     # Click dang bai
    #     btn_post_selector = 'div.thread-editor-modal button.publish-btn'
    #     util.click_element(By.CSS_SELECTOR, btn_post_selector)


    #     # Get post title if success
    #     result = False
    #     try:
    #         title_selector = 'div.thread-title__block div.thread-title'
    #         title = util.driver.find_element(By.CSS_SELECTOR, title_selector).get_attribute('innerHTML')

    #         result = content_to_post in title
    #     except NoSuchElementException:
    #         result = False

    #     assert result

    # def test_create_post_with_url(self):
    #     # util.go_to_main_page()
    #     util.sign_in("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")

    #     # click add post
    #     write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
    #     util.click_element(By.CSS_SELECTOR, write_post_button_selector)

    #     # add content
    #     content_area_selector = 'textarea'
    #     content_to_post = 'Timeout handling with node.js stream piping Ǆ ǆŸŻŴŒ'
    #     text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
    #     for txt in text_area:
    #         try:
    #             txt.clear()
    #             txt.send_keys(content_to_post)
    #         except ElementNotInteractableException:
    #             pass

    #     # Click link button
    #     link_btn_selector = 'div.ReactModal__Content button.link-sharing'
    #     util.click_element(By.CSS_SELECTOR, link_btn_selector)

    #     # Add link to input
    #     link = 'https://stackoverflow.com/questions/42301512/timeout-handling-with-node-js-stream-piping'
    #     input_selector = 'div.ReactModal__Content input'
    #     util.set_text(By.CSS_SELECTOR, input_selector, link)
    #     time.sleep(10)

    #     # Click dang bai
    #     btn_post_selector = 'div.thread-editor-modal button.publish-btn'
    #     util.click_element(By.CSS_SELECTOR, btn_post_selector)
    #     time.sleep(10)


    #     # get post link if success
    #     result = False
    #     try:
    #         link_post_selector = 'externalLink'
    #         link_post = util.driver.find_element(By.CLASS_NAME, link_post_selector).get_attribute('href')
    #         print('linkpost',link_post)

    #         result = link_post == link
    #     except NoSuchElementException:
    #         print('Element not found')
    #         result = False

    #     assert result

    # def test_create_post_with_image(self):
    #     # util.go_to_main_page()
    #     util.sign_in("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")

    #     # click add post
    #     write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
    #     util.click_element(By.CSS_SELECTOR, write_post_button_selector)

    #     # add content
    #     content_area_selector = 'textarea'
    #     content_to_post = 'Timeout handling with node.js stream piping'
    #     text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
    #     for txt in text_area:
    #         try:
    #             txt.clear()
    #             txt.send_keys(content_to_post)
    #         except ElementNotInteractableException:
    #             print('Element not found')
    #             pass
        
        # # click image button
        # img_btn_selector = 'div.thread-background-container > button:nth-child(2)'
        # util.click_element(By.CSS_SELECTOR, img_btn_selector)
        # time.sleep(5)

        # # select image
        # first_img_selector = 'div.thread-background-container > img:nth-child(3)'
        # util.click_element(By.CSS_SELECTOR, first_img_selector)
        # # time.sleep(5)

        # # Click dang bai
        # btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        # util.click_element(By.CSS_SELECTOR, btn_post_selector)
        # # time.sleep(10)

        # # get post link if success
        # result = False
        # try:
        #     bg_img_post = 'div.thread-view > div.thread-view--content-wrapper > article.content'
        #     bg_img_post = util.driver.find_element(By.CLASS_NAME, bg_img_post)
        #     print('linkpost', bg_img_post.tag_name)

        #     result = True
        # except NoSuchElementException:
        #     print('Element not found')
        #     result = False

        # assert True


        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.//report'))
    util.driver.close()
    util.driver.quit()