from flask import Response, jsonify
import json

class CustomResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)

        if isinstance(rv, list):
            rv = json.dumps(rv)

        return super(CustomResponse, cls).force_type(rv, environ)
