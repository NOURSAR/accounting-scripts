melon_names = {
    'Honeydew': { 'price': 0.99,
                  'seedlessness': True,
                  'flesh_color': None,
                  'wiegt': None,
                  'rind_color': None,
                  'source': None
                },
    'Crenshaw': {'price': 2.00,
                 'seedlessness': False,
                 'flesh_color': None,
                 'wieght': None,
                 'rind_color': None,
                 'source': None
                },
    'Crane':    {'price': 2.50,
                 'seedlessness': False,
                 'flesh_color': None,
                 'wieght': None,
                 'rind_color': None,
                 'source': None,
                },
    'Casaba':   {'price': 2.50,
                 'seedlessness': False,
                 'flesh_color': None,
                 'wieght': None,
                 'rind_color': None,
                 'source': None
                },
    'Cantaloupe':{'price': 2.00,
                 'seedlessness': False,
                 'flesh_color': None,
                 'wieght': None,
                 'rind_color': None,
                 'source': None
                 }
}

for k, v in melon_names.items():  #will get an error without .items()
    print(k)
    for b in v:
        print(b, v[b])
