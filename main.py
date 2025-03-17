import numpy as np
import cv2
import midiutil
from scipy.fftpack import fft2, fftshift
import random

# Carregar imagem e verificar se foi carregada corretamente
imagem = cv2.imread("download2.jpg")
if imagem is None:
    raise ValueError("Erro ao carregar a imagem. Verifique o caminho do arquivo.")

# Aplicar Transformada de Fourier para cada canal de cor (RGB)
fft_b = fft2(imagem[:, :, 0])  # Canal azul
fft_g = fft2(imagem[:, :, 1])  # Canal verde
fft_r = fft2(imagem[:, :, 2])  # Canal vermelho

# Fazer o deslocamento de Fourier (shift)
fft_b_shift = fftshift(fft_b)
fft_g_shift = fftshift(fft_g)
fft_r_shift = fftshift(fft_r)

# Calcular a magnitude para cada canal
magnitude_b = np.abs(fft_b_shift)
magnitude_g = np.abs(fft_g_shift)
magnitude_r = np.abs(fft_r_shift)

# Evitar valores muito pequenos antes de aplicar log
magnitude_b[magnitude_b == 0] = np.min(magnitude_b[magnitude_b > 0])
magnitude_g[magnitude_g == 0] = np.min(magnitude_g[magnitude_g > 0])
magnitude_r[magnitude_r == 0] = np.min(magnitude_r[magnitude_r > 0])

# Aplicar log na magnitude
magnitude_b = np.log(magnitude_b)
magnitude_g = np.log(magnitude_g)
magnitude_r = np.log(magnitude_r)

# Normalizar os valores para o intervalo de notas do piano (21 a 108 no MIDI)
min_freq_b, max_freq_b = np.min(magnitude_b), np.max(magnitude_b)
min_freq_g, max_freq_g = np.min(magnitude_g), np.max(magnitude_g)
min_freq_r, max_freq_r = np.min(magnitude_r), np.max(magnitude_r)

if min_freq_b == max_freq_b: max_freq_b += 1
if min_freq_g == max_freq_g: max_freq_g += 1
if min_freq_r == max_freq_r: max_freq_r += 1

# Normalizar cada canal individualmente
normalized_b = np.interp(magnitude_b, (min_freq_b, max_freq_b), (0, 1))
normalized_g = np.interp(magnitude_g, (min_freq_g, max_freq_g), (0, 1))
normalized_r = np.interp(magnitude_r, (min_freq_r, max_freq_r), (0, 1))

# Ajuste não linear para equilibrar graves e agudos
normalized_b = np.power(normalized_b, 0.5)
normalized_g = np.power(normalized_g, 0.5)
normalized_r = np.power(normalized_r, 0.5)

# Normalizar para o intervalo de notas do piano (21 a 108)
normalized_b = np.interp(normalized_b, (0, 1), (21, 108))
normalized_g = np.interp(normalized_g, (0, 1), (21, 108))
normalized_r = np.interp(normalized_r, (0, 1), (21, 108))

# Identificar os picos mais relevantes
num_picos = 400  # Quantidade de notas a serem tocadas
indices_b = np.dstack(np.unravel_index(np.argsort(-magnitude_b.ravel()), magnitude_b.shape))[0][:num_picos]
indices_g = np.dstack(np.unravel_index(np.argsort(-magnitude_g.ravel()), magnitude_g.shape))[0][:num_picos]
indices_r = np.dstack(np.unravel_index(np.argsort(-magnitude_r.ravel()), magnitude_r.shape))[0][:num_picos]

# Criar arquivo MIDI
midi = midiutil.MIDIFile(1)
midi.addTempo(0, 0, random.randint(90, 130))  # Tempo variável para humanização

duration = 3 * 60  # 2 minutos em segundos
tempo_base = duration / num_picos

# Definir probabilidades de pausas e variação de notas
pause_chance = 0.15  # 15% de chance de pausa
chord_chance = 0.2   # 20% de chance de tocar um acorde

# Função para gerar acordes
def criar_acorde(note, intervalo=3):
    return [note, note + intervalo, note + 7]  # Acorde de terça maior e quinta

# Adicionar notas com variação de tempo, dinâmica e pausas
for i in range(num_picos):
    if random.random() < pause_chance:
        continue  # Criar pausas aleatórias

    # Combinação das magnitudes dos três canais para determinar a nota
    note = int((normalized_b[indices_b[i][0], indices_b[i][1]] + 
                normalized_g[indices_g[i][0], indices_g[i][1]] + 
                normalized_r[indices_r[i][0], indices_r[i][1]]) / 3)
    
    velocity = int(np.interp(np.mean([magnitude_b[indices_b[i][0], indices_b[i][1]], 
                                      magnitude_g[indices_g[i][0], indices_g[i][1]], 
                                      magnitude_r[indices_r[i][0], indices_r[i][1]]]), 
                             (min(min_freq_b, min_freq_g, min_freq_r), max(max_freq_b, max_freq_g, max_freq_r)), 
                             (50, 127)))  # Dinâmica variável
    
    start_time = i * tempo_base + random.uniform(-0.15, 0.15)  # Mais variação no tempo
    note_length = random.uniform(0.4, 2.0)  # Notas de duração variada
    midi.addNote(0, 0, note, max(0, start_time), note_length, velocity)

    # Criar acordes ocasionais
    if random.random() < chord_chance:
        acordes = criar_acorde(note)
        for acorde in acordes:
            midi.addNote(0, 0, acorde, max(0, start_time), note_length, max(50, velocity - 20))

# Salvar arquivo MIDI
with open("output.mid", "wb") as f:
    midi.writeFile(f)

print("Arquivo MIDI gerado: output.mid")
