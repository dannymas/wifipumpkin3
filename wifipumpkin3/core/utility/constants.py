import os

# This file is part of the wifipumpkin3 Open Source Project.
# wifipumpkin3 is licensed under the Apache 2.0.

# Copyright 2020 P0cL4bs Team - Marcos Bomfim (mh4x0f)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

dir_of_executable = os.path.dirname(__file__)
dir_path = os.getcwd()
user_config_dir = os.path.expanduser("~")

SYSTEMCOMMAND = [
    "ifconfig",
    "iw",
    "iwconfig",
    "route",
    "iptables",
    "ls",
    "clear",
    "nano",
]

HELPFILESPATH = user_config_dir + "/.config/wifipumpkin3/helps/"
EXCEPTFILESPATH = user_config_dir + "/.config/wifipumpkin3/exceptions/"

# DHCP logger connected
CLIENTS_CONNECTED = (
    user_config_dir + "/.config/wifipumpkin3/config/session/connected.json"
)

DHCPSERVERBINARY = "core/packets/binary/dhcpserver"

# DNS file hosts
DNSHOSTS = user_config_dir + "/.config/wifipumpkin3/config/app/dns_hosts.ini"

# donation button
# TODO: add donation in readme
DONATE = "https://github.com/P0cL4bs/wifipumpkin3#donation"
DONATE_TXT = (
    "Consider donating to support the development and maintenance of WiFi-Pumpkin. "
)

# settings DHCP
DHCPLEASES_PATH = "/var/lib/dhcp/dhcpd.leases"
DHCPCONF_PATH = "core/config/dhcpd_wp.conf"

# settings HOSTAPD
HOSTAPDCONF_PATH = user_config_dir + "/.config/wifipumpkin3/config/hostapd/hostapd.conf"
HOSTAPDCONF_PATH2 = (
    user_config_dir + "/.config/wifipumpkin3/config/hostapd/hostapd+.conf"
)
ALGORITMS = ("TKIP", "CCMP", "TKIP + CCMP")

# system configs
NETWORKMANAGER = "/etc/NetworkManager/NetworkManager.conf"
IPFORWARD = "/proc/sys/net/ipv4/ip_forward"

# Docker settings
DOCKERIPTABLESPATH = "/etc/iptables.ipv4.nat"
DOCKERHOSTAPDCONF_PATH = "/etc/hostapd/hostapd.conf"

# logging
LOG_PUMPKINPROXY = user_config_dir + "/.config/wifipumpkin3/logs/ap/pumpkin_proxy.log"
LOG_PYDNSSERVER = user_config_dir + "/.config/wifipumpkin3/logs/ap/pydns_server.log"
LOG_SNIFFKIN3 = user_config_dir + "/.config/wifipumpkin3/logs/ap/sniffkin3.log"
LOG_CAPTIVEPO = user_config_dir + "/.config/wifipumpkin3/logs/ap/captiveportal.log"
LOG_RESPONDER3 = user_config_dir + "/.config/wifipumpkin3/logs/ap/responder3.log"
LOG_HOSTAPD = user_config_dir + "/.config/wifipumpkin3/logs/ap/hostapd.log"
LOG_ALL = user_config_dir + "/.config/wifipumpkin3/logs/everything.log"


# APP SETTINGS
CONFIG_INI = user_config_dir + "/.config/wifipumpkin3/config/app/config.ini"
CONFIG_SK_INI = user_config_dir + "/.config/wifipumpkin3/config/app/sniffkin3.ini"
CONFIG_PP_INI = user_config_dir + "/.config/wifipumpkin3/config/app/pumpkinproxy.ini"
CONFIG_CP_INI = user_config_dir + "/.config/wifipumpkin3/config/app/captive-portal.ini"

TEMPLATES = "templates/fakeupdate/Windows_Update/Settins_WinUpdate.html"
TEMPLATE_PH = "templates/phishing/custom/index.html"
TEMPLATE_CLONE = "templates/phishing/web_server/index.html"
EXTRACT_TEMP = "cd templates/ && tar -xf fakeupdate.tar.gz"
LCOMMITS = "https://raw.githubusercontent.com/P0cL4bs/WiFi-Pumpkin/master/Core/config/commits/Lcommits.cfg"
SOURCE_URL = "https://github.com/P0cL4bs/WiFi-Pumpkin.git"


# settings template
TEMPLATES_FLASK = user_config_dir + "/.config/wifipumpkin3/config/"
TEMP_CUSTOM = dir_path + "/templates/phishing/custom"
TEMP_Win = dir_path + "/templates/fakeupdate/Windows_Update"
TEMP_Java = dir_path + "/templates/fakeupdate/Java_Update"

# plugins path
RESPONDER_EXEC = "plugins/external/Responder/Responder.py"
DNS2PROXY_EXEC = "plugins/external/dns2proxy/dns2proxy.py"
BDFPROXY_EXEC = "plugins/external/BDFProxy-ng/bdf_proxy.py"
