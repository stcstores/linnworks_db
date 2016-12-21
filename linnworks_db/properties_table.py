from . linnworks_db import LinnworksDB


class PropertiesTable(LinnworksDB):
    name = 'Custom Properties Table'
    table = 'customproperties'

    def __init__(self):
        self.no_update_columns = ('id')
        self.update_key = 'SKU'
        super().__init__()
