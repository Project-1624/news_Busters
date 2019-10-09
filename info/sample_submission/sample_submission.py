"""This script is a sample submission for the Leaders Prize competition.
It reads in a dataset and creates a sample predictions file.
"""

import json
import os
from random import randint


# These are the file paths where the validation/test set will be mounted (read only)
# into your Docker container.
METADATA_FILEPATH = '/usr/local/dataset/metadata.json'
ARTICLES_FILEPATH = '/usr/local/dataset/articles'

# This is the filepath where the predictions should be written to.
PREDICTIONS_FILEPATH = '/usr/local/predictions.txt'


# Read in the metadata file.
with open(METADATA_FILEPATH, 'r') as f:
    claims = json.load(f)

# Inspect the first claim.
claim = claims[0]
print('Claim:', claim['claim'])
print('Speaker:', claim['claimant'])
print('Date:', claim['date'])
print('Related Article Ids:', claim['related_articles'])

# Print the first evidence article.
idx = claim['related_articles'][0]
print('First evidence article id:', idx)
with open(os.path.join(ARTICLES_FILEPATH, '%d.txt' % idx), 'r') as f:
    print(f.read())

# Create a predictions file.
print('\nWriting predictions to:', PREDICTIONS_FILEPATH)
with open(PREDICTIONS_FILEPATH, 'w') as f:
    for claim in claims:
        f.write('%d,%d\n' % (claim['id'], randint(0, 2)) )
print('Finished writing predictions.')
