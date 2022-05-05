import os
import time
import unittest
from urllib.request import urlretrieve
import HtmlTestRunner

from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By

from util import Util

util = Util()

account = 'trunghiu0301'
password = 'hieu1234'


class CreatePostTest(unittest.TestCase):
    def test_create_normal_short_post(self):
        # sign in
        util.sign_in(account, password)

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # add content
        content_area_selector = 'textarea'
        content_to_post = 'Timeout handling with node.js stream piping'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        
        # Click dang bai
        btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        time.sleep(10)


        # Get post title if success
        result = False
        try:
            title_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div.thread-title'
            title = util.driver.find_element(By.CSS_SELECTOR, title_selector).get_attribute('innerHTML')

            result = content_to_post in title
        except NoSuchElementException:
            result = False

        assert result

    def test_create_short_post_with_special_text(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # add content
        content_area_selector = 'textarea'
        content_to_post = 'Timeout handling with node.js stream piping Ǆ ǆŸŻŴŒ'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass
        
        # Click dang bai
        btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        time.sleep(10)


        # Get post title if success
        result = False
        try:
            title_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div.thread-title'
            title = util.driver.find_element(By.CSS_SELECTOR, title_selector).get_attribute('innerHTML')

            result = content_to_post in title
        except NoSuchElementException:
            result = False

        assert result

    def test_create_short_post_with_url(self):
        util.go_to_main_page()
        # util.sign_in("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # add content
        content_area_selector = 'textarea'
        content_to_post = 'Timeout handling with node.js stream piping Ǆ ǆŸŻŴŒ'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                pass

        # Click link button
        link_btn_selector = 'div.ReactModal__Content button.link-sharing'
        util.click_element(By.CSS_SELECTOR, link_btn_selector)

        # Add link to input
        link = 'https://stackoverflow.com/questions/42301512/timeout-handling-with-node-js-stream-piping'
        input_selector = 'div.ReactModal__Content input'
        util.set_text(By.CSS_SELECTOR, input_selector, link)
        time.sleep(10)

        # Click dang bai
        btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        time.sleep(10)


        # get post link if success
        result = False
        try:
            link_post_selector = 'externalLink'
            link_post = util.driver.find_element(By.CLASS_NAME, link_post_selector).get_attribute('href')
            print('linkpost',link_post)

            result = link_post == link
        except NoSuchElementException:
            print('Element not found')
            result = False

        assert result

    def test_create_short_post_with_image(self):
        util.go_to_main_page()
        # util.sign_in("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # add content
        content_area_selector = 'textarea'
        content_to_post = 'Timeout handling with node.js stream piping'
        text_area = util.driver.find_elements(By.TAG_NAME, content_area_selector)
        for txt in text_area:
            try:
                txt.clear()
                txt.send_keys(content_to_post)
            except ElementNotInteractableException:
                print('Element not found')
                pass
        
        # click image button
        img_btn_selector = 'div.thread-background-container > button:nth-child(2)'
        util.click_element(By.CSS_SELECTOR, img_btn_selector)
        time.sleep(5)

        # select image
        first_img_selector = 'div.thread-background-container > img:nth-child(3)'
        util.click_element(By.CSS_SELECTOR, first_img_selector)
        # time.sleep(5)

        # Click dang bai
        btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        # time.sleep(10)

        # get post link if success
        result = False
        try:
            bg_img_post = 'div.thread-view > div.thread-view--content-wrapper > article.content'
            bg_img_post = util.driver.find_element(By.CLASS_NAME, bg_img_post).get_attribute('src')

            result = bg_img_post == 'https://photo2.tinhte.vn/data/attachment-files/2020/01/4892133_Background-tinhte-1.jpg'
        except NoSuchElementException:
            print('Element not found')
            result = False

        assert result

    def test_crate_short_post_with_empty_content(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # Click dang bai
        btn_post_selector = 'div.thread-editor-modal button.publish-btn'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        time.sleep(10)

        # get post link if success
        result = False
        try:
            bg_img_post = 'div.thread-view > div.thread-view--content-wrapper > article.content'
            error_selector = 'body > div:nth-child(11) > div > div > div.jsx-659482973.middle-area > div.jsx-659482973.err > span'
            error_alert = util.driver.find_element(By.CLASS_NAME, error_selector).get_attribute('innerHTML')

            result = error_alert == 'Vui lòng không để nội dung trống'
        except NoSuchElementException:
            print('Element not found')
            result = False

        assert result

    def test_create_normal_long_post(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # click write long post
        long_post_btn_selector = 'body > div:nth-child(11) > div > div > div.jsx-659482973.middle-area div.jsx-659482973.textbox-area > div > div.jsx-659482973.textbox__tools > a'
        util.click_element(By.CSS_SELECTOR, long_post_btn_selector)

        # add title
        title_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div'
        title = 'Ông Trịnh Văn Quyết bị bắt, nhưng đừng "bắt" Tập đoàn FLC sụp đổ'
        util.set_text(By.CSS_SELECTOR, title_selector, title)

        # add content
        content_input_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div > p'
        content = 'Ông Trịnh Văn Quyết - Chủ tịch HĐQT Công ty CP Tập đoàn FLC đã bị khởi tố, bắt tạm giam về tội "Thao túng thị trường chứng khoán", gây ra một chấn động lớn mà ảnh hưởng đầu tiên chính là Tập đoàn FLC. Đương nhiên, khi chủ tịch một tập đoàn bị khởi tố bắt tạm giam vì một hành vi vi phạm pháp luật, thì chính tập đoàn đó chịu tổn thất ngay lập tức. Tuy nhiên, không vì thế mà đẩy cho một doanh nghiệp và tập thể người lao động ở đó đến sự sụp đổ, mà cần phải có cách hỗ trợ để giữ vững sản xuất kinh doanh.'
        util.set_text(By.CSS_SELECTOR, content_input_selector, content)
        
        # Click dang bai
        btn_post_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > button'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

        # Get post title if success
        result = False
        try:
            title_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div'
            title_post = util.driver.find_element(By.CSS_SELECTOR, title_post_selector).get_attribute('innerHTML')

            content_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > article > div > div > div > div > span'
            content_post = util.driver.find_element(By.CSS_SELECTOR, content_post_selector).get_attribute('innerHTML')

            result = content_post == content and title_post == title
        except NoSuchElementException:
            result = False

        assert result


    def test_create_long_post_with_tag(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # click write long post
        long_post_btn_selector = 'body > div:nth-child(11) > div > div > div.jsx-659482973.middle-area div.jsx-659482973.textbox-area > div > div.jsx-659482973.textbox__tools > a'
        util.click_element(By.CSS_SELECTOR, long_post_btn_selector)

        # add title
        title_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div'
        title = 'Ông Trịnh Văn Quyết bị bắt, nhưng đừng "bắt" Tập đoàn FLC sụp đổ'
        util.set_text(By.CSS_SELECTOR, title_selector, title)

        # add content
        content_input_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div > p'
        content = 'Ông Trịnh Văn Quyết - Chủ tịch HĐQT Công ty CP Tập đoàn FLC đã bị khởi tố, bắt tạm giam về tội "Thao túng thị trường chứng khoán", gây ra một chấn động lớn mà ảnh hưởng đầu tiên chính là Tập đoàn FLC. Đương nhiên, khi chủ tịch một tập đoàn bị khởi tố bắt tạm giam vì một hành vi vi phạm pháp luật, thì chính tập đoàn đó chịu tổn thất ngay lập tức. Tuy nhiên, không vì thế mà đẩy cho một doanh nghiệp và tập thể người lao động ở đó đến sự sụp đổ, mà cần phải có cách hỗ trợ để giữ vững sản xuất kinh doanh.'
        util.set_text(By.CSS_SELECTOR, content_input_selector, content)

        # add tag
        tag_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > textarea.jsx-3766057795.tag-input'
        tag = 'FLC'
        util.set_text(By.CSS_SELECTOR, tag_selector, tag)
        
        # Click dang bai
        btn_post_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor-header > div.jsx-3766057795.toolbar > div:nth-child(2) > button'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)
        confirm_btn_selector = 'body > div.ReactModalPortal > div > div > div:nth-child(2) > button:nth-child(1)'
        util.click_element(By.CSS_SELECTOR, confirm_btn_selector)

        # Get post title if success
        result = False
        try:
            title_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div'
            title_post = util.driver.find_element(By.CSS_SELECTOR, title_post_selector).get_attribute('innerHTML')

            content_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > article > div > div > div > div > span'
            content_post = util.driver.find_element(By.CSS_SELECTOR, content_post_selector).get_attribute('innerHTML')

            tag_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.no-user-select.below-first-post.false > div.jsx-3147581474.thread-tags-container > div > a'  
            tag_post = util.driver.find_element(By.CSS_SELECTOR, tag_post_selector).get_attribute('innerHTML')


            result = content_post == content and title_post == title and tag_post == tag
        except NoSuchElementException:
            result = False

        assert result

    def test_create_long_post_with_image(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # click write long post
        long_post_btn_selector = 'body > div:nth-child(11) > div > div > div.jsx-659482973.middle-area div.jsx-659482973.textbox-area > div > div.jsx-659482973.textbox__tools > a'
        util.click_element(By.CSS_SELECTOR, long_post_btn_selector)

        # add title
        title_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div'
        title = 'Ông Trịnh Văn Quyết bị bắt, nhưng đừng "bắt" Tập đoàn FLC sụp đổ'
        util.set_text(By.CSS_SELECTOR, title_selector, title)

        # add image
        img_btn_selector = 'body > div.ck-body-wrapper > div > div.ck.ck-balloon-panel.ck-balloon-panel_arrow_nw.ck-balloon-panel_with-arrow.ck-toolbar-container > div > div > span.ck-file-dialog-button > button > svg'
        util.driver.find_element(By.CSS_SELECTOR, img_btn_selector).send_keys(os.getcwd() + 'assests/Screenshot from 2022-05-04 16-57-26.png')
        
        # Click dang bai
        btn_post_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > button'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

        # Get post title if success
        result = False
        try:
            title_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div'
            title_post = util.driver.find_element(By.CSS_SELECTOR, title_post_selector).get_attribute('innerHTML')

            img_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > article > div > div > div > div > span > span > img'
            img_post = util.driver.find_element(By.CSS_SELECTOR, img_post_selector).get_attribute('alt')

            result = title_post == title and img_post == 'Screenshot from 2022-05-04 16-57-26.png'
        except NoSuchElementException:
            result = False

        assert result


    def test_create_long_post_with_image_url(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # click write long post
        long_post_btn_selector = 'body > div:nth-child(11) > div > div > div.jsx-659482973.middle-area div.jsx-659482973.textbox-area > div > div.jsx-659482973.textbox__tools > a'
        util.click_element(By.CSS_SELECTOR, long_post_btn_selector)

        # add title
        title_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div'
        title = 'Ông Trịnh Văn Quyết bị bắt, nhưng đừng "bắt" Tập đoàn FLC sụp đổ'
        util.set_text(By.CSS_SELECTOR, title_selector, title)

        # add image url
        img_link_btn_selector = 'body > div.ck-body-wrapper > div > div.ck.ck-balloon-panel.ck-balloon-panel_arrow_nw.ck-balloon-panel_with-arrow.ck-toolbar-container > div > div > button:nth-child(6) > svg'
        util.click_element(By.CSS_SELECTOR, img_link_btn_selector)

        # set link
        img_link_input_selector = '#ck-labeled-field-view-eccd8af627d60b9a297dabe8bc354ae48'
        img_link = 'https://fo4.garena.vn/wp-content/uploads/2020/12/MbappeLoadingScreen_1200x675.png'
        util.set_text(By.CSS_SELECTOR, img_link_input_selector, img_link)

        # Oke link
        oke_link_btn_selector = 'body > div.ck-body-wrapper > div > div.ck.ck-balloon-panel.ck-balloon-panel_arrow_nw.ck-balloon-panel_visible.ck-balloon-panel_with-arrow > div > div.ck-balloon-rotator__content > form > button.ck.ck-button.ck-off.ck-button-save > svg'
        util.click_element(By.CSS_SELECTOR, oke_link_btn_selector)
        
        # Click dang bai
        btn_post_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > button'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

        # Get post title if success
        result = False
        try:
            title_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div'
            title_post = util.driver.find_element(By.CSS_SELECTOR, title_post_selector).get_attribute('innerHTML')

            img_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > article > div > div > div > img'
            img_post = util.driver.find_element(By.CSS_SELECTOR, img_post_selector).get_attribute('src')

            result = title_post == title and img_post == img_link
        except NoSuchElementException:
            result = False

        assert result


    def test_create_long_post_with_website_url(self):
        util.go_to_main_page()

        # click add post
        write_post_button_selector = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div.jsx-365471853.item.hidden-sm > div > button'
        util.click_element(By.CSS_SELECTOR, write_post_button_selector)

        # click write long post
        long_post_btn_selector = 'body > div:nth-child(11) > div > div > div.jsx-659482973.middle-area div.jsx-659482973.textbox-area > div > div.jsx-659482973.textbox__tools > a'
        util.click_element(By.CSS_SELECTOR, long_post_btn_selector)

        # add title
        title_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > div.jsx-3766057795.editor > div'
        title = 'Ông Trịnh Văn Quyết bị bắt, nhưng đừng "bắt" Tập đoàn FLC sụp đổ'
        util.set_text(By.CSS_SELECTOR, title_selector, title)

        # add image url
        img_link_btn_selector = 'body > div.ck-body-wrapper > div > div.ck.ck-balloon-panel.ck-balloon-panel_arrow_nw.ck-balloon-panel_with-arrow.ck-toolbar-container > div > div > button:nth-child(6) > svg'
        util.click_element(By.CSS_SELECTOR, img_link_btn_selector)

        # set link
        web_link_input_selector = '#ck-labeled-field-view-eccd8af627d60b9a297dabe8bc354ae48'
        web_link = 'https://fo4.garena.vn/wp-content/uploads/2020/12/MbappeLoadingScreen_1200x675.png'
        util.set_text(By.CSS_SELECTOR, web_link_input_selector, web_link)

        # Oke link
        oke_link_btn_selector = 'body > div.ck-body-wrapper > div > div.ck.ck-balloon-panel.ck-balloon-panel_arrow_nw.ck-balloon-panel_visible.ck-balloon-panel_with-arrow > div > div.ck-balloon-rotator__content > form > button.ck.ck-button.ck-off.ck-button-save > svg'
        util.click_element(By.CSS_SELECTOR, oke_link_btn_selector)
        
        # Click dang bai
        btn_post_selector = '#__next > div.root > div.jsx-362892249.editor > div > div.jsx-3766057795.tinhte-editor > button'
        util.click_element(By.CSS_SELECTOR, btn_post_selector)

        # Get post title if success
        result = False
        try:
            title_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > div.jsx-3147581474.thread-title__block.false > div'
            title_post = util.driver.find_element(By.CSS_SELECTOR, title_post_selector).get_attribute('innerHTML')

            web_post_selector = '#__next > div.jsx-4091196271.thread-view > div > div.jsx-3866953344.threadpage.false > div.jsx-3866953344.section.bg-white.false > div.jsx-3866953344.fst.false > div > div > div.jsx-3147581474.thread-view--content-wrapper > article > div > div > div > img'
            web_post = util.driver.find_element(By.CSS_SELECTOR, web_post_selector).get_attribute('src')

            result = title_post == title and web_post == web_link
        except NoSuchElementException:
            result = False

        assert result
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.//report'))
    util.driver.close()
    util.driver.quit()
