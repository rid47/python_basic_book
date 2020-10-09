import falcon
from timestamp import Timestamp
from waitress import serve

api = falcon.API()
timestamp = Timestamp()
api.add_route('/timestamp', timestamp)

serve(api, host="127.0.0.1", port=8001)
