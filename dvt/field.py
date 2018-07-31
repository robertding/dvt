# -*- coding:utf-8 -*-
from __future__ import absolute_import


# 基本类型

class Field():
    pass


class Int(Field):
    pass


class Str(Field):
    pass


class Bool(Field):
    pass


class Float(Field):
    pass


class List(Field):
    pass


# 扩展类型

class Date(Field):
    pass


class DateTime(Field):
    pass


# 复合类型

class Nested(Field):
    pass


# 元类型

class Function(Field):
    pass
