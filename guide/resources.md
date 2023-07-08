---
title: BMON Resources
previous:
  title: "How to Use BMON Sensor Data"
  url: /guide/use-data.html
next:
  title: "Appendix - Configuring LoRaWAN Sensors"
  url: /guide/appx-config-lorawan.html
---

## User Guide Contents
{: #manual-contents}

### Introduction to BMON
- [Acknowledgements](intro#acknowledgements)
- [Introduction](intro#introduction)
  - **Figure:** [Alaskan BMON User Collecting Fuel Use Data](intro#image2)
  - **Figure:** [Basic Architecture of the BMON System](intro#image1)
  - **Video:** [Introduction to BMON](intro#video-introduction-bmon)

### How to Choose/Set Up Sensors
- [Introduction](sensors#introduction)
  - **Figure:** [Basic Architecture of the BMON System](sensors#image1)
  - **Table:** [LoRaWAN Sensor Comparison](sensors#image2)
  - **Figure:** [Types of Electrical Outputs Found in Sensors](sensors#image3)
- [Temperature](sensors#temperature)
  - **Figure:** [Potential Energy Savings of Measuring Building Temperature](sensors#image4)
  - **Figure:** [Collecting Indoor Temperature Data Using an Existing Building Control System](sensors#image5)
  - **Figure:** [Ecobee Thermostat](sensors#image6)
  - **Table:** [Examples of Elsys and Dragino LoRaWAN Indoor Temperature Sensors](sensors#table1)
  - **Table:** [Wireless Outdoor Temperature Sensor Options](sensors#table2)
  - **Figure:** [Installation Guidelines for Temperature Sensors](sensors#image11)
- [Light Levels](sensors#light-levels)
  - **Figure:** [Potential Energy Savings of Measuring Light Levels](sensors#image12)
  - **Table:** [Recommended Wireless Light Level Sensors](sensors#table3)
- [Indoor Carbon Dioxide (CO<sub>2</sub>) Levels](sensors#indoor-carbon-dioxide)
  - **Figure:** [Potential Energy Savings of Measuring Indoor Carbon Dioxide Levels](sensors#image15)
  - **Figure:** [Elsys ERS CO<sub>2</sub> LoRaWAN Sensor*](sensors#image13)
  - **Figure:** [What to Consider When Installing CO<sub>2</sub> Sensors](sensors#image16)
- [Boiler and Domestic Hot Water Temperature](sensors#boiler-domestic-hot)
  - **Figure:** [Potential Energy Savings of Measuring Boiler and Domestic Hot Water Temperatures](sensors#image17)
  - **Figure:** [Wireless Temperature Sensor Options With External Temperature Probes](sensors#table4)
  - **Figure:** [A Temperature Probe Correctly Installed on a Pipe](sensors#image19)
- [Building Electric Power](sensors#building-electric-power)
  - **Figure:** [Potential Energy Savings of Measuring Electricity](sensors#image20)
  - **Video:** [Wiring an External Sensor to Elsys ELT LoRaWAN Sensor](sensors#video-wiring-external-sensor)
- [Building Fuel Use Data](sensors#building-fuel-use)
  - **Figure:** [Potential Energy Savings in Measuring Fuel Use](sensors#image21)
  - **Figure:** [Natural Gas Meter With a Monnit Wireless Pulse Counter](sensors#image22)
  - **Figure:** [Typical LoRaWAN Pulse Counter, Elsys ELT-Lite LoRaWAN Sensor](sensors#image9)
  - **Figure:** [An Elster 4p Fuel Flow Meter Installation](sensors#image23)
  - **Figure:** [Boiler Burner Fuel Solenoid Showing Placement of a Dry Contact Sensor](sensors#image24)
  - **Figure:** [A Motor Sensor Used to Sense Whether a Motor is On or Off](sensors#image25)
- [Typical Sensor Wiring Examples](sensors#typical-sensor-wiring)
  - **Figure:** [Wiring a Voltage-Output Sensor or a Switch Closure Sensor to an Elsys ELT-Lite Sensor](sensors#image26)
  - **Figure:** [Correct Wiring of a 4-20mA Output on an ELT-Lite Sensor With Resistor](sensors#image27)
  - **Figure:** [Correct Wiring of an External Sensor Powered From the ELT Sensor Battery](sensors#image28)
  - **Figure:** [Internal Temperature Sensor Wired Inside the ELT-Lite Sensor Enclosure](sensors#image29)
- [Connecting Wireless Sensors to the Internet with Gateways](sensors#gateways-wireless-sensors)
  - **Figure:** [Gateways for Wireless Sensors](sensors#image30)
  - **Table:** [Pros and Cons of Select LoRaWAN Gateways](sensors#image31)
  - **Figure:** [Solutions for Potential Sensor Connection Issues](sensors#image32)
  - **Figure:** [Simple External Antenna That Can Be Mounted on a Wall Or Roof Fascia](sensors#image33)
  - **Figure:** [A Properly Installed Exterior Antenna for a LoRaWAN Gateway](sensors#image34)

### How to Set Up Your BMON System
  - **Figure:** [What you Need to Set Up a Basic BMON System](setup-bmon#image1)
- [The BMON User Interface vs the System Administrator Interface](setup-bmon#bmon-user-interface)
  - **Figure:** [Ways to Interact with the BMON Software](setup-bmon#image2)
- [LoRaWAN Wireless Sensor Configuration](setup-bmon#lorawan-wireless-sensor)
- [Overview of the System Administrator Interface](setup-bmon#overview-system-administrator)
  - **Figure:** [A View of the BMON System Administrator Interface](setup-bmon#image3)
  - **Figure:** [How to Access the Administrator Interface](setup-bmon#image4)
  - **Video:** [System Administration Interface](setup-bmon#video-system-administration-interface)
- [Adding a Building](setup-bmon#adding-building)
  - **Figure:** [Essential Information Needed to Add a Building in BMON](setup-bmon#image5)
  - **Video:** [Basic Information for Adding a New Building into BMON](setup-bmon#video-basic-information-adding)
  - **Figure:** [Examples of Building Details That Can Be Entered in BMON](setup-bmon#image6)
  - **Video:** [Advanced Building Information; Occupied Schedule & Additional Description](setup-bmon#video-advanced-building-information)
- [Adding a Sensor and Assigning it to a Building](setup-bmon#adding-sensor-assigning)
  - **Figure:** [Information Needed to Add a Sensor to the BMON Software](setup-bmon#image7)
  - **Video:** [How to use Unassigned Sensors when Setting Up New Sensors](setup-bmon#video-how-use-unassigned)
  - **Video:** [Basic Steps for Adding a New Sensor](setup-bmon#video-basic-steps-adding)
- [Editing Information for an Existing Sensor](setup-bmon#editing-information-existing)
  - **Video:** [Editing Sensor Information](setup-bmon#video-editing-sensor-information)
- [Adding Weather Data from the Internet](setup-bmon#adding-weather-data)
  - **Video:** [Getting National Weather Service Temperature and Wind Data](setup-bmon#video-getting-national-weather)
- [Assigning Sensors used by Energy Reports](setup-bmon#assigning-sensors-used)
  - **Video:** [Identifying & Entering Key Sensors for Energy Reports](setup-bmon#video-identifying-entering-key)
- [Creating a Dashboard](setup-bmon#c-reating-dashboard)
  - **Figure:** [The Dashboard for the AHFC Headquarters Building Illustrates Some Options of What Can Be Displayed](setup-bmon#image8)
  - **Figure:** [Guidelines for a Useful Dashboard](setup-bmon#image9)
  - **Video:** [Choosing Sensors to Display on the Building Dashboard](setup-bmon#video-choosing-sensors-display)
  - **Video:** [Adding Custom Reports and Links to the Dashboard](setup-bmon#video-adding-custom-reports)
- [Using and Creating Alerts](setup-bmon#using-creating-alerts)
  - **Figure:** [Examples of What to Use Alerts for in BMON](setup-bmon#image10)
  - **Figure:** [How to Create an Alert](setup-bmon#image11)
  - **Video:** [Creating Alerts and assigning Recipients](setup-bmon#video-creating-alerts-assigning)
- [Editing and Cleaning Sensor Data](setup-bmon#editing-cleaning-sensor)
  - **Video:** [Sensor Data Utilities](setup-bmon#video-sensor-data-utilities)

### How to Use BMON Sensor Data
- [Creating a Monitoring Plan](use-data#creating-monitoring-plan)
  - **Figure:** [Key Steps to an Effective Monitoring Strategy](use-data#image1)
- [Analyzing Data](use-data#analyzing-data)
  - **Figure:** [Drop Down Menu in the Graph/Report Tab That Allows Selection of Available Data Visualization Tools](use-data#image3)
  - **Figure:** [Listing of the Most Common BMON Graphs and Reports](use-data#image4)
  - **Figure:** [The top part of a Current Sensor Values report](use-data#image5)
  - **Figure:** [Example of a Plot Sensor Values over Time Graph Used to Measure Temperature of Selected Building Areas Over a Period of Months](use-data#image6)
  - **Video:** [Plot Sensor Values over Time Graph](use-data#video-plot-sensor-values)
  - **Figure:** [Example of an X vs Y Scatter Plot Used to Measure the Correlation Between Fuel Use and Outdoor Temperature](use-data#image7)
  - **Video:** [Sensor X vs Y Scatter Plot](use-data#video-sensor-x-vs)
  - **Figure:** [Example of an Hourly Profile Plot Used to Measure Differences in a Building’s Electric Use on Occupied and Unoccupied Days](use-data#image8)
  - **Video:** [Hourly Profile Plots](use-data#video-hourly-profile-plots)
  - **Video:** [Overview of Other Available Reports/Graphs](use-data#video-overview-other-available)
  - **Video:** [Custom Reports](use-data#video-custom-reports)
  - **Figure:** [Indoor Temp Report in the Energy Reports Section of BMON](use-data#image9)
  - **Figure:** [A Closer View of the Indoor Temp Report](use-data#image10)
  - **Figure:** [Indoor Temperature Report Displaying a Potential Problem in a Building’s Heating Pattern](use-data#image11)
  - **Figure:** [Temperature Energy Report Feature That Alerts Users of Indoor Temperatures Outside the Normal Range](use-data#image12)
  - **Figure:** [Lighting Energy Report Showing Several Light Sensor Patterns Through a Week](use-data#image13)
  - **Figure:** [Lighting Energy Report Showing a Single Light Sensor](use-data#image14)
  - **Figure:** ["Heat Map Hourly Profile" for One Light Sensor at AHFC Headquarters](use-data#image15)
  - **Figure:** [Examples of Energy Reports That Focus on Displaying and Analyzing Electric and Fuel Data](use-data#image16)
  - **Figure:** [Ways to Compare Fuel Use and Account for Outdoor Temperature](use-data#image17)
  - **Figure:** [What to Look for When Diagnosing High Energy Use in an Unoccupied Building](use-data#image18)
  - **Figure:** [Sensors Over Time Plot with Supply, Return, and Outdoor Temperature Can Show if an Outdoor Reset is Working](use-data#image19)
  - **Figure:** [X vs Y Scatter Plot Showing a Boiler with an Outdoor Reset Curve Applied to the Supply Temperature Controls](use-data#image20)
  - **Figure:** [X vs Y Scatter Plot for a Heating System Without an Outdoor Reset Curve](use-data#image21)
  - **Figure:** [Why Measuring Domestic Hot Water Supply Temperature is Useful](use-data#image22)
  - **Figure:** [Example of an IAQ Energy Report](use-data#image23)

### Appendix: Configuring LoRaWAN Sensors for BMON
- [Introduction](appx-config-lorawan#introduction)
- [Registering Sensors on the Things Network](appx-config-lorawan#register-sensors-things)
  - **Figure:** [Screenshot of Activation, Version, and Network Settings](appx-config-lorawan#image3)
  - **Figure:** [Screenshot of Device ID](appx-config-lorawan#image1)
  - **Figure:** [Screenshot of Frequency Plan](appx-config-lorawan#image2)
  - **Figure:** [Screenshot of Root Keys](appx-config-lorawan#image8)
  - **Figure:** [Import End Devices link on the End Devices Page](appx-config-lorawan#image14)
- [Configuring an Elsys Sensor](appx-config-lorawan#configuring-elsys-sensor)
  - **Video:** [Configuring Elsys Sensors with your Smartphone](appx-config-lorawan#video-config-elsys-smartphone)
  - **Figure:** [Screenshot of Sensor, Timebase, and External Sensor Settings in the Elsys Sensor App](appx-config-lorawan#image11)
  - **Figure:** [Screenshot of Period Settings in the Elsys Sensor App](appx-config-lorawan#image13)
  - **Figure:** [Screenshot of Sensor Keys Settings in the Elsys Sensor App](appx-config-lorawan#image15)
  - **Figure:** [Screenshot of LoRaWAN Configuration Settings in the Elsys Sensor App](appx-config-lorawan#image9)
  - **Figure:** [Screenshot of Extended LoRaWAN Configuration Settings in the Elsys Sensor App](appx-config-lorawan#image16)

### Appendix: Notes on Various Sensor Applications
- [Notes About External Sensors Connected to the Elsys ELT-Lite or ELT-2](appx-sensor-applications#notes-about-external)
  - **Table:** [Elsys External Sensor Wiring and Configuration](appx-sensor-applications#elsys-sensor-table)
- [Miscellaneous Sensor Wiring and Configuration](appx-sensor-applications#miscellaneous-sensor-wiring)
  - **Table:** [Use and Configuration of Selected LoRaWAN Sensors](appx-sensor-applications#misc-sensor-table)

### Appendix: Configuring Dragino LoRaWAN Gateways
  - **Figure:** [System Diagram for Dragino LoRaWAN Gateway](appx-dragino-gateway#image6)
- [Configuring a Gateway for the Things Network](appx-dragino-gateway#configure-gateway-things)
  - **Figure:** [Screenshot of LoRa Radio Settings](appx-dragino-gateway#image1)
  - **Figure:** [Screenshot of Gateway ID](appx-dragino-gateway#image5)
  - **Figure:** [Screenshot of Primary LoRaWAN Server](appx-dragino-gateway#image4)
  - **Figure:** [Screenshot of Frequency Plan](appx-dragino-gateway#image3)
  - **Figure:** [System Diagram for Dragino LoRaWAN Gateway with Green Checkmarks](appx-dragino-gateway#image2)

## Other Resources
{: #other-resources}

Other web resources helpful for developing a monitoring plan and
implementing BMON:

- **[BMON User Forum](https://forum.bmon.org/){:target="_blank"}:** A forum for all users to
post questions, answers and tips on hardware, software or anything else
related to BMON and energy use in buildings.

- **[Analysis North](https://analysisnorth.com/){:target="_blank"}:** The primary software developer, contains links to other related projects such as the [heat pump calculator](https://akheatsmart.org/resources/calculator/){:target="_blank"} and [AkWarm energy modeling software](https://www.ahfc.us/efficiency/pro-builders/akwarm-energy-rating-software){:target="_blank"}.

- **[BMON documentation](https://bmon-documentation.readthedocs.io/en/latest/){:target="_blank"}:** Detailed software documentation for more complex situations and network
administrators.

- **[AHFC SEMP Manual](https://www.ahfc.us/application/files/9414/5193/2592/SEMP-Master_Manual_FINAL_AHFC_12.31.15.pdf){:target="_blank"}:** A manual to introduce public facility owners and managers to tools and
resources that can be used to complete successful energy efficiency
retrofit projects.

- **[LoRa Alliance](https://lora-alliance.org/?gclid=CjwKCAiA9vOABhBfEiwATCi7GLt4J4GiNHHCqJsDrNvlfHuLOuvDYP5YykZtjRnmmy6ssL1ra7BzpxoCu3YQAvD_BwE){:target="_blank"}:** the group representing the communication technology LoRa (Long-Range wireless communication).

- **[The Things Network](https://www.thethingsnetwork.org/){:target="_blank"}:** The web service that enables LoRaWAN devices to communicate with BMON.

- **[Monnit](https://www.monnit.com/){:target="_blank"}:** A wireless sensor manufacturer utilizing a proprietary technology.

- **[Dragino](https://www.dragino.com/){:target="_blank"}:** A wireless sensor manufacturer utilizing LoRaWAN technology.

- **[Elsys](https://www.elsys.se/en/){:target="_blank"}:** wireless sensor manufacturer utilizing LoRaWAN technology.
