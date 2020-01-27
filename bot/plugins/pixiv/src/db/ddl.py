import re
import sqlite3


class Factory:

    def __init__(self, conn):
        if not isinstance(conn, sqlite3.Connection):
            module_ = type(conn).__module__
            name_ = type(conn).__name__
            if module_ == 'builtins':
                type_ = name_
            else:
                type_ = module_ + '.' + name_

            raise TypeError('class need a "sqlite3.Connection", got "%s"' % type_)
        self.conn = conn
        self.cur = self.conn.cursor()

    def init(self):
        ddl_methods = self._get_ddl_func_name()

        for ddl in ddl_methods:
            ddl_obj = getattr(self, ddl)
            ddl_sql = ddl_obj()
            self.cur.execute(ddl_sql)
            # self.cur.


    def _get_ddl_func_name(self):
        method_dict = self.__dir__()
        ddl_dict = []
        for item in method_dict:
            res = re.match('^db_table_', item)
            if res is not None:
                ddl_dict.append(item)

        return ddl_dict

    def db_table_favorite_illustor(self):
        sql = """
        CREATE TABLE IF NOT EXISTS favorite_illustor
        (
            id int primary key unique,
            illustor_id varchar(255) unique,
            illustor_name varchar(255)
        );
        """
        return sql

    def db_table_illust_history(self):
        sql = """
        CREATE TABLE IF NOT EXISTS illust_history
        (
            id int primary key unique,
            illust_id varchar(255) unique,
            catch_time int(11)
        );
        """
        return sql

