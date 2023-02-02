import nltk
import PyPDF2
import os
import re 
import string 
import nltk 
import spacy 
import pandas as pd 
import numpy as np 
import math
import visualise_spacy_tree


from tqdm import tqdm 

from spacy.matcher import Matcher 
from spacy.tokens import Span 
from spacy import displacy
from IPython.display import Image, display

# load spaCy model
nlp = spacy.load("en_core_web_sm")

# sample text 
text = "This study uses the National Household Food Acquisition and Purchase Survey data set to examine the effect of reporting error on food-related outcomes." 

# create a spaCy object 
doc = nlp(text)

png = visualise_spacy_tree.create_png(doc)
display(Image(png))
