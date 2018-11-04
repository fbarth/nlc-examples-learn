import json
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

natural_language_classifier = NaturalLanguageClassifier(
    iam_apikey='{apikey}',
    url='{url}')

classifiers = natural_language_classifier.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))