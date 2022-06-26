# Automatic Precisiation of Meaning of Adjectives and Adverbs

This is a library allowing to automatically precisiate the meaning of adjectives and adverbs based on their semantic similarity, as presented in:

M. Colombo and E. Portmann, "An Algorithm for the Automatic Precisiation of the Meaning of Adjectives," 2020 Joint 11th International Conference on Soft Computing and Intelligent Systems and 21st International Symposium on Advanced Intelligent Systems (SCIS-ISIS), 2020, pp. 1-6, doi: 10.1109/SCISISIS50064.2020.9322674.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/colombmo/precisiation.git
$ cd precisiation
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

The precisiation package has to be instantiated as follows before using its functions:
```python
from precisiation import Precisiation
precisiation = Precisiation()
``` 

Then, the following functions from the `precisiation.py` module can be used:

```python
precisiation.get_category([words]) # Retrieve the most likely common category to which the words in the list belong to
precisiation.precisiate(word, category, lvl=2) # Precisiate the meaning of "word" of type "category", using the lvl-th order of synonymy in the semantic similarity, using the FIRST iteration of the algorithm
precisiation.precisiate_v2(word, category, lvl=2) # Precisiate the meaning of "word" of type "category", using the lvl-th order of synonymy in the semantic similarity, using the SECOND (improved!) iteration of the algorithm
```