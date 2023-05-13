

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

building the docker image:
clone this repositorory and at the top level run
sudo docker build -t elmo-embedding-api .

placing the model:
downloa the desired model to the ./model/ direcotry and unzip it.

start the container (initial start and call will take few extra seconds):
sudo docker run -p 5001:5001 -v ./model:/app/model -v ./logs:/app/logs --name elmo-embedding-api peterromanowski/elmo-embedding-api:0.1.4


pulling from docker.hub:

docker pull peterromanowski/elmo-embedding-api:0.1.4   [nearly ~4GB]   (use sudo if you get perm issues)

example:
#curl -X POST http://localhost:5001/v1/embeddings -H 'Content-Type: application/json' -d "{\\"input\\": [\\"some text\\",\\"some more interesting text\\",\\"additional context\\"]}"


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



I hope it will help you in your own project. 
If you do have questions feel free to reach out. 
Enjoy!
