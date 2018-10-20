## A Simple Server with Python Flask

This is a simple skeleton Flask server project that works on any of the devices supported by [resin][resin-link].

This project simply serves up `"Hello World!"` on port `:80` of your resin device.

And the temperature from the Sensor Hat in the `/temp` route.

To get this project up and running, you will need to signup for a resin account [here][signup-page] and set up a device, have a look at our [Getting Started tutorial][gettingStarted-link]. Once you are set up with resin, you will need to clone this repo locally:
```
$ git@github.com:vperezb/simple-server-python.git
```
Then add your resin application's remote:
```
$ cd simple-server-python
$ git remote add resin <USERNAME>@git.resin.io:<USERNAME>/<APPNAME>.git
```
and push the code to the newly added remote:
```
$ git push resin master
```
or
```
$ git push resin master --force
```
It should take a few minutes for the code to push. While you wait, lets enable device URLs so we can see the server outside of our local network. This option can be toggled on the device summary page, pictured below or in the `Actions` tab in your device dashboards.

![Enable device URL](/img/enable-public-URLs.png)

Once the device is updated, you should see this in your logs:
![log output](/img/log-output.png)

Then in your browser you should be able to open the device URL and see the message "Hello World!".


[resin-link]:https://resin.io
[signup-page]:https://dashboard.resin.io/login
[gettingStarted-link]: https://docs.resin.io/learn/getting-started/raspberrypi3/python/
