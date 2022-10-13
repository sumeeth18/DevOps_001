# dictionaries is collection of values for their list which are closed in curly braces
# eg:
def state_wise_capital():
    state_capital = {
        'Maharashtra': 'Mumbai',
        'Karnataka': 'Bengaluru',
        'Kerala': 'Cochin',
        'Telangana': 'Hyderabad'
    }

    ca_capital = state_capital['Kerala']
    print(ca_capital)

    for k in state_capital.keys():
        print('{} is the capital of {}'.format(state_capital[k], k))

