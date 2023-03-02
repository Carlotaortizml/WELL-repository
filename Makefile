#################### PACKAGE ACTIONS ###################

reinstall_packages:
	@pip uninstall -y well || :
	@pip install -r requirements.txt
	pip install torch

reinstall_packages_moritz:
	make reinstall_packages
	pip install torch --extra-index-url https://download.pytorch.org/whl/cu116


run_api:
	uvicorn well.api.main:app --port 8080 --reload

run_streamlit:
	streamlit run well/frontend/chat.py
