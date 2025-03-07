import pyautogui as pa
import time
from random_word import RandomWords

pa.PAUSE = 2

r = RandomWords()
palavra_aleatoria = r.get_random_word()

pa.press ('win')
pa.write ('edge')
pa.press ('ENTER')

time.sleep (5)

pa.write(palavra_aleatoria)
pa.press ('ENTER')
time.sleep (5)

num_pesquisas = 3

for _ in range(num_pesquisas):
    pa.hotkey('ctrl','t')
    time.sleep(5)
    palavra_aleatoria = r.get_random_word()

    pa.write(palavra_aleatoria)
    pa.press ('ENTER')

    time.sleep(10)
    pa.hotkey('ctrl','w')
    time.sleep(5)