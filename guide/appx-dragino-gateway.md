---
title: "Appendix: Configuring Dragino LoRaWAN Gateways"
toc: false
previous:
  title: "Appendix - Notes on Various Sensor Applications"
  url: /guide/appx-sensor-applications.html
---
Dragino makes a few different LoRaWAN gateways, including the LPS8N
and the outdoor DLOS8. This
section gives some notes on how to configure these gateways. Full
documentation for each gateway is on the Dragino website and should be
consulted for detailed information.

When you power up the gateway, it broadcasts a new Wi-Fi network that
you can connect to with a PC (just like connecting to a Wi-Fi network at
a coffee shop). The network name always starts with “dragino", for
example “dragino-1eb408". The Wi-Fi password for connecting to this
network is “dragino+dragino".

Next, you need to use a web browser to access the configuration web
pages located on the gateway. You access those pages by typing in the
following IP address into the address bar of your browser: 10.130.1.1.
The first time you try to access this address, a dialog will pop up
requesting you to log in. For this log in, the username is “root" and
the password is “dragino". You are then presented with the following
system diagram:

![]({{ site.baseurl }}/assets/guide/appx-dragino-gateway/image6.png)
<br>{: #image6}*System Diagram for Dragino LoRaWAN Gateway*{: .small_text}

which generally displays which parts of the gateway are working. Access
to different configuration pages can be done by clicking on parts of the
diagram or by using the menus at the top of the page.

It is often a good idea to upgrade the firmware of the gateway when you
first receive it. Check the User Manual for details. First, you need to
download the latest firmware from the Dragino website. Then, click the
“Firmware Upgrade" option from the System menu at the top of the Home
Dragino web page you accessed above. Finally, you “Upload Firmware File"
from your PC to the Gateway and “Proceed with Flash". You will be forced
to reconnect to the gateway Wi-Fi network and access the configuration
page again.

## Configuring Gateway for the Things Network
{: #configure-gateway-things}

Here are the key settings that need to be changed to configure the
gateway for US operation on the Things Network:

1.  From the “LoRa" menu, click the “LoRa" item. Change the Radio
    Settings section to look like the following:
    ![]({{ site.baseurl }}/assets/guide/appx-dragino-gateway/image1.png)
<br>{: #image1}*Screenshot of LoRa Radio Settings*{: .small_text}

    Click the “Save&Apply" button at the bottom of the page.

2.  From the “LoRaWAN" menu, click the “LoRaWAN" item. Copy and save the
    Gateway ID from the General Settings section, as you will need this
    later when you register this gateway on the Things Network. Do not
    change the ID.

    ![]({{ site.baseurl }}/assets/guide/appx-dragino-gateway/image5.png)
<br>{: #image5}*Screenshot of Gateway ID*{: .small_text}

    Then set the “Primary LoRaWAN Server" as follows:
    ![]({{ site.baseurl }}/assets/guide/appx-dragino-gateway/image4.png)
<br>{: #image4}*Screenshot of Primary LoRaWAN Server*{: .small_text}

    Click the “Save&Apply" button at the bottom of the page.

3.  If you are going to connect the gateway to the Internet via a wired
    Ethernet connection, there is no more configuration required on the
    gateway. If you want to use Wi-Fi to connect the gateway to the
    Internet, then you need to access the “Network" menu and click
    “WiFi". On the WiFi page, you must fill out the settings in the
    “WiFi WAN Client Settings" section of the page, making sure to
    “Enable WiFi WAN Client" and to properly fill out the name of the
    Wi-Fi network (SSID) and the Passphrase. Also, keep the “Enable WiFi
    Access Point" checkbox enabled so that you can access the gateway in
    the future for configuration (i.e. make no changes in that
    section).
    Note one issue we have discovered with filling out and enabling the
    “WiFi WAN Client Settings" section: if that Wi-Fi connection is
    not available, an Ethernet connection will also not work. If you use
    Wi-Fi for testing the gateway but ultimately intend to use an
    Ethernet connection, make sure you disable the Wi-Fi WAN Client.
    If your gateway is capable of a cellular connection to the Internet,
    you can set that up on the "Network" page as well.  You need to
    know the APN of the cellular network you are connecting to.

4.  You then need to register the gateway on the Things Network through
    the [Things
    Console](https://console.cloud.thethings.network/https://console.cloud.thethings.network/){:target="_blank"}.
    The important settings there are the “Gateway EUI", which is the
    “Gateway ID" that we copied in a prior step (it is called the
    Gateway ID on the Dragino configuration page, but it is labeled
    Gateway EUI on the Things Console). Also, the frequency plan must be
    set correctly:
    ![]({{ site.baseurl }}/assets/guide/appx-dragino-gateway/image3.png)
<br>{: #image3}*Screenshot of Frequency Plan*{: .small_text}

5.  Unplug and then re-power the gateway. If you reconnect to the
    gateway’s Wi-Fi network and visit the home page at 10.130.1.1, you
    should see green checkmarks:


![]({{ site.baseurl }}/assets/guide/appx-dragino-gateway/image2.png)
<br>{: #image2}*System Diagram for Dragino LoRaWAN Gateway with Green Checkmarks*{: .small_text}
