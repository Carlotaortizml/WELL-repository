run_api:
	uvicorn well.api.main:app --port 8080 --reload

run_streamlit:
	streamlit run well/frontend/chat.py
