#!/usr/bin/env python
# -*- coding:utf-8 -*-
def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None


if __name__ == '__main__':
    phonebook = [
        ("John Doe", "555-555-5555"),
        ("Albert Einstein", "212-555-5555"),
    ]
    print("John Doe's phone number is",
          find_phonenumber(phonebook, "John Doe"))
    phonebook = {
        "John Doe": "555-555-5555",
        "Albert Einstein": "212-555-5555",
    }
    print("John Doe's phone number is", phonebook["John Doe"])
