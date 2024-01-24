# Leetcode solutions

I'll be using this repo to store my solutions to selected [LeetCode](https://leetcode.com/) challenges.

# Organization

The directories are organized following the path suggested by [NeetCode](https://neetcode.io/roadmap).

# How to run tests

First, install `virtualenv`:

```shell
$ sudo apt-get install python3-virtualenv # Linux
$ brew install virtualenv # Mac
```

Then, create a virtualenv, activate it and install the appropriate requirements:

```shell
$ mkdir venv && virtualenv --python=python3 venv
$ . ./venv/bin/activate
$ pip3 install -r requirements.txt
```

Finally, run the tests:

```shell
python3 -m pytest -vvv
```
