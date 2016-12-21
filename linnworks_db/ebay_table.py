from . linnworks_db import LinnworksDB


class EbayTable(LinnworksDB):
    name = 'Ebay Products Table'
    table = 'ebayproducts'
    no_update_columns = ('id')
