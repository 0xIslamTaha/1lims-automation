from ui_testing.testcases.base_test import BaseTest
from unittest import skip
from parameterized import parameterized


class companyProfileTestCases(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page.login(
            username=self.base_selenium.username, password=self.base_selenium.password)
        self.base_selenium.wait_until_page_url_has(text='dashboard')
        self.company_profile_page.get_company_profile_page()

    def test001_user_can_search_in_the_country_field(self):
        """
        Company profile: Country Approach: Make sure that you can search in the country field

        LIMS-6295
        """
        search_text = 'Egy'
        # get the results
        country_field_results = self.base_selenium.get_drop_down_suggestion_list(
            element='company_profile:country_field', item_text=search_text)
        # check if the country name is in the results
        self.assertIn(search_text, country_field_results)

    @parameterized.extend(['name', 'street_name', 'street_number', 'postal_code', 'location'])
    def test002_user_can_change_any_field_and_cancel(self, field_name):
        """
        Company profile: Make sure after you edit any data and press on cancel button, nothing occur 

        LIMS-6096
        """
        # set field type depanding on name
        field_type = 'text'
        if field_name == 'country':
            field_type = 'drop_down'

        # get the field value before edit
        field_value_before_edit = self.company_profile_page.get_field_value(
            field_name, field_type)

        # change the value
        self.company_profile_page.set_field_value(field_name, field_type)

        # click on cancel
        self.company_profile_page.click_on_cancel()

        # get the field value after edit
        field_value_after_edit = self.company_profile_page.get_field_value(
            field_name, field_type)

        # compare the before value and the after value
        self.assertEqual(field_value_before_edit, field_value_after_edit)

    def test003_user_can_update_company_profile(self):
        """
        Company Profile: Make sure that you can create company profile 
        with all data( name, street name, street number, ....) 

        LIMS-6093
        """
        # update the profile and get the values before saving
        company_profile = self.company_profile_page.update_company_profile()

        # refresh the page
        self.company_profile_page.get_company_profile_page()

        # check that the values before save are matching the values after refresh.
        self.assertEqual(company_profile['name'], self.company_profile_page.get_field_value('name'))
        self.assertEqual(company_profile['street_name'], self.company_profile_page.get_field_value('street_name'))
        self.assertEqual(company_profile['street_number'], self.company_profile_page.get_field_value('street_number'))
        self.assertEqual(company_profile['postal_code'], self.company_profile_page.get_field_value('postal_code'))
        self.assertEqual(company_profile['location'], self.company_profile_page.get_field_value('location'))
        self.assertEqual(company_profile['country'], self.company_profile_page.get_field_value(field_name='country', field_type='drop_down'))


        