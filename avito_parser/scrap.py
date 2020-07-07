from avito_parser import get_all_ads

ads = get_all_ads('ps4', sort_by='date', by_title=True)
print(ads)