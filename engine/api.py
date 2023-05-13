from flask import Blueprint, jsonify, request, render_template
from .elmo_processing import elmo_processing
import requests
import os
import logging


api = Blueprint('api', __name__)
LOG = logging.getLogger(__name__)
elmo_proc = elmo_processing()

@api.route('/', methods=['GET'])
def buy_me_a_coffee():
    ascii_art = '''

    ╭━━━┳╮╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
    ┃╭━━┫┃╱╱╱╱╱╱╱╱╱┃╭━━╯╱╱┃┃╱╱╱╱╱╱┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃
    ┃╰━━┫┃╭╮╭┳━━╮╱╱┃╰━━┳╮╭┫╰━┳━━┳━╯┣━╯┣┳━╮╭━━┳━━╮╱╱╱╱╭╮┣╮┃
    ┃╭━━┫┃┃╰╯┃╭╮┣━━┫╭━━┫╰╯┃╭╮┃┃━┫╭╮┃╭╮┣┫╭╮┫╭╮┃━━┫╭━━╮┃╰╯┃┃
    ┃╰━━┫╰┫┃┃┃╰╯┣━━┫╰━━┫┃┃┃╰╯┃┃━┫╰╯┃╰╯┃┃┃┃┃╰╯┣━━┃╰━━╯╰╮╭╯╰╮
    ╰━━━┻━┻┻┻┻━━╯╱╱╰━━━┻┻┻┻━━┻━━┻━━┻━━┻┻╯╰┻━╮┣━━╯╱╱╱╱╱╰┻━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯

          "author":"Piotr Romanowski"
          "version": "1.4"
    '''
    return render_template('index.html', ascii_art=ascii_art)


@api.route('/ver', methods=['GET'])
def version():
    log_event()
    return jsonify({"version": "1.4", "author":"Piotr Romanowski","compiled":"11-05-2023 17:53","served_by":os.uname()[2]})

@api.route('/v1/embeddings', methods=['POST'])
def create_embedding():
    j_input = request.get_json()
    #model = elmo_processing()
    embedding = elmo_proc.embedding(text_list=j_input['input'])
    log_event()
    return jsonify(
        embedding
        )

def log_event():
    hostname = os.uname()[1]
    LOG.info('served from {}'.format(os.uname()[2]))


#curl -X POST http://localhost:5001/v1/embeddings -H 'Content-Type: application/json' -d "{\"input\": [\"some text\",\"some more interesting text\",\"additional context\"]}"
