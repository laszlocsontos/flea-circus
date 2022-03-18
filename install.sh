#!/usr/bin/env bash

env_name="venv"
python_version="3"

if [ ! -d ${env_name} ]; then
  python${python_version} -m venv ${env_name}
  source ${env_name}/bin/activate
  python${python_version} -m pip install --requirement requirements.txt
else
  source ${env_name}/bin/activate
fi
