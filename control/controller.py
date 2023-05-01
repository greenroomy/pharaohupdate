import models.dboperator


class MyController(object):
    def __init__(self):
        pass

    def controller_execute(self):
        # 全体の処理
        # DBへ接続してテーブル"pharaoh"からASINを取得
        mydboperator = models.dboperator.MyDBOperator()
        db_asin_list = mydboperator.get_asin_list()
        print('ASINリスト', db_asin_list)



