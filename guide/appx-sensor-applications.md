---
title: "Appendix: Notes on Various Sensor Applications"
previous:
  title: "Appendix - Configuring LoRaWAN Sensors"
  url: /guide/appx-config-lorawan.html
next:
  title: "Appendix - Configuring Dragino LoRaWAN Gateways"
  url: /guide/appx-dragino-gateway.html
---

This Appendix gives wiring diagrams and configuration settings relevant to a
number of different Sensor Applications, such as sensing the runtime of
a motor and measuring the fill level of fuel tank.

## Notes About External Sensors Connected to the Elsys ELT-Lite or ELT-2
{: #notes-about-external}

In this section we give some details about how to connect and configure
a variety of external sensors to the Elsys ELT-Lite or ELT-2 sensor.
Consult the Elsys ELT User Manuals
([ELT-Lite](https://elsys.se/public/manuals/Operating%20Manual%20ELT%20Lite.pdf){:target="_blank"},
[ELT-2](https://elsys.se/public/manuals/Operating%20Manual%20ELT-2.pdf){:target="_blank"})
for more details.

*Elsys External Sensor Wiring and Configuration*{: .small_text}
{: #elsys-sensor-table}

<table border="1">
<thead style="background-color: #A5D0E0, color: white">
<tr>
<th><strong>Sensor Type</strong></th>
<th><strong>Elsys Configuration &amp; Wiring</strong></th>
<th><strong>BMON Configuration</strong></th>
</tr>
</thead>
<tbody style= "background-color: #99CCFF">
<tr>
<td style="vertical-align:top"><strong>Temperature Sensor<br />
</strong>This must be a DS18B20-type temperature sensor such as the one sold by Elsys or <a href="https://www.amazon.com/HiLetgo-DS18B20-Temperature-Stainless-Waterproof/dp/B00M1PM55K/" target="_blank">these</a> on Amazon. It can also be a <a href="https://www.digikey.com/en/products/detail/maxim-integrated/DS18B20/956983" target="_blank">bare DS18B20</a> mounted directly to the terminal block in the Elsys. Note that the ELT-2 has a built-in temperature and humidity sensor, in addition to allowing for an external sensor.</td>
<td style="vertical-align:top"><p>“External sensor" setting on the Elsys should be “1-wire Temperature probe". Wiring of the external probe is:</p>
<p><em>Sensor Wire : Elsys Terminal</em><br />
Red : B+</p>
<p>Yellow/White : IN<br />
Black : Gnd ⏚<br />
<br />
For the bare DS18B20:<br />
<img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/image6.png" style="width:0.95035in;height:1.46354in" /></p></td>
<td style="vertical-align:top">The external temperature sensor shows up as a “xxx_extTemperature" (°F units) Sensor ID; the internal sensor in the ELT-2 is “xxx_temperature" and “xxx_humidity" (%RH units) for the relative humidity measurement.</td>
</tr>
<tr class="even">
<td style="vertical-align:top"><strong>Pulse Output Sensor</strong><br />
Sensors like electric power transducers, fuel flow meters, water meters.</td>
<td style="vertical-align:top"><p>The two wires from the pulse output wire to the IN and Gnd ⏚ terminals on the Elsys.</p>
<p>Some pulse output sensors are pure dry switch closures (e.g. reed switches in water meters and fuel flow meters), so there is no polarity to the wiring. Some pulse output contacts are done electronically and have a + and a - terminal. + goes to IN on the Elsys, and - goes to Gnd ⏚.<br />
The “External Sensor" setting on the Elsys should be “Absolute pulse Input, pull up", unless the pulse output sensor puts out voltage pulses instead of switch closure pulses. In that rarer case the setting should be “Absolute pulse count, no pull up/down".</p></td>
<td style="vertical-align:top">The pulse count shows up in BMON as “xxx_pulse". It will be a cumulative pulse count and is usually converted into a rate-of-use value like gallons/minute or kW, using the special “rate" variable in the BMON Transform. See <a href="https://bmon-documentation.readthedocs.io/en/latest/transform-expressions.html#pulse-counter-transforms" target="_blank">this section</a> of the BMON documentation.</td>
</tr>
<tr class="odd">
<td style="vertical-align:top"><strong>Analysis North Motor Sensor</strong><br />
This sensor attaches to a motor or other electric device emitting an AC electric field, and it senses when the device turns On and Off.<br />
<img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/image7.png" style="width:1.78125in;height:1.18056in" /></td>
<td style="vertical-align:top"><p>Wiring to the Elsys is:</p>
<p><em>Sensor Wire : Elsys Terminal</em><br />
Red : B+</p>
<p>White : IN<br />
Black : Gnd ⏚</p>
<p>The “External Sensor" setting should be “Switch, dual edge trig", which causes the Elsys to send a reading when the sensed motor turns On and when it turns Off.</p>
<p>The other critical setting in the “Sample times" section of the configuration is the “External startup time", which should be set to 10 million (10000000, a 1 with seven zeroes and no commas). This setting ensures that battery power will be continuously delivered to the Motor Sensor from the Elsys ELT.</p></td>
<td style="vertical-align:top">Readings appear in BMON with a Sensor ID of “xxx_digital". A good unit selection is “1=On 0=Off" since the reading value is a 1 when the motor is On and a 0 when it is Off.</td>
</tr>
<tr class="even">
<td style="vertical-align:top"><strong>Switch Closure<br />
</strong>You may have a Relay wired across a device to sense when the device turns On and Off. Or, you may have a door sensor that closes a switch when the door shuts.</td>
<td style="vertical-align:top"><p>For a dry switch closure, there is no polarity and wiring at the Elsys is across the IN and Gnd ⏚ terminals.</p>
<p>The “External Sensor" setting should be “Switch, dual edge trig" if you want to receive a reading for both a closing and an opening of the switch. If you just want a reading when the switch closes, select “Switch (normally open)".</p></td>
<td style="vertical-align:top">Readings in BMON are the same as with the Motor Sensor: “xxx_digital" Sensor ID, and a value of 1 when switch is closed and 0 when it is opened.</td>
</tr>
<tr class="odd">
<td style="vertical-align:top"><strong>Sensor with 0 - 10 VDC Output<br />
</strong>Pressure sensors and other types of sensors can be obtained with a 0 - 10 VDC output signal.</td>
<td style="vertical-align:top"><p>Here we are assuming that the external sensor has its own power supply. To read the output with the Elsys, you need two wires from the sensor, wired as follows:<br />
<br />
<em>Sensor Terminal : Elsys Terminal<br />
</em>Signal Output (0 - 10 VDC) : IN<br />
Ground : Gnd ⏚</p>
<p>The “External Sensor" setting should be set to “Analog 0-10V".</p></td>
<td style="vertical-align:top"><p>Readings in BMON arrive with a Sensor ID of “xxx_analog", measured in Volts. A <a href="https://bmon-documentation.readthedocs.io/en/latest/transform-expressions.html" target="_blank">BMON Transform</a> is required to convert this to engineering units. For example, if a pressure can read a maximum of 25 PSI, which corresponds to 10 V output, the Transform formula to produce readings in PSI would be:</p>
<p>25.0 * val / 10.0</p></td>
</tr>
<tr class="even">
<td style="vertical-align:top"><strong>Sensor with 0 - 10 VDC Output, powered by the Elsys<br />
</strong><br />
With the addition of a Voltage Converter board, it is possible to have the Elsys ELT supply power to an external sensor that needs a relatively high power supply voltage. Sensors with a 0 - 10 VDC output generally need a power supply voltage of 14 Volts or more. The Elsys battery itself can only supply about 3.6 Volts.</td>
<td style="vertical-align:top"><p>Here is a <a href="https://www.amazon.com/Eiechip-Voltage-Regulator-Converter-Module/dp/B07RNBJK5F/" target="_blank">suitable voltage converter board</a>. The picture below shows it mounted in the Elsys ELT-Lite enclosure:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/image5.png" style="width:2.6875in;height:2.86111in" /></p>
<p>The screw-adjustable potentiometer on the board must be set to provide the proper voltage to the external sensor, usually from 14 - 24 VDC.</p>
<p>Wiring is as follows:</p>
<p>Sensor + Power Input → VOUT+ on Converter</p>
<p>Sensor Gnd → VOUT- on Converter</p>
<p>Sensor 0 - 10V Output → Elsys IN</p>
<p>VIN+ on Converter → Elsys B+</p>
<p>VIN- on Converter → Elsys Gnd ⏚</p>
<p>For the Elsys configuration, “External Sensor" is set to “Analog 0-10V". The “External startup time" setting determines how early power is applied to the external sensor before it is read by the Elsys. Some sensors need as little as 20 milliseconds to stabilize. Others can require 750 milliseconds or more. Experimentation or an oscilloscope test can determine this value. Longer times are the safe approach but reduce battery life.</p></td>
<td style="vertical-align:top">Same as the prior row, “xxx_analog" is Sensor ID, and a suitable BMON Transform must be entered to convert to engineering units.</td>
</tr>
<tr class="odd">
<td style="vertical-align:top"><strong>Sensor with 4 - 20 mA Current Output<br />
</strong>Some sensors have a current output varying from 4 to 20 milliamperes (mA). The Elsys ELT cannot read current directly, but a resistor can be used to convert the current output into a voltage output, which can be read by the Elsys.</td>
<td style="vertical-align:top"><p>The proper resistor value is <a href="https://www.digikey.com/en/products/detail/yageo/MFR-25FBF52-150R/12831" target="_blank">150 Ohms, 1% accuracy</a>. Here is a wiring picture:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/image12.png" style="width:1.59896in;height:1.29528in" /></p>
<p>The red and black wires go to the 4 - 20 mA sensor; the negative return wire from the sensor is cut and the red and black leads are wired as follows:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/image10.png" style="width:2.05729in;height:1.84997in" /></p>
<p>The “External Sensor" setting should be set to “Analog 0-3V".</p></td>
<td style="vertical-align:top"><p>The Sensor ID will be “xxx_analog". A BMON Transform is needed to convert the voltage into engineering units. The Transform should be:<br />
<br />
&lt;full-scale value&gt; *<br />
(val - 0.588) / 2.352</p>
<p>So, for a pressure sensor with a max value of 25 PSI, the Transform would be:<br />
<br />
25.0 * (val - 0.588) / 2.352</p>
<p>(this accounts for the 7,400 Ohm internal resistance of the Elsys ELT).</p></td>
</tr>
<tr class="even">
<td style="vertical-align:top"><strong>Maxbotix Distance Sensor</strong><br />
Can be used to measure depth of fuel in a fuel or water tank.</td>
<td style="vertical-align:top"><p>Can be used with an ELT-2.  Set the "External Sensor" setting to "Maxbotix".</p>
<p>Red wire Maxbotix → Elsys B+<br />
Blue Maxbotix → Elsys IN<br />
Black Maxbotix → Elsys Gnd ⏚</p>
<p>Clip the shield and all other colored wires.</p></td>
<td style="vertical-align:top"></td>
</tr>
<tr class="odd">
<td style="vertical-align:top">
<p><strong>Fuel Tank Level Sensor</strong><br />
Allows sensing the level in a fuel tank using a float-based sensor such
as <a href="https://www.amazon.com/dp/B08DLMSJQF/ref=twister_B0C5SXG464" target="_blank">this one.</a></p>

<img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/fuel-float.jpg" style="width:1.2in;height:1.86in" />

</td>
<td style="vertical-align:top">
ELT wiring involves a 150 Ohm 1% accuracy resistor connected from the B+ terminal to the
IN terminal.  The fuel sensor wires connect to the IN and Gnd ⏚ terminals as 
shown here with an ELT-Lite:

<img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/fuel-float-wiring.png" style="width:2.2in;height:1.71in" />

<p>Important settings for the ELT sensor are:<br />
<strong>External sensor:</strong>  Analog 0-3V<br />
<strong>External period:</strong>  1<br />
<strong>External startup time:</strong> 20
</p>
</td>
<td style="vertical-align:top">
<p>Most fuel float sensors, including the one linked to in the
left column, have a varying resistance output from 33 Ohms (full) to 
240 Ohms (empty). With this sensor, the following BMON Transform will
produce a value of 0 for Empty and 100 for Full:</p>

<p>100 - 65.7 * (val - 0.631)</p>

<p>This value will be affected by battery voltage and temperature. If
higher accuracy is needed, A
more complicated BMON setup is possible. Contact the BMON development
team for more information.</p>
</td>
</tr>
</tbody>
</table>

## Miscellaneous Sensor Wiring and Configuration
{: #miscellaneous-sensor-wiring}

The table below gives details on use and configuration of some selected
LoRaWAN sensors, not addressed in the prior Elsys table.

*Use and Configuration of Selected LoRaWAN Sensors*{: .small_text}
{: #misc-sensor-table}
<table border="1">
<thead>
<tr class="header">
<th><strong>Sensor</strong></th>
<th><strong>Configuration &amp; Wiring</strong></th>
<th><strong>BMON Configuration</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="vertical-align:top"><strong>Dragino LSN50v2-D23<br />
</strong>This sensor comes with three external temperature probes. An example use is to measure boiler supply, boiler return, and domestic hot water temperatures.</td>
<td style="vertical-align:top"><p>Dragino sensors generally need to be configured by AHFC, as configuration is done with a serial-cable connection to a PC. For this particular sensor, no special wiring is required, as it comes pre-wired with the three sensors, color-coded with black, red, and white heat shrink tubing:</p>
<p><img src="{{ site.baseurl }}/assets/guide/appx-sensor-applications/image4.png" style="width:2.6875in;height:2.69444in" /></p></td>
<td style="vertical-align:top"><p>The temperature sensors show up as “xxx_extTemperature1", “xxx_extTemperature2", and “xxx_extTemperature3" (°F units) Sensor ID, where “xxx" is the Device ID (EUI). The color coding on the probes is as follows:</p>
<p><strong>White:</strong> temperature 1</p>
<p><strong>Red:</strong> temperature 2</p>
<p><strong>Black:</strong> temperature 3</p></td>
</tr>
</tbody>
</table>
