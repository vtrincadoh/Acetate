import logging

from lib import * #} pylint: disable=unused-import
import csv
from const import TAG_ATTRIBUTES
from datetime import datetime

logging.basicConfig(filename='output.log',
                    format='%(asctime)s %(message)s',
                    filemode='w')
        
csv_output = open('csv_shopify.csv', 'w', newline='')
csv_writer = csv.DictWriter(csv_output, SHOPIFY_DICT.keys())

csv_input_filename = input('Drag input CSV:')
start_time = datetime.now()
csv_input_filename = cleanFilename(csv_input_filename)
csv_input = open(csv_input_filename, 'r', encoding= 'utf-8-sig')
csv_reader = csv.DictReader(csv_input)

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
    
    csv_writer.writerow(shopify_row)
    release_ok = '{0} - {1} // OK'.format(tags['artists'], tags['title'])
    logger.info(release_ok)
    print(release_ok)

csv_input.close()
csv_output.close()

end_time = datetime.now()
delta_time = str(end_time - start_time).split('.')[0]

print('Done! Completed in {0}'.format(delta_time))