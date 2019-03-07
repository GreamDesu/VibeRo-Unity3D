# VibeRo-Unity3D

Unity project which uses Beaglebone and VibeRo setup to simulate soft object in VR.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
### Prerequisites

- Unity3D 
- Oculus VR (I used CV1)
- VibeRo setup
- Beaglebone Black


### Installing and deployment

Clone repo to your local machine.
Upload `Beaglebone\pwm.py` to your beaglebone. Change 

```
serverAddr = ('192.168.7.1', 7000)
```
according to your IP and port if needed.

Open Unity project and change `Assets\Scripts\TCPChat.cs` to change port and IP of server.
```
tcpListener = new TcpListener (IPAddress.Parse ("192.168.7.1"), 7000)
```
Run project in Unity and run Python script on beaglebone.

Enjoy

## Code Authors

* **Amir Yelenov** - *Unity project* - [GreamDesu](https://github.com/GreamDesu)
* **Adilzhan Adilkhanov** - *Python script* - [adilzhaniwe](https://github.com/Adilzhaniwe)

