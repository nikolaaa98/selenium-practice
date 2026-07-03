from pages.checkboxes import CheckboxesPage

def test_click_on_checkbox(driver):
    checkboxes_page = CheckboxesPage(driver)
    checkboxes_page.open()
    
    # Click on the first checkbox (index 0)
    checkboxes_page.click_on_checkbox(0)
    
    # Click on the second checkbox (index 1)
    checkboxes_page.click_on_checkbox(1)
    
    # Add assertions here to verify the state of the checkboxes if needed
    checkboxes_page.unclick_on_checkbox(0)
    checkboxes_page.unclick_on_checkbox(1)

