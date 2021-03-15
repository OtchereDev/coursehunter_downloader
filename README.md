# COURSEHUNTER DOWNLOADER (CH-DOWNLOAD) v2.0

# Download videos (course) from coursehunter.net

### How to install needed packages ( Python 3.\* required):

```sh
~ git clone https://github.com/OtchereDev/coursehunter_downloader
~ cd coursehunter-downloader
~ pip install -r requirements.txt
```

### How to download a webdriver (Required or else downloader wont work)
```sh
# if you are have Google chrome installed on your computer
~ go to https://chromedriver.chromium.org/downloads

~ then download the version of driver which is compactible with the browser version you have

~ Finally extract and place the driver in the root directory of the cloned repository

# if you are have Mozilla Firefox installed on your computer
~ go to https://github.com/mozilla/geckodriver/releases

~ then download the version of driver which is compactible with the browser version you have

~ Finally extract and place the driver in the root directory of the cloned repository

```

### Download premium courses (required paid subscription)

```sh
# from downloaded directory
~ python main.py
```

### User Inputs:

```sh

Email: email for login

Password: password for login

Course_links : url to the course (eg. https://coursehunter.net/course_name)

Webdriver Delay time (eg. 20) in seconds: how long should the driver wait before failing if your internet connection is not strong (default 20)

Which type of download would you like to make: A  to download all course lesson
                                               R  to download a range of course lesson eg. 10,15
                                               S to download a single lesson eg. 5

Would you like to download the course material: Y to download course material 
                                                N or Enter skip downloading it

```

## Author:

- [Oliver Otchere](https://github.com/OtchereDev)

### Inspiration:

- This is a python port of [ch-download](https://github.com/alekseylovchikov/ch-download) by [Alekseylovchikov](https://github.com/alekseylovchikov) but has support for current restructuring of the website
