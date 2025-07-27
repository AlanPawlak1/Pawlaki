from seleniumbase import SB

with SB(uc=True, test=True) as pawl:

    if True:
        url = "https://kick.com/brutalles"
        pawl.uc_open_with_reconnect(url, 5)
        pawl.uc_gui_click_captcha()
        pawl.sleep(1)
        pawl.uc_gui_handle_captcha()
        pawl.sleep(1)
        if pawl.is_element_present('button:contains("Accept")'):
            pawl.uc_click('button:contains("Accept")', reconnect_time=4)
        if pawl.is_element_visible('#injected-channel-player'):
            pawl.sleep(10)
            while pawl.is_element_visible('#injected-channel-player'):
                pawl.sleep(10)
    pawl.sleep(1)
