#!/usr/bin/python3
from selenium import webdriver

url = "http://keybr.com/practice"
letter_selector = "span.TextInput-item"
close_tour_selector = "a.Tour-close"
focus_input_selector = ".TextInput.TextInput--sizeX0"

# how many times to fill the field
attempts = 10

# open browser
browser = webdriver.Firefox()
browser.get(url)

# close the modal at the start
browser.find_element_by_css_selector(close_tour_selector).click()
# focus input
browser.find_element_by_css_selector(focus_input_selector).click()

for _ in range(attempts):
    # get letters
    letters = browser.find_elements_by_css_selector(letter_selector)
    for letter in letters:
        if letter.text == " ":
            continue

        value = letter.text if letter.text != "␣" else " "
        letter.send_keys(value)

browser.close()
