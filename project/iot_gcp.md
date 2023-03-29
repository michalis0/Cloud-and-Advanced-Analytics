# How to push data on Google Cloud service

Click [here](https://www.youtube.com/watch?v=PmXZ08tknxM) for the video tutorial.

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

* Go to [this link](https://colab.research.google.com/drive/16X6q78X_r_gdjOi-2Dr5vRV905hrTvHp?usp=sharing). Go to File -> Save a copy in drive. On the left panel, click on the folder icon and then drag and drop your private key there. In the second cell of the notebook, change the private_key_file to be the name of your private key, and the project_id to be your project id. Run all cells and take note of the ID. Pay attention: you'll need to re-do this when the jwt expires! (I set 1000 minutes validity, which is 16hour)
* In the microython file (simple_cloud_app.py), you need to fill the first few lines with the IDs you annotated during the procedure, your wifi, and the jwt you've just created.
* Copy-paste the micropython code to flow and run.

* If everything was done correctly you should see new data on your BigQuery
  table
  
> PAY ATTENTION: the jwt expires. The duration of validity can be specified in the Colab notebook, inside "timedelta"

> PS: if you are looking for the old version, where I was suggesting to use ampy, look into the "legacy" folder


> Possible tricks to do debugging
> * what's explained in [this video](https://www.youtube.com/watch?v=V67MY-1ccqM)
> * using try, except in your code
> * using the screen command: `sudo screen -L /dev/ttyACM0 115200` command should allow you to see what you print
