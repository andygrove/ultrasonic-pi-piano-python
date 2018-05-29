import sys
import time
from octasonic.octasonic import Octasonic

class Key:
    def __init__(self, note):
        self.note = note
        self.counter = 0	

    def set_note(self, note):
        self.note = note;
        self.counter = 0;

class Synth:
  def __init__(self):
    pass

  def note_on(self, channel, note):
    print "noteon ", channel, " ", note, " ", 127
    sys.stdout.flush()

  def note_off(self, channel, note):
    print "noteoff ", channel, " ", note, " ", 127
    sys.stdout.flush()


def main():
    octasonic = Octasonic(0)
    protocol_version = octasonic.get_protocol_version()
    firmware_version = octasonic.get_firmware_version()
    print "Protocol v%s; Firmware v%s" % (protocol_version, firmware_version)
    octasonic.set_sensor_count(8)
    print "Sensor count: %s" % octasonic.get_sensor_count()

    scale = [0, 2, 4, 5, 7, 9, 11]
    max_distance = 100
    start_note = 12
    octave_offset = 12
    key = []
    for i in range(0,7):
        key.append(Key(0))

    synth = Synth()

    while True:
      for i in range(0,7):
        channel = i + 1
        distance = octasonic.get_sensor_reading(i)
        if distance < max_distance:
            scale_start = start_note + octave_offset * i
            new_note = scale_start + scale[distance%7]
            if new_note != key[i].note:
                synth.note_on(channel, new_note)



     

if __name__ == "__main__":
    main()
