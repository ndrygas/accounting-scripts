"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness 


def print_melon(name, price, seedless, flesh_color = None, 
                rind_color = None, average_weight = None):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # for key, value in name:
    caps = name.upper()

    print(f'''{caps}\nPrice: {price}\nSeedless: {seedless}
Flesh Color: {flesh_color}\nRind Color: {rind_color}
Average Weight: {average_weight}\n''')


for i in melon_names:
    print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
