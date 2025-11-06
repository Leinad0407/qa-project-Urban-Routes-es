from Test_clases.main_test import TestUrbanRoutes
testUrbanRoutes = TestUrbanRoutes()

try:
    def test_field_directions_panel():
        testUrbanRoutes.open_main_page()
        testUrbanRoutes.number_of_elements_directions_panel()
        testUrbanRoutes.placeholder_from_input()
        testUrbanRoutes.placeholder_to_input()
        testUrbanRoutes.fill_panel_directions_texts()

    def test_mode_options():
        testUrbanRoutes.modes_options()

    def test_transport_cards_field():
        testUrbanRoutes.number_transport_cards()

    def test_phone_number_input():
        testUrbanRoutes.phone_number_field()

    def test_card_number_input():
        testUrbanRoutes.card_confirmation_field()

    def test_message_driver_input():
        testUrbanRoutes.write_driver_message_input()

    def test_requirements_user():
        testUrbanRoutes.requirements()

    def test_close_app():
        testUrbanRoutes.teardown_class()

except Exception as e:
    print(f"Error en la prueba {e}")
    pass
