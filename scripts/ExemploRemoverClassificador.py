import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{apikey}',
    url='{url}')

status = natural_language_classifier.delete_classifier('{classifier_id}').get_result()
print(json.dumps(status, indent=2))