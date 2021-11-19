SHOPIFY_DICT = {
 'Handle': {
     'args': ('artist', 'title'), 
     'func': lambda artist, title: (artist + '-' + title).lower().replace(' ', '-')},
 'Title': {
     'args': ('artist', 'title'), 
     'func': lambda artist, title: artist + ' - ' + title},
 'Body (HTML)': {
     'args': (), ### Ver en más detalle
     'func': None},
 'Vendor': {
     'args': ('labels'), 
     'func': lambda x:x},
 'Tags': {
     'args': (), ### Ver en más detalle
     'func': None},
 'Published': {
     'args': (), 
     'func': lambda _:True},
 'Option1 Name': {
     'args': (), 
     'func': None},
 'Option1 Value': {
     'args': (), 
     'func': None},
 'Option2 Name': {
     'args': (), 
     'func': None},
 'Option2 Value': {
     'args': (), 
     'func': None},
 'Option3 Name': {
     'args': (), 
     'func': None},
 'Option3 Value': {
     'args': (), 
     'func': None},
 'Variant SKU': {
     'args': ('barcode'), # FIXED TO N&R
     'func': lambda b: 'N'+b},
 'Variant Grams': {
     'args': ('tracklist'), 
     'func': lambda x:len(x)*110},
 'Variant Inventory Tracker': {
     'args': (), 
     'func': lambda _:'shopify'},
 'Variant Inventory Qty': {
     'args': ('qty'), 
     'func': lambda x:x},
 'Variant Inventory Policy': {
     'args': (), 
     'func': None},
 'Variant Fulfillment Service': {
     'args': (), 
     'func': None},
 'Variant Price': {
     'args': ('price'), 
     'func': lambda x:x},
 'Variant Compare At Price': {
     'args': (), 
     'func': None},
 'Variant Requires Shipping': {
     'args': (), 
     'func': None},
 'Variant Taxable': {
     'args': (), 
     'func': None},
 'Variant Barcode': {
     'args': ('barcode'), ### FIXED TO N&R
     'func': lambda b: str(ord('N'))+b},
 'Image Src': {
     'args': ('images'), 
     'func': lambda x:x},
 'Image Position': {
     'args': (), 
     'func': lambda _: 1},
 'Image Alt Text': {
     'args': (), 
     'func': None},
 'Gift Card': {
     'args': (), 
     'func': None},
 'SEO Title': {
     'args': (), 
     'func': None},
 'SEO Description': {
     'args': (), 
     'func': None},
 'Google Shopping / Google Product Category': {
     'args': (), 
     'func': None},
 'Google Shopping / Gender': {
     'args': (), 
     'func': None},
 'Google Shopping / Age Group': {
     'args': (), 
     'func': None},
 'Google Shopping / MPN': {
     'args': (), 
     'func': None},
 'Google Shopping / AdWords Grouping': {
     'args': (), 
     'func': None},
 'Google Shopping / AdWords Labels': {
     'args': (), 
     'func': None},
 'Google Shopping / Condition': {
     'args': (), 
     'func': None},
 'Google Shopping / Custom Product': {
     'args': (), 
     'func': None},
 'Google Shopping / Custom Label 0': {
     'args': (), 
     'func': None},
 'Google Shopping / Custom Label 1': {
     'args': (), 
     'func': None},
 'Google Shopping / Custom Label 2': {
     'args': (), 
     'func': None},
 'Google Shopping / Custom Label 3': {
     'args': (), 
     'func': None},
 'Google Shopping / Custom Label 4': {
     'args': (), 
     'func': None},
 'Variant Image': {
     'args': (), 
     'func': None},
 'Variant Weight Unit': {
     'args': (), 
     'func': None},
 'Variant Tax Code': {
     'args': (), 
     'func': None},
 'Cost per item': {
     'args': (), 
     'func': None},
 'Status': {
     'args': (), 
     'func': None},
 'Standard Product Type': {
     'args': (), 
     'func': None},
 'Custom Product Type': {
     'args': (), 
     'func': None}
 }

TAG_ATTRIBUTES = ['artists', 'title', 'labels', 'genres', 'year', 'country', 'images', 'tracklist']