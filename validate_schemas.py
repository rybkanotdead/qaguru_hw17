from jsonschema import validate

def validate_json_schema(schema, response):
    body = response.json()
    validate(instance=body, schema=schema)