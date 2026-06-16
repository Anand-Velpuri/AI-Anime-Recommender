# This file is to create the vector store from the processed CSV file. It will be used in the recommendation pipeline.
from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv(override=True)

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline...")
        
        loader = AnimeDataLoader("./data/anime_with_synopsis.csv", "./data/anime_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info("Data loaded and processed successfully...")

        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store built and saved successfully...")
        logger.info("Pipeline built successfully...")
    except Exception as e:
        logger.error(f"Error in building pipeline: {e}")
        raise CustomException(f"Error in building pipeline: {e}")

if __name__ == "__main__":
    main()
