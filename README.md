<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo TBD" width="80" height="80">
  </a>

<h3 align="center">FANUC Ethernet IP Drivers</h3>

  <p align="center">
    Drivers to control FANUC robots using Ethernet IP
    <br />
    <a href="https://uofi-cdacs.github.io/FANUC-Ethernet_IP_Drivers/documentation/html/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>




<!-- ABOUT THE PROJECT -->
## About The Project

<!-- ADD SCREENSHOT HERE -->
This project aims to give developers tools to control FANUC robots in new ways using Ethernet IP

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python-shield]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

#### 1. Clone the repo
```sh
  git clone https://github.com/UniversityOfIdahoCDACS/FANUC-Ethernet_IP_Drivers.git
```
####  2. Install required libaries
```sh
  python3 -m venv venv
  source venv/bin/activate

  pip install pycomm3
```
####  3. Start the FANUC TP program
Below is a video on how to do this.
<a href="https://www.youtube.com/shorts/izM8dLgkj2w"> Video Link </a>

####  4. Run script
```sh
  cd examples/
  python quick_start.py
```


## Troubleshooting
<a href="https://docs.google.com/document/d/1N1k1eQPG0qeFhDfgyBnDlwhtVD0UiQ-7i8RM8bexTCA/edit?tab=t.0#heading=h.ybj6n73925tj" > Common Troubleshooting Issues </a>

<!-- ROADMAP -->
## Roadmap

- [x] Ethernet IP Control

See the [open issues](https://github.com/UniversityOfIdahoCDACS/FANUC-Ethernet_IP_Drivers/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/UniversityOfIdahoCDACS/FANUC-Ethernet_IP_Drivers](https://github.com/UniversityOfIdahoCDACS/FANUC-Ethernet_IP_Drivers)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-shield]:  https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
