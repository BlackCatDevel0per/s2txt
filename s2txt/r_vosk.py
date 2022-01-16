import os
import queue
import sounddevice as sd
import vosk
import sys

#import asyncio


from awaits.awaitable import awaitable  # Amazing!

@awaitable
# for now only Russian language
def s2txt_vosk(timeout: int, blocksize=8000, samplerate=None, device_index: int = 1):
    q = queue.Queue()

    from config import Config
    modeldir = os.path.join(Config().app_path, 'src', 'model')

    samplerate = None

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    try:
        if not os.path.exists(modeldir):
            print (
                "Please download a model for your language from https://alphacephei.com/vosk/models")
            print (f"and unpack as '{modeldir}' in the current folder.")
            exit(0)
        if samplerate is None:
            device_info = sd.query_devices(device_index, 'input')
            # soundfile expects an int, sounddevice provides a float:
            samplerate = int(device_info['default_samplerate'])
            # print(samplerate) # 48000

        model = vosk.Model(modeldir)

        with sd.RawInputStream(samplerate=int(samplerate * timeout), blocksize=blocksize, device=device_index, dtype='int16',
                               channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    if eval(rec.Result())['text'] is not "":
                        #print("T: "+eval(rec.Result())['text'])
                        text = eval(rec.Result())['text']
                        return text
                        exit(0)
                else:
                    if eval(rec.PartialResult())['partial'] is not "":
                        text = eval(rec.PartialResult())['partial']
                        #print("P: "+eval(rec.PartialResult())['partial'])
                        return text
                        exit(0)

    except KeyboardInterrupt:
        print('\nDone')
        exit(0)
    except Exception as e:
        exit(type(e).__name__ + ': ' + str(e))
