import json
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

natural_language_classifier = NaturalLanguageClassifier(
    iam_apikey='{apikey}',
    url='{url}')

with open('../data/train.csv', 'rb') as training_data:
    classifier = natural_language_classifier.create_classifier(
        training_data=training_data, 
        metadata='{"name": "Sao Paulo","language": "pt"}').get_result()
print(json.dumps(classifier, indent=2))

