# -*- coding: utf-8 -*-

from model.group import Group

def test_add_empty_group(app):
    app.group.group_create( Group(name="", header="", footer=""))

def test_add_group(app):
    app.group.group_create( Group(name="griou", header="ytu", footer="rtyw"))
