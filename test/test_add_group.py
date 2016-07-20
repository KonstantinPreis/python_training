# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("1q2w", "11", "22"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))



