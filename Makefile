install:
	poetry install

run_m0:
	python m0/run.py

run_m1a:
	python m1a/run.py

run_m1b:
	python m1b/run.py

run_m1c:
	python m1c/run.py

run_m1d:
	python m1d/run.py

run_m1e:
	python m1e/run.py

run_m1f:
	python m1f/run.py

run_m1g:
	python m1g/run.py

run_m2:
	python m2/run.py

run_m2a:
	dagit -f m2/run.py -h 0.0.0.0

run_m2b:
	docker build -t dagster-dooblies .
	docker run dagster-dooblies  /bin/bash -c "make run_m2"

run_m2c:
	docker build -t dagster-dooblies .
	docker run -p 3000:3000 dagster-dooblies  /bin/bash -c "dagit -f m2/run.py -h 0.0.0.0"
