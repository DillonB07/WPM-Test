from essential_generators import DocumentGenerator

gen = DocumentGenerator()


with open('text.txt', 'w') as f:
    for _ in range(1000000):
        sentence = gen.sentence()
        f.write(f'{sentence}\n')
