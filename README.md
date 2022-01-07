
<p align="center">
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/realKarthikNair/GBoard-Dictionary-Maker.svg?style=for-the-badge" /></a>
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/network/members" alt="Forks">
        <img src="https://img.shields.io/github/forks/realKarthikNair/GBoard-Dictionary-Maker.svg?style=for-the-badge" /></a>
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/stargazers" alt="Stars">
        <img src="https://img.shields.io/github/stars/realKarthikNair/GBoard-Dictionary-Maker.svg?style=for-the-badge" /></a>
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/issues" alt="Issues">
        <img src="https://img.shields.io/github/issues/realKarthikNair/GBoard-Dictionary-Maker.svg?style=for-the-badge" /></a>
</p>
<br />
<div align="center">
  <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker">
    <img src="https://i.ibb.co/TH5068T/gboarddictionarylogo.png" alt="Logo" width="300" height="250">
  </a>

<h2 align="center">GBoard-Dictionary-Maker</h2>
 
 
  <p align="center">
 <h3>Make GBoard importable dictionaries with ease ! </h3>
    <br />
</div>
<p align="center">
    <a href="#installation" alt="Installation">
        <img src="https://img.shields.io/badge/Installation-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-brightgreen" /></a>
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/issues/new/choose" alt="Report a Bug">
        <img src="https://img.shields.io/badge/%20%20Report%20a%20Bug-%F0%9F%90%9E-orange" /></a>
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/issues/new/choose" alt="Request a Feature">
        <img src="https://img.shields.io/badge/Request%20a%20Feature-%F0%9F%93%88-yellowgreen" /></a>
    <a href="https://telegra.ph/payment-links-coming-soon-01-07" alt="Donate">
        <img src="https://img.shields.io/badge/donate-%F0%9F%92%B0-lightgrey" /></a>
    <a href="https://github.com/realKarthikNair/GBoard-Dictionary-Maker/tree/legacy" alt="Legacy Branch">
        <img src="https://img.shields.io/badge/Legacy%20Branch-%F0%9F%91%B4-blue" /></a>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#what-is-a-gboard-dictionary-why-do-you-need-to-make-one">What is a GBoard Dictionary? Why do you need to make one?</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-to-create-one">How to create a GBoard Dictionary manually</a>
      <a href="#okay-that-seems-easy-so-whats the point of this project">Motive of this project</a>
      <a href="#features">Features</a>
      <a>Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#catch-us-on">Contact Us</a></li>
  </ol>
</details>


## *What is a GBoard Dictionary? Why do you need to make one?*
GBoard Dictionaries allow GBoard- The Google Keyboard to display word suggestion pop-ups whenever you start typing. These suggestions save a lot of our typing time, right?<br>
Now, GBoard also allows you to create many such custom dictionary elements, like keybindings, e.g., you type in "hey" and boom! you get an entire sentence "Hey There! This is Jennifer" as a suggestion, which you can tap and automatically type in an entire sentence that quickly. <br> Making several such custom shortcuts can increase your typing speed upto any extent and save you a lot of time, especially if you're leading a really busy life!
<br>
Also that these shortcuts can be made with any language, or even emojis!
<br>

### Built With

* [Python3](https://www.python.org/)
* [TKinter](https://docs.python.org/3/library/tkinter.html)
* [Python Zipfile](https://docs.python.org/3/library/zipfile.html)

## *How to create one?*
Gboard Settings>Dictionary>Personal dictionary>All languages>Then tap on the "+" icon and create shortcuts. 
<br>
<p align="right">(<a href="#top">back to top</a>)</p>
## *"Okay that seems easy, so what's the point of this project?"*
Well, imagine you have to make 100 such shortcuts. You'll follow the steps above, then go to the previous menu, then again tap the "+" icon, repeat it for 100 times? That's exactly why we made this project. <br>GBoard-Dictionary-Maker can create mutiple such shortcuts in bulk on a single window and then generate a GBoard importable zip!
<br>
<p align="right">(<a href="#top">back to top</a>)</p>
## *Features*
 1. Create Gboard importable dictionary file
 2. Edit existing zip/txt dictionary file given
 3. 100% made with Python and yes , it's FOSS<br>
<p align="right">(<a href="#top">back to top</a>)</p>
## *Prerequisites*
 1. Python
 2. Tkinter
<br>A simple Google search of the format "install Python/Tkinter on \<your platform\>" would lead you to the right pages<br> e.g.,Google "Install Python on Windows" and "install Tkinter on Windows"
<p align="right">(<a href="#top">back to top</a>)</p>
## *Installation*
### **Installation from the command line**
    git clone https://github.com/realKarthikNair/GBoard-Dictionary-Maker
    cd GBoard-Dictionary-Maker
    python3 main.py

### **manual installation: download the latest zip from 'releases'**
1. unzip it
2. Open the folder
3. Run main.py file
<p align="right">(<a href="#top">back to top</a>)</p>
### How to import in Gboard?
**Run the code , generate the zip, copy it to your mobile and import from Gboard settings>Dictionary>Personal Dictionary>All Languages>then choose import option from the drop-down menu**
<p align="right">(<a href="#top">back to top</a>)</p>
## Roadmap

- [x] Add a Graphical User Interface (GUI)
- [x] Ability to add more shortcuts to existing dictionary zips
- [ ] Support on Mac and Android
- [ ] Documenting and further optimisation of code
- [ ] Fix some graphical glitches in Linux (possibly in Mac OS and other UNIX derivatives too)
- [ ] Multi-language Support

See the [open issues](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/issues) for a full list of proposed features (and known issues).
<p align="right">(<a href="#top">back to top</a>)</p>
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make GBoard-Dictionary-Maker, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!
### **We Urgently need someone on Mac to help us extend project compatibility**
<p align="right">(<a href="#top">back to top</a>)</p>
## License 
This software is being licensed on [these](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/blob/main/LICENSE.md) terms 
## *Enjoy !*

>Made with Love™ ❤️<br>
>by Karthik Nair and Karan Arora

<!-- > Upcoming updates are being cooked in the 'alpha'  branch: feel free to test them out...-->
<p align="right">(<a href="#top">back to top</a>)</p>
## Catch us on: 
### [Karthik Nair](https://github.com/realkarthiknair)
*[instagram ](https://www.instagram.com/harry_kris_) <br>*
*[twitter](https://www.twitter.com/realkarthiknair) <br>*

### [Karan Arora](https://github.com/AroraKaran19)
*[instagram ](https://www.instagram.com/arorakaran_18)*
<p align="right">(<a href="#top">back to top</a>)</p>
<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.png
