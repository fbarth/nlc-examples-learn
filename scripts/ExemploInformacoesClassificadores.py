import json
from ibm_watson import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{apikey}',
    url='{url}')

status = natural_language_classifier.get_classifier('{classifier_id}').get_result()
print (json.dumps(status, indent=2))