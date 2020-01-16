from ui_testing.pages.orders_page import Orders
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from random import randint

class Order(Orders):
    def get_order(self):
        return self.base_selenium.get_text(element='order:order').split('\n')[0]

    def get_order_number(self):
        return self.base_selenium.get_text(element='order:order_number_add_form').split('\n')[0]

    def set_new_order(self):
        self.base_selenium.LOGGER.info('Set new order.')
        self.base_selenium.select_item_from_drop_down(
            element='order:order', item_text='New Order')

    def set_existing_order(self):
        self.base_selenium.select_item_from_drop_down(
            element='order:order', item_text='Existing Order')

    def set_material_type(self, material_type=''):
        if material_type:
            self.base_selenium.select_item_from_drop_down(
                element='order:material_type', item_text=material_type)
        else:
            self.base_selenium.select_item_from_drop_down(
                element='order:material_type')
            return self.get_material_type()

    def get_material_type(self):
        return self.base_selenium.get_text(element='order:material_type').split('\n')[0]

    def get_article(self):
        return self.base_selenium.get_text(element='order:article').split('\n')[0]

    def set_article(self, article=''):
        if article:
            self.base_selenium.select_item_from_drop_down(element='order:article', item_text=article)
        else:
            self.base_selenium.select_item_from_drop_down(element='order:article')
            return self.get_article()

    def is_article_existing(self, article):
        self.set_article(article=article)
        return self.base_selenium.check_item_in_items(element='order:article', item_text=article)

    def set_contact(self, contact=''):
        if contact:
            self.base_selenium.select_item_from_drop_down(
                element='order:contact', item_text=contact)
        else:
            self.base_selenium.select_item_from_drop_down(
                element='order:contact')
            return self.get_contact()

    def get_contact(self):
        return list(map(lambda s: {"name": str(s).split(' No: ')[0][1:], "no": str(s).split(' No: ')[1]}, self.base_selenium.get_text(element='order:contact').split('\n')))

    def set_test_plan(self, test_plan=''):
        if test_plan:
            self.base_selenium.select_item_from_drop_down(element='order:test_plan', item_text=test_plan)
        else:
            self.base_selenium.select_item_from_drop_down(element='order:test_plan')
            return self.get_test_plan()

    def get_test_plan(self):
        test_plans = self.base_selenium.get_text(element='order:test_plan')
        if "×" in test_plans:
            return test_plans.replace("× ", "").split('\n')
        else:
            return []

    def clear_test_plan(self):
        if self.get_test_plan():
            self.base_selenium.clear_items_in_drop_down(element='order:test_plan')

    def clear_test_unit(self):
        if self.get_test_unit():
            self.base_selenium.clear_items_in_drop_down(element='order:test_unit')

    def set_test_unit(self, test_unit=''):
        if test_unit:
            self.base_selenium.select_item_from_drop_down(element='order:test_unit', item_text=test_unit)
        else:
            self.base_selenium.select_item_from_drop_down(element='order:test_unit')
            return self.get_test_unit()

    def get_test_unit(self):
        test_units = self.base_selenium.get_text(element='order:test_unit')
        if "×" in test_units:
            return test_units.replace("× ", "").split('\n')
        else:
            return []

    def create_new_order(self, material_type='', article='', contact='', test_plans=[''], test_units=[''],
                         multiple_suborders=0, departments=''):
        self.base_selenium.LOGGER.info(' Create new order.')
        self.click_create_order_button()
        self.set_new_order()
        self.set_contact(contact=contact)
        self.sleep_small()
        self.set_departments(departments=departments)
        self.set_material_type(material_type=material_type)
        self.sleep_small()
        self.set_article(article=article)
        self.sleep_small()
        order_no = self.get_no()

        for test_plan in test_plans:
            self.set_test_plan(test_plan=test_plan)
        for test_unit in test_units:
            self.set_test_unit(test_unit)
        if multiple_suborders > 0:
            self.get_suborder_table()
            self.duplicate_from_table_view(number_of_duplicates=multiple_suborders)

        self.save(save_btn='order:save_btn')
        self.base_selenium.LOGGER.info(' Order created with no : {} '.format(order_no))
        return self.get_suborder_data()

    def create_existing_order(self, no='', material_type='', article='', contact='', test_units=[],
                              multiple_suborders=0):
        self.base_selenium.LOGGER.info(' Create new order.')
        self.click_create_order_button()
        self.set_existing_order()
        order_no = self.set_existing_number(no)
        self.set_material_type(material_type=material_type)
        self.set_article(article=article)
        self.set_contact(contact=contact)

        for test_unit in test_units:
            self.set_test_unit(test_unit)

    def create_existing_order_with_auto_fill(self, no=''):
        self.base_selenium.LOGGER.info(' Create new order.')
        self.click_create_order_button()
        self.set_existing_order()
        order_no = self.set_existing_number(no)
        self.sleep_tiny()
        self.click_auto_fill()
        self.base_selenium.LOGGER.info(' Order Auto filled with data from order no : {} '.format(order_no))
        return order_no

    def get_no(self):
        return self.base_selenium.get_value(element="order:no")

    def set_no(self, no):
        self.base_selenium.LOGGER.info(' set no. {}'.format(no))
        self.base_selenium.set_text(element="order:no", value=no)

    def set_existing_number(self, no=''):
        if no:
            self.base_selenium.select_item_from_drop_down(
                element='order:order_number_add_form', item_text=no)
        else:
            self.base_selenium.select_item_from_drop_down(
                element='order:order_number_add_form')
            return self.get_order_number()

    def edit_random_order(self, edit_method, edit_value, save=True):
        if 'contact' in edit_method:
            self.set_contact(edit_value)
        elif 'departments' in edit_method:
            self.set_departments(edit_value)
        # elif 'material_type' in edit_method:
        # self.set_material_type(edit_value)
        # elif '' in edit_method:
        # self.set_contact(edit_value)

        if save:
            self.save()
        else:
            self.cancel()

    def get_last_order_row(self):
        rows = self.result_table()
        return rows[0]

    def get_shipment_date(self):
        return self.base_selenium.get_value(element='order:shipment_date')

    def get_random_suborder_data(self, row_id=None):
        
        # get all the suborders
        suborders = self.base_selenium.get_table_rows(element='order:suborder_table')
        # select random row id
        if not row_id:
            if len(suborders) > 1:
                row_id = randint(0, len(suborders) - 1)
            else:
                row_id = 0

        self.info('Getting suborder no. {}'.format(row_id))

        # get the current suborder data
        suborder = self.base_selenium.get_row_cells_id_dict_related_to_header(
            row=suborders[row_id], table_element='order:suborder_table')
        # attach the row_id to the suborder
        suborder['row_id'] = row_id
        # attach the row element to the suborder
        suborder['row_element'] = suborders[row_id]
        return suborder

    def open_suborder_edit_mode(self, row_id=None):
        # get the suborder
        suborder_data = self.get_random_suborder_data(row_id)
        self.info('Open suborder no. {} for edit mode'.format(suborder_data['row_id']))
        # click the table row (used script because the tr is not clickable)
        self.base_selenium.driver.execute_script('arguments[0].click();', suborder_data['row_element'])
        return suborder_data['row_id']

    def close_suborder_edit_mode(self):
        self.info('Close the suborder edit mode')
        webdriver.ActionChains(self.base_selenium.driver).send_keys(Keys.ESCAPE).perform()

    def get_test_date(self, row_id=None):
        # open the row in edit mode
        row_id = self.open_suborder_edit_mode(row_id=row_id)
        self.info('Get the test date value')
        # get the test_date field of the selected row
        test_date = self.base_selenium.find_element_by_xpath('//*[@id="date_testDate_{}"]'.format(row_id))
        return test_date.get_attribute('value')

    def set_test_date(self, date='', row_id=None):
        # set random date
        if not date:
            date = self.get_random_date()
        self.info('Set the test date value to {}'.format(date))
        # open the row in edit mode
        row_id = self.open_suborder_edit_mode(row_id=row_id)
        # get the test_date field of the selected row
        test_date = self.base_selenium.find_element_by_xpath('//*[@id="date_testDate_{}"]'.format(row_id))
        test_date.clear()
        test_date.send_keys(date)
        return date

    def set_shipment_date(self, date=''):
        if not date:
            date = self.get_random_date()
        self.base_selenium.set_text(element='order:shipment_date', value=date)
        return date

    def get_departments(self):
        departments = self.base_selenium.get_text(
            element='order:departments').split('\n')[0]
        if departments == 'Search':
            return ''
        return departments

    def get_department(self):
        return self.base_selenium.get_text(element='order:departments').split('\n')[0]

    def set_departments(self, departments=''):
        if departments:
            self.base_selenium.select_item_from_drop_down(element='order:departments', item_text=departments)
        else:
            self.base_selenium.select_item_from_drop_down(element='order:departments')
            return self.get_departments()

    def get_suborder_table(self):
        self.base_selenium.LOGGER.info(' Get suborder table list.')
        self.base_selenium.click(element='order:suborder_list')

    def create_new_suborder(self, material_type='', article_name='', test_plan='', **kwargs):
        self.get_suborder_table()
        rows_before = self.base_selenium.get_table_rows(element='order:suborder_table')

        self.base_selenium.LOGGER.info(' Add new suborder.')
        self.base_selenium.click(element='order:add_new_item')

        rows_after = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborder_row = rows_after[len(rows_before)]

        suborder_elements_dict = self.base_selenium.get_row_cells_elements_related_to_header(row=suborder_row,
                                                                                             table_element='order:suborder_table')
        self.base_selenium.LOGGER.info(' Set material type : {}'.format(material_type))
        self.base_selenium.update_item_value(item=suborder_elements_dict['Material Type: *'],
                                             item_text=material_type.replace("'", ''))
        self.base_selenium.LOGGER.info(' Set article name : {}'.format(article_name))
        self.base_selenium.update_item_value(item=suborder_elements_dict['Article: *'],
                                             item_text=article_name.replace("'", ''))
        self.base_selenium.LOGGER.info(' Set test plan : {}'.format(test_plan))
        self.base_selenium.update_item_value(item=suborder_elements_dict['Test Plan: *'],
                                             item_text=test_plan.replace("'", ''))

        for key in kwargs:
            if key in suborder_elements_dict.keys():
                self.base_selenium.update_item_value(item=suborder_elements_dict[key], item_text=kwargs[key])
            else:
                self.base_selenium.LOGGER.info(' {} is not a header element!'.format(key))
                self.base_selenium.LOGGER.info(' Header keys : {}'.format(suborder_elements_dict.keys()))
        
        return self.get_suborder_data()

    def duplicate_from_table_view(self, number_of_duplicates=1, index_to_duplicate_from=0):
        suborders = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborders_elements = self.base_selenium.get_row_cells_elements_related_to_header(
            row=suborders[index_to_duplicate_from],
            table_element='order:suborder_table')

        duplicate_element = self.base_selenium.find_element_in_element(source=suborders_elements['Options'],
                                                                       destination_element='order:duplicate_table_view')
        for duplicate in range(0, number_of_duplicates):
            duplicate_element.click()

    def duplicate_suborder(self):
        self.get_suborder_table()
        self.base_selenium.LOGGER.info(' Duplicate order')
        suborders = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborders_elements = self.base_selenium.get_row_cells_elements_related_to_header(row=suborders[0],
                                                                                         table_element='order:suborder_table')
        duplicate_element = self.base_selenium.find_element_in_element(source=suborders_elements['Options'],
                                                                       destination_element='order:duplicate_table_view')
        duplicate_element.click()

    # this method to be used while you are order's table with add page ONLY, and you can get the required data by sending the index, and the needed fields of the suborder
    def get_suborder_data(self, sub_order_index=0):
        webdriver.ActionChains(self.base_selenium.driver).send_keys(Keys.ESCAPE).perform()
        table_suborders = self.base_selenium.get_table_rows(element='order:suborder_table')
        self.base_selenium.LOGGER.info('getting main order data')
        order_data = {
            "orderNo": self.get_no(),
            "contacts": self.get_contact(),
            "suborders": []
        }
        suborders_data = []
        self.base_selenium.LOGGER.info('getting suborders data')
        for suborder in table_suborders:
            suborder_data = self.base_selenium.get_row_cells_id_dict_related_to_header(row=suborder, table_element='order:suborder_table')
            article = {"name": suborder_data['article'].split(' No:')[0], "no": suborder_data['article'].split(' No:')[1]} if len(suborder_data['article'].split(' No:')) > 1 else '-'
            testunits =[]
            rawTestunitArr = suborder_data['testUnits'].split(',\n')
            
            for testunit in rawTestunitArr:
                if len(testunit.split(' No: ')) > 1:
                    testunits.append({
                        "name": testunit.split(' No: ')[0],
                        "no": testunit.split(' No: ')[1]
                    })
                else:
                    testunits.append('-')

            temp_suborder_data = {
                'analysis_no': suborder_data['analysisNo'],
                'departments': suborder_data['departments'].split(',\n'),
                'material_type': suborder_data['materialType'],
                'article': article,
                'testplans': suborder_data['testPlans'].split(',\n') ,
                'testunits': testunits,
                'shipment_date': suborder_data['shipmentDate'],
                'test_date': suborder_data['testDate']
            }
            suborders_data.append(temp_suborder_data)
        order_data['suborders'] = suborders_data
        return order_data

    def remove_testplan_by_name(self, index, testplan_name):
        suborder_table_rows = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborder_row = suborder_table_rows[index]
        suborder_elements_dict = self.base_selenium.get_row_cells_id_elements_related_to_header(row=suborder_row,
                                                                                                table_element='order:suborder_table')
        self.base_selenium.update_item_value(item=suborder_elements_dict['testPlans'],
                                             item_text=testplan_name.replace("'", ''))

    def remove_testunit_by_name(self, index, testunit_name):
        suborder_table_rows = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborder_row = suborder_table_rows[index]
        suborder_elements_dict = self.base_selenium.get_row_cells_id_elements_related_to_header(row=suborder_row,
                                                                                                table_element='order:suborder_table')
        self.base_selenium.update_item_value(item=suborder_elements_dict['testUnits'],
                                             item_text=testunit_name.replace("'", ''))

    def update_suborder(self, sub_order_index=0, contacts=False, departments=[], material_type=False, articles=False,
                        test_plans=[], test_units=[], shipment_date=False, test_date=False, form_view=True):
        if form_view:
            self.get_suborder_table()
        suborder_table_rows = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborder_row = suborder_table_rows[sub_order_index]

        suborder_elements_dict = self.base_selenium.get_row_cells_id_elements_related_to_header(row=suborder_row,
                                                                                                table_element='order:suborder_table')
        contacts_record = 'contact with many departments'

        if material_type:
            self.base_selenium.LOGGER.info(' Set material type : {}'.format(material_type))
            self.base_selenium.update_item_value(item=suborder_elements_dict['materialType'],
                                                 item_text=material_type.replace("'", ''))

        if articles:
            self.base_selenium.LOGGER.info(' Set article name : {}'.format(articles))
            self.base_selenium.update_item_value(item=suborder_elements_dict['article'],
                                                 item_text=articles.replace("'", ''))

        self.base_selenium.LOGGER.info(' Set test plan : {} for {} time(s)'.format(test_plans, len(test_plans)))
        for testplan in test_plans:
            self.base_selenium.update_item_value(item=suborder_elements_dict['testPlans'],
                                                 item_text=testplan.replace("'", ''))

        self.base_selenium.LOGGER.info(' Set test unit : {} for {} time(s)'.format(test_units, len(test_units)))
        for testunit in test_units:
            self.base_selenium.update_item_value(item=suborder_elements_dict['testUnits'],
                                                 item_text=testunit.replace("'", ''))

        if shipment_date:
            pass

        if test_date:
            pass

        if contacts:
            self.set_contact(contact=contacts_record)

        if departments:
            self.base_selenium.LOGGER.info(' Set departments : {}'.format(departments))
            for department in departments:
                self.base_selenium.update_item_value(item=suborder_elements_dict['departments'], item_text=department)

        if articles:
            self.update_article_suborder(row=suborder_elements_dict, article=articles)

        if len(test_plans) > 0:
            self.add_multiple_testplans_suborder(row=suborder_elements_dict, testplans=test_plans)

        if len(test_units) > 0:
            self.add_multiple_testunits_suborder(row=suborder_elements_dict, testunits=test_units)

        if contacts:
            self.set_contact(contact=contacts)

        if departments:
            self.update_departments_suborder(row=suborder_elements_dict, departments=departments)

    def update_material_type_suborder(self, row, material_type):
        self.base_selenium.LOGGER.info(' Set material type : {}'.format(material_type))
        self.base_selenium.update_item_value(item=row['materialType'],
                                             item_text=material_type.replace("'", ''))

    def update_article_suborder(self, row, article):
        self.base_selenium.LOGGER.info(' Set article name : {}'.format(article))
        self.base_selenium.update_item_value(item=row['article'],
                                             item_text=article.replace("'", ''))

    def add_multiple_testplans_suborder(self, row, testplans):
        self.base_selenium.LOGGER.info(' Set test plan : {} for {} time(s)'.format(testplans, len(testplans)))
        for testplan in testplans:
            self.base_selenium.update_item_value(item=row['testUnits'],
                                                 item_text=testplan.replace("'", ''))

    def add_multiple_testunits_suborder(self, row, testunits):
        self.base_selenium.LOGGER.info(' Set test unit : {} for {} time(s)'.format(testunits, len(testunits)))
        for testunit in testunits:
            self.base_selenium.update_item_value(item=row['testUnits'],
                                                 item_text=testunit.replace("'", ''))

    def update_departments_suborder(self, row, departments):
        self.base_selenium.LOGGER.info(' Set departments : {}'.format(departments))
        for department in departments:
            self.base_selenium.update_item_value(item=row['departments'], item_text=department)

    def archive_suborder(self, index, check_pop_up=False):
        self.get_suborder_table()
        self.sleep_tiny()
        self.base_selenium.LOGGER.info('archive suborder with index {}'.format(index + 1))
        suborders = self.base_selenium.get_table_rows(element='order:suborder_table')
        self.base_selenium.LOGGER.info(' Archive order no #{}'.format(index + 1))
        suborders_elements = self.base_selenium.get_row_cells_elements_related_to_header(row=suborders[index],
                                                                                         table_element='order:suborder_table')
        archive_element = self.base_selenium.find_element_in_element(source=suborders_elements['Options'],
                                                                     destination_element='order:delete_table_view')

        archive_element.click()
        self.sleep_tiny()
        if check_pop_up:
            self.base_selenium.LOGGER.info('confirm archiving')
            self.base_selenium.click(element='articles:confirm_archive')
        else:
            self.base_selenium.LOGGER.info('cancel archiving')
            self.base_selenium.click(element='articles:cancel_archive')

    def click_auto_fill(self):
        button = self.base_selenium.find_element_in_element(source_element='order:auto_fill_container',
                                                            destination_element='order:auto_fill')
        button.click()

    def create_new_suborder_with_test_units(self, material_type='', article_name='', test_unit='', **kwargs):
        self.get_suborder_table()
        rows_before = self.base_selenium.get_table_rows(element='order:suborder_table')

        self.base_selenium.LOGGER.info(' Add new suborder.')
        self.base_selenium.click(element='order:add_new_item')

        rows_after = self.base_selenium.get_table_rows(element='order:suborder_table')
        suborder_row = rows_after[len(rows_before)]

        suborder_elements_dict = self.base_selenium.get_row_cells_elements_related_to_header(row=suborder_row,
                                                                                             table_element='order:suborder_table')
        self.base_selenium.LOGGER.info(' Set material type : {}'.format(material_type))
        self.base_selenium.update_item_value(item=suborder_elements_dict['Material Type: *'],
                                             item_text=material_type.replace("'", ''))
        self.base_selenium.LOGGER.info(' Set article name : {}'.format(article_name))
        self.base_selenium.update_item_value(item=suborder_elements_dict['Article: *'],
                                             item_text=article_name.replace("'", ''))
        self.base_selenium.LOGGER.info(' Set Test Unit  : {}'.format(test_unit))
        self.base_selenium.update_item_value(item=suborder_elements_dict['Test Unit: *'],
                                             item_text=test_unit.replace("'", ''))

        for key in kwargs:
            if key in suborder_elements_dict.keys():
                self.base_selenium.update_item_value(item=suborder_elements_dict[key], item_text=kwargs[key])
            else:
                self.base_selenium.LOGGER.info(' {} is not a header element!'.format(key))
                self.base_selenium.LOGGER.info(' Header keys : {}'.format(suborder_elements_dict.keys()))

    def get_order_id(self):
        current_splited_url = self.base_selenium.get_url().split('/')
        order_id = current_splited_url[(len(current_splited_url)-1)]
        return order_id

    def navigate_to_analysis_tab(self):
        self.base_selenium.click('order:analysis_tab')
        self.sleep_small()
