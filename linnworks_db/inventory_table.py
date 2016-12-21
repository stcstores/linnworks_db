from . linnworks_db import LinnworksDB


class InventoryTable(LinnworksDB):
    name = 'Linnworks Inventory Table'
    table = 'inventory'
    no_update_columns = ('id')
    update_key = 'SKU'

    def update_from_file(self, update_file):
        self.truncate()
        super().update_from_file(update_file, split_rows=8000)
