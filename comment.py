from asyncio import sleep
import HtmlTestRunner
from operator import truediv
import unittest
import time
from unittest import result

from util import Util
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

util = Util()


class CommentsPostTest(unittest.TestCase):
    def test_cmt_normal(self):
        # sign in
        util.sign_in("giangbui12345", "f4kAUjzS")

        # open post
        open_post_button_selector = '#__next > div.root > div.jsx-2599222059.main-page > div:nth-child(3) > div > div > div.jsx-2790954478.col-main.additional-padding.undefined > div.jsx-3834913322.featured-threads > ol > li:nth-child(2) > div > article > div > a'
        util.click_element(By.CSS_SELECTOR, open_post_button_selector)
        
        #open box cmt
        cmt_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.no-user-select.below-first-post.false > div.jsx-3147581474.thread-actions.border > div.jsx-3147581474.thread-actions__left > button'
        util.click_element(By.CSS_SELECTOR, cmt_selector)
        
        # add content
        content_area_selector = 'textarea'
        content_to_post = 'Article is very perfect'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        
        # post cmt
        btn_post_selector = 'div.jsx-3593820457.post-reply-actions > button.jsx-3593820457.post-reply-submit.active'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

    def test_cmt_special(self):
        # go to main page
        util.go_to_main_page()

        # open post
        open_post_button_selector = '#__next > div.root > div.jsx-2599222059.main-page > div:nth-child(3) > div > div > div.jsx-2790954478.col-main.additional-padding.undefined > div.jsx-3834913322.featured-threads > ol > li:nth-child(2) > div > article > div > a'
        util.click_element(By.CSS_SELECTOR, open_post_button_selector)
        
        # open box cmt
        cmt_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.no-user-select.below-first-post.false > div.jsx-3147581474.thread-actions.border > div.jsx-3147581474.thread-actions__left > button'
        util.click_element(By.CSS_SELECTOR, cmt_selector)
        
        #add content cmt
        content_area_selector = 'textarea'
        content_to_post = 'Bài viết như lồng đèn ông sao'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        
        # post cmt
        btn_post_selector = 'div.jsx-3593820457.post-reply-actions > button.jsx-3593820457.post-reply-submit.active'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

    def test_cmt_sticker(self):
            # sign in
        util.go_to_main_page()

        # click add post
        open_post_button_selector = '#__next > div.root > div.jsx-2599222059.main-page > div:nth-child(3) > div > div > div.jsx-2790954478.col-main.additional-padding.undefined > div.jsx-3834913322.featured-threads > ol > li:nth-child(2) > div > article > div > a'
        util.click_element(By.CSS_SELECTOR, open_post_button_selector)
        
        cmt_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.no-user-select.below-first-post.false > div.jsx-3147581474.thread-actions.border > div.jsx-3147581474.thread-actions__left > button'
        util.click_element(By.CSS_SELECTOR, cmt_selector)
        
        #add content
        content_area_selector = 'textarea'
        content_to_post = 'Bài viết như lồng đèn ông sao'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        sticker = 'div.jsx-3593820457.post-reply-actions > div > div > button'
        util.click_element(By.CSS_SELECTOR, sticker)

        #choose sticker
        choose = 'div.jsx-3593820457.post-reply-actions > div > div > div > div > div.jsx-32732841.stickers > div > div > button:nth-child(1)'
        util.click_element(By.CSS_SELECTOR, choose)

        # Click cmt
        btn_post_selector = 'div.jsx-3593820457.post-reply-actions > button.jsx-3593820457.post-reply-submit.active'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

    def test_cmt_reply(self):
        #go to page main
        util.go_to_main_page()

        # click add post
        open_post_button_selector = '#__next > div.root > div.jsx-2599222059.main-page > div:nth-child(4) > div > div > div.jsx-2790954478.col-main.additional-padding.undefined > div.jsx-934348644.latest-threads > div.jsx-934348644.threads > div.jsx-934348644.thread-containers > ol > li:nth-child(1) > div > article > a:nth-child(2)'
        util.click_element(By.CSS_SELECTOR, open_post_button_selector)
        
        cmt_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.no-user-select.below-first-post.false > div.jsx-3147581474.thread-actions.border > div.jsx-3147581474.thread-actions__left > button'
        util.click_element(By.CSS_SELECTOR, cmt_selector)
        
        rep_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div:nth-child(14) > div.jsx-1984507624 > div > div.jsx-691990575.thread-comment > div > div.jsx-691990575.thread-comment__wrapper > div.jsx-691990575.thread-comment__action.no-user-select > div > button'
        util.click_element(By.CSS_SELECTOR, rep_selector)
        
        content_area_selector = '#post-reply-62489317 > textarea'
        content_to_post = 'Pefrfect'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        #add cmt
        btn_post_selector = '#post-reply-62489317 > div.jsx-3593820457.post-reply-actions > button.jsx-3593820457.post-reply-submit.active'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
       

    def test_cmt_normal_story(self):
        #go to page main
        
        util.go_to_main_page()

        # open post
        open_post_button_selector = '#__next > div.root > div.jsx-2599222059.main-page > div:nth-child(2) > div > div > div > div > div.jsx-4083475239.main > div > div:nth-child(2) > div > div > button.jsx-3067764999.preview-mask'
        util.click_element(By.CSS_SELECTOR, open_post_button_selector)
        
        
        #add cmt
        content_area_selector = 'textarea'
        content_to_post = 'Article is very perfect'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        
        # add cmt
        btn_post_selector = 'div.jsx-3593820457.post-reply-actions > button.jsx-3593820457.post-reply-submit.active'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        
        
    
    def test_cmt_link(self):
        # go to page main
        util.go_to_main_page()

        # open post
        open_post_button_selector = '#__next > div.root > div.jsx-2599222059.main-page > div:nth-child(4) > div > div > div.jsx-2790954478.col-main.additional-padding.undefined > div.jsx-934348644.latest-threads > div.jsx-934348644.threads > div.jsx-934348644.thread-containers > ol > li:nth-child(1) > div > article > a:nth-child(2)'
        util.click_element(By.CSS_SELECTOR, open_post_button_selector)
        
        #cmt on post
        cmt_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.no-user-select.below-first-post.false > div.jsx-3147581474.thread-actions.border > div.jsx-3147581474.thread-actions__left > button'
        util.click_element(By.CSS_SELECTOR, cmt_selector)
        
        #rep cmt other
        rep_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div:nth-child(14) > div.jsx-1984507624 > div > div.jsx-691990575.thread-comment > div > div.jsx-691990575.thread-comment__wrapper > div.jsx-691990575.thread-comment__action.no-user-select > div > button'
        util.click_element(By.CSS_SELECTOR, rep_selector)
        
        #add content
        content_area_selector = '#post-reply-62489317 > textarea'
        content_to_post = 'https://stackoverflow.com/questions/42301512/timeout-handling-with-node-js-stream-piping'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        #click add cmt
        btn_post_selector = '#post-reply-62489317 > div.jsx-3593820457.post-reply-actions > button.jsx-3593820457.post-reply-submit.active'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)


        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.//report'))
    util.driver.close()
    util.driver.quit()
