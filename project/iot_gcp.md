# How to push data on Google Cloud service

## Create a project on Google Cloud

* Go to [Google Cloud Console web site](https://console.cloud.google.com) and
  create a new project
  * Enter a project name
* You can already report the project ID in the file `config.json`
* Using the top left menu go to **Google Cloud IoT API** and activate the API
* Once the API activated we will create a *registry*. Go to **IoT Core**.
  * Enter an ID and choose a project region
  * You can leave the other fields empty
* You can report the registry ID and the region in the `config.json` file
* Now click on *Devices* (should be on the left of your screen) to create a new
  device
  * Entre a device ID and create the device
  * In your terminal generate a public/private key pair with the following
    commands then jump to the authentication section to add the generated public
    key to the device. You can directly upload the generated file (the public one).
```bash
openssl genrsa -out rsa_private.pem 2048
openssl rsa -in rsa_private.pem -pubout -out rsa_public.pem
```
* You can now report the device ID to the file `config.json`
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
* We need to send some files to the m5Stack. In order to send the data, we need to use the ampy library. On linux/Mac , You can install `ampy` with `sudo pip3 install adafruit-ampy`, on Windows `pip install adafruit-ampy` more info [here](https://github.com/scientifichackers/ampy). Once installed, you need to connect the m5 via cable to your pc, then you need to identify the name of the port to which it is connected. 
* - On windows, open "Device Manager", look for PORTS, then you should see something like (not necessarily identical): "Silicon Labs CP210x USB to UART Bridge (COM5). The port is COM5.
* - On Mac, open "System information", go to USB, you should see something like USB 3.0 Bus, then CP2104 USB to UART Bridge Controller. Note the serial number.
* To send data to the m5 via ampy you need to use the following command: `ampy --port YOUR_PORT_HERE put LOCAL_FILE DESTINATION_FILE`. Examples:
* - `ampy --port /dev/tty.usbserial-025653AD put app_test.py /flash/apps/app_test.py`
* - `ampy --port COM5 put app_test.py /flash/apps/app_test.py`
* You need to send to the m5Stack the following files:
1. TLS certificate (you downloaded it in the step above) in location `/flash`. This needs to be pushed through ampy because of the size of the file. 
2. The micropython file should be placed under `/flash/apps`. For this, you can also directly use flow.m5stack by copy-pasting the code. As an initial test, use simple_cloud_app.py. Then, you can add your code and build your app for the project.


* If everything was done correctly you should see new data on your BigQuery
  table


> Could be useful to debug
> * `sudo screen -L /dev/ttyACM0 115200` command should allow you to see the print
