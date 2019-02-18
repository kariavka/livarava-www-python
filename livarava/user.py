# coding=utf-8
"""
    livarava.user
    ~~~~~~~~~~~~

    LivaRava User

    :copyright: (c) 2019 by Artem Kariavka, LivaRava.
    :license: LivaRava License
"""
from py2neo.ogm import GraphObject, Property

__title__ = 'LivaRava User'
__author__ = 'kariavka'


class User(GraphObject):
    __primarylabel__ = 'user'

    # IDs
    id = Property()
    uid = Property()

    # Datetime
    created = Property()
    updated = Property()
    activated = Property()

    # User
    email = Property()
    password = Property()
    fullname = Property()
    firstname = Property()
    lastname = Property()
    username = Property()
    usertype = Property()
    phone = Property()
    link = Property()

    def __init__(self, node=None):
        super(User, self).__init__(node)
