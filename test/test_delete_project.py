from model.project import Project
import random


def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.session.login(username, password)
    if len(app.project.get_list_project()) == 0:
        app.project.create_project(Project(name="First project"))
    old_projects = app.soap.get_project_list(username, password, app.base_url)
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_project_list(username, password, app.base_url)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
