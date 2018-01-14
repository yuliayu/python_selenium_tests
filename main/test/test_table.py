from main.pages import *

# Verify sorting by Last Name ASC scenario
def test_sorting_asc(browser):
    table_page=TablesPage(browser)
    table_page.open()
    table_page.sort_asc()
    names = table_page.get_names_list()
    for i in range (1,len(names)):
        assert names[i] > names[i-1]

# Verify sorting by Last Name DESC scenario
def test_sorting_desc(browser):
    table_page=TablesPage(browser)
    table_page.open()
    table_page.sort_desc()
    names = table_page.get_names_list()
    for i in range (1,len(names)):
        assert names[i] < names[i-1]

