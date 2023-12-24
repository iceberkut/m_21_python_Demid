import wave
import struct


def break_the_silence():
    original = wave.open("in.wav", mode="rb")
    res = wave.open("out.wav", mode="wb")
    res.setparams(original.getparams())
    frames_count = original.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h",
                         original.readframes(frames_count))
    newdata = list(filter(lambda x: abs(x) > 5, data))
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    res.writeframes(newframes)
    original.close()
    res.close()


break_the_silence()
