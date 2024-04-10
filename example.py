import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def getContentFromAI(text):

    with open('googlekey.txt', 'r') as file:
        key = file.read()

    safety_settings = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]
    GOOGLE_API_KEY=key
    genai.configure(api_key=GOOGLE_API_KEY)

    # text = 'Black Death Article Talk Read View source View history Tools Page semi-protected From Wikipedia, the free encyclopedia For other uses, see Black Death (disambiguation). "The Plague" redirects here. For other uses, see The Plague (disambiguation). Black Death The spread of the Black Death in Europe and the Near East (1346–1353) The spread of the Black Death in Europe, North Africa and the Near East (1346–1353) Disease	Bubonic plague Location	Eurasia and North Africa[1] Date	1346–1353 Deaths	25,000,000 – 50,000,000 (estimated) The Black Death was a bubonic plague pandemic occurring in Europe from 1346 to 1353. One of the most fatal pandemics in human history, as many as 50 million people[2] perished, perhaps 50% of Europe’s 14th century population.[3] Bubonic plague is caused by the bacterium Yersinia pestis and spread by fleas.[4][5] One of the most significant events in European history, the Black Death had far-reaching population, economic, and cultural impacts. The Black Death was the beginning of the second plague pandemic.[6] The plague created religious, social and economic upheavals, with profound effects on the course of European history. The origin of the Black Death is disputed.[7] Genetic analysis points to the evolution of Yersinia pestis in the Tian Shan mountains on the border between Kyrgyzstan and China 2,600 years ago. The immediate territorial origins of the Black Death and its outbreak remain unclear, with some evidence pointing towards Central Asia, China, the Middle East, and Europe.[8][9] The pandemic was reportedly first introduced to Europe during the siege of the Genoese trading port of Kaffa in Crimea by the Golden Horde army of Jani Beg in 1347. From Crimea, it was most likely carried by fleas living on the black rats that travelled on Genoese ships, spreading through the Mediterranean Basin and reaching North Africa, Western Asia, and the rest of Europe via Constantinople, Sicily, and the Italian Peninsula.[10] There is evidence that once it came ashore, the Black Death mainly spread from person-to-person as pneumonic plague, thus explaining the quick inland spread of the epidemic, which was faster than would be expected if the primary vector was rat fleas causing bubonic plague.[11] In 2022, it was discovered that there was a sudden surge of deaths in what is today Kyrgyzstan from the Black Death in the late 1330s; when combined with genetic evidence, this implies that the initial spread may not have been due to Mongol conquests in the 14th century, as previously speculated.[12][13] The Black Death was the second great natural disaster to strike Europe during the Late Middle Ages (the first one being the Great Famine of 1315–1317) and is estimated to have killed 30% to 60% of the European population, as well as approximately 33% of the population of the Middle East.[14][15][16] There were further outbreaks throughout the Late Middle Ages and, also due to other contributing factors (the Crisis of the Late Middle Ages), the European population did not regain its 14th century level until the 16th century.[a][17] Outbreaks of the plague recurred around the world until the early 19th century.'
    modify = "I will give you a paragraph. Try to generate some questions that test the understanding of the paragraph and provide the solutions"

    model = genai.GenerativeModel('gemini-pro')
    request = model.generate_content(text, safety_settings=safety_settings)
    print(request.text)
    return request.text


@app.route('/getContent/<text>', methods=['GET'])
def handle_form_submission(text):
    data = {'title': 'subject',
            'content': 'this is the content',
            }
    data['content']=getContentFromAI(text)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)