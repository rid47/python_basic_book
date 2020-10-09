import json
import falcon
from waitress import serve


class ObjRequest:
    def on_get(self, req, resp):
        data = req.stream.read()
        print(json.loads(data))

        content = {
                'name': 'Mizan',
                'age': '28',
                'country': 'Bangladesh'
        }

        resp.body = json.dumps(content)


api = falcon.API()

api.add_route('/test', ObjRequest())
serve(api, host="127.0.0.1", port=8001)
