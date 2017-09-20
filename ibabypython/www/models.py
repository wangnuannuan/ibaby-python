#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time, uuid

from transwarp.orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Device(Model):
    __table__ = 'devices'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    node_id = StringField(ddl='varchar(50)')
    device_name = StringField(ddl='varchar(50)')
    device_data = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)

class State(Model):
    __table__ = 'states'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    line=FloatField(default=time.time)
    room_light = BooleanField(default=False)
    door_lock=BooleanField(default=False)
    room_temp=FloatField(default=time.time)
    message=FloatField(default=time.time)
    #tip1 = FloatField(default=time.time)
    #tip2 = FloatField(default=time.time)