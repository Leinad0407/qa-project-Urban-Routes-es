import data
from Page_elements_path_class.main_elements_path import  UrbanRoutes_elments_path
from Service import code_number

import time

class UrbanRoutesActionsPage:

    data = data
    elementPath = UrbanRoutes_elments_path()
    timeOut = 1

    def __init__(self, driver):
        self.driver = driver
        self.code_number = None

    def initialize_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def fill_panel_form_from_direction(self):
        element = self.driver.find_element(*self.elementPath.reservationForm_from)
        element.send_keys(*self.data.address_from)
        self.driver.implicitly_wait(self.timeOut)

    def get_text_panel_from_directions(self):
        element = self.driver.find_element(*self.elementPath.reservationForm_from)
        element_text = element.get_attribute("value")
        return element_text

    def get_text_panel_to_direction(self):
        element = self.driver.find_element(*self.elementPath.reservationForm_to)
        element_text = element.get_attribute("value")
        return element_text

    def fill_panel_form_to_direction(self):
        element = self.driver.find_element(*self.elementPath.reservationForm_to)
        element.send_keys(*self.data.address_to)
        self.driver.implicitly_wait(self.timeOut)

    def get_placeholder_from_direction(self):
        element = self.driver.find_element(*self.elementPath.reservationForm_from)
        self.driver.implicitly_wait(self.timeOut)
        return element.get_attribute('placeholder')

    def get_placeholder_to_direction(self):
        element = self.driver.find_element(*self.elementPath.reservationForm_to)
        self.driver.implicitly_wait(self.timeOut)
        return element.get_attribute('placeholder')

    def get_elements_in_panel_directions(self):
        elements = self.driver.find_elements(*self.elementPath.destination_picker_inputs)
        return len(elements)

    def fill_panel_direction(self):
        self.fill_panel_form_from_direction()
        self.fill_panel_form_to_direction()

    def get_elements_mode_options(self):
        elements = self.driver.find_elements(*self.elementPath.modes_options)
        return len(elements)

    def get_text_mode_optimum(self):
        element = self.driver.find_element(*self.elementPath.mode_panel_selection_optimum)
        self.driver.implicitly_wait(self.timeOut)
        return element.text

    def get_text_mode_flash(self):
        element = self.driver.find_element(*self.elementPath.mode_panel_selection_flash)
        self.driver.implicitly_wait(self.timeOut)
        return  element.text

    def get_text_mode_personal(self):
        element = self.driver.find_element(*self.elementPath.mode_panel_selection_personal)
        self.driver.implicitly_wait(self.timeOut)
        return element.text

    def get_number_transport_cards(self):
        elements = self.driver.find_elements(*self.elementPath.transport_card_options)
        return len(elements)

    def select_mode_flash(self):
        element = self.driver.find_element(*self.elementPath.mode_panel_selection_flash)
        element.click()

    def select_taxi_option(self):
        element = self.driver.find_element(*self.elementPath.panel_taxi_option)
        element.click()

    def click_confirmation_button(self):
        element = self.driver.find_element(*self.elementPath.panel_confirmation_button)
        element.click()

    def confirmation_reservation_taxi(self):
        self.select_mode_flash()
        self.click_confirmation_button()

    def click_vehicle_comfort_option(self):
        element = self.driver.find_element(*self.elementPath.panel_vehicle_comfort_selection)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    def click_vehicle_comfort_phone_field(self):
        element = self.driver.find_element(*self.elementPath.panel_number_field)
        element.click()

    def click_input_phone_number_field(self):
        element = self.driver.find_element(*self.elementPath.card_phone_number_field)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    def send_phone_number(self):
        element = self.driver.find_element(*self.elementPath.card_phone_number_field)
        input_element = self.driver.find_element(*self.elementPath.card_phone_number_input_text)
        element.click()
        input_element.send_keys(*self.data.phone_number)

    def confirmation_phone_number(self):
        element = self.driver.find_element(*self.elementPath.card_phone_number_button_confirmation)
        element.click()

    def get_code_number(self):
        self.driver.implicitly_wait(self.timeOut)
        code = code_number.get_phone_number_code(self.driver)
        self.code_number = code
        self.driver.implicitly_wait(self.timeOut)

    def write_code_number_confirmation_field(self):
        element = self.driver.find_element(*self.elementPath.card_input_code_confirmation)
        element.send_keys(self.code_number)
        self.driver.implicitly_wait(self.timeOut)

    def click_confirmation_code_button(self):
        element = self.driver.find_element(*self.elementPath.card_confirmation_code_button)
        element.click()

    #Acciones globales para confiramcion de codigo de verificación
    def confirmation_code_panel(self):
        self.write_code_number_confirmation_field()
        self.click_confirmation_code_button()
        self.driver.implicitly_wait(self.timeOut)

    def click_page_form_pay_button(self):
        element = self.driver.find_element(*self.elementPath.page_form_pay_input)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    def click_add_pay_card_field_page(self):
        element = self.driver.find_element(*self.elementPath.page_add_pay_card)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    #Card pay information
    def click_add_pay_card_number_field(self):
        element = self.driver.find_element(*self.elementPath.input_add_card_pay_number_field)
        element.send_keys(*self.data.card_number)

    def click_form_pay_card_info(self):
        element = self.driver.find_element(*self.elementPath.form_pay_card)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    def add_pay_card_code_number(self):
        element = self.driver.find_element(*self.elementPath.form_pay_card)
        element.click()

    def add_code_card_pay_number(self):
        element = self.driver.find_element(*self.elementPath.input_code_card)
        element.send_keys(self.code_number)

    def click_confirmation_card_pay(self):
        element = self.driver.find_element(*self.elementPath.confirmation_card_info_button)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    # mensaje para el conductor
    def write_message_driver_input(self):
        element = self.driver.find_element(*self.elementPath.input_message_driver_field)
        element.send_keys(*self.data.message_for_driver)

    def get_message_text_conductor(self):
        element = self.driver.find_element(*self.elementPath.input_message_driver_field)
        return element.get_attribute('value')

    #Selección de manta y pañuelos
    def select_manta_pañuelos(self):
        element = self.driver.find_element(*self.elementPath.switch_manta_pañuelos)
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    #Selección de heado
    def select_ice_cream_quantity(self):
        element = self.driver.find_element(*self.elementPath.get_ice_cream_quantity)
        element.click()
        element.click()
        self.driver.implicitly_wait(self.timeOut)

    def get_ice_cream_quantity_value(self):
        element = self.driver.find_element(*self.elementPath.get_ice_cream_quantity_value)
        return element.text

    def confirmation_phone_number_panel(self):
        element = self.driver.find_element(*self.elementPath.phone_number_confirmation_field)
        self.driver.implicitly_wait(self.timeOut)
        return element.text

    def get_pay_type_input_field(self):
        element = self.driver.find_element(*self.elementPath.card_number_confirmation_field)
        return element.text

    def close_add_pay_card_window(self):
        element = self.driver.find_element(*self.elementPath.close_pay_card_window)
        element.click()


