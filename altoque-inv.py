from lib import * #} pylint: disable=unused-import
from datetime import datetime

TAG_ATTRIBUTES = ['artists', 'title', 'labels', 'genres', 'year', 'country', 'images']
SRC_STRCT = ('qty', 'price', 'barcode')

old_barcode = ''

filename = input('Drag xlsx file:')
filename = cleanFilename(filename)
startTime = datetime.now()
workbook = openBook(filename)
worksheet = openSheet(workbook)
iter_row = unpackIterRow(worksheet)

for row in iter_row:
    row = dict(zip(SRC_STRCT, (str(item) for item in row)))
    barcode = int(row['barcode'])
    if barcode == old_barcode:
        worksheet = assignTags(list(new_row.values()), worksheet)
        continue
    try:
        release = searchByProperty(barcode, 'barcode')
    except:
        worksheet = assignTags([], worksheet)
        print(' - NOT FOUND - ')
        continue
    release = checkObjectType(release)
    tags = extractTags(release, TAG_ATTRIBUTES)
    new_row = row | tags
    worksheet = assignTags(list(new_row.values()), worksheet)
    print(tags['title'] + ' - OK')
    old_barcode = barcode

saveSheet(workbook)

endTime = datetime.now()
delta = str(endTime-startTime).split('.')[0]
print('Done in {0}'.format(delta))