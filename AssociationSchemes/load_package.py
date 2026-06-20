from sage.all import load

BASE_URL = "https://raw.githubusercontent.com/sarobidy19/association-schemes/refs/heads/main/AssociationSchemes/"

modules_to_load = [
    "permutation_group",
    "generic_schemes",
    "schemes_with_names",
    "perfect_matching"
]

for module_name in modules_to_load:
    url = f"{BASE_URL}{module_name}.py"
    load(url)

print("Package successfully loaded")
