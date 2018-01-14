from .base_page_object import BasePage


class TablesPage(BasePage):
    locators={
        "table2":"//table[@id='table2']",
        "last_name":"//table[@id='table2']//span[@class='last-name']",
        "last_name_cell":"//table[@id='table2']//td[1]"
    }

    def open(self):
        self.browser.get("http://the-internet.herokuapp.com/tables")

# Sort Last Name column of Example 2 table in ASC order
    def sort_asc(self):
        last_name=self.find(TablesPage.locators["last_name"])
        last_name.click()

# Sort Last Name column of Example 2 table in DESC order
    def sort_desc(self):
        last_name=self.find(TablesPage.locators["last_name"])
        #Sort list in ASC order
        last_name.click()
        #Sort list in DESC order
        last_name.click()

# Get the Last Name column values
    def get_names_list(self):
        names=[]
        rows=self.browser.find_elements_by_xpath(TablesPage.locators["last_name_cell"])
        for cell in rows:
            text = cell.text
            names.append(text)
        return names
