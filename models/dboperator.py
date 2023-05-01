from mydatabase.dbsettings import table_pharaoh, session, engine
from sqlalchemy import distinct


class MyDBOperator(object):
    def __init__(self):
        self.asin_list = []

    def get_asin_list(self):
        self.asin_list = session.query(distinct(table_pharaoh.asin))\
                            .all()
        return self.asin_list

