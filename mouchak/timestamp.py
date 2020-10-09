import json
import falcon
import arrow


class Timestamp(object):
    def on_get(self, req, res):
        payload = {}
        payload['utc'] = arrow.utcnow().format('YYYY-MM-DD HH:mm:SS')
        payload['unix'] = arrow.utcnow().timestamp

        res.body = json.dumps(payload)
        res.status = falcon.HTTP_200


