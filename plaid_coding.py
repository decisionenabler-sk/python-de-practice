from collections import defaultdict
# Routing nums each routing num to one bank
# Bank name: string (eg Boa, American)
# Bank Id:
# Exmaple :
rn_to_name= {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
    "125": "Amex"
}
name_to_bank_id= [
  # There are multiple common ways to write the name of this bank
  ("Wells Fargo", 1),
  ("Wells", 1),

  ("Chase", 2),
  ("Capital One", 3),
  ("Bank of America", 4),

  # These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]
rn_bank_name = [
  {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
  {
    "123": "Wells Fargo",
    "456": "Chase",
  },
  {
    "123": "Wells",
    "789": "Capital One",
    "456": "Bank of America",
  },
  {
    "123": "Bank of America",
    "456": "Chase",
    "555": "Capital One",
  },
]
# Expected output:
# 123 -> 1
# 456 -> 2
# 789 -> 3
# 555 -> 5,6
output = {"123":[1], "456":[2], "789":[3], "555":[5,6]}
output = {"123":[1,4], "456":[2], "789":[3], "555":[5,6]}
from typing import Dict, List, Tuple

# create_routing_number_mapping combines a map from routing number to bank name with a list of relationships between
# bank names and bank IDs to create a single map with routing numbers as keys and a list of related bank IDs as values.
# Milestone 2
def create_routing_number_mapping(rn_to_name: Dict[str, str], name_to_bank_id: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    output = defaultdict(list)
    for rn,name in rn_to_name.items():
        for bank in name_to_bank_id:
            # print(bank[0])
            if bank[0] ==  name:
                output[rn].append(bank[1])          
    return dict(output)
print(create_routing_number_mapping(rn_to_name, name_to_bank_id))
# Milestone 2
def create_routing_number_mappings(rn_bank_name: List[Dict[str, str]], name_to_bank_id: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    output = defaultdict(list)
    banks = defaultdict(list)
    for nums in rn_bank_name:
        for rn,name in nums.items():
            banks[rn].append(name)
    for rn,names in banks.items():
        for bank in name_to_bank_id:
            if bank[0] in names:
                output[rn].append(bank[1])  
    return dict(output)
create_routing_number_mappings(rn_bank_name, name_to_bank_id)