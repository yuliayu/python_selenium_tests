from main.pages import *

# Hover over the avatar and verify profile name
def test_hover(browser):
    hover_page = HoversPage(browser)
    hover_page.open()
    # Verify for each avatar :
    for id in range(1,3):
        hover_page.hover_item(id)
        hover_text=hover_page.get_hover_text(id)
        validation_text="user"+str(id)
        assert validation_text in hover_text
