import jsonschema
import logging
from pathlib import Path
import json

SCHEMAS_DIR = Path(__file__).parent.parent / "json_schema"


def load_schema(schema_name: str) -> dict:
    file_path = SCHEMAS_DIR / f"{schema_name}.json"
    with open(file_path) as f:
        return json.load(f)


def validate(data: dict, schema_name: str):
    logging.info(f"Валидация ответа по схеме: {schema_name}")
    jsonschema.validate(
        data,
        load_schema(schema_name),
        format_checker=jsonschema.FormatChecker()
    )
    logging.info(f"Валидация схемы пройдена: {schema_name}")
