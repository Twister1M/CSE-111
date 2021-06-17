import random
import importlib
from .sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase

def main():
    test_get_determiner()
    test_get_noun()
    test_get_verb()
    test_get_preposition()
    test_get_prepositional_phrase()


def test_get_determiner():
    rq = [1,2]
    quantity = random.choice(rq)
    get_determiner(quantity)

def test_get_noun():
    rq = [1,2]
    quantity = random.choice(rq)
    get_noun(quantity)

def test_get_verb():
    rq = [1,2]
    quantity = random.choice(rq)
    rt = ['past','present','future']
    tense = random.choice(rt)
    get_verb(quantity,tense)

def test_get_preposition():
    get_preposition()

def test_get_prepositional_phrase():
    rq = [1,2]
    quantity = random.choice(rq)
    get_prepositional_phrase(quantity)

main()