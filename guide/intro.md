---
title: User Guide
header:
  image: /assets/images/banner2.png

---

*This site is best viewed with the Google Chrome or Microsoft Edge web browsers.*

## Acknowledgements
{: #acknowledgements}

This material is based upon work supported by the U.S. Department of
Energy's (DOE) Office of Energy Efficiency and Renewable Energy (EERE)
under the Advanced Building Construction with Energy Efficient
Technologies & Practices (ABC) award, award number DE-EE0009088.

This manual was created under a contract with Analysis North over the
Alaska state fiscal years 2021 and 2022. Many thanks to Information
Insishts and Loeffler Engineering for editing this manual.

## Introduction
{: #introduction}

The Building Monitoring (BMON) System, often referred to as simply BMON,
is a free, open-source software platform designed by Alaska Housing
Finance Corporation (AHFC) and built by Alaska energy experts to track
and analyze energy use and operations in buildings of all sizes.
Analysis North has been the primary software developer of the BMON
application through a contract funded by the DOE State Energy Program.

![]({{ site.baseurl }}/assets/guide/intro/image2.png)
<br>{: #image2}*Alaskan BMON User Collecting Fuel Use Data (photo credit to Andrew Kroll)*{: .small_text}
<br>

While the software is available to the public at no cost, a BMON user’s
data collection and storage costs must be weighed against potential
energy cost savings such that an acceptable payback on monitoring can be
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

  - Measuring heating fuel use of a building to properly size a
    replacement boiler.

  - Tracking lighting against the occupied schedule to make sure
    lighting is not used unnecessarily during unoccupied times.

  - Monitoring indoor temperatures compared to the occupied schedule to
    properly time warm-up sequence.

Here are examples of a couple different BMON information sites:

[Alaska Housing Finance Corporation BMON Site](https://bms.ahfc.us/){:target="_blank"}

[Alaska Native Tribal Health Consortium](https://anthc.bmon.org/){:target="_blank"}


![]({{ site.baseurl }}/assets/guide/intro/image1.png)
<br>{: #image1}*Basic Architecture of the BMON System*{: .small_text}
<br>

***Video:*** *Introduction to BMON*
{: #video-introduction-bmon}
{% include video id="672543509" provider="vimeo" %}

### Purpose of this Manual
{: #purpose-this-manual}

This manual is a guide to setting up and using the [Building
Monitoring](https://bms.ahfc.us/reports/?select_org=0&select_group=0&select_bldg=2&select_chart=0&select_sensor=680){:target="_blank"}
(BMON)
[System](https://bms.ahfc.us/reports/?select_org=0&select_group=0&select_bldg=2&select_chart=0&select_sensor=680){:target="_blank"}.
The manual is not a comprehensive guide to building monitoring and
BMON; instead, it focuses on a basic but valuable monitoring system that
allows the user to identify energy savings potential, better maintain
and operate a facility, and avoid catastrophic failures, such as frozen
pipes. The information in this manual is intended for those seeking to
use BMON for energy management, indoor air-quality management, occupant
comfort, and identification of equipment malfunction to prevent
catastrophic failures. This manual contains the information necessary
to set up and use the BMON system, plus some tips based on past
experience. More in-depth information can be found in the [BMON software
documentation](https://bmon-documentation.readthedocs.io/en/latest/user-introduction.html){:target="_blank"}.

This manual covers:

  - The types of sensors used with BMON, what they measure, and how
    those measurements can be useful to a facilities manager, energy
    manager, or a building owner.

  - The process of configuring a new building and dashboard in BMON,
    installing the sensors and internet-connected hardware, setting up
    alerts, and using the data for simple but powerful analysis.

### Value of BMON
{: #value-bmon}

BMON was originally created to help building owners and managers save
energy through efficiency and conservation measures informed by data.
BMON organizes information that can be used to make low-cost changes to
operational schedules, set-points, and general strategies to reduce
energy waste and wear and tear on components. The changes made through
monitoring and analysis can potentially reduce the financial burden of
high energy costs and equipment repair or replacement. Although saving
energy is still the main purpose of BMON, some other uses of the system
include:

  - Identifying equipment malfunctions to prevent catastrophic failures
    such as freeze-ups, loss of building pressure, equipment
    overheating, etc. Equipment may operate erratically or
    intermittently prior to a failure so monitoring critical equipment
    can provide early warning of a problem.

  - Monitoring building occupancy to make the best use of space and
    maximize safety for occupants. Measuring actual occupancy can
    provide valuable insights into the usage of a building that can
    promote safety and productivity practices.

  - Providing an operations log as a reference and a record of
    maintenance activities.

  - If HVAC equipment is going to be replaced, measuring the actual
    loads required by a building or space to help determine the proper
    size of the new equipment. This is especially true if retrofits
    occurred in the building, making it more efficient, or if the usage
    of the building has changed since it was built. Measuring the space
    heating and/or water heating needs is valuable because the equipment
    being replaced may not have been properly sized in the first place
    and substantial savings may be realized by right-sizing equipment.
