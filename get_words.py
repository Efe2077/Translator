from random import sample


with open('Words in German.txt', 'r') as text:
    kit = []
    for el in text.readlines()[0].split(', '):
        kit.append(el.strip().capitalize())
    text.close()

kit = sample(kit, k=len(kit))
