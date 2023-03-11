import json
from pprint import pprint

with open("service-policy.json", "r") as open_file:
    policy = json.load(open_file)

(policy["Statement"]["Effect"]) = "Deny"

with open("service-policy.json", "w") as opened_file:
    policy = json.dump(policy, opened_file)

pprint(policy)


