# Bugs
All bugs has been reported in [Github Issues](https://github.com/rafaelcs/code_challenge/issues). Each issue contains more than one bug (enumerated)

### Download and Run Docker Image

Pull the Docker image:

```sh
docker pull public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest
```

### Setup

Clone the repo:

```sh
git clone https://github.com/rafaelcs/code_challenge.git
cd code-challenge
```

Create and Activate Virtual Environment:

```sh
pyenv virtualenv 3.12.1 code_challenge_venv
pyenv activate code_challenge_venv
```

Install Requirements:

```sh
pip install -r requirements.txt
```

### Run Tests

Execute tests by pointing the report dir

```sh
pytest -s tests --alluredir report
```

## Report

To view the report:

```sh
allure serve report
```