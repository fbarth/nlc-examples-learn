import pandas as pd
import numpy as np
import json
import sys
import csv
from ibm_watson import NaturalLanguageClassifierV1
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{apikey}',
    url='https://gateway.watsonplatform.net/natural-language-classifier/api')

result = pd.DataFrame(columns=['class', 'predicted', 'confidence'])
with open('../data/test_cerveja.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
      classes = natural_language_classifier.classify('{classifier_id}', row[0]).get_result()
      result.loc[-1] = [row[1], classes['classes'][0]['class_name'], classes['classes'][0]['confidence']]
      print([row[1], classes['classes'][0]['class_name'], classes['classes'][0]['confidence']])
      result.index = result.index + 1
      result = result.sort_index()

print(sum(result['class'] == result['predicted']) / len(result))
m = confusion_matrix(result['class'], result['predicted'])
print(m)
accr = accuracy_score(result['class'], result['predicted'])
print(accr)