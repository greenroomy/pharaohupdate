from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

dialect = "mysql"
driver = "mysqldb"
username = "root"
password = "jpt01130"
host = "localhost"
port = "3306"
database = "pharaoh"
charset_type = "utf8"
db_url = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type}"

# DB接続するためのEngineインスタンス
engine = create_engine(db_url, echo=True)

# # DBに対してORM操作するときに利用
# # Sessionを通じて操作を行う
# session = scoped_session(
#     sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
# )
#
# # 各modelで利用
# # classとDBをMapping
# Base = declarative_base()

# テーブルpharaohをautomapを使ってpythonクラスにテーブルをマッピング
Base = automap_base()

Base.prepare(engine, reflect=True)
table_pharaoh = Base.classes.pharaoh

# セッションの作成
session = sessionmaker(bind=engine)()
