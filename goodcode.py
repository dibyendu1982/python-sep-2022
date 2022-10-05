
# ~! switch-case is evil or if-else-if

accountList = ["Savings Account", "Checking Account", "Fixed Deposit", "Flexi Deposit"]

def account(accountType):
    if accountType >= 1 and accountType < len(accountList):
        return accountList[accountType -1]
    return "unknown"

key_dict ={
    33: "{UP}",
    45: "{ESC}",
    52: "{PGDN}",
    65: "{Home}",
}

def key_label(key_code):
    #*~ No if else is present here 
    
    #*# Using the non-exception method (get) to avoid getting exception if the key does not match it returns None 
    label = key_dict.get(key_code) 
    # ternary operator --> Condition ? when-true: when-false 
    #                  --> when-true Condition else when-false
    # return label if label is not None else "Unknown" 

    return label or "Unknown"

def key_label1(key_code):
    # Null Coalescing operator 
    return key_dict(key_code) or "Unknown"

print(key_label(34))
print (key_dict.values())
key_dict.update({65: "{DOWN}"})
key_dict.setdefault(67, "Default")

print(key_dict.keys())
print(key_dict.items())