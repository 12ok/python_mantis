from model.project import Project
import pytest
import data.project


@pytest.mark.parametrize("project", data.project.testdata, ids=[repr(y) for y in data.project.testdata])
def test_add_project(app, project):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.session.login(username, password)
    old_projects = app.project.get_list_project()
    app.project.create_project(project)
    new_projects = app.project.get_list_project()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
