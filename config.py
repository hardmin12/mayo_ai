import os
from dotenv import load_dotenv

#환경 변수 로드
load_dotenv()

DEEPGRAM_API_KEY = os.getenv("딥그램 api key")
OPENAI_API_KEY = os.getenv("오픈ai api key")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("구글 애플리케이션 credentials")

os.environ["구글 애플리케이션 크레덴셜"] = GOOGLE_APPLICATION_CREDENTIALS