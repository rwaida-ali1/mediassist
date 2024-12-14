from dotenv import load_dotenv
import os


def load_env_vars():
    load_dotenv()


def get_openai_config():
    return {
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "api_base": os.environ.get("OPENAI_API_BASE"),
        "model_name": os.environ.get("OPENAI_MODEL_NAME"),
    }


def get_serper_api_key():
    return os.environ.get("SERPER_API_KEY")
