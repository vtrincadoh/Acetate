SHOPIFY_DICT = {
 'Handle': {
     'args': ('artists', 'title'), 
     'func': lambda artist, title: (artist + '-' + title).lower().replace(' ', '-')},
 'Title': {
     'args': ('artists', 'title'), 
     'func': lambda artist, title: artist + ' - ' + title},
 'Body (HTML)': {
     'args': (), ### Ver en más detalle
     'func': lambda:""},
 'Vendor': {
     'args': ('labels', ), 
     'func': lambda x:x},
 'Tags': {
     'args': (), ### Ver en más detalle
     'func': lambda:""},
 'Published': {
     'args': (), 
     'func': lambda :True},
 'Option1 Name': {
     'args': (), 
     'func': lambda:""},
 'Option1 Value': {
     'args': (), 
     'func': lambda:""},
 'Option2 Name': {
     'args': (), 
     'func': lambda:""},
 'Option2 Value': {
     'args': (), 
     'func': lambda:""},
 'Option3 Name': {
     'args': (), 
     'func': lambda:""},
 'Option3 Value': {
     'args': (), 
     'func': lambda:""},
 'Variant SKU': {
     'args': ('barcode', ), # FIXED TO N&R
     'func': lambda b: 'N'+b},
 'Variant Grams': {
     'args': ('tracklist', ), 
     'func': lambda x:x*110},
 'Variant Inventory Tracker': {
     'args': (), 
     'func': lambda:'shopify'},
 'Variant Inventory Qty': {
     'args': ('qty', ), 
     'func': lambda x:x},
 'Variant Inventory Policy': {
     'args': (), 
     'func': lambda:""},
 'Variant Fulfillment Service': {
     'args': (), 
     'func': lambda:""},
 'Variant Price': {
     'args': ('price', ), 
     'func': lambda x:x},
 'Variant Compare At Price': {
     'args': (), 
     'func': lambda:""},
 'Variant Requires Shipping': {
     'args': (), 
     'func': lambda:""},
 'Variant Taxable': {
     'args': (), 
     'func': lambda:""},
 'Variant Barcode': {
     'args': ('barcode', ), ### FIXED TO N&R
     'func': lambda b: str(ord('N'))+b},
 'Image Src': {
     'args': ('images', ), 
     'func': lambda x:x},
 'Image Position': {
     'args': (), 
     'func': lambda: 1},
 'Image Alt Text': {
     'args': (), 
     'func': lambda:""},
 'Gift Card': {
     'args': (), 
     'func': lambda:""},
 'SEO Title': {
     'args': (), 
     'func': lambda:""},
 'SEO Description': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Google Product Category': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Gender': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Age Group': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / MPN': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / AdWords Grouping': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / AdWords Labels': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Condition': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Custom Product': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Custom Label 0': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Custom Label 1': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Custom Label 2': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Custom Label 3': {
     'args': (), 
     'func': lambda:""},
 'Google Shopping / Custom Label 4': {
     'args': (), 
     'func': lambda:""},
 'Variant Image': {
     'args': (), 
     'func': lambda:""},
 'Variant Weight Unit': {
     'args': (), 
     'func': lambda:""},
 'Variant Tax Code': {
     'args': (), 
     'func': lambda:""},
 'Cost per item': {
     'args': (), 
     'func': lambda:""},
 'Status': {
     'args': (), 
     'func': lambda:""},
 'Standard Product Type': {
     'args': (), 
     'func': lambda:""},
 'Custom Product Type': {
     'args': (), 
     'func': lambda:""}
 }

TAG_ATTRIBUTES = ['artists', 'title', 'labels', 'genres', 'year', 'country', 'images', 'tracklist']