.PHONY: install lint test deploy clean

install:
    ansible-galaxy install -r requirements.yml
    pipenv install

lint:
    ansible-lint .

test:
    tox

deploy:
    ansible-playbook -i inventory playbook.yml

clean:
    find . -name "*.retry" -delete
    rm -rf .tox
    rm -rf .molecule
