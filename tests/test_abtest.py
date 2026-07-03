from pages.abtest import ABtest

def test_get_heading(driver):
    abtest_page = ABtest(driver)
    abtest_page.open()
    heading = abtest_page.get_heading()
    assert heading in ["A/B Test Control", "A/B Test Variation 1"]

def test_get_paragraph(driver):
    abtest_page = ABtest(driver)
    abtest_page.open()
    paragraph = abtest_page.get_paragraph()
    assert paragraph == "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."