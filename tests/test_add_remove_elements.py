from pages.add_remove_elements import AddRemoveElementsPage

def test_add_element(driver):
    page = AddRemoveElementsPage(driver)
    page.open()

    page.click_add_element()

    assert page.is_element_present(page.DELETE_BUTTON)

def test_remove_element(driver):
    page = AddRemoveElementsPage(driver)
    page.open()

    page.click_add_element()
    page.click_on_delete_button()

    assert not page.is_element_present(page.DELETE_BUTTON)

def test_add_remove_multiple(driver):
    page = AddRemoveElementsPage(driver)
    page.open()

    for _ in range(5):
        page.click_add_element()

    for _ in range(5):
        page.click_on_delete_button()

    assert not page.is_element_present(page.DELETE_BUTTON)