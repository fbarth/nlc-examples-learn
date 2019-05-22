import json
from ibm_watson import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{apikey}',
    url='{url}')

with open('../data/train.csv', 'rb') as training_data:
    classifier = natural_language_classifier.create_classifier(
        training_data=training_data, 
        metadata='{"name": "Sao Paulo","language": "pt"}').get_result()
print(json.dumps(classifier, indent=2))

