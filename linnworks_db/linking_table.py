from . linnworks_db import LinnworksDB


class LinkingTable(LinnworksDB):
    name = 'Linnworks Linking Table'
    table = 'linking'
    no_update_columns = ('id')

    def update_from_file(self, update_file):
        self.truncate()
        super().update_from_file(update_file, split_rows=8000)

    def printUpdate(self, file):
        records_updated, records_inserted = self.update_from_file(file)
        print('Update Complete.')
        print(str(records_inserted) + ' records inserted')
