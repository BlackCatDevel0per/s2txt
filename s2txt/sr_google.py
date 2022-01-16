import speech_recognition as sr
import pyaudio
import wave

#import asyncio



from awaits.awaitable import awaitable  # Amazing!

@awaitable
def s2txt_google(device_index: int = 1, language: str = "ru", clear_voice: bool = False, timeout: int = 2, phrase_time_limit: int = 10):
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=device_index) as source:
            if clear_voice is True:
                r.adjust_for_ambient_noise(source)  # Удаление шума
            #print("Say anything...")
            # Входной звук + таймаут
            audio = r.listen(source, timeout=timeout,
                             phrase_time_limit=phrase_time_limit)
            # audio = r.listen(source)  # Входной звук

        # Отправка голоса в Google
        txt = r.recognize_google(audio, language=language)
        lowtxt = txt.lower()
        #print("Text: " + lowtxt)

        # return txt
        return lowtxt
    except sr.UnknownValueError:
        return "SPErr01: Не удалось распознать аудио"
    except sr.RequestError:
        return "SPErr02: Не удалось запросить результаты из службы распознавания речи"
    except sr.WaitTimeoutError:
        return "SPErr03: Превышено время ожидания речи"

    except Exception as e:
        if "[Errno -9998] Invalid number of channels" in str(e):
            return "SPErr04: Вы выбрали верное устройство для ввода звука?"
        else:
            return f"SPErr0666: {e}"
