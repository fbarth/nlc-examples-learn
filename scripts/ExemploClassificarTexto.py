import json
import sys
from ibm_watson import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{apikey}',
    url='{url}')

text = sys.argv[1]
classes = natural_language_classifier.classify('{classifier_id}', text).get_result()
print(json.dumps(classes, indent=2))