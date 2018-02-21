import json

from moto.core.responses import BaseResponse

class AthenaHandler(BaseResponse):

    def error(self, type_, message='', status=400):
        headers = self.response_headers
        headers['status'] = status
        return json.dumps({'__type': type_, 'message': message}), headers,

    def start_query_execution(self):
        query = self._get_param('QueryString')

        if not query:
            return self.error('ValidationException', 'Parameter QueryString is required.')

        return json.dumps({'QueryExecutionId': '1'}), self.response_headers
