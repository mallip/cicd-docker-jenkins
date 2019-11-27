#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate

# Download requirements to build cache
#pip download -d /build -r requirements_test.txt --no-input

# Install application test requirements
python -m pip install -r requirements_test.txt

# Run test.sh arguments
exec $@
