# Conduit

# debian specific
please run the following to make sure you maeeting nearly all the dependencies.
`sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev`
## Installation

1. Clone this repository: `git clone https://github.com/vaibhav-rbs/conduit-django/`.
2. `cd` into `conduit-django`: `cd conduit-django`.
3. Install [pyenv](https://github.com/yyuu/pyenv#installation).
    3.1 `brew update; brew install pyenv`
4. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
    4.1 `brew install pyenv-virtualenv`
5. Install Python 3.5.1: `pyenv install 3.5.1`.
6. Create a new virtualenv called "conduit": `pyenv virtualenv 3.5.1 conduit`.
7. Set the local virtualenv to "conduit": `pyenv local conduit`.
8. Reload the `pyenv` environment: `pyenv rehash`.

If all went well then your command line prompt should now start with `(conduit)`.

If your command line prompt does not start with `(conduit)` at this point, try running `pyenv activate conduit` or `cd ../conduit-django`. 

If pyenv is still not working, visit us in the Thinkster Slack channel so we can help you out.
NOTE:
please include the following in ~/.zshrc

`export PATH="/home/vaibhavchauhan/.pyenv/bin:$PATH"`
`eval "$(pyenv init -)"`
`eval "$(pyenv virtualenv-init -)"`
