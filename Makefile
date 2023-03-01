#################### PACKAGE ACTIONS ###################

reinstall_packages:
	@pip uninstall -y well || :
	@pip install -e .

run_api:
	uvicorn well.api.main:app --port 8080 --reload

run_streamlit:
	streamlit run well/frontend/chat.py
