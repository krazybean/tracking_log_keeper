import MySQLdb
from MySQLdb.cursors import DictCursor

class Mysql(object):
    """ Setup for mysql connector """
    # Leaving this a class incase of multiple endpoints
    def connect(self, host=None, user=None, passwd=None, db=None):
        """ connection object """
        db = MySQLdb.connect(host=host,
                             user=user,
                             passwd=passwd,
                             db=db,
                             cursorclass=DictCursor)
        return db
