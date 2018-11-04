import json
import sys
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

natural_language_classifier = NaturalLanguageClassifier(
    iam_apikey='{apikey}',
    url='{url}')

text = sys.argv[1]
classes = natural_language_classifier.classify('{classifier_id}', text).get_result()
print(json.dumps(classes, indent=2))