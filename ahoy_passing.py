#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def simple_say_hello():
    return "Ahoy-hoy!!"
    
def say_hello_to_someone(name):
    return "Hello " + name

def random_say_hello():
    greetings = ["Hello!", "Bonjour!", "Ahoy"]
    return random.choice(greetings)
    
def greeting(person_a, person_b):
    greeting_a = random_say_hello() + person_a
    greeting_b = say_hello_to_someone(person_b)
    return greeting_a, greeting_b


if __name__ == '__main__':
    print "Ahoy world"
    #print simple_say_hello()
    #print random_say_hello()
    #print say_hello_to_someone('seth')
    #print greeting('seth', 'dogi')
    