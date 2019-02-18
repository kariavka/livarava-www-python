# coding=utf-8
"""
    livarava.job
    ~~~~~~~~~~~~

    LivaRava Job

    :copyright: (c) 2019 by Artem Kariavka, LivaRava.
    :license: LivaRava License
"""
from py2neo.ogm import GraphObject, Property, RelatedFrom

__title__ = 'LivaRava Job'
__author__ = 'kariavka'


class Job(GraphObject):
    __primarylabel__ = 'job'

    # IDs
    id = Property()
    uid = Property()

    # Datetime
    created = Property()
    updated = Property()

    # Properties
    title = Property()
    main_image_url = Property()
    description = Property()
    summary = Property()
    language = Property()
    meta_title = Property()
    meta_description = Property()
    meta_keywords = Property()
    # author = RelatedFrom('User', 'JOB_AUTHOR')

    def __init__(self, node=None):
        super(Job, self).__init__(node)
