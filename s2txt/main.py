import speech_recognition as sr
import pyaudio
import wave

# first install pyaudio!!!
def get_device_index(data: str = "name&index"):
    names = list()
    indexes = list()
    nameWindex = dict()
    mics = enumerate(sr.Microphone.list_microphone_names())
    for index, name in mics:
        names.append(name)
        indexes.append(index)
        nameWindex[name] = index
        #print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))

    if data == "name":
        return names  # return name list
    elif data == "index":
        return indexes  # return index list
    elif data == "name&index":
        # return names, indexes
        return nameWindex  # return dictonary name=index (default)
    else:
        return "Input Error!"
"""
	mics = sr.Microphone.list_microphone_names()
	print(mics)
"""