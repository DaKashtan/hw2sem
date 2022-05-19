import re

def pattern(fprimer, rprimer):
    fprimer, rprimer = fprimer.upper(), rprimer.upper()
    fdict = {'A': 'A', 'T': 'T', 'C': 'C', 'G': 'G', 'B': '[CGT]', 'D': '[AGT]', 'H': '[ACT]', 'K': '[GT]',
                 'M': '[AC]', 'N': '[ACGT]', 'R': '[GA]', 'S': '[GC]', 'V': '[ACG]', 'W': '[AT]', 'Y': '[CT]'}
    rdict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'B': '[GCA]', 'D': '[TCA]', 'H': '[TGA]', 'K': '[CA]',
               'M': '[TG]', 'N': '[ACGT]', 'R': '[CT]', 'S': '[CG]', 'V': '[TGC]', 'W': '[TA]', 'Y': '[GA]'}
    pattern = ''
    for i in fprimer:
        pattern += fdict[i]
    pattern += '.+'
    for j in rprimer:
        pattern += rdict[j]
    return pattern

with open(input('Введите имя файла в формате fasta: ') as seq_file:
    name_sequence = []
    sequence = []
    for l in seq_file:
        if '>' in l:
            name_sequence.append(l.strip())
        else:
            sequence.append(l.strip())
fprimer = input('Прямой праймер: ')
rprimer = input('Обратный праймер: ')
patt = pattern(fprimer, rprimer)
for i in range(len(sequence)-1):
    res_search = re.findall(patt, sequence[i])
    if res_search==[]:
        continue
    print(res_search)

