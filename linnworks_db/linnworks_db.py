from pydatabase import DatabaseTable


class LinnworksDB(DatabaseTable):
    database = 'linnworks'
    table = None
    user = 'axevalley'
    host = 'localhost'
    password = 'fred'

    def __init__(self):
        super().__init__(
            database=self.database, table=self.table, user=self.user,
            host=self.host, password=self.password)
