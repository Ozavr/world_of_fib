from jsonschema import validate
from .schemas import fib_input_schema


class FibValidator:
    def __init__(self):
        self.schema = fib_input_schema

    def run(self, data):
        main_status = False
        schema_status = self.is_validate(data)
        if schema_status:
            data_status = self.validate_data(data)
        else:
            data_status = False
        if schema_status and data_status:
            main_status = True
        return main_status

    def is_validate(self, data):
        status = True
        try:
            validate(data, self.schema)
        except Exception as e:
            print(e)
            status = False
        return status

    def validate_data(self, data):
        status = True
        if data['from'] >= data['to']:
            status = False
        return status