# ASKEY RTL6300-D354 5G CPE Integration

Custom integration to monitor and control the ASKEY RTL6300 5G CPE router via REST API.

## Installation 

### Option 1: [HACS](https://hacs.xyz/) Link

~~1. Click [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=dbuezas&category=integration&repository=askey_rtl6300_5g_cpe)~~
~~2. Restart Home Assistant~~updates
To be added


### Option 2: [HACS](https://hacs.xyz/)

1. Or `HACS` > `Integrations` > `⋮` > `Custom Repositories`
2. `Repository`: paste the url of this repo `https://github.com/cretudorin/askey_rtl6300_5g_cpe`
3. `Category`: Integration
4. Click `Add`
5. Close `Custom Repositories` modal
6. Click `+ EXPLORE & DOWNLOAD REPOSITORIES`
7. Search for `askey_rtl6300_5g_cpe`
8. Click `Download`
9. Restart _Home Assistant_

### Option 3: Manual copy

1. Copy `askey_rtl6300_5g_cpe` folder into your Home Assistant `custom_components` directory.
2. Restart Home Assistant
3. Go to Integrations and add "ASKEY RTL6300 5G CPE"
4. Enter router IP

## Supported Sensors 

Here’s the revised markdown table without the values, organized by category:

| **Category**         | **Sensor Name**               | **Description**                                                                 |
|----------------------|-------------------------------|---------------------------------------------------------------------------------|
| **Connection**       | Connection Type               | Type of network connection (e.g., LTE, 5G).                                    |
|                      | External IPv4                 | External IPv4 address assigned to the device.                                   |
|                      | External IPv6                 | External IPv6 address assigned to the device (if available).                    |
|                      | IPv4 Status                   | Status of the IPv4 connection.                                                 |
|                      | IPv6 Status                   | Status of the IPv6 connection.                                                 |
| **Traffic**          | Current Download              | Current download data volume.                                                  |
|                      | Current Upload                | Current upload data volume.                                                    |
|                      | Last Traffic Update           | Timestamp of the last traffic data update.                                    |
|                      | Monthly Download              | Total received data for the month.                                             |
|                      | Monthly Upload                | Total transmitted data for the month.                                          |
|                      | Monthly Total                 | Total combined data usage for the month.                                       |
| **SMS**              | SMS Inbox Count               | Number of unread messages in the inbox.                                         |
|                      | SMS Outbox Count              | Number of messages in the outbox.                                               |
| **Diagnostic**       | Allocated Bandwidth Download  | Allocated bandwidth for download.                                               |
|                      | Allocated Bandwidth Upload    | Allocated bandwidth for upload.                                                 |
| **Network**          | IPv4 DNS 1                    | Primary IPv4 DNS server address.                                                |
|                      | IPv4 DNS 2                    | Secondary IPv4 DNS server address.                                              |
|                      | IPv4 Gateway                  | IPv4 gateway address.                                                           |
|                      | IPv6 DNS 1                    | Primary IPv6 DNS server address (if available).                                |
|                      | IPv6 DNS 2                    | Secondary IPv6 DNS server address (if available).                              |
|                      | IPv6 Gateway                  | IPv6 gateway address (if available).                                            |
| **PCC (Primary Cell)** | PCC Band                   | Primary cell band.                                                              |
|                      | PCC Bandwidth                | Bandwidth of the primary cell.                                                  |
|                      | PCC Count                    | Number of primary cells.                                                        |
|                      | PCC CQI                      | Channel Quality Indicator for the primary cell.                                |
|                      | PCC ENB                      | eNodeB ID for the primary cell.                                                 |
|                      | PCC GCI                      | Global Cell Identity for the primary cell.                                      |
|                      | PCC MCC                      | Mobile Country Code for the primary cell.                                       |
|                      | PCC MNC                      | Mobile Network Code for the primary cell.                                       |
|                      | PCC PCI                      | Physical Cell ID for the primary cell.                                          |
|                      | PCC RSRP                     | Reference Signal Received Power for the primary cell.                           |
|                      | PCC RSRQ                     | Reference Signal Received Quality for the primary cell.                          |
|                      | PCC RSSI                     | Received Signal Strength Indicator for the primary cell.                        |
|                      | PCC RX Channel               | Receive channel for the primary cell.                                           |
|                      | PCC RX Freq                  | Receive frequency for the primary cell.                                         |
|                      | PCC SINR                     | Signal to Interference plus Noise Ratio for the primary cell.                    |
|                      | PCC TAC                      | Tracking Area Code for the primary cell.                                        |
|                      | PCC TX Channel               | Transmit channel for the primary cell.                                          |
|                      | PCC TX Freq                  | Transmit frequency for the primary cell.                                        |
| **Traffic Stats**    | RX Dropped                    | Number of dropped received packets.                                             |
|                      | RX Errors                    | Number of received packets with errors.                                         |
|                      | RX Packets                   | Total number of received packets.                                               |
|                      | TX Dropped                   | Number of dropped transmitted packets.                                          |
|                      | TX Errors                    | Number of transmitted packets with errors.                                      |
|                      | TX Packets                   | Total number of transmitted packets.                                            |
| **SCC1 (Secondary Cell)** | SCC1 Band                | Secondary cell band.                                                            |
|                      | SCC1 Bandwidth              | Bandwidth of the secondary cell.                                                |
|                      | SCC1 PCI                     | Physical Cell ID for the secondary cell.                                        |
|                      | SCC1 RSRP                    | Reference Signal Received Power for the secondary cell.                         |
|                      | SCC1 RSRQ                    | Reference Signal Received Quality for the secondary cell.                        |
|                      | SCC1 RSSI                    | Received Signal Strength Indicator for the secondary cell.                      |
|                      | SCC1 RX Channel              | Receive channel for the secondary cell.                                          |
|                      | SCC1 RX Freq                 | Receive frequency for the secondary cell.                                        |
|                      | SCC1 SINR                    | Signal to Interference plus Noise Ratio for the secondary cell.                  |
|                      | SCC1 TX Channel              | Transmit channel for the secondary cell.                                         |
|                      | SCC1 TX Freq                 | Transmit frequency for the secondary cell.                                       |

