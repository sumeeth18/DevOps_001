#creating a function to call in other fucntion by its file name
#creating dictionaries by using curly braces which are sepreted by ,and :
#syntax: varname ={'key:'value',.....}

def State_dictionaries():
    state_list = {
        'ANDHRA PRADESH':' AMARAVATI',
        'ARUNACHAL PRADESH': 'ITANAGAR',
        'ASSAM': 'DISPUR',
        'BIHAR': 'PATNA',
        'CHHATTISGARH': 'RAIPUR',
        'GOA': 'PANAJI',
        'GUJARAT': 'GANDHINAGAR',
        'HARYANA': 'CHANDIGARH',
        'HIMACHAL PRADESH': 'SHIMLA(SUMMER) DHARAMSHALA(WINTER)',
        'JHARKHAND': 'RANCHI',
        'KARNATAKA': 'BENGALURU',
        'KERALA': 'THIRUVANANTHAPURAM',
        'MADHYA PRADESH': 'BHOPAL',
        'MAHARASHTRA': 'MUMBAI',
        'MANIPUR': 'IMPHAL',
        'MEGHALAYA': 'SHILLONG',
        'MIZORAM': 'AIZAWL',
        'NAGALAND': 'KOHIMA',
        'ODISHA': 'BHUBANESWAR',
        'PUNJAB': 'CHANDIGARH',
        'RAJASTHAN': 'JAIPUR',
        'SIKKIM': 'GANGTOK',
        'TAMIL NADU': 'CHENNAI',
        'TELANGANA': 'HYDERABAD',
        'TRIPURA': 'AGARTALA',
        'UTTAR PRADESH': 'LUCKNOW',
        'UTTARAKHAND': 'DEHRADUN(WINTER) GAIRSAIN(SUMMER)',
        'WEST BENGAL': 'KOLKATA'
    }
    ip_state=input("enter state name") # using interactive input method
    ip_state_uppercase=ip_state.upper() #converting to upper case
    state_capital=state_list[ip_state_uppercase]#calling key from dictionaries
    print(f'"{state_capital}" is capital of "{ip_state_uppercase}"') # printing capital city of selected stateusing f string keyword

# State_dictionaries()