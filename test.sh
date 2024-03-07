#!/bin/bash

# There is an additional bug that prevents us from setting up the environment as a
# part of the devcontainer build.
conda env update -n base -f environment.yml

# Run the tests
conda run -n base pytest test_exec_example.py