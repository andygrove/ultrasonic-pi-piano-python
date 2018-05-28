from octasonic.octasonic import Octasonic

if __name__ == '__main__':
    octa = Octasonic(0)
    print octa.get_firmware_version()