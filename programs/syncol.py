"""
syncol: Synonym collection

It is time intensive to have to call the thesaurus API every single time I want to get synonyms, so instead I am
creating a program to get all the synonyms for all the queries and store them locally.

This way I can leave the program running overnight, and it speeds up all subsequent development processes.

I will need to be able to pass a synonym dictionary as a parameter to the Synonym information retrieval class
in order to access these, and if None is passed, only then does it call thesaurus.com with Synonyms.

"""