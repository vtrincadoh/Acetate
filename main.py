import logging

from lib import * #} pylint: disable=unused-import
import csv
from const import TAG_ATTRIBUTES
from datetime import datetime
from re import sub

csv.register_dialect('semicolon', delimiter=';', quoting=csv.QUOTE_NONE)

base_filename = input('Drag input CSV:')
start_time = datetime.now()
base_filename = cleanFilename(base_filename)

logging.basicConfig(filename=base_filename+'.log',
                    format='%(asctime)s %(message)s',
                    filemode='w')
        
csv_output = open(base_filename+'_OUTPUT.csv', 'w', newline='')
csv_writer = csv.DictWriter(csv_output, SHOPIFY_DICT.keys())

csv_input = open(base_filename + '.csv', 'r', encoding= 'utf-8-sig')
csv_reader = csv.DictReader(csv_input, dialect='semicolon')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

csv_writer.writeheader()

for row in csv_reader:
    try:
        release = searchByProperty(row['barcode'], 'barcode')
    except RuntimeError as error:
        logger.error(error)
        print(error)
        continue
    tags = extractTags(release, TAG_ATTRIBUTES)
    tags = row | tags

    shopify_row = {}

    for key in SHOPIFY_DICT.keys():
        shopify_row.update({key: valueOfShopifyProperty(tags, key)})

    try:
        csv_writer.writerow(shopify_row)
    except UnicodeEncodeError:
        def replaceSpecialChars(data):
            if not isinstance(data, str):
                return data
            
            return sub('[^A-Za-z0-9]+', '', data)
        shopify_row = {key: replaceSpecialChars(value) for key, value in shopify_row.items()}
        csv_writer.writerow(shopify_row)
    release_ok = '{0} - {1} // OK'.format(tags['artists'], tags['title'])
    #logger.info(release_ok)
    print(release_ok)

csv_input.close()
csv_output.close()

end_time = datetime.now()
delta_time = str(end_time - start_time).split('.')[0]

print('Done! Completed in {0}'.format(delta_time))