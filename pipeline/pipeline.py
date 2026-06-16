# This is the actual pipeline that will be used in the application. It will load the vector store and use it to generate recommendations based on user queries.
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException


logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        try:
            logger.info("Initializing Anime Recommendation Pipeline...")
            vector_build = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)

            retriever = vector_build.load_vectorstore().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Pipeline initialized successfully...")
        except Exception as e:
            logger.error(f"Error initializing pipeline: {e}")
            raise CustomException(f"Error initializing pipeline: {e}")
    
    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info(f"Recommendation generated successfully...")
            return recommendation
        except Exception as e:
            logger.error(f"Error generating recommendation: {e}")
            raise CustomException(f"Error generating recommendation: {e}")