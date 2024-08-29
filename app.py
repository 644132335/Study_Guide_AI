from typing import Dict, List

from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from pydantic import BaseModel

from gemini_generate import getContentFromAI
from json_helper import extract_json, model_to_json

app = Flask(__name__)
CORS(app)


class qaModel(BaseModel):
    questions: List[Dict[str, str]]
    summary: str


json_model = model_to_json(
    qaModel(questions=[{"question": "answer"}], summary="summary")
)

base_prompt = "I will give you a paragraph in the delimiter. Try to generate some questions that test readers' understanding of the paragraph and provide solutions. "

optimized_prompt = (
    base_prompt
    + f".Please provide a response in a structured JSON format that matches the following model: {json_model}"
)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/getContent", methods=["POST"])
def handle_form_submission_text() -> tuple:
    data = request.get_json()
    number = data.get("number")
    text = data.get("text")
    base_prompt_for_qa = f"I will give you a passage in the delimiter. First give a summary to the passage. Then, try to generate {number} questions that test readers' understanding of the passage and provide solutions."
    optimized_qa_prompt = (
        base_prompt_for_qa
        + f" Please provide a response in a structured JSON format that matches the following model: {json_model}"
    )
    generatedQA = getContentFromAI(optimized_qa_prompt + f"'''{text}'''")
    extractJson = extract_json(generatedQA)
    try:
        data = jsonify(extractJson)
        return data, 200
    except Exception as e:
        data = jsonify({"error": str(e)})
        return data, 500


@app.route("/getContentByImage", methods=["POST"])
def handle_form_submission_image() -> tuple:
    """
    This function is responsible for handling the form submission for the image.
    Supported file types are: png, jpeg, webp, heic, heif
    """
    image = request.files["image"]
    number = request.form["number"]

    base_prompt_for_qa = f"I will give you a passage in the image. First give a summary to the passage. Then, try to generate {number} questions that test readers' understanding of the passage and provide solutions."
    optimized_qa_prompt = (
        base_prompt_for_qa
        + f" Please provide a response in a structured JSON format that matches the following model: {json_model}"
    )
    image = Image.open(
        image.stream
    )  # convert the filestorage object to an PIL image object
    generatedQA = getContentFromAI(optimized_qa_prompt, img=image)
    extractJson = extract_json(generatedQA)
    try:
        data = jsonify(extractJson)
        return data, 200
    except Exception as e:
        data = jsonify({"error": str(e)})
        return data, 500


if __name__ == "__main__":
    app.run(debug=True)
