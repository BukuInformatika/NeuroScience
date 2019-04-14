import mindwave, time 

headset = mindwave.Headset('COM4','1425')
time.sleep(2)

headset.connect()
print "Connecting..."

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print "Retrying connect.."
print " Connetcted."

while True:
    #print "Auttention: %s, meditation: %s" % (headset.attention, headset.meditation)
    #print headset.serial_open()
    print headset.raw_value#"raw_value: %s" % (headset.raw_value)
    time.sleep(0.1) #pause 0.5 seconds