## Services

- Read / send SMS
- Clear inbox / outbox

## Reading the SMS
- call the "Get Inbox" action
- the messages will be published to as an event under "askey_rtl6300_5g_cpe_sms_inbox_data" 

Sample Automation 
```
alias: Handle SMS Inbox Data
description: ""
triggers:
  - event_type: askey_rtl6300_5g_cpe_sms_inbox_data
    trigger: event
actions:
  - data:
      message: "{{ trigger.event.data.messages }}"
      level: info
    action: system_log.write
```

- Select what you see on creation
- pin managment / change pin

## Readonly endpoints
| URL                                                | Method | Description                                                 |   
|----------------------------------------------------|--------|-------------------------------------------------------------|
| IP                                                 |        |                                                             | 
| http://172.20.168.1/restful/CMGR/v4_status_info    | GET    | connectivity status (v4)                                    |
| http://172.20.168.1/restful/CMGR/v6_status_info    | GET    | connectivity status (v4)                                    |
| SMS                                                |        |                                                             | 
| http://172.20.168.1/restful/sms/outbox_list_count  |        | number of sms in inbox                                      | 
| http://172.20.168.1/restful/sms/outbox_list        |        | read all                                                    | 
| http://172.20.168.1/restful/sms/inbox_list_count   |        | number of sms in inbox                                      | 
| http://172.20.168.1/restful/sms/inbox_list         |        | read all                                                    | 
| http://172.20.168.1/restful/sms/send_msg/          | PUT    | delete, mark as read                                        | 
| Unsorted                                           |        |                                                             | 
| http://172.20.168.1/restful/lte/apn                | GET    | LTE APN configuration                                       |
| http://172.20.168.1/restful/lte/cellular_info      | GET    | basic cellular info                                         |
| http://172.20.168.1/restful/lte/cellular_info_ex   | GET    | extended cellular information                               |
| http://172.20.168.1/restful/lte/cellular_stats     | GET    | cellular network traffic stats                              |
| http://172.20.168.1/restful/lte/throughput         | GET    | upload / download throughput                                | 
| http://172.20.168.1/restful/lte/device_info        | GET    | SIM / device info                                           |
| http://172.20.168.1/restful/lte/status_info        | GET    | SIM / LTE status info                                       |
| http://172.20.168.1/restful/lte/signal_info        | GET    | 5G NR signal info                                           |
| http://172.20.168.1/restful/traffic/daily          | GET    | daily data usage                                            | 
| http://172.20.168.1/restful/traffic/monthly        | GET    | monthly data usage                                          |
| http://172.20.168.1/restful/lte/cellular_info_ca   | GET    | carrier aggregation info                                    |
| http://172.20.168.1/restful/tr069/other_info       | POST   | fake "TR‑069"                                               |


## Control endpoints

| Control                   | URL                                                  | Method | Payload                                                                                     |
|---------------------------|-------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------|
| Reconnect LTE             | http://172.20.168.1/restful/lte/control               | PUT | `{"command": "2", "ifname": "rmnet_data0"}`                                                   | 
| Disconnect LTE            | http://172.20.168.1/restful/lte/control               | PUT | `{"command": "1", "ifname": "rmnet_data0"}`                                                   | 
| Connect LTE               | http://172.20.168.1/restful/lte/control               | PUT | `{"command": "0", "ifname": "rmnet_data0"}`                                                   | 
| Get APN Settings          | http://172.20.168.1/restful/lte/apn                   | GET | None                                                                                          | 
| Set APN Settings          | http://172.20.168.1/restful/lte/apn                   | PUT | `{"auto": "0", "name": "", "user": "", "pwd": "", "auth": "", "pdn": ""}`                     |
| Get Roaming Settings      | http://172.20.168.1/restful/lte/roaming               | GET | None                                                                                          | 
| Set Roaming Settings      | http://172.20.168.1/restful/lte/roaming               | PUT | `{"enable": "1"}`                                                                             | 
| Get Airplane Mode         | http://172.20.168.1/restful/lte/airplane_mode         | GET | None                                                                                          | 
| Set Airplane Mode         | http://172.20.168.1/restful/lte/airplane_mode         | PUT | `{"enable": "1"}`                                                                             | 
| Change SIM PIN            | http://172.20.168.1/restful/lte/sim_change_pin        | PUT | `{"old_pin_code": "old_pin", "new_pin_code": "new_pin"}`                                      | 
| Lock SIM PIN              | http://172.20.168.1/restful/lte/sim_pin_lock          | PUT | `{"enable": "1", "pin_code": "your_pin"}`                                                     | 
| Unlock SIM PIN            | http://172.20.168.1/restful/lte/sim_unlock_pin        | PUT | `{"pin_code": "your_pin"}`                                                                    | 
| Unlock SIM PUK            | http://172.20.168.1/restful/lte/sim_unlock_puk        | PUT | `{"new_pin_code": "new_pin", "puk_code": "your_puk"}`                                         | 
| Get SIM PIN Left Attempts | http://172.20.168.1/restful/lte/sim_pin_left          | GET | None                                                                                          | 
| Get Supported PDN Types   | http://172.20.168.1/restful/CMGR/list_support_v4_info | GET | None                                                                                          | 
| Reboot device             | http://172.20.168.1/restful/sysadm/reboot             | PUT |  `{ "option": "1"}`                                                                           |
