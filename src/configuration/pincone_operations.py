import sys
import logging
import pinecone
from src.exception import CustomException

# initializing logger
logger = logging.getLogger(__name__)


class PineconOperation:
    def __init__(self, pinecone_api_key: str, pinecone_environment: str) -> None:
        self.pinecone_api_key = pinecone_api_key
        self.pinecone_environment = pinecone_environment


    def create_index(self, index_name: str, vector_dimension: int, metric: str, pods: int) -> None:
        logger.info("Entered the create_index method of PineconeOperation class")
        try:
            pinecone.init(api_key=self.pinecone_api_key, environment=self.pinecone_environment)

            pinecone.create_index(name=index_name, dimension=vector_dimension, metric=metric, pods=pods)

            logger.info("Exited the create_index method of PineconeOperation class")

        except Exception as e:
            raise CustomException(e, sys) from e
        

    def get_similar_docs(self, docsearch: object, query: str, k: int) -> list:
        logger.info("Enetred the get_similar_docs method of PineconeOperation class")
        try:
            similar_docs = docsearch.similarity_search(query, k=k)

            logger.info("Exited the get_similar_docs method of PineconeOperation class")
            return similar_docs

        except Exception as e:
            raise CustomException(e, sys) from e
