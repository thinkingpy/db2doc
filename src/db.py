import pymysql
import logging
from settings import *
logging.basicConfig(level=logging.NOTSET)

class Db(object):

    def __init__(self):
        logging.debug('DATABASES==>'+str(DATABASES))
        self.conn=pymysql.connect(**DATABASES)
        self.a_conn=self.conn.cursor()
        self.a_conn.execute('set names utf8')

        self.sql_tables="select table_name,table_comment from information_schema.tables where table_schema = '%s'" %DATABASES['db']
        self.sql_full_fields = "SHOW FULL FIELDS FROM %s.%s"

    def getTables(self):
        self.a_conn.execute(self.sql_tables)
        logging.debug('getTables sql==>'+self.sql_tables)

        rst = self.a_conn.fetchall()
        logging.debug('getTables data==>'+str(rst))

        return rst

    def getFullFields(self,tb_name):
        sql=self.sql_full_fields %(DATABASES['db'],tb_name)
        logging.debug('getTables sql==>'+sql)
        self.a_conn.execute(sql)
        rst = self.a_conn.fetchall()
        logging.debug('getTables data==>'+str(rst))

        return rst

    def close(self):
        self.a_conn.close()

if __name__=='__main__':
    db=Db()
    tbs=db.getTables()
    for tb in tbs:
        print(tb)
        fds=db.getFullFields(tb[0])
        print(fds)
    db.close()