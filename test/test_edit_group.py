from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.group_create(Group(name="test"))
    app.group.edit_first_group( Group(name="new", header="new", footer="new"))