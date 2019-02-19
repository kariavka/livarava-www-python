# coding=utf-8
"""
    livarava.job
    ~~~~~~~~~~~~

    LivaRava Job

    :copyright: (c) 2019 by Artem Kariavka, LivaRava.
    :license: LivaRava License
"""
from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

__title__ = 'LivaRava Job'
__author__ = 'kariavka'


class Job(GraphObject):
    __primarylabel__ = 'job'
    __primarykey__ = '__id__'

    # IDs
    id = None
    uid = Property()

    # Datetime
    created = Property()
    updated = Property()

    # Properties
    title = Property()
    header = Property()
    image_url = Property()
    description = Property()
    summary = Property()
    language = Property()

    # Meta
    meta_title = Property()
    meta_description = Property()
    meta_keywords = Property()
    meta_image_url = Property()

    # Relationships
    author = RelatedTo('User', 'JOB_AUTHOR')

    @property
    def _id(self):
        return self.__node__.identity
