import json
import falcon
from waitress import serve


class ObjRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        # data = json.loads(req.stream.read())
        data = req.params['name']

        print(req.params['age'])

        output = {
            'msg': 'Hello {0}'.format(data)
        }

        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        print(f"{data['x']} & {data['y']}")

        equal = data['x'] + data['y']

        output = {
            'msg': 'x: {x} + y: {y} is equal to {e}'.format(x=data['x'], y=data['y'], e=equal)
        }

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/demo', ObjRequestClass())

serve(api, host="127.0.0.1", port=8001)
