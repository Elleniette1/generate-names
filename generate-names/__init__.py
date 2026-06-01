import random
from bisect import bisect_left
from os.path import abspath, join, dirname

def _load(file: str):
    names, cumulative = [], []
    with open(file, 'r') as f:
        for line in f:
            parts = line.split()
            names.append(parts[0])
            cumulative.append(float(parts[2]))
        max_cum = cumulative[-1]
    return names, cumulative, max_cum

_data = lambda f: abspath(join(dirname(__file__), 'data', f))

female_names, female_cum, female_max = _load(_data('dist.female.first'))
male_names, male_cum, male_max = _load(_data('dist.male.first'))
last_names, last_cum, last_max = _load(_data('dist.all.last'))

def generate_name(sex: str = 'male', last: bool = False) -> str:
    if sex.lower() == 'male':
        n = random.uniform(0, male_max)
        name: str = male_names[bisect_left(male_cum, n)]
    elif sex.lower() == 'female':
        n = random.uniform(0, female_max)
        name: str = female_names[bisect_left(female_cum, n)]
    else:
        name = ""
    if last:
        n = random.uniform(0, last_max)
        return f"{name} {last_names[bisect_left(last_cum, n)]}".strip().title()