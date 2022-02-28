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
<p align="right">(<a href="#top">back to top</a>)</p>

<img src = "res/demo2.gif" width ="240" /> <img src = "res/demo3.gif" width ="240" /> <img src = "res/demo1.gif" width ="240" />

### Built With

* [Python3](https://www.python.org/)
* [TKinter](https://docs.python.org/3/library/tkinter.html)
* [Python Zipfile](https://docs.python.org/3/library/zipfile.html)

<p align="right">(<a href="#top">back to top</a>)</p>

## *How to create one?*
Gboard Settings>Dictionary>Personal dictionary>All languages>Then tap on the "+" icon and create shortcuts. 
<br>

## *"Okay that seems easy, so what's the point of this project?"*
Well, imagine you have to make 100 such shortcuts. You'll follow the steps above, then go to the previous menu, then again tap the "+" icon, repeat it for 100 times? That's exactly why we made this project. <br>GBoard-Dictionary-Maker can create mutiple such shortcuts in bulk on a single window and then generate a GBoard importable zip!
<br>
## *Features*
 1. Create Gboard importable dictionary file
 2. Edit existing zip/txt dictionary file given
 3. 100% made with Python and yes , it's FOSS<br>
## *Prerequisites*
 1. Python
 2. Tkinter (incase your installation of python didn't come with tkinter preinstalled)
<br>A simple Google search of the format "install Python/Tkinter on \<your platform\>" would lead you to the right pages<br> e.g.,Google "Install Python on Windows" and "install Tkinter on Windows"

## *Installation*

### **On Windows, Linux and BSD**
### *Installation from the command line*
    git clone https://github.com/realKarthikNair/GBoard-Dictionary-Maker
    cd GBoard-Dictionary-Maker
    python3 main.py

### *manual installation: download the latest zip from 'releases'*
1. unzip it
2. Open the folder
3. Run main.py file

### **On Android**
### *For now, use the [legacy](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/tree/legacy) branch)*

### **On MacOS**
#### *Normal installation should work, but we can't guarantee since [the code is untested](https://github.com/realKarthikNair/GBoard-Dictionary-Maker#we-urgently-need-someone-on-mac-to-help-us-extend-project-compatibility). Incase you encounter issues on Mac, kindly either help us by raising an [issue](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/issues/new/choose) and help us in extending compatibility. You can alternatively choose the [legacy](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/tree/legacy) branch*

### How to import in Gboard?
**Run the code , generate the zip, copy it to your mobile and import from Gboard settings>Dictionary>Personal Dictionary>All Languages>then choose import option from the drop-down menu**

## Roadmap

   ✅ Add a Graphical User Interface (GUI)<br>
   ✅ Ability to add more shortcuts to existing dictionary zips<br>
   ✅ Fix some graphical glitches in Linux (possibly in Mac OS and other UNIX derivatives too)<br>
  〚 〛 Support on Mac and Android<br>
  〚 〛  Documenting and further optimisation of code<br>
  〚 〛 Multi-language Support<br>

See the [open issues](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/issues) for a full list of proposed features (and known issues).
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make GBoard-Dictionary-Maker, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

### **We Urgently need someone on Mac to help us extend project compatibility since we don't own an Apple computer and thus can't test the code**
## License 
This software is being licensed on [these](https://github.com/realKarthikNair/GBoard-Dictionary-Maker/blob/main/LICENSE.md) terms 
## *Enjoy !*

>Made with Love™ ❤️<br>
>by Karthik Nair and Karan Arora

<!-- > Upcoming updates are being cooked in the 'alpha'  branch: feel free to test them out...-->

## Catch us on: 
### [Karthik Nair](https://github.com/realkarthiknair)

<p align="left">
    <a href="https://www.instagram.com/karthiknair.sh" alt="instagram">
        <img src="https://img.shields.io/badge/Instagram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-yellowgreen" /></a>
    <a href="https://www.twitter.com/realkarthiknair" alt="twitter">
        <img src="https://img.shields.io/badge/Twitter-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-orange" /></a>
</p>


### [Karan Arora](https://github.com/AroraKaran19)

<p align="left">
    <a href="https://www.instagram.com/arorakaran_18" alt="instagram">
        <img src="https://img.shields.io/badge/Instagram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-yellowgreen" /></a>
    <a href="https://www.telegram.me/karan_arora18" alt="Telegram">
        <img src="https://img.shields.io/badge/Telegram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-orange" /></a>
</p>

### Support US

<img src="donate.jpg">

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.png
