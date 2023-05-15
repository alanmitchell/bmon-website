---
layout: single
title: "BMON and Building Monitoring"
toc: true
---
## Website Under Construction !!

*The content here is only for testing purposes!*

## Acknowledgements

This material is based upon work supported by the U.S. Department of
Energy\'s Office of Energy Efficiency and Renewable Energy (EERE) under
the Advanced Building Construction with Energy Efficient Technologies &
Practices (ABC) award, award number DE-EE0009088.

<details markdown="1">
<summary>Click to see Contract Information</summary>

This manual was created under a contract with Analysis North over the
Alaska state fiscal years 2021 and 2022. Many thanks to Ben Loeffler
(Loeffler Engineering) for editing this manual.

This is the text used to create this section:

    <details markdown="1">
    <summary>Click to see Contract Information</summary>
    This manual was created under a contract with Analysis North
    over the Alaska state fiscal years 2021 and 2022. Many thanks
    to Ben Loeffler (Loeffler Engineering) for editing this manual.
    </details>

Below is a test of nesting another collapsing section under this one.

<details markdown="1">
<summary>A Nested Collapsing Section</summary>

This section is nested beneath the first collapsing section.
</details>

</details>

## Introduction

BMON is a free, open-source software platform designed by Alaska Housing
Finance Corporation (AHFC) and built by Alaska energy experts to track
and analyze energy use and operations in buildings of all sizes.
Analysis North has been the primary software developer of the BMON
application through a contract funded by the DOE State Energy Program.

While the software is available to the public at no cost, data
collection and storage costs must be weighed against potential energy
cost savings such that an acceptable payback on monitoring can be
achieved. The BMON software and data collection system has many uses and
some technical aspects but the basic functions can be used by anyone.
One of the biggest advantages of BMON over other systems is that it can
receive input from multiple data sources, including automation systems,
on-site sensors, local weather stations, utility companies, and other
databases.

This tool allows users to see overall building energy usage at any scale
and time period alongside specific equipment data. By comparing multiple
data sources, patterns emerge that can identify the causes of high
energy consumption and unexpected costs. Benefits can also include
improved operations due to advanced warning of equipment failures and/or
runtime data. This is particularly useful for facilities where the
manager may not be on site. The goal of this manual is to explain how
BMON can be used to identify high energy consumption and safely reduce
wasted energy through operational modifications. BMON can be used to
support existing energy efficiency goals and to create awareness of
energy use for general energy and cost savings.

Examples of BMON uses:

-   Measuring heating fuel use of a building to properly size a replacement boiler

-   Tracking lighting with occupied schedule to make sure lighting is not on unnecessarily during unoccupied times

-   Monitoring indoor temperatures in comparison to occupied schedule to properly time warm-up sequence

Here are examples of a couple different BMON sites:

Alaska Housing Finance Corporation:
[https://bms.ahfc.us/](https://bms.ahfc.us/)

Alaska Native Tribal Health Consortium:
[https://anthc.bmon.org/reports/](https://anthc.bmon.org/reports/)

![]({{ site.baseurl }}/assets/guide/image1.png)
**Figure 1:** Diagram of the basic architecture of the BMON system showing how sensor data becomes visible in the user interface.

### Video: Intro to BMON
This video gives a brief overview of viewing data on the BMON system.
{% include video id="672543509" provider="vimeo" %}

## Purpose of this Manual

This manual is a guide to setting up and using the [BMON
system](https://bms.ahfc.us/reports/?select_org=0&select_group=0&select_bldg=2&select_chart=0&select_sensor=680).
The manual is not a comprehensive guide to building monitoring and BMON;
instead it focuses on creating a basic but valuable monitoring system
that allows the user to identify energy savings potential, better
maintain and operate a facility, and avoid catastrophic failures such as
frozen pipes. The information contained in this manual is intended for
those seeking to set up and use the BMON system for energy management,
indoor air-quality management, occupant comfort, and identification of
equipment malfunction to prevent catastrophic failures. Although this
manual contains the information that will be necessary to set up and use
the BMON system, as well as some tips based on past experience, more
in-depth information can be found in the [BMON software
documentation](https://bmon-documentation.readthedocs.io/en/latest/user-introduction.html).

This manual goes over:

- The types of sensors used with BMON, what they measure, and how those measurements can be useful to a facilities manager, energy manager, or a building owner.

- The process of configuring a new building and dashboard in BMON, installing the sensors and internet-connected hardware, setting up alerts, and using the data for simple but powerful analysis.

## Value of BMON

BMON was originally created to help building owners and managers save
energy through efficiency and conservation measures informed by data.
BMON organizes information that can be used to make low-cost changes to
operational schedules, set-points, and general strategies to reduce
energy waste and wear and tear on components. The changes made through
monitoring and analysis can potentially reduce the financial burden of
high energy costs and equipment repair or replacement. Although saving
energy is still the main purpose of BMON, some other uses of the system
include:

-   Identifying equipment malfunctions to prevent catastrophic failures
    such as freeze-ups, loss of building pressure, equipment
    overheating, etc. Equipment may operate erratically or
    intermittently prior to a failure so monitoring critical equipment
    can provide early warning of a problem.

-   Monitoring building occupancy to make the best use of space and
    maximize safety for occupants. Often building uses are different
    from the original uses the building was designed for. Measuring
    actual occupancy can provide invaluable insights into the usage of
    a building that can promote safety and productivity practices.

-   Providing an operations log as a reference as well as a record of
    maintenance activities.

-   If HVAC equipment is going to be replaced, measurements of the
    actual loads required by a building or space can help determine
    the proper size of the new equipment. This is especially true if
    retrofits occurred in the building, making it more efficient, or
    if the usage has changed since it was built. It is also worth
    measuring the space heating and/or water heating needs because the
    equipment being replaced may not have been properly sized in the
    first place and substantial savings may be realized by
    right-sizing equipment.

## Other Resources

Other web resources helpful for developing a monitoring plan and
implementing BMON:

[BMON User Forum](https://forum.bmon.org/) - A forum for
all users to post questions, answers and tips on hardware, software or
anything else related to BMON and energy use in buildings.

[Analysis North](http://www.analysisnorth.com/) - The
primary software developer, contains links to other related projects
such as the heat pump calculator and AkWarm energy modeling software.

[BMON documentation](https://bmon-documentation.readthedocs.io/en/latest/) - Detailed software documentation for more complex situations and network administrators.

[AHFC SEMP Manual](https://www.ahfc.us/application/files/9414/5193/2592/SEMP-Master_Manual_FINAL_AHFC_12.31.15.pdf) - A manual to introduce public facility owners and managers to tools and
resources that can be used to complete successful energy efficiency
retrofit projects.

[LoRa Alliance](https://lora-alliance.org/?gclid=CjwKCAiA9vOABhBfEiwATCi7GLt4J4GiNHHCqJsDrNvlfHuLOuvDYP5YykZtjRnmmy6ssL1ra7BzpxoCu3YQAvD_BwE) - the group representing the communication technology LoRa (Long-Range wireless communication).

[The Things Network](https://www.thethingsnetwork.org/) -
The web service that enables LoRaWAN devices to communicate with BMON.

[Monnit](https://www.monnit.com/) - A wireless sensor
manufacturer utilizing a proprietary technology.

[Dragino](https://www.dragino.com/) - A wireless sensor
manufacturer utilizing LoRaWAN technology.

[Elsys](https://www.elsys.se/en/) - wireless sensor
manufacturer utilizing LoRaWAN technology.

