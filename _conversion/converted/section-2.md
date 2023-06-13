# Section 2: *How to Choose/Set Up Sensors*
{: #section-2-how}

# Selection and Set-up of Sensors
{: #selection-set-up}

## Introduction
{: #introduction}

This section identifies a number of important energy-related data
collection activities within a building. After explaining the general
importance of collecting each type of data, the manual describes the
best sensors and data collection methods for gathering data for storage
and analysis in the Building Monitoring (BMON) System, often referred to
as simply BMON. With BMON, data is often collected using sensors in the
building, but can also be collected directly from the Internet (e.g.,
weather data), from the local electric utility, or directly from the
utility meter on the building.

In a number of cases, battery-powered, wireless sensors are a good tool
for data collection. Using wireless sensors to collect data involves two
types of hardware: 1) the actual sensors to sense and wirelessly
transmit temperature, light, or some other measured parameter; and 2) a
“wireless sensor gateway” that receives the data from sensors and
forwards the data to a server on the Internet.

### Sensor Platforms
{: #sensor-platforms}

BMON currently supports two different wireless sensor platforms: LoRaWAN
and Monnit.

\#details markdown=”1”

<summary>**LoRaWAN Wireless Sensors**</summary>

[LoRaWAN](https://www.thethingsnetwork.org/docs/lorawan/): LoRaWAN
wireless sensors and the associated internet gateways are available from
numerous suppliers, although parts of the technology are proprietary.
AHFC is currently using the world-wide [Things
Network](https://www.thethingsnetwork.org/) to collect readings from
LoRaWAN sensors and send those readings to BMON. Any gateway on this
network is publicly available for use by your sensors, without charge.
You are able to add your own gateways to the network. AHFC can help you
determine whether gateways exist in your area that may provide coverage
for a new project.

\[Basic Architecture of the BMON System\]

![](media/image1.png)
<br>{: #image1}*Caption*

</details>

<details markdown=”1”>

<summary>**Monnit Wireless Sensors**</summary>

[Monnit](https://www.monnit.com/): This wireless sensor platform has
been used with BMON since its beginning. The platform is proprietary,
and does involve annual subscription fees to support the Internet
servers that initially store the data before forwarding to BMON. This
platform offers dozens of different sensor types, and these have been
used in many different facilities connected to BMON.

![](media/image1.png)
<br>{: #image1}*Caption*

*\[*[*Basic architecture of the
BMON*](https://docs.google.com/document/d/1fwnPoB7YwxwVNMFqyS7TBZ5SwejImogETXJxpg7i7Ng/edit#figur_diagram)
[this figure is in here twice (see previous page). Delete this
one*system*](https://docs.google.com/document/d/1fwnPoB7YwxwVNMFqyS7TBZ5SwejImogETXJxpg7i7Ng/edit#figur_diagram)*\]*

</details>

The rest of the BMON User Manual will focus on using LoRaWAN wireless
sensors, rather than Monnit sensors. More information on using Monnit
sensors can be found
[online](https://bmon-documentation.readthedocs.io/en/latest/adding-buildings-and-sensors.html#adding-sensors).

The primary LoRaWAN sensor manufacturers,
[Elsys](https://www.elsys.se/en/) and
[Dragino](https://dragino.com/products/lora-lorawan-end-node.html), are
covered in more detail in (link sections). There are dozens of
additional manufacturers that make compatible LoRaWAN sensors, but these
two manufacturers cover building monitoring needs well. A comparison of
these two brands is below.

\[LoRaWAN Sensor Comparison\]

![](media/image2.png)
<br>{: #image2}*Caption*

### Sensor Types
{: #sensor-types}

These two sensor platforms are able to read numerous types of sensors
and post their data to BMON. In general, sensors have four types of
electrical outputs, detailed below.

\[Types of Electrical Outputs Found in
Sensors\]![](media/image3.png)*
<br>{: #image3}*Caption*
\*Additional information on this special configuration is*
*[available](https://bmon-documentation.readthedocs.io/en/latest/transform-expressions.html#pulse-counter-transforms).*

Temperature

The temperature at various locations in a building is a valuable
quantity to measure. From this temperature data, you can learn whether
spaces are being heated or cooled evenly and within a range needed for
occupant comfort and efficiently manage heating and cooling needs over
time. Heating system failures can potentially freeze pipes and other
valuable contents of a building. BMON alerts can notify maintenance
staff of heating failures before damage occurs.

<details markdown=”1”>

<summary>**Potential BMON-Guided Energy Savings of Measuring
Temperature**</summary>

**\[**Potential Energy Savings of Measuring Building
Temperature\]![](media/image4.png)A building’s energy
<br>{: #image4}*Caption*
consumption is almost always affected by the outdoor temperature.
Heating and cooling energy use relate to heat loss or gain through the
building shell, which is proportional to the temperature difference
between the inside and outside of the building. When analyzing the
energy use data for a building, it is very important to have accurate
outside temperature data to make valid comparisons.

</details>

### Indoor Temperature Collection Methods
{: #indoor-temperature-collection}

Wireless temperature sensors are an excellent and common method to
collect indoor temperatures. Depending on your system you may
alternatively work with temperature data directly from your building
control system or from Ecobee thermostats.

<details markdown=”1”>

<summary>**Retrieval from the Building Control System**</summary>

\[Collect Indoor Temperature Data Using an Existing Building Control
System\]

![](media/image5.png)
<br>{: #image5}*Caption*

To determine whether this is a viable technique for temperature
collection within your building, contact [Tyler
Boyes](mailto:tboyes@ahfc.us) at AHFC.

</details>

![](media/image6.png)<details markdown=”1”>
<br>{: #image6}*Caption*

<summary>**Retrieval from Ecobee Thermostats**</summary>

BMON knows how to retrieve data from the Ecobee line of smart,
Internet-connected thermostats. If your building utilizes this brand of
thermostat, the Ecobee platform can be configured to forward
temperature, humidity, temperature setpoint and heating system runtime
data to the BMON platform.

<details markdown=”1”>

<summary>**Gathering Ecobee Data**</summary>

Details on configuring BMON to gather Ecobee data are available
[online.](https://bmon-documentation.readthedocs.io/en/latest/periodic-scripts.html#collect-data-from-ecobee-thermostats)
This requires using the “System Administrator” portion of BMON, a topic
that is addressed in this section of the manual.

</details>

</details>

Battery-powered wireless temperature sensors are easy to install, low
cost, and have reasonable battery life (over two years, and generally
last more than four years).

<details markdown=”1”>

<summary>**Wireless Sensors Tested to Work with BMON**</summary>

\[Examples of Elsys and Dragino LoRaWAN Indoor Temperature Sensors\]

<table>
<tbody>
<tr class="odd">
<td><p><a href="https://www.elsys.se/en/ers/">Elsys ERS LoRaWAN Sensor</a>:<br />
All of the Elsys ERS sensors provide a temperature reading, ranging from the full-featured ERS CO2 sensor down to the ERS Lite sensor</p>
<p><img src="media/image7.png" style="width:3.02083in;height:2.91667in" /></p></td>
<td><p><a href="http://www.dragino.com/products/lora-lorawan-end-node/item/151-lht65.html">Dragino LHT65 Temperature/Humidity LoRaWAN Sensor</a></p>
<p><img src="media/image8.png" style="width:3.02083in;height:3.58333in" /></p></td>
</tr>
</tbody>
</table>

The two LoRaWAN sensors listed above also measure humidity of the indoor
space. Although humidity is less important than temperature, it does
provide information about the comfort of the space. Thirty to 50% is
considered a comfortable range of indoor humidity; higher levels may
indicate poor ventilation and can potentially drive damaging levels of
water vapor into the shell of the building.

</details>

### Outdoor Temperature Collection Methods
{: #outdoor-temperature-collection}

There are a number of good methods for collecting outdoor temperature
data for a building. The National Weather Service has numerous weather
stations in Alaska, and the Weather Service makes this data available on
the [Internet for free](https://www.weather.gov/aawu/stnlist). BMON has
the capability to retrieve this data directly from the Internet and this
is the preferred source of outdoor temperature data, since a sensor does
not need to be purchased or maintained, and the quality of the data is
generally good. For additional information on the use of Mesonet API and
wireless temperature sensors, click below.

**National Weather Service (NWS):** Information is available
[online](https://bmon-documentation.readthedocs.io/en/latest/calculated-fields.html#acquiring-weather-data-from-the-internet)
on how to integrate NWS data into your BMON system using the System
Administrator functions of BMON. You can also acquire wind speed data
from the NWS using this method.

Detail on the System Administrator functions of BMON are in this section
of the [manual](#_gtapnkhesz37).

<details markdown=”1”>

<summary>**Mesonet API Weather Data**</summary>

Synoptic Developers provides a service called the [Mesonet
API](https://developers.synopticdata.com/mesonet/), which provides
weather data from a wide variety of weather station networks, including
the National Weather Service. Limited use of the Mesonet API is free,
but extensive use requires enrolling in a paid subscription. Only use
this service if you don’t have a nearby NWS station that can be acquired
for free from NWS. How to acquire data from the Mesonet API is
[available
online](https://bmon-documentation.readthedocs.io/en/latest/calculated-fields.html#acquiring-weather-data-from-the-internet).

</details>

<details markdown=”1”>

<summary>**Wireless Temperature Sensor Weather Data**</summary>

If an existing weather station is not available, using a wireless
temperature sensor placed outdoors is a reasonable method for collecting
outdoor temperature data. Here are some choices for wireless temperature
sensors:

\[Wireless Outdoor Temperature Sensor Options\]

<table>
<tbody>
<tr class="odd">
<td><p><a href="https://www.elsys.se/en/lora-elt-lite/">Elsys ELT-Lite LoRaWAN Sensor</a>: This weatherproof unit can accept many types of sensors, including a temperature sensor. Elsys sells an external temperature probe that can be used to sense outdoor temperature, or a <a href="https://www.digikey.com/en/products/detail/maxim-integrated/DS18B20/956983">bare DS18B20</a> temperature sensor can be attached inside the ELT-Lite unit.</p>
<p><img src="media/image9.png" style="width:2.94236in;height:2.53889in" /></p></td>
<td><p><a href="http://www.dragino.com/products/lora-lorawan-end-node/item/151-lht65.html">Dragino LHT65 Temperature/Humidity LoRaWAN Sensor</a>: This sensor is reasonably weatherproof, although some overhead protection would be desirable.</p>
<p><img src="media/image10.png" style="width:3.02083in;height:1.95833in" /></p></td>
</tr>
</tbody>
</table>

When installing an outdoor temperature sensor, the most common mistake
is to install it where sunshine can affect the reading. In Alaska, the
summer sun wraps around to the north side of buildings, so simply
installing a sensor on the north side is not enough to avoid distorted
readings at some times of the day. If you cannot find a
completely-shaded spot, consider using a solar radiation shield such as
[this
one](https://www.amazon.com/Crosse-Technology-925-1418-Sensor-Protection/dp/B00VSXENM4/)
in addition to placing the sensor in the most shaded location. Also,
mount the sensor at least 3 feet away from building walls, as the sun on
those walls and heat loss from the building can distort the temperature
readings.

</details>

### Installing Temperature Sensors
{: #installing-temperature-sensors}

If you are installing your own temperature sensor, as opposed to
gathering data from the building control system sensors or from Ecobee
thermostats, you should adhere to guidelines similar to installing a
thermostat:

**\[**Installation Guidelines for Temperature Sensors\]

![](media/image11.png)
<br>{: #image11}*Caption*

## Light Levels
{: #light-levels}

Measuring light levels in a building is primarily important for
determining when lights are on and when they are off. Despite
substantial improvements in efficiency, lighting is still one of the
largest electricity uses in commercial buildings.

<details markdown=”1”>

<summary>**Potential BMON-Guided Energy Savings in Measuring Light
Levels**</summary>

\[Potential Energy Savings of Measuring Light Levels\]

![](media/image12.png)
<br>{: #image12}*Caption*

</details>

### Light Level Sensors
{: #light-level-sensors}

Wireless battery-powered light level sensors are the best method for
measuring light in various building spaces. The two types of wireless
light sensors on the market are 'analog' and 'digital'; 'digital'
sensors are very limited and not recommended. For recommended sensors,
click below.

<details markdown=”1”>

<summary>**Analog Light Level Sensors**</summary>

“Analog” sensors measure the amount of light, or light levels, usually
in units of lux. Typical office lighting levels are [500
lux](https://www.waveformlighting.com/home-residential/what-is-the-difference-between-lux-and-lumens)
or more. This is the preferred type of sensor.

</details>

<details markdown=”1”>

<summary>**Digital Light Level Sensors**</summary>

Some manufacturers sell a “digital” light sensor that only reports
whether lights are on or off. While determining the on/off status of a
light is the primary purpose of reading light levels, this type of
sensor is difficult to calibrate correctly so that it accurately knows
when lights are on. Daylight can trigger the sensor to report that
lights are on even though they are not. This sensor does not provide
information on how much daylight a space is getting. For these reasons,
“digital” sensors are not recommended.

</details>

Here are some recommended wireless light level sensors:

\[Recommended Wireless Light Level Sensors\]

<table>
<tbody>
<tr class="odd">
<td><a href="https://www.elsys.se/en/ers/">Elsys ERS LoRaWAN Sensor</a>: for the ERS Lite and the ERS CO2 Lite come with a light sensor.<br />
<img src="media/image13.png" style="width:2.61944in;height:2.6375in" /></td>
<td><p><a href="http://www.dragino.com/products/lora-lorawan-end-node/item/151-lht65.html">Dragino LHT65-E5 Temperature/Humidity/Light LoRaWAN Sensor</a>: One version of the LHT65 sensor comes with an external light level sensor, which plugs into the main sensor unit via a 20” cable (shown here).</p>
<p><img src="media/image14.png" style="width:3.10417in;height:2.55556in" /></p></td>
</tr>
</tbody>
</table>

### Installing Light Level Sensors
{: #installing-light-level}

Guidelines for installing light sensors depend on the purpose for which
you are monitoring light levels. To determine whether lights are being
left on at times when they shouldn’t be, install the sensor so that it
is nearby and has a good view of a light fixture. Preferably, install it
so that daylight from nearby windows does not affect the sensor much.
High up on a wall is often a good location. For details on installation
of daylight controls, click below. <details markdown=”1”>

<summary>**How Do I Know if I Should Use Daylight
Controls?**</summary>

To determine whether daylight controls could be useful, install the
sensor in a location representative of a work surface in the space, such
as on a desk. At this location, both artificial light and daylight will
be measured in roughly the proportion they contribute to useful
lighting. The influence of daylight will make it somewhat harder to
determine when artificial lights are on, but it still will be possible.

</details>

## Indoor Carbon Dioxide (CO<sub>2</sub>) Levels
{: #indoor-carbon-dioxide}

CO2 indicates whether the ventilation system for a building or space is
supplying adequate outside air for the health and wellbeing of the
occupants. Ventilation helps dilute contaminants in indoor air and
replaces oxygen that is removed by breathing. Ventilation can use a lot
of energy both in operating the fans that move air through a building,
and through the heated air that is exhausted to the outside. So while
ventilation is important, it can drive up both the electric usage and
the heating fuel usage of a facility if it is not measured.

<details markdown=”1”>

<summary>**Potential BMON-Guided Energy Savings in Measuring
CO<sub>2</sub> Levels**</summary>

**\[**Potential Energy Savings of Measuring Indoor Carbon Dioxide
Levels\]![](media/image15.png)
<br>{: #image15}*Caption*

</details>

###
{: #}

###
{: #}

### Methods of Collecting CO<sub>2</sub> data
{: #methods-collecting-co}

CO<sub>2</sub> can be measured either from a building automation system
or with wireless sensors. Use of wireless sensors is described in detail
below.

<details markdown=”1”>

<summary>**Measuring CO<sub>2</sub> from a Building Automation
System**</summary>

CO<sub>2</sub> can be measured from a building automation system if one
is available. This will usually be a measurement of CO<sub>2</sub> in
the return air plenum of a building HVAC system so the measurement
represents a mix of the air throughout the building. Some modern
automation systems have CO<sub>2</sub> sensors in spaces, which allows
you to see how ventilation air is distributed through a building and/or
whether the ventilation airflow is keeping up with occupancy in specific
spaces. Accessing CO<sub>2</sub> measurements from a control system can
be done using [this
process](https://bmon-documentation.readthedocs.io/en/latest/setting-up-sensors-to-post-to-bmon.html#general-method-for-gathering-data-from-building-automation-systems).
A potential downside of gathering CO<sub>2</sub> measurements from a
Building Automation Systems (BAS) is that the sensors may drift out of
calibration. Also, if only one measurement exists, the correct reading
will be hard to determine.

<details markdown=”1”>

<summary>**Calibrating Your CO<sub>2</sub> Sensor**</summary>

CO<sub>2</sub> sensors require calibration, following the appropriate
set-up procedure is important. Refer to page 13, Section 7.4 of the
[Elsys Operating
Manual](https://elsys.se/public/manuals/Operating%20Manual%20ERS2%20series_v10.pdf).

</details>

</details>

Wireless sensors are currently limited to a few manufacturers, but the
Elsys ERS CO<sub>2</sub> sensor has been shown to work reliably.

<details markdown=”1”>

<summary>***Elsys Sensor Calibration***</summary>

The Elsys sensor, when set up properly, auto-calibrates every 8 days so
the measurements should be accurate for years and not suffer from the
drift that others can experience.

[Elsys ERS CO2 LoRaWAN Sensor](https://www.elsys.se/en/ers/)

\[Elsys ERS CO2 LoRaWAN Sensor\]

![](media/image13.png)
<br>{: #image13}*Caption*

The ERS CO<sub>2</sub> Lite and ERS CO<sub>2</sub> come with a
CO<sub>2</sub> sensor.

</details>

### Installing CO<sub>2</sub> Sensors
{: #installing-co-sub}

CO<sub>2</sub> levels will vary dramatically based on how a space is
used and how much ventilation air is supplied to that space. Sensor
placement will depend on where you are most concerned about having a
lack of fresh air in an occupied indoor space. CO<sub>2</sub> is
measured in parts per million (ppm). This means small changes in the
amount of CO<sub>2</sub> in a sample of air can have large impacts on
the ppm of CO<sub>2</sub> recorded.

\[What to Consider When Installing CO<sub>2</sub> Sensors\]

![](media/image16.png)
<br>{: #image16}*Caption*

## Boiler and Domestic Hot Water Temperature
{: #boiler-domestic-hot}

Collecting the temperature of boiler supply and domestic hot water (DHW)
supply is relatively easy to do and provides useful information to save
energy and detect equipment failures. Significant decreases in either of
those temperatures that last for more than a half hour or so probably
indicate a failure in the system. BMON alerts can be set up to detect
those failures. Also, large decreases in DHW temperature that occur
during periods of heavy usage possibly indicate that the system is sized
too small.

<details markdown=”1”>

<summary>**Potential BMON-Guided Energy Savings in Measuring Water
Temperature**</summary>

\[Potential Energy Savings of Measuring Boiler and Domestic Hot Water
Temperatures\]

![](media/image17.png)
<br>{: #image17}*Caption*

</details>

### Methods for Collecting Boiler and DHW Temperatures
{: #methods-collecting-boiler}

Wireless temperature sensors are an effective and always-available
method of measuring boiler and domestic hot water temperatures. Click
below for alternative methods of collecting these temperatures.

<details markdown=”1”>

<summary>**Collecting Water Temperature Data from your Building
Control System**</summary>

Boiler and DHW temperatures can sometimes be collected directly from the
building control system, through [this
process](https://bmon-documentation.readthedocs.io/en/latest/setting-up-sensors-to-post-to-bmon.html#general-method-for-gathering-data-from-building-automation-systems)
or other ways of communicating with the control system. If heating
equipment has a MODBUS interface, a small computer such as a [Raspberry
Pi](https://mini-monitor-documentation.readthedocs.io/en/latest/index.html)
can be programmed to retrieve the readings and report them to BMON.

</details>

The wireless sensor used for this purpose must have an external
temperature probe. Here are three possibilities:

\[Wireless Temperature Sensor Options With External Temperature Probes\]

<table>
<thead>
<tr class="header">
<th><p><a href="https://www.elsys.se/en/lora-elt-lite/">Elsys ELT-Lite LoRaWAN Sensor</a><br />
<img src="media/image9.png" style="width:3.10417in;height:2.34375in" /></p>
<p>This weatherproof unit can accept many types of sensors, including a temperature sensor probe.</p></th>
<th><p><a href="http://www.dragino.com/products/lora-lorawan-end-node/item/151-lht65.html">Dragino LHT65 Temperature/Humidity LoRaWAN Sensor</a></p>
<p><img src="media/image10.png" style="width:3.10417in;height:2.01389in" /></p>
<p>The standard configuration of the LHT65 wireless sensor includes an external temperature probe, as shown in the picture above.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://www.tindie.com/products/edwin/lsn50v2-d23-lorawan-waterproof-outdoor-tempera/">Dragino LSN50v2-D23 Triple Temperature Sensor</a></p>
<p><img src="media/image18.png" style="width:2.84514in;height:4.38542in" /></p>
<p>This weatherproof unit includes three temperature probes, with about 3 feet of cable on each. Very economically priced (~$60).</p></td>
<td></td>
</tr>
</tbody>
</table>

### Installing Boiler and Domestic Hot Water Sensors
{: #installing-boiler-domestic}

When installing a temperature probe on a pipe, it is important to make
good thermal contact for higher accuracy (within 5 degrees Fahrenheit).
Thermal heat sink paste, such as this [Super Lube
product](https://www.amazon.com/Super-Lube-98003-Silicone-White/dp/B0044NI2M2/),
works well. The image below shows a well done installation of a
temperature probe on a pipe:

\[A Temperature Probe Correctly Installed on a Pipe\]

![](media/image19.png)
<br>{: #image19}*Caption*

*A temperature probe installed on a pipe with heat sink compound to
promote good thermal contact and accurate temperature readings.*

After attaching the probe as shown above, make sure to reinstall the
pipe insulation on top of the probe. Make sure to route wires to avoid
pulling or snagging when a technician services the boiler or hot water
system.

## Building Electric Power
{: #building-electric-power}

Electricity is always a substantial source of energy usage for a
building and should be monitored if at all possible. Electricity usage
data can be used to find energy saving opportunities in a number of
different ways. For more detail, click below.

<details markdown=”1”>

<summary>**Potential BMON-Guided Energy Savings in Measuring
Electricity Use**</summary>

**\[**Potential Energy Savings of Measuring Electricity\]

![](media/image20.png)
<br>{: #image20}*Caption*

</details>

### Methods for Collecting Building Electric Data
{: #methods-collecting-building}

The easiest way to collect 15-minute electricity use data is to acquire
it directly from the electric utility, if that is possible. Many
electric utilities are using “smart meters”, which have the ability to
collect and transmit 15-minute data back to the utility. To view two
alternative methods of collecting electrical use data, click below.

<details markdown=”1”>

<summary>**Accessing Building Electric Data from
Utilities**</summary>

Not all utilities utilize this feature or make it available to
consumers. But, some do and have made the data available to BMON without
charge. These include:

  - [Chugach Electric Association](https://www.chugachelectric.com/)

  - [Matanuska Electric Association](https://www.mea.coop/)

  - [Golden Valley Electric Association](https://www.gvea.com/)

We are currently working with other Alaska electric utilities to capture
this type of data, including Alaska Village Electric Cooperative.
Hopefully, this data will be available soon. If this option is not
available from your utility, please contact [Tyler
Boyes](mailto:tboyes@ahfc.us) for assistance with this task.

For other options on how to acquire this data, click below.

</details>

<details markdown=”1”>

<summary>**Electrical Utility Installs KYZ Pulse Output
Unit**</summary>

Another option is to have your electric utility install a KYZ pulse
output unit on your electric meter. That unit will output electrical
pulses proportional to how much electricity is being used. A wireless
pulse counter, such as the Elsys ELT-Lite or the Dragino LHT65
(previously pictured) can be used to count the pulses and transmit them
to BMON.

</details>

<details markdown=”1”>

<summary>**Electrician Installed Electrical Power
Transducer**</summary>

If the above options are not available, another option is to hire an
electrician to install an electrical power transducer on the main power
service entering the building. This type of sensor is available from
companies such as:

  - [Continental Control Systems](https://ctlsys.com/), the Watt-Node
    product line.

  - [EKM Metering](https://www.ekmmetering.com/).

These sensors generally can output electrical pulses, which can be
counted by the Elsys ELT-Lite or Dragino LHT65 sensors, previously
shown.

</details>

### Installing Electrical Sensors
{: #installing-electrical-sensors}

If you are not able to collect electrical data from your utility and
must use sensors, you will be using pulse output data.

The video below shows how to wire a sensor with a pulse output to an
Elsys ELT-Lite LoRaWAN sensor. While the video focuses on a pulse output
sensor, its main focus is to give general hints on wiring external
sensors to Elsys ELT sensors.

**VIDEO:** [**Wiring External Sensor to Elsys ELT LoRaWAN
Sensor**](https://vimeo.com/566390563)

A later section of the manual ([NOTE: link will need to be updated with
final one onlineAdding a Sensor and Assigning it to a
Building](https://docs.google.com/document/d/1nrUgCqQxBiAhx5_4Gt4D7KoNxHRiORMZON_rd539IkE/edit#heading=h.sjg4w4cro0yw))
shows how to add and configure sensors in BMON. For more detail on how
the data from these sensors must be configured to be useful, click
below.

<details markdown=”1”>

<summary>**Configuring Pulse Outputs**</summary>

Sensors that have a pulse output, such as electrical power sensors, need
to be configured with a special transform function in order to convert
the sensor output into meaningful values that can be graphed and
analyzed. How to set up this special configuration is [available
online](https://bmon-documentation.readthedocs.io/en/latest/transform-expressions.html#pulse-counter-transforms).

</details>

## Building Fuel Use Data
{: #building-fuel-use}

Heating fuel is a major source of energy use in most every Alaska
building. Therefore, closely monitoring fuel use is very important for
identifying and measuring energy savings opportunities. The benefits of
measuring fuel are very similar to the benefits of measuring electricity
use, described in this section. For details on the benefits of measuring
fuel, click below.

<details markdown=”1”>

<summary>**Potential BMON-Guided Energy Savings in Measuring Fuel
Use**</summary>

**\[**Potential Energy Savings in Measuring Fuel Use\]

![](media/image21.png)
<br>{: #image21}*Caption*

</details>

### Methods for Collecting Building Fuel Use Data
{: #methods-collecting-building}

The method for measuring fuel use will depend on the fuel type. Here we
focus on natural gas and fuel oil and also offer a data collection
method for buildings using a district heat system (i.e., waste
electrical generator heat or a central oil or biomass burner) .

**Natural Gas**

A couple of different methods are available to measure natural gas use
with good time resolution (1 hour or better). For details on these
methods, click below.

<details markdown=”1”>

<summary>**Meter Transmitter Reading**</summary>

Most gas meters have a transmitter that sends out the reading on the
meter every 30 seconds or so; these transmissions are received by
utility meter-reading personnel who typically drive by on a monthly
basis. But, these transmissions can also be received by a small computer
connected to a “software-defined radio”. The [AHFC Mini-Monitor
project](https://mini-monitor-documentation.readthedocs.io/en/latest/hardware.html#part-cv4-sdr-radio-for-utility-meter-reading)
uses an inexpensive Raspberry Pi computer coupled with a RTL-SDR
receiver such as [this
one](https://www.amazon.com/NooElec-NESDR-Smart-Bundle-R820T2-Based/dp/B01GDN1T4S/)
to perform this task; the required hardware costs about $120. This
set-up can send the received readings to BMON.

</details>

<details markdown=”1”>

<summary>**Pulse Output Unit**</summary>

In situations where the gas meter does not have a compatible transmitter
or is too far away to be received, the natural gas utility can usually
install a pulse-output unit on the natural gas meter. Then, a LoRaWAN
wireless pulse counter can be used to read and transmit those pulse
counts to BMON.

\[Natural Gas Meter With a Monnit Wireless Pulse Counter\]

![](media/image22.png)
<br>{: #image22}*Caption*

*A natural gas meter with a pulse output attachment. Also shown is a
flexible conduit leading to a wireless pulse counter that records and
transmits the reading to BMON.*

A Monnit wireless pulse counter is shown above. Below is a typical
LoRaWAN pulse counter, with a weatherproof enclosure, that can also
perform this task:

\[Typical LoRaWAN Pulse Counter, [Elsys ELT-Lite LoRaWAN
Sensor](https://www.elsys.se/en/lora-elt-lite/)\]
![](media/image9.png)
<br>{: #image9}*Caption*

This weatherproof unit can be configured as a Pulse Counter to read
pulses from any meter (electric, fuel, water, BTU) or device equipped
with a pulse-output unit.

</details>

**Fuel Oil**

The type of system for measuring fuel oil use depends heavily on the
type of heating systems used in the building. Flow meter and tank level
methods will work with any system, however local weather conditions such
as ice fog can cause problems with the measurements from tank level
sensors. Alternative monitoring methods are available for systems with a
constant rate of firing and for Toyostoves.

**Flow Meter and Tank Level Methods for Measuring Fuel Usage**

<details markdown=”1”>

<summary>**Flow Meter in the Fuel Line**</summary>

A fuel flow meter installed in the fuel line is a possibility, although
some meters do not measure accurately at the low flows that occur with a
Toyostove. Another disadvantage of a flow meter is that the meter
introduces another point in the fuel line that can become clogged. Fuel
flow meters can be purchased with a pulse output option and then
connected to a wireless pulse counter, such as the Elsys ELT-Lite or the
Dragino LTH65.

\[An Elster 4p Fuel Flow Meter Installation\]

![](media/image23.png)
<br>{: #image23}*Caption*

*The flow meter is the translucent enclosure in the upper right corner
of the picture.*

</details>

<details markdown=”1”>

<summary>**Fuel Level in the Tank**</summary>

Another approach to measuring the fuel use from a tank is to sense the
level of fuel in the tank and determine the amount of fuel used from the
change in the oil level in the tank. Ultrasonic distance measuring
devices or pressure measurement devices can be used to determine tank
level. These devices can be battery-powered and transmit their readings
via a LoRaWAN sensor. A [current
project](https://analysisnorth.com/fuel-mon/oil-fuel-mon.html) at Alaska
Housing Finance Corporation is underway to determine the viability of
these approaches.

</details>

**Fixed Firing Rate Systems**

Some fuel oil heating systems utilize a combustion burner that runs at a
constant rate of firing / fuel use. For these systems, if you know the
firing rate of the burner, you can measure how long the burner is on in
order to then determine how much fuel was used.

**Firing rate**

If you can determine the size of the fuel oil nozzle used in the burner
(e.g. 1.10 gallon per hour, GPH), you have a reasonably accurate
estimate of the fuel consumption rate of the heating appliance when it
is on. You can refine your estimate of fuel rate by also measuring the
oil pressure supplied to the nozzle. The rated flow rate is achieved
when the oil pressure at the nozzle is 100 PSI. If the pressure is
different than 100 PSI, the flow will be different and can be determined
from a chart [like this
one](https://www.hvacrschool.com/oil_nozzles/#:~:text=Nozzle%20flow%20is%20rated%20in,the%20flue%20as%20unused%20energy.).

While all of these sensors are handy tools, they will never compare to
empirical, hands-on testing. Be sure to verify your readings by dipping
the tank and cross referencing with a tank chart. Once you have an
estimate of the fuel consumption rate of the heating system when it is
on, you then need to determine how to measure the on and off cycles of
the boiler.

**Fuel Solenoid Sensing**

One approach is to connect an electrical relay across the fuel solenoid
or the oil burner (sensing the fuel solenoid is more accurate than
sensing the burner, since burners often operate for a short period of
time both before and after burning fuel). Whenever power is applied to
the fuel solenoid (or to the burner), the relay will close; the relay
contacts can then be connected to a wireless switch sensor, such as the
Elsys ELT-Lite or the Dragino LHT65. These sensors will transmit a
reading whenever the burner turns on and off. The image below is one
example of a relay connected to an oil burner; a wireless switch (Dry
Contact) sensor is shown wired to the relay contacts.

\[Boiler Burner Fuel Solenoid Showing Placement of a Dry Contact
Sensor\]

![](media/image24.png)
<br>{: #image24}*Caption*

**Motor Sensor**

Another approach to monitoring the On/Off cycles of a fuel solenoid or
burner is to use a Motor Sensor, such as one made by Analysis North.
This device attaches with velcro to a motor or any AC electrical device
that energizes a substantial coil of wire. The device senses when the
coil is energized and connects to a wireless switch sensor to transmit
that reading. The image below shows a motor sensor attached to small
circulating pump:

\[A Motor Sensor Used to Sense Whether a Motor is On or Off\]

![](media/image25.png)
<br>{: #image25}*Caption*

<details markdown=”1”>

<summary>**Toyostove Fuel Measurement Device**</summary>

**Toyostove Fuel Measurement Device**

A Toyostove heating system has multiple different fuel consumption rates
(Low, Medium, High), so simply measuring when it is running will not
allow you to make an accurate estimate of fuel consumption. The Alaska
Center for Energy and Power has developed a technique for measuring
Toyostove fuel consumption by measuring the fuel pump on the Toyostove
heater. [Contact them](https://acep.uaf.edu/about/contact.aspx) to learn
more about their PuMA Fuel Meter.

</details>

**District Heat Systems (i.e, biomass, oil, or electric generator waste
heat)**

Some buildings are heated by a District Heat System, perhaps delivering
waste heat recovered from an electrical generator or delivering heat
produced by a central oil or biomass boiler. You can install a BTU meter
on the heat delivery system to the building to measure the heat load of
the building. For details on additional methods, click below.

<details markdown=”1”>

<summary>**Additional Methods of Measuring Heat Load**</summary>

The ONICON System 10 and System 40 meters have been used if cutting into
the hydronic piping is a possibility. Otherwise, an ultrasonic BTU meter
should be used to measure heat delivery. Note that none of these methods
measures the fuel burned but can give an accurate measurement of the
heating demand of an individual building. LoRaWAN pulse counters or
RS485 sensors can be used to report this heat load to BMON.

</details>

## Typical Sensor Wiring Examples
{: #typical-sensor-wiring}

This section will show some typical wiring configurations for the
sensors discussed above. There is a more [detailed table of wiring and
configuration](https://docs.google.com/document/d/1PFpajCRwzp9jceMrVn5ofAVRoKa2LfpkqDQGIWKlfTo/edit#heading=h.90rhtdafs2zm)
information for Elsys ELT sensors in the Appendix of this document.

Click below for more detail on each configuration.

<details markdown=”1”>

<summary>**Voltage Output or Switch Closure Sensor
Wiring**</summary>

This image shows how to wire a voltage-output sensor or a switch closure
sensor to an Elsys ELT-Lite. The negative or ground lead from the
voltage-output sensor goes to the Ground terminal on the ELT-Lite
(marked ⏚). The positive or signal lead from the voltage-output sensor
goes to the IN terminal on the ELT-Lite. When connecting a
switch-closure or pulse-output sensor, the wiring is the same. Some
switch and pulse sensors have no positive/negative polarity to their
connections, but other sensors do have polarity: positive to IN and
negative to ⏚ ground.

\[Wiring a Voltage-Output Sensor or a Switch Closure Sensor to an Elsys
ELT-Lite Sensor\]

![](media/image26.png)
<br>{: #image26}*Caption*

</details>

<details markdown=”1”>

<summary>**Converting a 4-20 mA Current Output Sensor to Voltage with
a Resistor**</summary>

If you are reading a sensor with a 4-20 mA current output, you can
convert the current into voltage by using a resistor, as shown in the
image below. The resistor wires across the IN and ⏚ground terminals of
the ELT-Lite. An appropriate size resistor is [150 ohms with 1%
accuracy](https://www.digikey.com/en/products/detail/yageo/MFR-25FBF52-150R/12831).
Then the ELT-Lite can be configured to use the 0 - 3 Volt Analog Voltage
scale. The following formula will convert the voltage read by the
ELT-Lite into the engineering value read by the sensor:

Engineering value = full\_scale\_reading \* (voltage - 0.588) / 2.352

(technical note: for those that know Ohm’s law, the above formula is
derived from an effective resistance of 147 Ohms, since the ELT-Lite has
an internal resistance of 7,400 Ohms in parallel with the 150 Ohm
resistor value).

BMON can do this conversion by entering a formula into the Transform
field when setting up a sensor. As an example, assume the sensor is a 0
- 10 PSI pressure sensor. The appropriate Transform formula to use in
BMON would be:

10.0 \* (val - 0.588) / 2.352

since the “val” variable holds the voltage read by the sensor.

\[Correct Wiring of a 4-20mA Output on an ELT-Lite Sensor With
Resistor\]

![](media/image27.png)
<br>{: #image27}*Caption*

</details>

<details markdown=”1”>

<summary>**Wiring for a Sensor that Needs to Receive Power from an
Elys ELT-Lite Battery** </summary>

This image shows the appropriate wiring for a sensor that needs to
receive power from the Elsys ELT-Lite battery. An example of such a
sensor is the Analysis North Motor Sensor. The Red lead going to the
Motor Sensor needs to be connected to the battery terminal of the
ELT-Lite, which is marked B+. The White lead from the motor sensor is
the signal output lead, which acts like an electronic switch, and is
connected to the IN terminal on the ELT-Lite. Finally, the Black lead
from the motor sensor goes to the ground ⏚ terminal on the ELT-Lite.
Similar wiring is used for any external sensor that needs to receive
power from the ELT-Lite.

\[Correct Wiring of an External Sensor Powered From the ELT Sensor
Battery\]![](media/image28.png)
<br>{: #image28}*Caption*

For external sensors that need to receive power from the ELT-Lite,
configuration of the ELT-Lite is important. In the “Sample Times”
section of the ELT-Lite configuration parameters, there is a setting
labeled “External startup time”. This setting determines how early power
is applied to the external sensor before the sensor is read. The setting
is expressed in milliseconds. For some sensors such as pressure sensors,
power can be turned off except for a short period of time prior to
reading the sensor. “External startup times” as short as 20 milliseconds
can work. But some sensors, such as the Analysis North Motor Sensor,
require that power be applied continually to the sensor. The “External
startup time” settings should be set to 10 million in those cases
(10000000), to ensure that power is continually applied to the external
sensor.

</details>

<details markdown=”1”>

<summary>**Wiring a Temperature Sensor Inside the ELT-Lite**
</summary>

This image shows a small temperature sensor wired inside the ELT-Lite.
Electronically, this is the same sensor that is sold as the Elsys
Temperature probe but is less expensive, less obtrusive, and can be used
if air temperature needs to be measured. (The “1-wire Temperature Probe”
is the correct External Sensor setting on the ELT-Lite). The model
number for the sensor is DS18B20, and sensors are available on
[Digikey](https://www.digikey.com/en/products/detail/maxim-integrated/DS18B20/956983),
[Amazon](https://www.amazon.com/Eiechip-DS18B20-Digital-Thermometer-Temperature/dp/B07MR71WVS/)
or other sources. When wiring the sensor, the flat face of the sensor
should be facing up as shown in the photo below.

\[Internal Temperature Sensor Wired Inside the ELT-Lite Sensor
Enclosure\]

![](media/image29.png)
<br>{: #image29}*Caption*

</details>

## Gateways for Wireless Sensors
{: #gateways-wireless-sensors}

**All wireless sensors need a gateway that serves as a central receiving
device to route sensor readings to the internet.** One advantage to
LoRaWAN sensors is that the gateway and sensor do not need to be from
the same manufacturer or installed on the same account. Gateways are
automatically shared across all users of the Things LoRaWAN network.
**This means that sensors can transmit data through other gateways if
they are within range of the sensors.**

\[Gateways for Wireless Sensors\]

![](media/image30.png)
<br>{: #image30}*Caption*

*Important considerations for LoRaWAN gateways are:*

  - *Gateways usually require 120V wall power rather than a battery.*

  - *Means of Connecting to the Internet: Ethernet, WiFi, Cellular.*

      - *An Ethernet connection tends to be the most reliable but limits
        where you can place the gateway.*

      - *A gateway can connect to the internet via an existing Wi-Fi
        network (if available).*

      - *A direct cellular connection can be built into a gateway, or
        can be accomplished through a separate Cellular Router that
        provides an Ethernet or Wi-Fi connection to the wireless sensor
        gateway.*

      - *A cellular connection will require a cellular data plan with a
        suitable amount of data (a minimum of 100 MB / month).*

  - *Gateways can be mounted indoors or outdoors (not Monnit, LoRaWAN
    only). An indoor gateway is protected from the weather and is less
    expensive than a gateway that can be mounted outdoors. However, an
    outdoor gateway has its antenna mounted outside as well, which
    significantly improves the coverage area of the gateway. **Extra
    coverage can be helpful if you are trying to serve multiple
    buildings with one gateway**. Another solution for good coverage is
    to use an indoor gateway but connect that gateway to an outdoor
    antenna through use of a coax cable from the antenna jack on the
    gateway to the antenna outdoors (seen in the photo below). This
    solution also keeps the gateway electronics protected from the
    elements.*

Here are some good choices for LoRaWAN gateways:

\[Pros and Cons of Select LoRaWAN Gateways\]

![](media/image31.png) *\*[Setup
<br>{: #image31}*Caption*
Instructions](https://www.thethingsindustries.com/docs/gateways/thethingsindoorgateway/)
for Things Indoor Gateway*

<details markdown=”1”>

<summary>**Dragino Gateway Setup** </summary>

Setup instructions for the Dragino gateways are found in their User
Manuals; some helpful hints are also provided in Section 5 of this
Manual\[Link to: Section 5 Configuring LoRaWAN Sensors for BMON,
Configuring Dragino LoRaWAN Gateways\]. For setup purposes, the gateway
will act like a Wi-Fi access point, which you can connect your laptop
to, and then browse with your browser to the Setup page for the gateway.
When you go to the Wi-Fi setup page, make sure you keep the Wi-Fi access
point enabled so you can come back later, if need be, to change
settings.

</details>

### More Notes on LoRaWAN Signal Coverage and Antennas
{: #more-notes-lorawan}

Gateways and Sensors communicate via radio signals, and both gateways
and sensors use antennas to radiate and receive signals. If a sensor is
having a difficult time reaching a gateway, you can either move the
sensor or improve the antenna of the sensor. Another option is to
improve the location or antenna of the gateway (or both).

\[Solutions for Potential Sensor Connection Issues\]

![](media/image32.png)
<br>{: #image32}*Caption*

This image shows a simple external antenna that can be used with a
sensor or gateway to improve signal strength between buildings.

\[Simple External Antenna That Can Be Mounted on a Wall Or Roof Fascia\]

![](media/image33.png)
<br>{: #image33}*Caption*

This photo shows a more capable antenna installation with the antenna
mounted above the roof of the building. This antenna is being used with
a gateway to cover a large portion of downtown Nome, Alaska. **Note the
drip loops on the coaxial cable (to prevent water leakage into the
building) and the placement of the antenna above the peak of the roof.**

\[A Properly Installed Exterior Antenna for a LoRaWAN Gateway\]

# ![](media/image34.jpeg)
{: #media-image34-jpeg}

<details markdown=”1”>

<summary>**Sourcing External Antennas and Mounts**</summary>

  - Antennas for LoRaWAN in the US must be tuned for the 900 - 930 MHz
    frequency band. They are generally marked “915 MHz” or “900 MHz”.

  - The antennas shown so far are:
    Taoglas WM.95.A.305111, available
    [Here](https://www.digikey.com/en/products/detail/taoglas-limited/WM-95-A-305111/11196960).
    Dragino Outdoor 915 MHz Antenna, available
    [Here](https://www.robotshop.com/en/dragino-lora-lorawan-glass-fiber-outdoor-antenna-915-mhz.html).
    Similar models available on Amazon, such as [this
    one](https://www.amazon.com/Gateway-Antenna-N-Female-SMA-Male-Extension/dp/B09J7Z7VV3/).

  - A J-pipe antenna mount shown in [*Figure 12*](#fig_gateway_antenna)
    is [available
    here](https://www.amazon.com/Skywalker-Signature-38in-Pipe-Antenna/dp/B01MSFGZIW/).

</details>

<details markdown=”1”>

<summary>**Antenna Connections Notes and Sourcing**</summary>

  - Signal loss occurs on the coax cable between the Antenna and the
    LoRaWAN gateway or sensor. A good choice for low-loss coax is Times
    Microwave LMR-240 for distances up to 60 feet. For distances less
    than 30 feet, Times Microwave LMR-200 is acceptable.

  - The end of the coax that connects to the gateway or sensor generally
    needs to have an SMA Male connector. The coax connector on the
    antenna end needs to mate with the connector on your antenna. You
    generally can buy a coax customized with the connectors you need and
    the length you want. Online, [WiFi
    Expert](https://www.ebay.com/str/wifiexpert) can provide custom coax
    cables.

  - [These
    clips](https://www.amazon.com/Single-Black-Mounting-Strain-Relief/dp/B077QH8R9G/)
    can secure the coax to the building.

</details>

On a final note, often installing multiple inexpensive, indoor gateways
in different buildings can be as effective as installing one outdoor
gateway or a gateway with a high external antenna. Multiple gateways
also provide redundancy if a gateway or the Internet serving the
gateways fails.
