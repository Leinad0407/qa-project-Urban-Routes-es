import Configuration
import data
from Actions_pages_class.main_actions import UrbanRoutesActionsPage

from selenium import webdriver

import time

class TestUrbanRoutes:

    config = Configuration
    data = data
    timeOut = 2

    def __init__(self):
        self.driver = self.setup_clas()
        self.actions = UrbanRoutesActionsPage(self.driver)

    def setup_clas(self):
        options = webdriver.ChromeOptions()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        driver = webdriver.Chrome(options=options)
        return driver

    #Inicialización de la página
    def open_main_page(self):
        self.actions.initialize_page(self.config.URBAN_ROUTES_URL)

    ##Verificacion del panel de direcciones##
    #Verifica que existan los elementos input "Desde" y "Hasta" en el panel de selección de ruta
    def number_of_elements_directions_panel(self):
        current_elements_number = self.actions.get_elements_in_panel_directions()
        expected_elements = 2
        assert current_elements_number == expected_elements, f"El numero de elementos esperado es: {expected_elements} pero se obtuvo: {current_elements_number}"

    # verifica el placeholder del campo from
    def placeholder_from_input(self):
        current_element_placeholder = self.actions.get_placeholder_from_direction()
        expected_element_placeholder = "East 2nd Street, 601"
        assert current_element_placeholder == expected_element_placeholder, f"El placeholder actual para el elemento input es: {current_element_placeholder}, pero se esperaba: {expected_element_placeholder}"

    # verifica el placeholder del campo to
    def placeholder_to_input(self):
        current_element_placeholder = self.actions.get_placeholder_to_direction()
        expected_element_placeholder = "1300 1st St"
        assert current_element_placeholder == expected_element_placeholder, f"El placeholder actual es: {current_element_placeholder}, pero se esperaba: {expected_element_placeholder}"

    #Verificación de textos introducidos en los inputs de direcciones
    def fill_panel_directions_texts(self):
        self.actions.fill_panel_direction()
        current_element_from_text = self.actions.get_text_panel_from_directions()
        current_element_to_text = self.actions.get_text_panel_to_direction()
        expected_element_from_text = "East 2nd Street, 601"
        expected_element_to_text = "1300 1st St"

        assert current_element_from_text == expected_element_from_text, f"El texto actual es: {current_element_from_text}, pero se esperaba: {expected_element_from_text}"
        assert current_element_to_text == expected_element_to_text, f"El texto actual es {expected_element_to_text}, pero se esperaba: {expected_element_to_text}"


    ##Verificacion de modos##
    def modes_options(self):
        current_elements_len = self.actions.get_elements_mode_options()
        expected_elements_len = 3

        current_optimum_mode_text = self.actions.get_text_mode_optimum()
        expected_optimum_mode_text = "Óptimo"

        current_flash_mode_text = self.actions.get_text_mode_flash()
        expected_flash_mode_text = "Flash"

        current_personal_mode_text = self.actions.get_text_mode_personal()
        expected_personal_mode_text = "Personal"

        assert current_elements_len == expected_elements_len, f"El número actual de elementos es: {current_elements_len} pero se esperaba: {expected_elements_len}"
        assert current_flash_mode_text == expected_flash_mode_text, f"El texto actual es: {current_flash_mode_text}, pero es esperaba: {expected_flash_mode_text}"
        assert current_personal_mode_text == expected_personal_mode_text, f"El texto actual es: {current_personal_mode_text}, pero es esperaba: {expected_personal_mode_text}"
        assert current_optimum_mode_text == expected_optimum_mode_text, f"El texto actual es: {current_optimum_mode_text}, pero es esperaba: {expected_optimum_mode_text}"


    ##Verificacion de panel de modos de viaje
    def number_transport_cards(self):
        time.sleep(1)
        elements = self.actions.get_number_transport_cards()
        current_elements = elements
        expected_elements = 6

        assert current_elements == expected_elements, f"El numero actual de transportes es {current_elements} pero se esperaba: {expected_elements}"


    #Verificación numero de telefono
    def phone_number_field(self):
        self.actions.confirmation_reservation_taxi()
        self.actions.click_vehicle_comfort_option()
        self.actions.click_vehicle_comfort_phone_field()
        self.actions.click_input_phone_number_field()
        self.actions.send_phone_number()
        self.actions.confirmation_phone_number()
        self.actions.get_code_number()
        self.actions.confirmation_code_panel()
        current_element_text = self.actions.confirmation_phone_number_panel()
        expected_element_text = "+1 123 123 12 12"

        assert current_element_text == expected_element_text, f"El numero de telefono actual es: {current_element_text}, pero se esperaba: {expected_element_text}"

    #Verificación agregar tarjeta de pago
    def card_confirmation_field(self):
        self.actions.click_page_form_pay_button()
        self.actions.click_add_pay_card_field_page()
        self.actions.click_add_pay_card_number_field()
        self.actions.click_form_pay_card_info()
        self.actions.add_pay_card_code_number()
        self.actions.add_code_card_pay_number()
        self.actions.click_confirmation_card_pay()
        self.actions.close_add_pay_card_window()

        current_element = self.actions.get_pay_type_input_field()
        expected_element = 'Tarjeta'

        assert current_element == expected_element, f"El tipo de pago actual es {current_element}, pero se esperaba: {expected_element}"

    #Verificación del campo, mensaje al conductor
    def write_driver_message_input(self):
        self.actions.write_message_driver_input()
        current_message = self.actions.get_message_text_conductor()
        expected_message = 'Muéstrame el camino'
        assert current_message == expected_message, f"El mensaje al conductor actual es {current_message}, pero se esperaba: {expected_message}"

    #Requisitos del pedido
    def requirements(self):
        self.actions.select_manta_pañuelos()
        self.actions.select_ice_cream_quantity()
        current_element = int(self.actions.get_ice_cream_quantity_value())
        expected_element = 2

        assert current_element == expected_element, f"El numero actual de helados es: ñ{current_element}, pero se esperaba: {expected_element}"

    def teardown_class(cls):
        cls.driver.quit()






