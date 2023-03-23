# Write a solution for the following problem.
# It doesn't have to be running but please do not use any framework like Django.
# You could do it in either in vanilla Python or pseudocode, it's all about the right architecture:
#
#
# The client is a big retail sales company that has multiple sources of transactions that have
# different formats and has to be able to draw stats out of them for BI purposes.
# We need to pull the data from all of the sources once a day and put them in a single db table.
# The following configurations will be fetched from and endpoint and it should be simple to add more of them to the process without doing changes in the code.
#
#
# Data sources:
#
# name: eu-west-1,
# type: mysql,
# address: xxx.xxx.xxx.xxx, username: euw1, password: 2818ehA,
# table: cat_transactions,
# relevant columns: id, cat_title, cat_trans_date, cat_price
#
#
# name: eu-west-2,
# type: postgresql,
# address: xxx.xxx.xxx.xxx, username: euw2, password: 3ja8dhj
# table: transaction_history,
# relevant columns: th_id, th_name, th_created_at, th_value
#
#
# name: eu-east-1,
# type: mongo,
# address: xxx.xxx.xxx.xxx, username: eue1, password: jfjj9a9aw77
# collection: transactions,
# relevant fields: identifier, title, date, price
#
#
# name: brazil-2,
# type: mongo,
# address: xxx.xxx.xxx.xxx, username: eue1, password: jfjj9a9aw77
# collection: cat_transações,
# relevant fields: identificador, título, encontro, preço
#
#
# Target DB table hosted on our side:
#
# name: transactions
# type: postgresql
# columns: id, title, date, price, source
from abc import ABC, abstractmethod


class DBConnectionConfig:

    def __init__(self, address, username, password, type):
        self.address = address
        self.username = username
        self.password = password
        self.type = type

    def get_driver(self):
        return None

    def open_connection(self):
        pass


class DBDataFetchMapperInterface(ABC):

    def __init__(self, source: str, attributes: list):
        self.source = source  # collection or table
        self.attributes = attributes

    @abstractmethod
    def query(self):
        pass


class DBDataFetchMapper(DBDataFetchMapperInterface):

    def query(self):
        pass


class DatabaseSource:

    def __init__(self, name: str, db_connection_config: DBConnectionConfig, db_data_fetch_mapper: DBDataFetchMapper):
        self.name = name
        self.db_connection_config = db_connection_config
        self.db_data_fetch_mapper = db_data_fetch_mapper

    def fetch(self):
        connection = db_connection_config.open_connection()
        connection.request(db_data_fetch_mapper.query())


class DataFetcher:

    def __init__(self):
        self.database_sources = []

    def add(self, database_source):
        self.database_sources.append(database_source)

    def fetch(self):
        # consider threads
        results = []
        for db_source in self.database_sources:
            result = db_source.fetch()
            results.append(result)
        return results


if __name__ == "__main__":
    # name: eu-west-1,
    # type: mysql,
    # address: xxx.xxx.xxx.xxx,
    # username: euw1,
    # password: 2818ehA,
    list_of_sources = []
    data_fetcher = DataFetcher()
    for source in list_of_sources:

        db_connection_config = DBConnectionConfig(
            username=source["username"],
            type=source["type"],
            address=source["address"],
            password=source["password"],
        )

        db_type = source["type"]
        if db_type == 'postgress':
            db_data_fetch_mapper = DBDataFetchMapper(
                source=source["source"],
                attributes=source["attributes"],
                query_builder=None
            )

            database_source = DatabaseSource(
                name=source["name"],
                db_connection_config=db_connection_config,
                db_data_fetch_mapper=db_data_fetch_mapper
            )
            data_fetcher.add(database_source)
        data_fetcher.fetch()
