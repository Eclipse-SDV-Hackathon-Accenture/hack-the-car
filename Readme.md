# Hack the Car 🚗

Did you ever want to work an actual research vehicle? Well, here you can!

The setup consists of:

- A VW Passat
- A Test driver that will drive around for you
- Cameras
- LiDARs
- GPS
- Vehicle Data
- You, your laptop and your software 😊

_Note that there will be no actual closed-loop control of the vehicle. You will only be able to read data from the vehicle, but not control it._

# 📚 About

[Eclipse eCAL™](http://ecal.io) is a **publish subscribe** Middleware with the main focus on research and development of **autonomous driving** algorithms.

- A Publisher **publishes data** to a topic, identified by a name.
- A Subscriber **subscribes to a topic**, identified by a name. When it received data, it calls a **callback function**.

# 👾 Hack Ideas

- Recognize predestrians
- Develop HMIs to fuse point cloud data on an OpenStreeMap
- Use the LiDAR to scan a 3D Object
- Welcome the owner à la Face ID

# 💻 Requirements

- A **laptop**:
    - Running Windows or Linux.
      _MacOS may work too, but eCAL is poorly tested on that OS._
    - An ethernet interface (or a USB to ethernet adapter)

- **Programming languages**
    - Recommended: Python or C++
    - Other options: C, C#, JavaScript, Rust

# 👨‍🏫 Hack-Coaches

- Kerstin Keller
- Florian Reimold
- Kristof Hannemann
- Rex Schilasky
- Florian Geis

# 🛠 Template Setup

1. Download and setup Eclipse eCAL:
    - 🐧 Ubuntu:
        ```bash
        sudo add-apt-repository ppa:ecal/ecal-latest
        sudo apt-get update
        sudo apt-get install ecal
        ```

    - 🪟 Windows:
        - Download the latest release from https://eclipse-ecal.github.io/ecal/_download_archive/download_archive.html

2. Connect your Laptop to the vehicle via ethernet cable.

Example measurement:
https://drive.google.com/drive/folders/1-wHCBS1mx420NWE4ZJfxF6UJuahHMS0J?usp=sharing

# 👀 All necessary links

**Eclipse eCAL**:
- 🏠 Homepage: http://ecal.io
- 👨‍💻 GH Repository: https://github.com/eclipse-ecal/ecal
- 💡 How to compile eCAL: https://eclipse-ecal.github.io/ecal/development/building_ecal_from_source.html
