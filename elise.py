from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame  # it is important to import pygame after that
import base64
import io
def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    pygame.mixer.music.load(music_file)
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    # check if playback has finished
    while pygame.mixer.music.get_busy():
        clock.tick(30)
mid64='''\
TVRoZAAAAAYAAQAEAGBNVHJrAAAAGgD/WAQDAhgIAP9ZAgAAAP9RAwehILMA/y8ATVRyawAAAmwA
/yEBAACwAAAAsCAAAMAuALAHf4FAkExAIEwAEEtAIEsAEExAIEwAEEtAIEsAEExAIEwAEEdAIEcA
EEpAIEoAEEhAIEgAEEVAgQBFAEBAQCBAABBFQCBFABBHQIEARwAQQEAgQAAQREAgRAAQR0AgRwAQ
SECBAEgAEEBAIEAAEExAIEwAEEtAIEsAEExAIEwAEEtAIEsAEExAIEwAEEdAIEcAEEpAIEoAEEhA
IEgAEEVAgQBFAEBAQCBAABBFQCBFABBHQIEARwAQQEAgQAAQSEAgSAAQR0AgRwAQRUCBAEUAEEdA
IEcAEEhAIEgAEEpAIEoAEExAgQBMABBDQCBDABBNQCBNABBMQCBMABBKQIEASgAQQUAgQQAQTEAg
TAAQSkAgSgAQSECBAEgAEEBAIEAAEEpAIEoAEEhAIEgAEEdAQEcAUEBAIEAAEExAIEwAEEBAIEAA
EExAIEwAEExAIEwAEFhAIFgAEEtAIEsAEExAIEwAEEtAIEsAEExAIEwAEEtAIEsAEExAIEwAEEtA
IEsAEExAIEwAEEtAIEsAEExAIEwAEEtAIEsAEExAIEwAEEdAIEcAEEpAIEoAEEhAIEgAEEVAgQBF
AEBAQCBAABBFQCBFABBHQIEARwAQQEAgQAAQREAgRAAQR0AgRwAQSECBAEgAEEBAIEAAEExAIEwA
EEtAIEsAEExAIEwAEEtAIEsAEExAIEwAEEdAIEcAEEpAIEoAEEhAIEgAEEVAgQBFAEBAQCBAABBF
QCBFABBHQIEARwAQQEAgQAAQSEAgSAAQR0AgRwAQRUCBAEUAEEdAIEcAEEhAAP8vAE1UcmsAAAEC
AP8hAQAAsQAAALEgAADBLgCxB26EcJE0QCA0ABA5QCA5ABA8QGA8AGA0QCA0ABA4QIEAOABwNEAg
NAAQOUCBADkAgxA0QDA0AAA5QCA5ABA8QGA8AGA0QCA0ABA4QIEAOABwNEAgNAAQOUCBADkAcDdA
IDcAEDxAgQA8AHA3QCA3ABA7QIEAOwBwNEAwNAAAOUCBADkAQChAICgAEDRAIDQAEEBAIEAAiDA0
QCA0ABA5QCA5ABA8QGA8AGA0QCA0ABA4QIEAOABwNEAgNAAQOUCBADkAgxA0QCA0ABA5QCA5ABA8
QGA8AGA0QDA0AAA4QIEAOABwNEAgNAAQOUBg/y8ATVRyawAAAIYA/yEBAACyAAAAsiAAAMIuALIH
boRAki1AgUAtAGAoQIFAKABgLUCBQC0AgwAtQIFALQBgKECBQCgAYC1AgUAtAGAwQIFAMABgK0CB
QCsAYC1AgUAtAIlgLUCBQC0AYChAgUAoAGAtQIFALQCDAC1AgUAtAGAoQIFAKABgLUCBQC0AAP8v
AA==
'''

# create a memory file object
try:
    # Python27
    midi_str = base64.b64decode(mid64)
    music_file = io.BytesIO(midi_str)
except TypeError:
    # Python3
    midi_bytes = base64.b64decode(mid64.encode())
    music_file = io.BytesIO(midi_bytes)
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
try:
    # use the midi file object from memory
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit

