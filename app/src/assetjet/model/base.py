# -*- coding: utf-8 -*-
import json
from sqlalchemy.ext.declarative import declarative_base
ModelBase = declarative_base()

class ajModel(object):
    def __unicode__(self):
        return "[%s(%s)]" % (self.__class__.__name__, ', '.join('%s=%s' % (k, self.__dict__[k]) for k in sorted(self.__dict__) if '_sa_' != k[:4]))