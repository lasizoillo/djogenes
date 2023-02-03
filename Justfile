# List this help
help:
    just --list

# Launch docker-compose
up: make-requirements
    docker-compose up --build

# Use hatch to generate requirements.txt
make-requirements:
    hatch run true  # trick to update dependencies in virtualenv
    hatch dep show requirements -p > requirements.txt
