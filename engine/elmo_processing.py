from simple_elmo import ElmoModel
import numpy as np
import tensorflow as tf

class elmo_processing:

    def __init__(self, model_path='./model/'):
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.model = ElmoModel()
            self.model.load(model_path)

    def embedding(self, text_list):
        with self.graph.as_default():
            embedding = self.model.get_elmo_vector_average(text_list)
            embeddings_list = embedding.tolist()
            response_embedding = self.transform_embedding_to_dict(embeddings_list,text_list)
            return response_embedding

    def transform_embedding_to_dict(self, embedding_list, text_list, model_name="text-embedding-elmo-002"):
        prompt_tokens = sum(len(text) for text in text_list)
        total_tokens = sum(len(embedding) for embedding in embedding_list)

        transformed_data = {
            "data": [
                {
                    "embedding": embedding,
                    "index": index,
                    "object": "embedding"
                }
                for index, embedding in enumerate(embedding_list)
            ],
            "model": model_name,
            "object": "list",
            "usage": {
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens
            }
        }
        return transformed_data