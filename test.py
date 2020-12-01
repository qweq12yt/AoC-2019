# Python Code
seq = [0, 1, 1]
for i in range(3, 10):
    seq.append(seq[i - 1] + seq[i - 2])

soma = sum(seq)
media = soma / 10
print('Soma = {}\nMedia = {}'.format(soma, media))