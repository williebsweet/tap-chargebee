from tap_chargebee.streams.base import BaseChargebeeStream


class OrdersStream(BaseChargebeeStream):
    TABLE = 'orders'
    ENTITY = 'order'
    BOOKMARK_PROPERTIES = ['updated_at']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['updated_at']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_url(self):
        return 'https://{}.chargebee.com/api/v2/orders'.format(self.config.get('site'))
