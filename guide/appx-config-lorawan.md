---
layout: single
title: BMON and Building Monitoring
toc: true
---

# **Configuring LoRaWAN Sensors for BMON**
{: #configuring-lorawan-sensors}

This section shows how to:

  - Register a LoRaWAN sensor on the [Things
    Network](https://www.thethingsnetwork.org/), the freely available
    network of servers that can accept sensor readings and forward them
    to BMON. This section assumes that there already is a Things Network
    account set up, and that there is an Application set up in that
    account that has the proper Integration for forwarding sensor
    readings to BMON.

  - Configure Elsys and Dragino sensors for use with your Things Network
    account and BMON.

<details markdown="1">

<summary>Registering a Sensor on the Things Network</summary>

Once an Application on the Things Network has been set up to receive
sensor readings and forward them to BMON via an HTTP Integration,
individual sensors must be registered with that Application.

[This Video by Things
Industries](https://www.youtube.com/watch?v=PpbkBgz1CbI) shows how to
create an Application and manually add Devices to that application. Note
that Application creation for the BMON Application should already be
done, so that portion of the video is not important. Also, the video
talks about adding a Payload Formatter to a Device; this also is not
needed as the payload data from the sensor is decoded and formatted
inside of BMON, not in the Things Application.

Adding a Device

For both the Elsys and Dragino sensors discussed in this document, here
are screenshots of critical settings (but not all settings) when
manually adding a Device:

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image3.png)
<br>{: #image3}*Screenshot of Some Critical Settings When Adding a Device*

For the “End device ID" shown below, you must create an ID that starts
with a code indicating the model of sensor. For the sensors known by
BMON, here are the codes:

**ers** : Any of the Elsys ERS sensors

**elt**: Either the Elsys ELT-Lite or the ELT-2 sensors

**lht65**: The Dragino LHT65 sensor

**ldds**: The Dragino LDDS20 or LDDS75 liquid level and distance sensors

**lwl01**: The Dragino LWL01 Water Leak Sensor

*Screenshot of More Critical Settings When Adding a Device*
![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image1.png)
<br>{: #image1}

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image2.png)
<br>{: #image2}

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image8.png)
<br>{: #image8}

The simplest way to enter a batch of Elsys sensors is to use the
[Elsys-to-Things Tool](https://elsys-to-things.bmon.org/). This web
application has you upload the CSV order file that Elsys provides with
each order; this file contains the critical IDs and keys for each of the
sensors. The Elsys-to-Things tool can then create a JSON file of the
proper format to upload to the Things Console at this “Import end
devices" link on the End Devices page in the Things Console:

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image14.png)
<br>{: #image14}*Import End Devices link on the End Devices Page*

The full batch of sensors will be entered into your Things Account at
one time.

</details>

# **Configuring an Elsys Sensor**
{: #configuring-elsys-sensor}

A LoRaWAN sensor needs to be configured in order to tell it a number of
things:

  - How frequently to report its readings.

  - What type of external sensor is connected (e.g. temperature, pulse,
    switch)

  - What frequencies the sensor should operate on.

  - Other settings related to the LoRaWAN network it is working with.

Many of these settings can be configured at the Elsys factory if you
request to do so with your order. There is a 1 EU charge per sensor for
orders less than quantity 100.

Even with factory configuration, adjustments to settings often need to
be made. Elsys sensors such as the ERS or ELT-Lite are configured
through use of an Android or Apple phone (in the respective App Stores,
search for “Elsys" to find the “Sensor settings" app). Settings are
entered into the phone application, and then the phone is “bumped"
against the sensor to transfer the settings (this is the conventional
NFC phone tap technology used to make payments at a store or
restaurant). Some inexpensive Android phones may not have NFC technology
so will not work with the Elsys app. Some relatively inexpensive Android
phones that do have NFC capability from vendors like Amazon are: Nokia
7.1, Ulefone Armor X7 Pro, Cubot Note 20 Pro, Blackview BV5500. You do
not need to buy a cellular plan to use the phone, as you can connect the
phone to Wi-Fi and download the necessary app.

When using the Elsys Sensor app, there are three modes of operation; the
“Advanced" mode, which is selected by the lightning bolt icon on the top
row of the App, is used here. To start the process of configuring a
sensor, you first tap the phone to the sensor to read in the existing
sensor settings. Then you adjust those settings as needed. The video
below shows how to use the Elsys Smartphone App to configure sensors.

***Video:*** *Configuring Elsys Sensors with your Smartphone*
{% include video id="654345666" provider="vimeo" %}

Your sensor supplier may have most of the following settings already
configured when you receive the sensor. However, you still may need to
adjust some of the settings described below, including how frequently
the sensor reports its readings and what type of external sensor is
connected. The following screen captures explain the important settings
in the App.

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image11.jpg)
<br>{: #image11}*Screenshot of Important Settings in the Elsys Sensor App*

The first three settings are *Sensor*, *Timebase*, and *External
sensor*. The Sensor setting was read from your actual unit and should be
correct. *Timebase* should be set according to how frequently you want
readings posted to BMON. The setting is measured in seconds, so the 600
value shown here means readings will be posted every 10 minutes.

The sensor used in this example is an ELT Lite sensor, which has
terminals to connect an *External sensor*. The type of *External sensor*
should be selected in the drop-down. See the [Elsys
Manual](https://www.elsys.se/en/documents-firmware/) for a full
description of the options, but here are commonly used selections for
BMON:

  - **Analog 0-10V:** Used for a sensor that puts out a 0 - 10 VDC
    output signal, like a pressure sensor.

  - **Analog 0-3V:** Used for sensors that output a lower range of
    voltage, less than 3 Volts. This is also the correct selection when
    reading a 4 - 20 mA current sensor that is converted to a voltage
    through use of a 150 Ohm resistor across the IN and ⏚ ground
    terminal.

  - **Absolute Pulse Input, pull up:** Used when connecting to a device
    that outputs “dry" (switch closure) pulses, such a pulse output on a
    gas meter or a KYZ pulse output unit on an electric meter.

  - **1-wire Temperature probe:** Used when you connect an external
    temperature probe, either available through Elsys or through vendors
    such as Amazon (see [these
    probes](https://www.amazon.com/gp/product/B00QGN0LKY/)).

  - **Switch:** Used when sensing whether a switch or a relay is closed.

  - **Switch, dual edge trigg:** This is the correct setting to use with
    a switch or the Analysis North Motor Sensor when you want to receive
    a sensor reading both when the switch closes (motor turns on ) and
    when it opens (motor turns off).

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image13.jpg)
<br>{: #image13}*Screenshot of Important Settings in the Elsys Sensor App, Continued*

For these settings, the “period" settings are important. These determine
which sensor readings will be included when a transmission occurs. So,
to receive the External Sensor reading, you must set *External period*
to 1 (it defaults to being set to 0). If you want to receive a reading
of the sensor battery voltage, *Battery period* should be 1, which is
the default. *Send period* also defaults to the correct value of 1,
which says to send a sensor transmission at an interval of 1 times the
*Timebase* value you set on the prior screen.

Another sometimes important setting on this screen is the *External
startup time*. If you are using an External sensor that needs to be
supplied power through the B+ terminal of the ELT sensor, you need to
put a positive value in *External startup time*. The value is expressed
in milliseconds and it tells the ELT sensor how early to apply power to
the External sensor before reading it. Some sensors need time to “warm
up" before being read, so may need a few hundred milliseconds of power
before being read. For the Analysis North Motor Sensor, the sensor must
be *continually* powered, so enter in a large number like 10 million
into the cell (10000000, with no commas).

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image15.jpg)
<br>{: #image15}*Screenshot of Important Settings in the Elsys Sensor App, Continued*

The *Sensor keys* section contains two important identifying numbers
that will be used when registering this sensor on the Things Network.
Nothing needs to be changed, *unless* the App EUI is set to all 0s and
you will try to register the Device on version 2 of the Things Network.
On that version, a 0 App EUI is invalid; for version 3 of the Things
Stack, all 0s is a valid entry. The App EUI should be set to a simple
number, like 0000000000000001, and just needs to match what is set when
you register the device on the Things Network.

If you will use the Multiple Write feature (described later) to
configure a number of different sensors, it is very important *to
collapse* the *Sensor Keys* section so these values will *not* be
included in the Multiple Write operation. They are ID values for this
one sensor and should *not* be written to other sensors.

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image9.jpg)
<br>{: #image9}*Screenshot of Important Settings in the Elsys Sensor App, Continued*

These are the default settings for *OTAA* and *Confirmed message* and
are the correct values for our application. *Frequency plan* and
*Sub-band* must be set to the values shown above; these values set the
Elsys sensor to operate on the correct frequency band.

![]({{ site.baseurl }}/assets/guide/appx-config-lorawan/image16.png)
<br>{: #image16}*Screenshot of Important Settings in the Elsys Sensor App, Continued*

Default values are OK here except for the three *Datarate* settings. The
sensor datarate affects how far the sensor can transmit--the lowest
datarate, DR0, gives the sensor the longest range, but at the expense of
battery life. The settings shown above allow the Things Network to
remotely adjust the datarate of the sensor according to how strong the
received signal is. For the settings shown, the network will be allowed
to adjust the datarate between DR0, DR1, DR2, and DR3.

If you know you have a large distance to cover, it is advisable to lock
down the datarate to the DR0 setting, ensuring the best chance for
sensor reading success. You do this by setting *Datarate default,
Datarate max,* and *Datarate min* to the value of DR0.

Use of the ERS CO2 or VOC sensor is a special case. Because these
sensors produce so many different readings (temperature, light, motion,
humidity, CO2), they are not supported at datarate DR0 in the United
States because of the large data payload size. For these sensors, **the
*Datarate default* and *Datarate min* must be set to DR1 at the
lowest**.

No other settings need to be modified on the Elsys sensor. To write the
new settings to the sensor, first make sure that all the sections where
you changed values are open and not collapsed, then you click the
*WRITE* button at the bottom of the screen and tap the sensor. Further
explanation is available in the appropriate Elsys manual.

The Elsys sensor app has a time-saving feature called *Multiple Write.*
You can turn this feature On from the drop-down menu in the upper left
of the App (three horizontal bars). With this feature On, you can write
the same settings to multiple sensors of the same type (e.g. ELT-Lite or
ERS CO2). It is very important that you do *not* have the *Sensor keys*
section open when you click the *WRITE* button. That section includes
the AppKey, which is unique for each sensor and should not be changed.

## **Notes About External Sensors Connected to the Elsys ELT-Lite or ELT-2**
{: #notes-about-external}

In this section we give some details about how to connect and configure
a variety of external sensors to the Elsys ELT-Lite or ELT-2 sensor.
Consult the Elsys ELT User Manuals
([ELT-Lite](https://elsys.se/public/manuals/Operating%20Manual%20ELT%20Lite.pdf),
[ELT-2](https://elsys.se/public/manuals/Operating%20Manual%20ELT-2.pdf))
for more details.

*Elsys External Sensor Wiring and Configuration Table*
{: #elsys-sensor-table}

<table>
<thead>
<tr class="header">
<th><strong>Sensor Type</strong></th>
<th><strong>Elsys Configuration &amp; Wiring</strong></th>
<th><strong>BMON Configuration</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Temperature Sensor<br />
</strong>This must be a DS18B20-type temperature sensor such as the one sold by Elsys or <a href="https://www.amazon.com/HiLetgo-DS18B20-Temperature-Stainless-Waterproof/dp/B00M1PM55K/">these</a> on Amazon. It can also be a <a href="https://www.digikey.com/en/products/detail/maxim-integrated/DS18B20/956983">bare DS18B20</a> mounted directly to the terminal block in the Elsys. Note that the ELT-2 has a built-in temperature and humidity sensor, in addition to allowing for an external sensor.</td>
<td><p>“External sensor" setting on the Elsys should be “1-wire Temperature probe". Wiring of the external probe is:</p>
<p><em>Sensor Wire : Elsys Terminal</em><br />
Red : B+</p>
<p>Yellow/White : IN<br />
Black : Gnd ⏚<br />
<br />
For the bare DS18B20:<br />
<img src="{{ site.baseurl }}/assets/guide/appx-config-lorawan/image6.png" style="width:0.95035in;height:1.46354in" /></p></td>
<td>The external temperature sensor shows up as a “xxx_extTemperature" (°F units) Sensor ID; the internal sensor in the ELT-2 is “xxx_temperature" and “xxx_humidity" (%RH units) for the relative humidity measurement.</td>
</tr>
<tr class="even">
<td><strong>Pulse Output Sensor</strong><br />
Sensors like electric power transducers, fuel flow meters, water meters.</td>
<td><p>The two wires from the pulse output wire to the IN and Gnd ⏚ terminals on the Elsys.</p>
<p>Some pulse output sensors are pure dry switch closures (e.g. reed switches in water meters and fuel flow meters), so there is no polarity to the wiring. Some pulse output contacts are done electronically and have a + and a - terminal. + goes to IN on the Elsys, and - goes to Gnd ⏚.<br />
The “External Sensor" setting on the Elsys should be “Absolute pulse Input, pull up", unless the pulse output sensor puts out voltage pulses instead of switch closure pulses. In that rarer case the setting should be “Absolute pulse count, no pull up/down".</p></td>
<td>The pulse count shows up in BMON as “xxx_pulse". It will be a cumulative pulse count and is usually converted into a rate-of-use value like gallons/minute or kW, using the special “rate" variable in the BMON Transform. See <a href="https://bmon-documentation.readthedocs.io/en/latest/transform-expressions.html#pulse-counter-transforms">this section</a> of the BMON documentation.</td>
</tr>
<tr class="odd">
<td><strong>Analysis North Motor Sensor</strong><br />
This sensor attaches to a motor or other electric device emitting an AC electric field, and it senses when the device turns On and Off.<br />
<img src="{{ site.baseurl }}/assets/guide/appx-config-lorawan/image7.png" style="width:1.78125in;height:1.18056in" /></td>
<td><p>Wiring to the Elsys is:</p>
<p><em>Sensor Wire : Elsys Terminal</em><br />
Red : B+</p>
<p>White : IN<br />
Black : Gnd ⏚</p>
<p>The “External Sensor" setting should be “Switch, dual edge trig", which causes the Elsys to send a reading when the sensed motor turns On and when it turns Off.</p>
<p>The other critical setting in the “Sample times" section of the configuration is the “External startup time", which should be set to 10 million (10000000, a 1 with seven zeroes and no commas). This setting ensures that battery power will be continuously delivered to the Motor Sensor from the Elsys ELT.</p></td>
<td>Readings appear in BMON with a Sensor ID of “xxx_digital". A good unit selection is “1=On 0=Off" since the reading value is a 1 when the motor is On and a 0 when it is Off.</td>
</tr>
<tr class="even">
<td><strong>Switch Closure<br />
</strong>You may have a Relay wired across a device to sense when the device turns On and Off. Or, you may have a door sensor that closes a switch when the door shuts.</td>
<td><p>For a dry switch closure, there is no polarity and wiring at the Elsys is across the IN and Gnd ⏚ terminals.</p>
<p>The “External Sensor" setting should be “Switch, dual edge trig" if you want to receive a reading for both a closing and an opening of the switch. If you just want a reading when the switch closes, select “Switch (normally open)".</p></td>
<td>Readings in BMON are the same as with the Motor Sensor: “xxx_digital" Sensor ID, and a value of 1 when switch is closed and 0 when it is opened.</td>
</tr>
<tr class="odd">
<td><strong>Sensor with 0 - 10 VDC Output<br />
</strong>Pressure sensors and other types of sensors can be obtained with a 0 - 10 VDC output signal.</td>
<td><p>Here we are assuming that the external sensor has its own power supply. To read the output with the Elsys, you need two wires from the sensor, wired as follows:<br />
<br />
<em>Sensor Terminal : Elsys Terminal<br />
</em>Signal Output (0 - 10 VDC) : IN<br />
Ground : Gnd ⏚</p>
<p>The “External Sensor" setting should be set to “Analog 0-10V".</p></td>
<td><p>Readings in BMON arrive with a Sensor ID of “xxx_analog", measured in Volts. A <a href="https://bmon-documentation.readthedocs.io/en/latest/transform-expressions.html">BMON Transform</a> is required to convert this to engineering units. For example, if a pressure can read a maximum of 25 PSI, which corresponds to 10 V output, the Transform formula to produce readings in PSI would be:</p>
<p>25.0 * val / 10.0</p></td>
</tr>
<tr class="even">
<td><strong>Sensor with 0 - 10 VDC Output, powered by the Elsys<br />
</strong><br />
With the addition of a Voltage Converter board, it is possible to have the Elsys ELT supply power to an external sensor that needs a relatively high power supply voltage. Sensors with a 0 - 10 VDC output generally need a power supply voltage of 14 Volts or more. The Elsys battery itself can only supply about 3.6 Volts.</td>
<td><p>Here is a <a href="https://www.amazon.com/Eiechip-Voltage-Regulator-Converter-Module/dp/B07RNBJK5F/">suitable voltage converter board</a>. The picture below shows it mounted in the Elsys ELT-Lite enclosure:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-config-lorawan/image5.png" style="width:2.6875in;height:2.86111in" /></p>
<p>The screw-adjustable potentiometer on the board must be set to provide the proper voltage to the external sensor, usually from 14 - 24 VDC.</p>
<p>Wiring is as follows:</p>
<p>Sensor + Power Input → VOUT+ on Converter</p>
<p>Sensor Gnd → VOUT- on Converter</p>
<p>Sensor 0 - 10V Output → Elsys IN</p>
<p>VIN+ on Converter → Elsys B+</p>
<p>VIN- on Converter → Elsys Gnd ⏚</p>
<p>For the Elsys configuration, “External Sensor" is set to “Analog 0-10V". The “External startup time" setting determines how early power is applied to the external sensor before it is read by the Elsys. Some sensors need as little as 20 milliseconds to stabilize. Others can require 750 milliseconds or more. Experimentation or an oscilloscope test can determine this value. Longer times are the safe approach but reduce battery life.</p></td>
<td>Same as the prior row, “xxx_analog" is Sensor ID, and a suitable BMON Transform must be entered to convert to engineering units.</td>
</tr>
<tr class="odd">
<td><strong>Sensor with 4 - 20 mA Current Output<br />
</strong>Some sensors have a current output varying from 4 to 20 milliamperes (mA). The Elsys ELT cannot read current directly, but a resistor can be used to convert the current output into a voltage output, which can be read by the Elsys.</td>
<td><p>The proper resistor value is <a href="https://www.digikey.com/en/products/detail/yageo/MFR-25FBF52-150R/12831">150 Ohms, 1% accuracy</a>. Here is a wiring picture:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-config-lorawan/image12.png" style="width:1.59896in;height:1.29528in" /></p>
<p>The red and black wires go to the 4 - 20 mA sensor; the negative return wire from the sensor is cut and the red and black leads are wired as follows:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-config-lorawan/image10.png" style="width:2.05729in;height:1.84997in" /></p>
<p>The “External Sensor" setting should be set to “Analog 0-3V".</p></td>
<td><p>The Sensor ID will be “xxx_analog". A BMON Transform is needed to convert the voltage into engineering units. The Transform should be:<br />
<br />
&lt;full-scale value&gt; *<br />
(val - 0.588) / 2.352</p>
<p>So, for a pressure sensor with a max value of 25 PSI, the Transform would be:<br />
<br />
25.0 * (val - 0.588) / 2.352</p>
<p>(this accounts for the 7,400 Ohm internal resistance of the Elsys ELT).</p></td>
</tr>
<tr class="even">
<td><strong>Maxbotix Distance Sensor</strong><br />
Can be used to measure depth of fuel in a fuel tank.</td>
<td>Can be used with an ELT-2.  Set the "External Sensor" setting to "Maxbotix".</td>
<td><p>Red wire Maxbotix → Elsys B+<br />
Blue Maxbotix → Elsys IN<br />
Black Maxbotix → Elsys Gnd ⏚</p>
<p>Clip the shield and all other colored wires.</p></td>
</tr>
</tbody>
</table>

## **Miscellaneous Sensor Wiring and Configuration**
{: #miscellaneous-sensor-wiring}

The table below gives details on use and configuration of some selected
LoRaWAN sensors, not addressed in the prior Elsys table.

*Use and Configuration of Selected LoRaWAN Sensors Table*
{: #misc-sensor-table}
<table>
<thead>
<tr class="header">
<th><strong>Sensor</strong></th>
<th><strong>Configuration &amp; Wiring</strong></th>
<th><strong>BMON Configuration</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dragino LSN50v2-D23<br />
</strong>This sensor comes with three external temperature probes. An example use is to measure boiler supply, boiler return, and domestic hot water temperatures.</td>
<td><p>Dragino sensors generally need to be configured by AHFC, as configuration is done with a serial-cable connection to a PC. For this particular sensor, no special wiring is required, as it comes pre-wired with the three sensors, color-coded with black, red, and white heat shrink tubing:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-config-lorawan/image4.png" style="width:2.6875in;height:2.69444in" /></p></td>
<td><p>The temperature sensors show up as “xxx_extTemperature1", “xxx_extTemperature2", and “xxx_extTemperature3" (°F units) Sensor ID, where “xxx" is the Device ID (EUI). The color coding on the probes is as follows:</p>
<p><strong>White:</strong> temperature 1</p>
<p><strong>Red:</strong> temperature 2</p>
<p><strong>Black:</strong> temperature 3</p></td>
</tr>
</tbody>
</table>
