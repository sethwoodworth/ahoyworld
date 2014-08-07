#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def simple_say_hello():
    print "Ahoy-hoy!!"
    
def say_hello_to_someone(name):
    print "Hello " + name

def random_say_hello():
    greetings = ["Hello!", "Bonjour!", "Ahoy"]
    print random.choice(greetings)
    

if __name__ == '__main__':
    #print "Ahoy world"
    #simple_say_hello()
    #random_say_hello()
    say_hello_to_someone('seth')
    
