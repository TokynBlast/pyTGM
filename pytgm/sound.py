def file(path):
    try:
        from winsound import PlaySound as PS, SND_FILENAME
        PS(path, SND_FILENAME)
    
    except:
        #macOS

        if os.uname().sysname == 'Darwin':
            system(f'afplay {path}')
         
        try: uname()
        except: from os import uname
        if uname().sysname == 'Darwin':
            try: system('echo  ')
            except: import system
            os.system(f'afplay {path}')
            
        #Linux
        else:
            try: system('echo  ')
            except: from os import system
            system(f'aplay {path}')

class frequency:
    import wave, math
    @staticmethod
    def big(frequency, duration, name, sample_rate=44100, volume=0.5):
        import os, array
        n_samples = int(sample_rate * duration)
    
        samples = array.array('h')
        
        for i in range(n_samples):
            t = i / sample_rate
            sample_value = volume * math.sin(2 * math.pi * frequency * t)
            samples.append(int(sample_value * 32767))
    
        with wave.open(name, 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(samples.tobytes())
    @staticmethod
    def small(frequency, duration, name, sample_rate=44100, volume=0.5):
        n_samples = int(sample_rate * duration)
        samples = []
        for i in range(n_samples):
            sample = volume * math.sin(2 * math.pi * frequency * (i / sample_rate))
            samples.append(int(sample * 32767))  # Convert to 16-bit PCM format
    
        # Write to a temporary WAV file
        with wave.open(name, 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(bytearray(samples))
    
    
