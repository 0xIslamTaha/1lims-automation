from ui_testing.testcases.base_test import BaseTest
from parameterized import parameterized
import re

class AuditTrailTestCases(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page.login(username=self.base_selenium.username, password=self.base_selenium.password)
        self.base_selenium.wait_until_page_url_has(text='dashboard')
        self.audit_trail_page.get_audit_trails_page()

    def test001_download_audit_trail_sheet(self):
        """
        Header: Audit trail: Make sure that you can export all the fields in the active table
        
        ** NB ** Everybody using the system should stop while this test case is running, because
        the export gets the latest info in the server while the rows are not the latest ** NB ** 

        LIMS-6357
        """
        self.audit_trail_page.info(' + Download XSLX sheet')
        self.audit_trail_page.download_xslx_sheet()
        rows_data = self.audit_trail_page.get_table_rows_data()
        for index in range(len(rows_data)):
            self.audit_trail_page.info(' + Comparing the audit trail no. {} '.format(index))
            fixed_row_data = self.fix_data_format(rows_data[index].split('\n'))
            values = self.audit_trail_page.sheet.iloc[index].values
            fixed_sheet_row_data = self.fix_data_format(values)
            for item in fixed_row_data:
                self.assertIn(item, fixed_sheet_row_data)
                
    
    def test002_audit_trail_filters(self):
        """
        Header: Audit trail Approach: Make sure that I can filter by all the following fields 
        ( action date & entity & action & entity no & changed by )

        LIMS-6357
        """

        # get random row in the table
        audit_trail_row = self.audit_trail_page.get_random_audit_trail_row()
        # map the header to the row data
        audit_trail_row_data = self.base_selenium.get_row_cells_dict_related_to_header(row=audit_trail_row)
        
        # get each column data from that row
        action_date = audit_trail_row_data['Action Date'].split(',')[0] # get only the date
        changed_by = audit_trail_row_data['Changed By']
        action = audit_trail_row_data['Action']
        entity = audit_trail_row_data['Entity']
        entity_number = audit_trail_row_data['Entity Number']

        # open filter menu
        self.audit_trail_page.open_filter_menu()

        # filter by Action Date
        self.audit_trail_page.filter_audit_trail_by(filter_name='action_date', filter_text=action_date, field_type='text')
        result = self.audit_trail_page.get_table_rows_data()[0]
        self.assertIn(action_date, result)

        # filter by Change By
        self.audit_trail_page.filter_audit_trail_by(filter_name='changed_by', filter_text=changed_by, field_type='drop_down')
        result = self.audit_trail_page.get_table_rows_data()[0]
        self.assertIn(changed_by, result)

        # filter by Action
        self.audit_trail_page.filter_audit_trail_by(filter_name='action', filter_text=action, field_type='drop_down')
        result = self.audit_trail_page.get_table_rows_data()[0]
        self.assertIn(action, result)

        # filter by Change By
        self.audit_trail_page.filter_audit_trail_by(filter_name='entity', filter_text=entity, field_type='drop_down')
        result = self.audit_trail_page.get_table_rows_data()[0]
        self.assertIn(entity, result)

        # filter by Change By
        self.audit_trail_page.filter_audit_trail_by(filter_name='entity_number', filter_text=entity_number, field_type='text')
        result = self.audit_trail_page.get_table_rows_data()[0]
        self.assertIn(entity_number, result)
        
        # close filter menu
        self.audit_trail_page.open_filter_menu()

