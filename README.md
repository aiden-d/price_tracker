# Price Tracker
 
This is a simple script which can be self-hosted to track price changes on your favorite websites, storing the current value and emailing you if the value gets updated.

At the moment basic knowledge of HTML and using Chrome Dev tools is required. But will be updated to become more user friendly in a later feature version.

# Installation

Clone the repo

```bash

git clone git@github.com:aiden-d/price_tracker.git

```

Enter the directory

``` bash

cd price_tracker

```

Edit `checker.py` to include a Gmail email and password (make sure to create a Gmail app password) to send the mails.

# Usage

Setup a cron job for `checker.py`.

Run `create_tracker` and fill in the relevant info for the HTML layout of the price field you would like to track.