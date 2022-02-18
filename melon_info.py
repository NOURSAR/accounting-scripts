"""Print out all the melons in our inventory."""


from melons import melon_names


def print_melon(name):
    """Print each melon with corresponding attribute information."""
    
    for key_melon, value_melon in melon_names.items():  #will get an error without .items()
        print(key_melon.upper())
        for key in value_melon:
            print(f'{key} : {value_melon[key]}')
print_melon(melon_names)

#print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
#n = list(melon_names.keys())
#m = list(melon_names.values())
#print(melon_names['Honeydew']['price'])