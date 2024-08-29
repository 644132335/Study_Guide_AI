import json
import re
from typing import get_type_hints

from pydantic import BaseModel, ValidationError


def model_to_json(model_instance: BaseModel) -> str:
    """
    Converts a Pydantic model instance to a JSON string.

    Args:
        model_instance (YourModel): An instance of your Pydantic model.

    Returns:
        str: A JSON string representation of the model.
    """
    return model_instance.model_dump_json()


def extract_json(text_response: str) -> dict:
    # This pattern matches a string that starts with '{' and ends with '}'
    pattern = r"\{[^{}]*\}"
    pattern_for_summary = r'(?<="summary": ")(.*?)(?=")|(?<="summary":")(.*?)(?=")'
    print(text_response)

    matches = re.finditer(pattern, text_response)
    summary_match = re.search(pattern_for_summary, text_response)
    summary = summary_match.group(0)
    json_objects = []

    for match in matches:
        json_str = match.group(0)
        try:
            # Validate if the extracted string is valid JSON
            json_obj = json.loads(json_str)
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            # Extend the search for nested structures
            extended_json_str = extend_search(text_response, match.span())
            try:
                json_obj = json.loads(extended_json_str)
                json_objects.append(json_obj)
            except json.JSONDecodeError:
                # Handle cases where the extraction is not valid JSON
                continue

    if json_objects:
        return {"summary": summary, "flashcards": json_objects}
    else:
        return None  # Or handle this case as you prefer


def extend_search(text: str, span: tuple) -> str:
    # Extend the search to try to capture nested structures
    start, end = span
    nest_count = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            nest_count += 1
        elif text[i] == "}":
            nest_count -= 1
            if nest_count == 0:
                return text[start : i + 1]
    return text[start:end]
