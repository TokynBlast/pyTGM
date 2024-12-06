try:
    import pytgm as tgm

    print('graphics.clear ------------ False')
    tgm.graphics.cls()
    print('graphics.clear ------------ True')

    #tgm.sound.file('sound.mp3')

    if tgm.random.num.integer(1, 2) in (range(1, 2)):
        print('random.num.integer -------- True')
    else:
        print('random.num.integer -------- False')
        

    if tgm.random.num.binary() in (0, 1):
        print('random.num.binary --------- True')
    else:
        print('random.num.binary --------- False')

    if tgm.random.seq.choose.choice([1]) == 1:
        print('random.seq.choose.choice -- True')
    else:
        print('random.seq.choose.choice -- False')

    if tgm.random.seq.choose.choices([1], 1) == [1]:
        print('random.seq.choices -------- True')
    else:
        print('random.seq.choices -------- False')

    if tgm.random.seq.modify.shuffle([1], 1) == [1]:
        print('random.modify.shuffle ----- True')
    else:
        print('random.modify.shuffle ----- Fasle')

    if tgm.random.seq.modify.duplicate([1], 1) == [1,1]:
        print('random.modify.duplicate -- True')
    else:
        print('random.modify.duplicate --- False')

    if tgm.random.seq.modify.remove([1, 1], 1) == [1]:
        # MAKE A SET AMOUNT TO  REMOVE! BUT BY DEFAULT, REMOVE ALL
        print('random.modify.remove ------ True')
    else:
        print('random.modify.remove ------ False')
        print(tgm.random.seq.modify.remove([1, 1], 1))

    if tgm.file.read.document('blank.txt') == '':
        print('tgm.read.document -------- True')
    else:
        print('tgm.read.document -------- False')


    tgm.graphics.color.RGB(255,0,0)
    print('graphics.pcolor --------- Colored')
    print(tgm.graphics.color.res)

    def frequency(frequency, duration, sample_rate=44100, volume=0.5):
        import wave
        import math

        n_samples = int(sample_rate * duration)
        samples = []
        for i in range(n_samples):
            sample = volume * math.sin(2 * math.pi * frequency * (i / sample_rate))
            samples.append(int(sample * 32767))  # Convert to 16-bit PCM format

        # Write to a temporary WAV file
        with wave.open('temp_tone.wav', 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(bytearray(samples))

        if os.name == 'nt':  # For Windows
            os.system('start temp_tone.wav')
        elif os.name == 'posix':  # For macOS and Linux
            os.system('afplay temp_tone.wav' if os.uname().sysname == 'Darwin' else 'aplay temp_tone.wav')


except Exception as E:
    print(E)
