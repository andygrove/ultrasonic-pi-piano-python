from octasonic.octasonic import Octasonic

def main():
    octasonic = Octasonic(0)
    protocol_version = octasonic.get_protocol_version()
    firmware_version = octasonic.get_firmware_version()
    print "Protocol v%s; Firmware v%s" % (protocol_version, firmware_version)
    octasonic.set_sensor_count(8)
    print "Sensor count: %s" % octasonic.get_sensor_count()
    for x in range(0, 100):
        octasonic.toggle_led()
        time.sleep(0.25)
        for i in range(0, 7):
            print octasonic.get_sensor_reading(i),
        print

if __name__ == "__main__":
    main()