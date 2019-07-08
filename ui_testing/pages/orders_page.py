from ui_testing.pages.base_pages import BasePages
from random import randint


class Orders(BasePages):
    def __init__(self):
        super().__init__()
        self.orders_url = "{}orders".format(self.base_selenium.url)

    def get_orders_page(self):
        self.base_selenium.get(url=self.orders_url)
        self.sleep_small()

    def click_create_order_button(self):
        self.base_selenium.click(element='orders:new_order')
        self.sleep_small()

    def archive_selected_orders(self, check_pop_up=False):
        self.base_selenium.scroll()
        self.base_selenium.click(element='orders:right_menu')
        self.base_selenium.click(element='orders:archive')
        self.confirm_popup()
        if check_pop_up:
            if self.base_selenium.wait_element(element='general:confirmation_pop_up'):
                return False
        return True

    def is_order_exist(self, value):
        results = self.search(value=value)
        if len(results) == 0:
            return False
        else:
            if value in results[0].text:
                return True
            else:
                return False

    def is_order_archived(self, value):
        results = self.search(value=value)
        if len(results) == 0:
            return False
        else:
            if value in results[0].text:
                return True
            else:
                return False

    def duplicate_order_from_table_overview(self, number_of_copies):
        self.base_selenium.scroll()
        self.base_selenium.click(element='general:right_menu')
        self.base_selenium.click(element='orders:duplicate')
        self.base_selenium.set_text(
            element='orders:number_of_copies', value=number_of_copies)
        self.base_selenium.click(element='orders:create_copies')
        self.sleep_medium()

    def get_random_order(self):
        self.base_selenium.LOGGER.info(' + Get random order.')
        row = self.get_random_order_row()
        self.get_random_x(row=row)
        return self.base_selenium.get_row_cells_dict_related_to_header(row=row)

    def get_random_order_row(self):
        return self.get_random_table_row(table_element='orders:orders_table')

    def get_orders_duplicate_data(self, order_no):
        self.base_selenium.LOGGER.info(' + Get orders duplicate data with no : {}.'.format(order_no))
        orders = self.search(order_no)
        orders_data = [self.base_selenium.get_row_cells_dict_related_to_header(order) for order in orders[:-1]]
        self.base_selenium.LOGGER.info(' + {} duplicate orders.'.format(len(orders)))
        return orders_data, orders
