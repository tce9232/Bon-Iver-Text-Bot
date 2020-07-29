# Bot Iver - The Bon Iver Text Bot

Bot Iver learns how to write lyrics just like Justin Vernon by training over their entire discography. 

## Installation

Clone this repository into a local folder. In the command line, create a conda environment and activate it.

```bash
conda create -n botiver
conda activate -n botiver
```

Then install the required libraries in your environment.

```bash
 conda install --file requirements.txt 
```

## Model Training

In order to start using this app, you either need to train your initial model or [download one I already trained](https://www.dropbox.com/sh/kl0qr3oh63bsi2e/AAA81ClI9km68jQJqE1iwX0Na?dl=0).

### Training your own model:

This option takes a bit more time and computing power. First, if you'd like to configure any variables in the machine learning model, open up and edit the config.yml file in the base folder. Without any edits, here are the original parameters:

```python
create_model:
    data_path: 'data/BonIver.txt'
    model_name : '124M' 
    steps : 70 
    restore_from : 'fresh' 
    run_name : 'run1' 
    print_every : 5 
    sample_every : 10 
    save_every : 50

```

After you're comfortable with the parameters, navigate to the base folder in the command line. This folder should contain app.py. 

Then in order to start training, run the following code in the command line:

```bash
make train
```

The training could take a while, but will ultimately result in model files in both the models and checkpoint folders. 

### Using my model:

In order to skip the training step, you can download the models and checkpoint folders directly from these Dropbox folders:
* The [124M model](https://www.dropbox.com/sh/ixpjn1ey1xnpugc/AACnduiAlvHbiW9QY3XKIm1Da?dl=0) goes in the models folder
* The [run1 model](https://www.dropbox.com/sh/0pzwdql6gewlron/AAAqavneijW6etF_bpD3hYnYa?dl=0) goes in the checkpoint folder

Unzip these folders in their respective folders.

## Twilio Setup

You'll need to set up a [Twilio](https://www.twilio.com/) account to interact with the text bot. Once you create your free account, create and name a new project.

After verifying your phone number, you can skip right to your Twilio dashboard. Here, you need to click the red "Get a trial number" button. This will give you your own Twilio trial phone number to use for this project. 

## Start Local Server

You need to start a server on your local computer in order for Twilio to interact with your model. To do this, navigate to the base folder in the command line and run

```bash
make server
```

Then open up another command line and run

```bash
make ngrok
```

This should cause your window to go black with white text. Copy the forwarding address from here (it should end in ngrok.io). We need to tell Twilio to forward messages to this address. 

Go to your Twilio dashboard and click on "Usage". Then your project name, then "Go to Phone Numbers". Click on the hyperlink of your phone number and scroll down to the bottom where it says "Messaging".

Paste the forwarding address in the webhook address for "a message comes in". Add "/sms" to the end of the address. Save the changes.

## Test the Connection

At this point, your connection should be set up and you should be able to text your Twilio phone number any prefix you want and receive back original Bot Iver lyrics that start with that prefix.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
