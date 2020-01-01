elements = {
    'general': {
        'child_table_arrow': {'method': 'class_name',
                              'value': 'm-datatable__toggle-subtable',
                              'order': 0},
        'table_child': {'method': 'class_name', 'value': 'dataTable', 'order': 1},

        'span': {'method': 'tag_name',
                 'value': 'span',
                 'order': 0},
        'li': {'method': 'tag_name',
                 'value': 'li',
                 'order': 0},
        'tag': {'method': 'tag_name',
                 'value': 'tag',
                 'order': 0},

        'search': {'method': 'id',
                   'value': 'generalSearch'},
        'table': {'method': 'id',
                  'value': 'table'},
        'table_child': {"method": "class_name",
                        "value": "dataTable",
                        "order": 1
                        },
        'save': {'method': 'class_name',
                 'value': 'btn-primary',
                 'order': 0},
        'cancel': {'method': 'class_name',
                   'value': 'btn-secondary',
                   'order': 1},
        'confirmation_pop_up': {
            'method': 'id',
            'value': 'swal2-title'},

        'confirm_pop': {'method': 'class_name',
                        'value': 'btn-success',
                        'order': 0},
        'confirm_cancel': {'method': 'class_name',
                           'value': 'btn-secondary',
                           'order': 0},
        'cant_delete_message': {'method': 'id',
                                'value': 'swal2-title'},
        'drop_down': {'method': 'class_name',
                      'value': 'ng-select',
                      'order': 0},
        'drop_down_options': {'method': 'class_name',
                              'value': 'ng-option'},
        'drop_down_div': {'method': 'class_name',
                          'value': 'ng-dropdown-panel-items',
                          'order': 0},
        'input': {'method': 'tag_name',
                  'value': 'input',
                  'order': 0},
        'menu_filter_view': {'method': 'id',
                             'value': 'custom-accordion-panel'},
        'filter': {'method': 'tag_name',
                   'value': 'span',
                   'order': 0},
        'filter_apply_btn': {'method': 'class_name',
                             'value': 'btn-primary',
                             'order': 0},
        # 'filter_reset_btn': {'method': 'class_name',
        #              'value': 'btn-secondary',
        #              'order': 1},
        'ng_values': {'method': 'class_name',
                      'value': 'ng-value',
                      'order': -1},
        'cancel_span': {'method': 'tag_name',
                        'value': 'span',
                        'order': 0},
        'checkbox': {'method': 'class_name',
                     'value': 'm-checkbox',
                     'order': 0},
        'child_table_arrow': {'method': 'class_name',
                              'value': 'm-datatable__toggle-subtable',
                              'order': 0},
        'label': {'method': 'tag_name',
                  'value': 'label',
                  'order': 0},
        'right_menu': {'method': 'xpath',
                       'value': '//*[@id="custom-accordion-panel"]/div/a/i'},
        'archive': {'method': 'link_text',
                    'value': 'Archive'},
        'alert_confirmation': {'method': 'id',
                               'value': 'noty_layout__topCenter'},
        'oh_snap_msg': {'method': 'id',
                        'value': 'ohSnapMsg'},
        'table_cells': {'method': 'tag_name',
                        'value': 'td',
                        'order': -1},
        'archived': {'method': 'link_text',
                     'value': 'Archived'},
        'restore': {'method': 'link_text',
                    'value': 'Restore'},
        'active': {'method': 'link_text',
                   'value': 'Active'},
        'delete': {'method': 'link_text',
                   'value': 'Delete'},
        'xslx': {'method': 'link_text',
                 'value': 'XSLX'},
        'table_info': {'method': 'id',
                       'value': 'table_info'},
        'filter_btn': {'method': 'id',
                       'value': 'filter_btn'},
        'filter_reset_btn': {'method': 'id',
                             'value': 'reset_btn'},
        'save_and_complete': {'method': 'id',
                              'value': 'submitWithVersion'
                              },
        'save_form': {'method': 'id',
                      'value': 'saveButton'},
        'col_6': {'method': 'class_name',
                  'value': 'col-md-6',
                  'order': -1},
        'configurations': {
            'method': 'xpath',
            'value': '//*[@id="custom-accordion-panel"]//a[4]'
        },
        'configurations_archived': {
            'method': 'xpath',
            'value': '//*[@id="tabs"]/li[2]/a'
        },
       'configure_table': {'method': 'xpath',
                            'value': '//a[@class="m-dropdown__toggle btn no-padding"]'},
       'configure_table_items': {'method': 'xpath',
                            'value': '//ul[@class="m-nav sortable sortable-table1 ui-sortable"]'},
       'apply_configure_table': {'method': 'xpath',
                            'value': '//a[@class="btn btn-primary m-btn pull-right"]'},
        'overview': {'method': 'xpath',
                     'value': "//span[contains(text(),'Overview')]"},
        'confirm_overview': {'method': 'xpath',
                             'value': "//div[contains(@class, 'swal2-actions')]//button[1]"},
        'cancel_overview': {'method': 'xpath',
                            'value': "//div[contains(@class, 'swal2-actions')]//button[2]"},
    },
    'login': {
        'username': {'method': 'name',
                     'value': 'username',
                     'order': 0},
        'password': {'method': 'name',
                     'value': 'password',
                     'order': 0},
        'login_btn': {'method': 'id',
                      'value': 'm_login_signin_submit'},
        'refresh': {'method': 'xpath',
                    'value': '/html/body/div[3]/div/div[2]/div[2]/button'},
        'logout_btn': {'method': 'xpath',
                    'value': '//a[@class="btn m-btn--pill btn-secondary m-btn m-btn--custom m-btn--label-brand m-btn--bolder"]'},

    },

    'articles': {
        'article_table': {'method': 'id',
                          'value': 'table'},
        'article_edit_button': {'method': 'tag_name',
                                'value': 'a',
                                'order': 2},
        'article_archive_button': {'method': 'tag_name',
                                   'value': 'a',
                                   'order': 0},
        'article_archive_dropdown': {'method': 'link_text',
                                     'value': 'Archive'},
        'confirm_archive': {'method': 'class_name',
                            'value': 'swal2-confirm',
                            'order': 0},
        'cancel_archive': {'method': 'class_name',
                           'value': 'swal2-cancel',
                           'order': 0},
        'new_article': {'method': 'link_text',
                        'value': 'New Article'},
        'archived': {'method': 'link_text',
                     'value': 'Archived'},
        'archive': {'method': 'link_text',
                    'value': 'Archive'},
        'active': {'method': 'link_text',
                   'value': 'Active'},
        'restore': {'method': 'link_text',
                    'value': 'Restore'},
        'delete': {'method': 'link_text',
                   'value': 'Delete'},
        'right_menu': {'method': 'xpath',
                       'value': '//*[@id="custom-accordion-panel"]/div/a/i'},
        'alert_confirmation': {'method': 'id',
                               'value': 'noty_layout__topCenter'},
                               
        'unit_field_options': {'method': 'xpath', 'value': '//*[@id="5_field"]//a'},
        'unit_field_archive': {'method': 'xpath', 'value': '//*[@id="5_field"]//li[1]/a'},
        'unit_field_restore': {'method': 'xpath', 'value': '//*[@id="5_field"]//li[2]/a'},

        'comment_field_options': {'method': 'xpath', 'value': '//*[@id="7_field"]//a'},
        'comment_field_archive': {'method': 'xpath', 'value': '//*[@id="7_field"]//li[1]/a'},
        'comment_field_restore': {'method': 'xpath', 'value': '//*[@id="7_field"]//li[2]/a'},

        'related_article_field_options': {'method': 'xpath', 'value': '//*[@id="18_field"]//a'},
        'related_article_field_archive': {'method': 'xpath', 'value': '//*[@id="18_field"]//li[1]/a'},
        'related_article_field_restore': {'method': 'xpath', 'value': '//*[@id="18_field"]//li[2]/a'},
    },
    'article': {
        'unit': {'method': 'id',
                 'value': 'unitfield'},
        'material_type': {'method': 'id',
                          'value': 'materialType'},
        'material_type_options': {'method': 'class_name',
                                  'value': 'ng-option'},
        'no': {'method': 'id',
               'value': 'Nofield'},
        'comment': {'method': 'id',
                    'value': 'comment'},
        'name': {'method': 'id',
                 'value': 'namefield'},

        'filter_test_plan': {'method': 'id',
                             'value': 'testPlansfield'},
        'filter_actions': {'method': 'class_name',
                           'value': 'actions',
                           'order': 0},
        'related_article': {'method': 'id',
                            'value': 'selectedArticles'},
        'field': {'method': 'id',
                  'value': 'field'},
        'field_items': {'method': 'class_name',
                        'value': 'padding',
                        'order': -1}

    },
    'test_plans': {
        'test_plans_table': {'method': 'id',
                             'value': 'table'},
        'test_plans_edit_button': {'method': 'tag_name',
                                   'value': 'a',
                                   'order': 1},
        'new_test_plan': {'method': 'link_text',
                          'value': 'New Test Plan'}
    },

    'test_units': {
        'test_units_table': {'method': 'id',
                             'value': 'table'},
        'right_menu': {'method': 'xpath',
                       'value': '//*[@id="custom-accordion-panel"]/div/a/i'},
        'archive': {'method': 'link_text',
                    'value': 'Archive'},
        'version_table': {'method': 'link_text',
                        'value': 'Versions'},
        'testunit_menu': {'method': 'css_selector',
                          'value': '[class="dropdown "]'},
        'versions': {'method': 'id',
                     'value': 'main_table_version'},
        'archived': {'method': 'link_text',
                     'value': 'Archived'},
        'restore': {'method': 'link_text',
                    'value': 'Restore'},
        'active': {'method': 'link_text',
                   'value': 'Active'},
        'new_testunit': {'method': 'link_text',
                         'value': 'New Test Unit'},
        'qualitative_value': {'method': 'id',
                              'value': 'textValueArrayfield'}
    },

    'test_plan': {
        'no': {'method': 'id',
               'value': 'numberfield'},
        'test_plan': {'method': 'id',
                      'value': 'testPlan'},
        'material_type': {'method': 'xpath',
                          'value': '//*[@id="materialTypefield"]'},
        'material_type_options': {'method': 'class_name',
                                  'value': 'ng-option'},
        'article': {'method': 'css_selector',
                    'value': '#selectedArticles > div'
                    },
        'article_options': {'method': 'class_name',
                            'value': 'ng-option'},
        'next': {'method': 'link_text',
                 'value': 'Next'},
        'test_units': {'method': 'id',
                       'value': 'selectedTestUnitsfield'},
        # 'add': {'method': 'class_name',
        #         'value': 'btn-primary',
        #         'order': 0},
        'save_btn': {'method': 'id',
                     'value': 'save_btn'},
        'add_test_units': {'method': 'id',
                           'value': 'first-col'},
        'testunit_upper_limit': {'method': 'class_name',
                                 'value': '//*[@id="88"]/div[2]/div/div[3]/input'},
        'testunit_lower_limit': {'method': 'xpath',
                                 'value': '//*[@id="88"]/div[2]/div/div[4]/input'},
        'testunits_selection': {'method': 'id',
                                'value': 'test_unit_selection_tab'},
        'delete_first_test_unit_btn': {'method': 'xpath',
                                       'value': '//*[@id="remove_testunit"]'},
        'testunit_label': {'method': 'class_name',
                           'value': 'm-portlet__head-text',
                           'order': 1},
        'table_card_switcher': {'method': 'id',
                                'value': 'table-switcher'},
        'testunits_table': {'method': 'id',
                            'value': 'table-with-add'},
        'row_delete_button': {'method': 'class_name',
                              'value': 'flaticon-close',
                              'order': 0},
        'cancel_button': {'method': 'class_name',
                          'value': 'swal2-cancel',
                          'order': 0},
        'ok': {'method': 'class_name',
               'value': 'swal2-confirm',
               'order': 0},
    },

    'test_unit': {
        'no': {'method': 'id',
               'value': 'numberfield'},
        'material_type': {'method': 'xpath',
                          'value': '//*[@id="materialTypefield"]'},
        'material_type_options': {'method': 'class_name',
                                  'value': 'ng-option'},
        'method': {
            'method': 'id',
            'value': 'methodfield'
        },
        'material_type_by_id': {
            'method': 'id',
            'value': 'selectedMaterialTypes'
        },
        'testunit_name': {
            'method': 'id',
            'value': 'namefield'
        },
        'testunit_number': {
            'method': 'id',
            'value': 'numberfield'
        },
        'category': {
            'method': 'id',
            'value': 'category'
        },
        'type': {
            'method': 'id',
            'value': 'typefield'
        },
        'iteration': {
            'method': 'id',
            'value': 'iterationsfield'
        },
        'use_specification': {'method': 'id',
                              'value': 'useSpec'},
        'use_quantification': {'method': 'id',
                               'value': 'useQuantification'},
        'spec_upper_limit': {'method': 'id',
                             'value': 'upperLimitfield'},
        'spec_lower_limit': {'method': 'id',
                             'value': 'lowerLimitfield'},
        'spec_unit': {'method': 'id',
                      'value': 'unitfield'},
        'spec_unit_preview': {'method': 'css_selector',
                               'value': '[class="form-control field-with-scrips"]'},
        'quan_upper_limit': {'method': 'id',
                             'value': 'quantificationUpperLimitfield'},
        'quan_lower_limit': {'method': 'id',
                             'value': 'quantificationLowerLimitfield'},
        'quan_unit': {'method': 'id',
                      'value': 'quantificationUnitfield'},
        'selected_cons': {'method': 'id',
                          'value': 'selectedConcs'},
        'qualitative_value': {'method': 'id',
                              'value': 'textValueArrayfield'}
    },
    'orders': {
        'orders_table': {'method': 'id',
                         'value': 'table'},
        'orders_edit_button': {'method': 'tag_name',
                               'value': 'a',
                               'order': 4},
        'new_order': {'method': 'link_text',
                      'value': 'New Order'},
        'right_menu': {'method': 'xpath',
                       'value': '//*[@id="custom-accordion-panel"]/div/a/i'},
        'archive': {'method': 'link_text',
                    'value': 'Archive'},
        'analysis-confirmation': {
            'method': 'class_name',
            'value': 'swal2-header'},
        'duplicate': {'method': 'link_text',
                      'value': 'Duplicate'},
        'number_of_copies': {'method': 'id',
                             'value': 'numberOfCopies'},
        'create_copies': {'method': 'id',
                          'value': 'create_copies_id'},
        'save_order': {'method': 'id',
                       'value': 'button_save_order'},
        'filter_order_no': {'method': 'id',
                            'value': 'orderNofield'},
        'analysis_filter': {'method': 'id',
                            'value': 'analysisfield'},
        'order_filter': {'method': 'id',
                         'value': 'orderNofield'},
        'contact_filter': {'method': 'id',
                           'value': 'companyfield'},
        'changed_by': {'method': 'id',
                       'value': 'lastModifiedUserfield'},
        'material_type_filter': {'method': 'id',
                                 'value': 'materialTypefield'},
        'article_filter': {'method': 'id',
                           'value': 'articlefield'},
        'chnaged_on_filter': {'method': 'id',
                              'value': 'start_createdAt'},
        'test_date_filter': {'method': 'id',
                             'value': 'start_testDate'},
        'shipment_date_filter': {'method': 'id',
                                 'value': 'start_shipmentDate'}
    },

    'audit_trail': {
        'filter_action_date': {'method': 'id', 'value': 'start_createdAt'},
        'filter_changed_by': {'method': 'id', 'value': 'createdByfield'},
        'filter_action': {'method': 'id', 'value': 'actionfield'},
        'filter_entity': {'method': 'id', 'value': 'entityfield'},
        'filter_entity_number': {'method': 'id', 'value': 'entityNumberfield'},
    },

    'order': {
        'order': {'method': 'id',
                  'value': 'orderTypefield'},
        'material_type': {'method': 'xpath',
                          'value': '//td//*[@id="materialType"]'},
        'article': {'method': 'xpath',
                    'value': '//td//*[@id="article"]'},
        'departments': {'method': 'xpath',
                        'value': '//td//*[@id="departments"]'},

        'auto_fill': {'method': 'xpath', 'value': '//*[@id="field"]/div[2]/div/span'},
        'auto_fill_container': {'method': 'xpath', 'value': '//*[@id="field"]/div[2]'},

        'contact': {'method': 'id',
                    'value': 'contact'},
        'tests': {'method': 'id',
                  'value': 'tests'},
        'test_plan': {'method': 'xpath',
                      'value': '//td//*[@id="testPlans"]'},
        'test_unit': {'method': 'xpath',
                      'value': '//td//*[@id="testUnits"]'},
        'test_plan_btn': {'method': 'tag_name',
                          'value': 'span',
                          'order': 0},
        'test_unit_btn': {'method': 'tag_name',
                          'value': 'span',
                          'order': 1},

        'save_btn': {'method': 'id',
                     'value': 'button_save_order'},

        'no': {'method': 'id',
               'value': 'orderNoWithYearfield'},

        'cancel_btn': {'method': 'id',
                       'value': 'button_cancel_order'},
        'value': 'orderNoWithYearfield',
        'cancel_button': {'method': 'class_name',
                          'value': 'swal2-cancel',
                          'order': 0},
        'ok': {'method': 'class_name',
               'value': 'swal2-confirm',
               'order': 0},

        'cancel': {'method': 'class_name',
                   'value': 'btn-secondary',
                   'order': 1},

        'order_number': {'method': 'id',
                         'value': 'orderNoWithYearfield'},
        'order_number_add_form': {'method': 'id',
                                  'value': 'selectedOrderNofield'},
        'shipment_date': {'method': 'id',
                          'value': 'date_shipmentDate'},
        'test_date': {'method': 'id',
                      'value': 'date_testDate'},
        'save': {'method': 'class_name',
                 'value': 'btn-primary',
                 'order': 1},
        'duplicate_table_view': {'method': 'id',
                                 'value': 'duplicate_table_view'},
        'delete_table_view': {'method': 'id',
                              'value': 'delete_table_view'},
        'change_view': {'method': 'class_name',
                        'value': 'icon-views',
                        'order': 0
                        },

        'suborder_list': {'method': 'class_name',
                          'value': 'flaticon-signs',
                          'order': 0},
        'suborder_table': {'method': 'id',
                           'value': 'table-with-add'},
        'add_new_item': {'method': 'class_name',
                         'value': 'addNewItem',
                         'order': 0},
        'order_no_error_message': {'method': 'xpath',
                                   'value': '//*[@id="field"]/div[3]/div/span'},
        'confirm_pop': {'method': 'class_name',
                        'value': 'btn-success',
                        'order': 0},
        'confirm_cancel': {'method': 'class_name',
                           'value': 'btn-secondary',
                           'order': 2},
        'analysis': {
            'filter_order_no': {
                'method': 'id',
                'value': 'orderNofield'}
        },
        'filter_analysis_no': {
            'method': 'id',
            'value': 'nofield'
        },
    },

    'header': {
        'header_button': {'method': 'xpath',
                  'value': '//*[@class="m--img-rounded m--marginless m--img-centered"]'},
        'user_management_button': {'method': 'xpath',
                  'value': '//*[contains(text(),"User Management")]'},
        'roles_and_permissions_button': {'method': 'xpath',
                  'value': '//*[contains(text(),"Role & Permissions")]'},
        'myprofile_button': {'method': 'xpath',
                  'value': '//*[contains(text(),"My Profile")]'},
        'companyprofile_button': {'method': 'xpath',
                  'value': '//*[contains(text(),"Company Profile")]'},

    },
   'user_management': {
       'right_menu': {'method': 'xpath',
                 'value': '//i[@class="flaticon-grid-menu-v2"]'},

       'archive': {'method': 'link_text',
                 'value': 'Archive'},

       'archived': {'method': 'link_text',
                 'value': 'Archived'},

       'restore': {'method': 'link_text',
                 'value': 'Restore'},

       'active': {'method': 'link_text',
                 'value': 'Active'},

       'user_table': {'method': 'id',
                 'value': 'table'},

       'user_name': {'method': 'id',
                 'value': 'usernamefield'},
        'user_number': {'method': 'id',
                 'value': 'userIdfield'},

       'user_role': {'method': 'xpath',
                     'value': '//*[@class="ng-input"]'},
       'user_email': {'method': 'id',
                     'value': 'emailfield'},
       'user_password': {'method': 'id',
                     'value': 'password'},
       'user_confirm_password': {'method': 'id',
                     'value': 'confirmPassword'},
       'create_user_button': {'method': 'xpath',
                     'value': '//*[contains(text(),"New User")]'},
       'save_btn': {'method': 'id',
                 'value': 'saveButton'},

       'filter_number': {'method': 'id',
                 'value':'userIdfield'},

       'filter_contact': {'method': 'xpath',
                   'value': '//*[@id="supplierfield"]//input'},

       'filter_changed_by': {'method': 'xpath',
                        'value': '//*[@id="lastModifiedUserfield"]//input'},

       'filter_created_on': {'method': 'id',
                 'value':'start_createdAt'},

       'filter_name': {'method': 'id',
                 'value':'usernamefield'},
       'filter_email': {'method': 'id',
                 'value':'emailfield'},

       'filter_role': {'method': 'xpath',
                 'value':'//ng-select[@id="rolefield"]//input'},

       'filter_reset_btn': {'method': 'id',
                 'value':'reset_btn'},
       'delete': {'method': 'link_text',
                 'value': 'Delete'},
       
       'overview_btn': {'method': 'xpath',
                               'value': '//span[contains(text(),"Overview")]'},
       'filter_configuration_btn': {'method': 'id',
                               'value': 'settings'},
       'switch_name_btn': {'method': 'xpath',
                               'value': '//div[@id="name"]//label[@class="switch"]'},
       'filter_configuration_save_btn': {'method': 'xpath',
                               'value': '//div[@id="filterConfig"]//button[@class="btn btn-primary"][contains(text(),"Save")]'},
       'content': {'method': 'xpath',
                              'value': '//div[@class="m-accordion__item-content"]'},

   },
    'contacts':{
        'new_contact': {'method': 'xpath',
                        'value': '//span[contains(text(),"New Contact")]'},

       'confirm_pop': {'method': 'class_name',
                        'value': 'btn-success',
                        'order': 0},

       'alert_confirmation': {'method': 'id',
                               'value': 'noty_layout__topCenter'},

       'overview_btn': {'method': 'xpath',
                               'value': '//span[contains(text(),"Overview")]'},

       'cancel': {'method': 'id',
                        'value': 'cancelButton'},
    },

    'contacts':{
        'new_contact': {'method': 'xpath',
                        'value': '//span[contains(text(),"New Contact")]'},
    },


    'contacts': {
        'contact_archive_button': {'method': 'tag_name',
                                   'value': 'a',
                                   'order': 0},
        'contact_table': {'method': 'id',
                          'value': 'table'},
        'new_contact': {'method': 'id',
                        'value': 'add-btn'},
       'delete_contact_msg': {'method': 'id',
                            'value': 'swal2-title'},
       'confirmation_button': {'method': 'xpath',
                            'value': '//button[@class="swal2-confirm btn btn-success m-btn m-btn--custom"]'},
       'edit_button': {'method': 'xpath',
                            'value': '//button[@class="mr-auto ng-star-inserted"]'},
        'contacts_table': {'method': 'id',
                           'value': 'table'},
    },

    'contact': {
        'name': {'method': 'id',
                 'value': 'namefield'},
        'no': {'method': 'id',
               'value': 'companyNofield'},
        'address': {'method': 'id',
               'value': 'addressfield'},
        'postalcode': {'method': 'id',
               'value': 'postalCodefield'},
        'location': {'method': 'id',
               'value': 'locationfield'},
        'country': {'method': 'id',
               'value': 'selectedcountryfield'},
        'email': {'method': 'id',
               'value': 'emailfield'},
        'phone': {'method': 'id',
               'value': 'phonefield'},
        'skype': {'method': 'id',
               'value': 'skypefield'},
        'website': {'method': 'id',
               'value': 'websitefield'},
        'departments': {'method': 'id',
               'value': 'departmentsfield'},
        'contacttype': {'method': 'id',
               'value': 'contactType'},
        'contacttype-isClient': {'method': 'id',
               'value': 'isClient'},
        'contacttype-isSupplier': {'method': 'id',
               'value': 'isSupplier'},
        'contacttype-isLaboratory': {'method': 'id',
               'value': 'isLaboratory'},
        'save': {'method': 'class_name',
                 'value': 'btn-primary',
                 'order': 1}, 
        'contact_persons': {'method': 'id',
                 'value': 'contact_persons_page'},
        'delete_table_view': {'method': 'id',
                 'value': 'delete_table_view'},
        'add_another_item': {'method': 'class_name',
                     'value': 'addNewItem',
                     'order': 0},
        'contact_persons_table': {'method': 'id',
                     'value': 'table-with-add'},
       'departments_field_tags': {'method': 'xpath',
                     'value': '//div[@class="ng2-tags-container"]'},
       'departments_tag': {'method': 'xpath',
                     'value': '//div[@class="tag__text inline"]'},
       'is_client_checkbox': {'method': 'xpath',
                     'value': '//label[@id="isClient"]//input[@type="checkbox"]'},
       'is_supplier_checkbox': {'method': 'xpath',
                     'value': '//label[@id="isSupplier"]//input[@type="checkbox"]'},
       'is_laboratory_checkbox': {'method': 'xpath',
                     'value': '//label[@id="isLaboratory"]//input[@type="checkbox"]'},
       'delete_person_button': {'method': 'id',
                     'value': 'delete_table_view'}

    }
}

