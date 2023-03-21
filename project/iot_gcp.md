# How to push data on Google Cloud service

## Create a project on Google Cloud

* Go to [Google Cloud Console web site](https://console.cloud.google.com) and
  create a new project
  * Enter a project name
* Take note of the project-id
* Using the top left menu go to **Google Cloud IoT API** and activate the API
* Once the API activated we will create a *registry*. Go to **IoT Core**.
  * Enter an ID and choose a project region
  * You can leave the other fields empty
* Take note of the registry id
* In the terminal of your pc generate a public/private key pair with the following
    commands then jump to the authentication section to add the generated public
    key to the device. You can directly upload the generated file (the public one).
* - On Mac/linux:
```
openssl genrsa -out rsa_private.pem 2048
openssl rsa -in rsa_private.pem -pubout -out rsa_public.pem
```
* - On Windows:
```
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
# Don't add passphrase
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub
```
* Now click on *Devices* (should be on the left of your screen) to create a new
  device
  * Entre a device ID and create the device. Take note of the device id. 
  * In "Authentication" Either upload or copypaste the file with the PUBLIC key
  
* Going back to the main page of our project go to the **BigQuery** section (top
  left menu)
  * Clicking on the three dots next to your project ID in the explorer section
    allow you to create a new dataset
  * Enter a dataset ID and a location
  * Clicking on the three dots of our new dataset you can create a new table
    * Enter a table name
    * In the Schema part add a *data* field and leave it as a string
    * Confirm 
* Now select **Pub/Sub** section for the top left menu
* Create a new topic and provide a topic ID
* Now create a new subscription (you can use the default subscription)
  * Enter a subscription ID 
  * For the Delivery type, select *write to BigQuery* and select the dataset and
    table you created before 
    * Note: The table name field does not have autocompletion
  * Then create the subscription
    * In case of an authorisation error : copy the bold red link and go to **IAM
      and Admin** section using the top left menu
    * Click on the Grant Access button; under new principal paste the red text
      and under role select *BigQuery Data Editor* 
    * Save your changes and retry to create the subscription
* Going back to the **Iot Core section**, select your registry and click on *add or
  edit topics*
  * Under *Cloud Pub/Sub topics* select the new created one
  * Finally click on update

## Use the micropython cloud Class

* To use the cloud class you need to download SSL/TLS certificate downloaded
  [here](https://pki.goog/roots.pem). We will need it in a few minutes.
* Substitute the path to the private key you generated and run the following command to get a jwt: 
  `python3 jwt_create.py PATH/TO/RSA_PRIVATE.PEM`
  You will need to insert the jwt in the app file (see code below).
* In the microython file, you need to fill the first few lines with the IDs you annotated during the procedure, your wifi, and the jwt.
* We need to send some files to the m5Stack. In order to send the data, we need to use the ampy library. On linux/Mac , You can install `ampy` with `sudo pip3 install adafruit-ampy`, on Windows `pip install adafruit-ampy` more info [here](https://github.com/scientifichackers/ampy). Once installed, you need to connect the m5 via cable to your pc, then you need to identify the name of the port to which it is connected. 
* - On windows, open "Device Manager", look for PORTS, then you should see something like (not necessarily identical): "Silicon Labs CP210x USB to UART Bridge (COM5). The port is COM5.
* - On Mac, open "System information", go to USB, you should see something like USB 3.0 Bus, then CP2104 USB to UART Bridge Controller. Note the serial number.
* To send data to the m5 via ampy you need to use the following command: `ampy --port YOUR_PORT_HERE put LOCAL_FILE DESTINATION_FILE`. The following are EXAMPLES to show what the ampy commands look like, they are not exactly the ones you need now:
* - `ampy --port /dev/tty.usbserial-025653AD put app_test.py /flash/apps/app_test.py`
* - `ampy --port COM5 put app_test.py /flash/apps/app_test.py`
* You need to send to the m5Stack the following file:
1. TLS certificate (you downloaded it in the step above) in location `/flash`. This needs to be pushed through ampy because of the size of the file. The command should be something like:
- `ampy --port YOUR_PORT put roots.pem`


* To send the micropython file, you have 2 possibilities: either sending it with ampy and placing it under `/flash/apps`, or copy-pasting the code on flow.m5stack. As an initial test, use `simple_cloud_app.py`. Then, you can add your code and build your app for the project. If you choose ampy, the command should be something like:
* - `ampy --port YOUR_PORT put simple_cloud_app.py /flash/apps/simple_cloud_app.py`
> I recommend the first route: copy-pasting the code on flow, as it's simpler and faster. 



* If everything was done correctly you should see new data on your BigQuery
  table
  
> PAY ATTENTION: the jwt expires. The duration of validity can be specified in the jwt_create.py file. The current value is set at 2 hours.
> OTHER NOTE: if ampy is not able to use the serial port, you will need to install a driver from here:
> https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads


> Possible tricks to do debugging
> * what's explained in (this video)[https://www.youtube.com/watch?v=V67MY-1ccqM]
> * using try, except in your code
> * using the screen command: `sudo screen -L /dev/ttyACM0 115200` command should allow you to see what you print
