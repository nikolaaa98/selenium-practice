from pages.context_menu import ContextMenuPage

def test_click_on_alert_ok(driver):
    context_menu_page = ContextMenuPage(driver)
    context_menu_page.open()

    assert context_menu_page.get_heading_text() == "Context Menu"
    assert context_menu_page.is_element_present(context_menu_page.HOTSPOT)
    
    context_menu_page.right_click_on_hotspot()
    context_menu_page.click_on_alert_ok()