from ui_testing.pages.base_pages import BasePages
from random import randint

class MyProfile(BasePages):
    def __init__(self):
        super().__init__()
        self.base_selenium.wait_until_page_url_has(text='dashboard')
        self.my_profile_url = "{}settings#myProfile".format(self.base_selenium.url)
        
    def get_my_profile_page(self):
        self.base_selenium.LOGGER.info(' + Get my profile page.')
        self.base_selenium.get(url=self.my_profile_url)
        self.sleep_small()

    def change_password(self, current_password, new_password, save=False):
        # change the password value
        self.base_selenium.set_text(
            'my_profile:current_password_field', current_password)
        self.base_selenium.set_text(
            'my_profile:new_password_field', new_password)
        self.base_selenium.set_text(
            'my_profile:confirm_password_field', new_password)

        if save:
            self.my_profile_page.save(True)
        else:
            self.my_profile_page.cancel(force=True)