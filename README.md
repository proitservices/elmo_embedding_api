

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
          "release": "13/05/2023 01:22"

# elmo_embedding_api
Drop in replacement for openai ada 

Reason - local is good 
limits - you can create a 1024 dimmensional embeddings for your application and only your box is the limit
tested - 9383 tokens in 2min 33 sec on 8 core i7 machine

how to start it up

- clone the repository https://github.com/proitservices/elmo_embedding_api.git
- start virtualenv with python (3.9.16 or later)
- download an elmo model of your choice from http://vectors.nlpl.eu/repository/20/209.zip (219.zip is also a good choice)
- unzip the model to ./model/
- python run.py to start the application
- call http://localhost:5001
 							/                   for author info 
 							/ver 	            version info
 							/v1/embeddings      to generate embeddings 



example:
#curl -X POST http://localhost:5001/v1/embeddings -H 'Content-Type: application/json' -d "{\"input\": [\"some text\",\"some more interesting text\",\"additional context\"]}"


response schema mimics open ai ada .. with added multi input and multi output as list 
```json
{
  "data": [
    {
      "embedding": [
        -0.006929283495992422,
        -0.005336422007530928,
        ...
        -4.547132266452536e-05,
        -0.024047505110502243
      ],
      "index": 0,
      "object": "embedding"
    }
  ],
  "model": "text-embedding-elmo-002",
  "object": "list",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}

