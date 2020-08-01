from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.group_create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    grup_new = Group(name="New group")
    app.group.modify_group_by_id(group.id, grup_new)
    assert len(old_groups)  == app.group.count()
    if check_ui:
        old_groups = db.get_group_list()
        new_groups = app.group.get_group_list()
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
