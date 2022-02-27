import discogs_client

from const import SHOPIFY_DICT

discogs = discogs_client.Client('AltoqueInv/0.1', user_token='NYklFhDVlpWgnjwsXzkyvADMuqNKpDqbdPuxlPhN')

def cleanFilename(filename):
    split_filename = filename.split('\'')
    filename = split_filename[-2].split('.')[0] if len(split_filename)>1 else filename.split('.')[0]
    return filename
def searchByProperty(data, property): #property es string, chequear valores de discogs_client
    def improvedMatch(releases):
        individual_release = next(releases, None)
        match individual_release:
            case None:
                raise RuntimeError('Release not found! - {0}: {1}'.format(property, data))
            case discogs_client.models.Release():
                return individual_release
            case discogs_client.models.Master():
                return individual_release.main_release
            case _:
                releases.remove(individual_release)
                return improvedMatch(releases)
    
    releases = discogs.search(str(data), type=property)
    return improvedMatch(iter(releases))
def extractTags(release, tag_attributes):
    def numberOfRecords(tracklist):
        try:
            tracks = {track.position[0] for track in tracklist}
        except:
            tracks = range(1)
        return len(tracks)
    
    '''
    Items in tag_attributes do not support list indexing, or sub-attributes
    '''
    tags = {}

    for attr in tag_attributes:
        item_in_dict = {attr: getattr(release, attr)}
        tags.update(item_in_dict)

        match attr:
            case ('artists' | 'labels'):
                tags[attr] = tags[attr][0].name.upper()
            case 'images':
                tags[attr] = tags[attr][0]['resource_url']
            case 'genres':
                tags[attr] = ','.join([tag.upper() for tag in tags[attr]])
            case 'tracklist':
                tags[attr] = numberOfRecords(tags[attr])
            case _:
               tags[attr] = str(tags[attr]).upper()
    return tags
def assignTags(tags, worksheet):
    worksheet.append(tags)
    return worksheet
def valueOfShopifyProperty(tags_row, shopify_key):
    def reqTags(shopify_attr):
        req_props = SHOPIFY_DICT[shopify_attr]
        req_tags = req_props['args']
        req_function = req_props['func']
        return req_tags, req_function

    req_tags, req_function = reqTags(shopify_key)
    args = (tags_row[tag] for tag in req_tags)
    shopify_prop = req_function(*args) 
    return shopify_prop 