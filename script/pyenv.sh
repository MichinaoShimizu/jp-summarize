#!/bin/sh
#!/usr/bin/env bash

# ./script/pyenv.sh
# source ~/.bash_profile

brew install pyenv
{
    echo "export PYENV_ROOT=\"$HOME/.pyenv\""
    echo "export PATH=\"$PYENV_ROOT/bin:$PATH\""
    echo "eval \"$(pyenv init -)\""
} >> ~/.bash_profile

pyenv install 3.10.2
pyenv install 3.9.10
pyenv install 3.8.12

pyenv local 3.9.10
{
    echo 3.9.10
    echo 3.10.2
    echo 3.8.12
} > .python-version
