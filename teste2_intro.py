import numpy as np 
import matplotlib.pyplot as plt
import soundfile as sf
import os
from pydub import AudioSegment
import wave

entrada = input('insita o diretório do arquivo:')

carregar_wav = wave.open(entrada, 'r')

def indexar_wav():
    cont = 1
    for nome in os.listdir(entrada):
        nome = nome.split('.')

        novo_nome = cont + '.wav'

        nome.replace(nome[0], novo_nome)
        
        cont = cont + 1


def downmixing(entrada):
    sound = AudioSegment.from_wav(entrada)
    sound = sound.set_channels(1)
    sound.export(entrada, format="wav")


def grafico(entrada):
    signal, samplerate = sf.read(entrada)

    time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate)

    plt.plot(time,signal)
    plt.show()
