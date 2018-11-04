import json
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

natural_language_classifier = NaturalLanguageClassifier(
    iam_apikey='{apikey}',
    url='{url}')

status = natural_language_classifier.get_classifier('{classifier_id}').get_result()
print (json.dumps(status, indent=2))