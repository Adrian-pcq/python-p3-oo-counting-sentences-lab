#!/usr/bin/env python3
import re;
class MyString():
    def __init__(self,value=""):
        self._value = value
  
    def  get_value(self):
        return self._value   
  
    def set_value(self,value):
        if type(value) == str:
          self._value = value
        else:
          print("The value must be a string.")
    value = property(get_value, set_value)  

    def is_sentence(self):
       return  self._value.endswith(".")
    
    def is_question(self):
       return self._value.endswith("?")
    
    def is_exclamation(self):
       return self._value.endswith("!")
    
    def count_sentences(self):
        count = 0
        splited = re.split("[.!?]", self._value)
        counter_list = [char for char in splited if char != ""]
        count = len(counter_list)
        return count
    
    # def count_sentences(self):
    #    counter = 0
    #    striped = self._value.strip(".!?")

    #    for char in striped:
    #       counter +=1
    #    return counter

    # def count_sentences(self):
    #   counter = 0
    #   striped = self._value.strip(".?!")
    #   splited =  re.split(".?!", striped)
    #   counter_list= [char for char in splited if char != ""] 
    #   for char in counter_list:
    #      counter += 1  
    #   return counter   
    
    # def count_sentences(self):
    #   count = 0
    #   sentence_ending=[".","!","?"]
    #   for char in self._value:
    #       if char in sentence_ending:
    #          count += 1
    #   return count  
    
    # def count_sentences(self):
    #     sentence_count = len(re.findall(r'\b[A-Z][^.!?]*[.!?]', self._value))
    #     return sentence_count        
