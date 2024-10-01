from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('привет', "гамарджоба")
print(a)