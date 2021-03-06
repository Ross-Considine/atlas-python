"""
MIT License

Copyright (c) 2018 Claude SIMON (https://q37.info/s/rmnmqd49)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import GPIOq, sys

sys.path.append("./Atlas.python.zip")
sys.path.append("../Atlas.python.zip")
sys.path.append("./Atlas")

import atlastk as Atlas

rPin = None
gPin = None
bPin = None

def readAsset(path):
	return Atlas.readAsset(path, "RGB")

class RGB:
	def __init__(this):
		pass

def set(dom, id, value):
	if value != None:
		dom.setContent(id, value)

def acConnect(RGB,dom,id):
	global rPin, gPin, bPin
	dom.setLayout("", readAsset( "Main.html") )
	set( dom, "Red", rPin)
	set( dom, "Green", gPin)
	set( dom, "Blue", bPin)
	dom.focus("Red")

def convert(hex):
	return int(int(hex,16) * 100 / 256)

def acSelect(RGB, dom, id):
	global rPin, gPin, bPin
	if ( ( rPin != None) and (gPin != None ) and ( bPin != None ) ):
		R = convert(id[0:2])
		G = convert(id[2:4])
		B = convert(id[4:6])
		print (R, G, B)
		GPIOq.softPWMWrite(rPin,100 - R)
		GPIOq.softPWMWrite(gPin,100 - G)
		GPIOq.softPWMWrite(bPin,100 - B)

def getPin(dom, id):
	pin = None
	value = dom.getContent(id).strip()

	try:
		pin = int(value)
		pin = None if ( pin > 99 ) or ( pin < 0 ) else pin
	except:
		pin = None

	if value  and ( pin == None ):
		dom.alert("Invalid pin number!")
		dom.setContent(id, "")
		dom.focus(id)
	elif pin != None:
		GPIOq.softPWMCreate(pin)

	return pin

def acRed(RGB, dom, id):
	global rPin
	rPin = getPin(dom, id)

def acGreen(RGB, dom, id):
	global gPin
	gPin = getPin(dom, id)

def acBlue(RGB, dom, id):
	global bPin
	bPin = getPin(dom, id)

callbacks = {
		"": acConnect,
		"Select": acSelect,
		"Red": acRed,
		"Green": acGreen,
		"Blue": acBlue,
	}

GPIOq.setup()

Atlas.launch(callbacks, RGB, readAsset("Head.html"), "RGB")
