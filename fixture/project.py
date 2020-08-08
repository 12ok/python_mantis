from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def open_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Create New Project']").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_project_page()
        self.open_create_project_page()
        self.fill_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def fill_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").send_keys(project.description)

    project_cache = None

    def get_list_project(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_page()
            self.open_project_page()
            self.project_cache = []
            table = wd.find_element_by_css_selector("table.width100[cellspacing='1']")
            rows = table.find_elements_by_xpath(".//tr[contains(@class, 'row')]")
            del rows[0]
            for row in rows:
                name = row.find_element_by_css_selector("td:nth-child(1)").text
                description = row.find_element_by_css_selector("td:nth-child(5)").text
                href = row.find_element_by_css_selector("td:nth-child(1) a").get_attribute("href")
                id = href[href.index('=') + 1:]
                self.project_cache.append(Project(id=id, name=name, description=description))
        return list(self.project_cache)
