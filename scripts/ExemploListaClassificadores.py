import json
from ibm_watson import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{apikey}',
    url='{url}')

classifiers = natural_language_classifier.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))