from lesson4.MobileDevices import MobileDevice

# device1 = MobileDevice()
# device1.price = 30000
# device1.model = "xyomi"
# device1.os = "android"
# device1.has_flash = True
# device1.version = 0.1
#
# device1.print_parameters()
#
# device2 = MobileDevice()
# device2.screen_height = 20
# device2.screen_width = 50
# device2.has_flash = False
#
# device2.calculate_area()
# device2.picture_quality()

device1 = MobileDevice(20, -30, "samsung", "android", 2.0, True, 3000)
device1.print_parameters()
