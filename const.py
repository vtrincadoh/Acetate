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
     'args': ('genres', ), ### Ver en más detalle
     'func': lambda x:x},
 'Published': {
     'args': (), 
     'func': lambda :'TRUE'},
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
     'func': lambda:"deny"},
 'Variant Fulfillment Service': {
     'args': (), 
     'func': lambda:"manual"},
 'Variant Price': {
     'args': ('price', ), 
     'func': lambda x:x},
 'Variant Compare At Price': {
     'args': (), 
     'func': lambda:""},
 'Variant Requires Shipping': {
     'args': (), 
     'func': lambda:"TRUE"},
 'Variant Taxable': {
     'args': (), 
     'func': lambda:"TRUE"},
 'Variant Barcode': {
     'args': ('barcode', ), ### FIXED TO N&R
     'func': lambda b: b},
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
     'func': lambda:"FALSE"},
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
     'func': lambda:"g"},
 'Variant Tax Code': {
     'args': (), 
     'func': lambda:""},
 'Cost per item': {
     'args': (), 
     'func': lambda:""},
 'Status': {
     'args': (), 
     'func': lambda:"active"},
 'Standard Product Type': {
     'args': (), 
     'func': lambda:""},
 'Custom Product Type': {
     'args': (), 
     'func': lambda:'Nuevos & Reediciones'}
 }

TAG_ATTRIBUTES = ['artists', 'title', 'labels', 'genres', 'year', 'country', 'images', 'tracklist']