import time
from contextlib import closing
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

with open("urls.txt", "r") as myfile:
    list_of_urls = myfile.readlines()

for url in list_of_urls:
    print url

    # Get website
    browser = webdriver.Firefox()
    browser.get(url)

    page_title = browser.title
    print page_title

    # Give time for javascript to being playing video
    time.sleep(3.00)

    video_playing = True

    # Click cc button
    if browser.find_element_by_css_selector("button.cc"):
        cc_button = browser.find_element_by_css_selector("button.cc")
        cc_button.click()

    # Click rate button to make the video play faster
    if browser.find_element_by_css_selector("button.rate"):
        cc_button = browser.find_element_by_css_selector("button.rate")

        # Click 3 times to go to fastest speed
        cc_button.click()
        cc_button.click()
        cc_button.click()

    # Grab video duration to know when video ends
    video_duration = browser.find_element_by_class_name("duration").text
    print "Video Duration: " + video_duration

    already_saved_subtitle_text = ""
    closed_captions = []
    time_checked = False

    while video_playing:

        current_video_time = browser.find_element_by_class_name("position").text
        time_checked = True
        if current_video_time == video_duration or (current_video_time == "0:00" and time_checked):
            break

        try:
            try:
                current_subtitle_text = browser.find_element_by_class_name("ui-playercaptionpanel-item").text
            except NoSuchElementException:
                if current_video_time == video_duration:
                    break
                continue
            if (current_subtitle_text != "" or current_subtitle_text != null) and current_subtitle_text != already_saved_subtitle_text:
                print current_subtitle_text
                closed_captions.append(current_subtitle_text)
                already_saved_subtitle_text = current_subtitle_text
        except StaleElementReferenceException:
            continue

    with open("closed_captions.txt", "a") as text_file:
        text_file.write("\n\n" + page_title)
        text_file.write(' '.join(closed_captions))
        text_file.close()

    browser.close()
