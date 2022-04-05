# Read and Write Serial

import serial
import time

ser = serial.Serial(port='COM7', baudrate=115200, timeout=1)



ser.write('% ***************************************************************\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Created for SDK ver:03.05\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Created using Visualizer ver:3.5.0.0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Frequency:77\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Platform:xWR16xx\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Scene Classifier:best_range_res\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Azimuth Resolution(deg):15\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Range Resolution(m):0.044\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Maximum unambiguous Range(m):9.02\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Maximum Radial Velocity(m/s):1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Radial velocity resolution(m/s):0.13\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Frame Duration(msec):100\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% RF calibration data:None\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Range Detection Threshold (dB):15\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Doppler Detection Threshold (dB):15\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Range Peak Grouping:enabled\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Doppler Peak Grouping:enabled\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Static clutter removal:disabled\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Angle of Arrival FoV: Full FoV\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Range FoV: Full FoV\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% Doppler FoV: Full FoV\n'.encode())
kv= ser.readall()
print(kv)

ser.write('% ***************************************************************\n'.encode())
kv= ser.readall()
print(kv)

ser.write('sensorStop\n'.encode())
kv= ser.readall()
print(kv)



ser.write('flushCfg\n'.encode())
kv= ser.readall()
print(kv)

ser.write('dfeDataOutputMode 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('channelCfg 15 3 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('adcCfg 2 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('adcbufCfg -1 0 1 1 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('profileCfg 0 77 429 7 57.14 0 0 70 1 256 5209 0 0 30\n'.encode())
kv= ser.readall()
print(kv)

ser.write('chirpCfg 0 0 0 0 0 0 0 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('chirpCfg 1 1 0 0 0 0 0 2\n'.encode())
kv= ser.readall()
print(kv)

ser.write('frameCfg 0 1 16 0 100 1 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('lowPower 0 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('guiMonitor -1 1 1 0 0 0 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('cfarCfg -1 0 2 8 4 3 0 15 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('cfarCfg -1 1 0 4 2 3 1 15 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('multiObjBeamForming -1 1 0.5\n'.encode())
kv= ser.readall()
print(kv)

ser.write('clutterRemoval -1 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('calibDcRangeSig -1 0 -5 8 256\n'.encode())
kv= ser.readall()
print(kv)

ser.write('extendedMaxVelocity -1 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('bpmCfg -1 0 0 1\n'.encode())
kv= ser.readall()
print(kv)

ser.write('lvdsStreamCfg -1 0 0 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('compRangeBiasAndRxChanPhase 0.0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('measureRangeBiasAndRxChanPhase 0 1.5 0.2\n'.encode())
kv= ser.readall()
print(kv)

ser.write('CQRxSatMonitor 0 3 5 121 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('CQSigImgMonitor 0 127 4\n'.encode())
kv= ser.readall()
print(kv)

ser.write('analogMonitor 0 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('aoaFovCfg -1 -90 90 -90 90\n'.encode())
kv= ser.readall()
print(kv)

ser.write('cfarFovCfg -1 0 0 8.92\n'.encode())
kv= ser.readall()
print(kv)

ser.write('cfarFovCfg -1 1 -1 1.00\n'.encode())
kv= ser.readall()
print(kv)

ser.write('calibData 0 0 0\n'.encode())
kv= ser.readall()
print(kv)

ser.write('sensorStart\n'.encode())


kv= ser.readall()
print(kv)
