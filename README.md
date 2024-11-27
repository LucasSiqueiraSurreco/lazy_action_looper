
# **Lazy Action Looper**

Lazy Action Looper is a Python-based automation tool that records and replays your keyboard and mouse actions. It has been developed and tested on **Arch Linux**.

## **Features**
- Record keyboard and mouse movements.
- Replay the recorded actions multiple times in a loop.
- Save recorded events in a JSON file for later use.

---

## **Requirements**
- **Python 3.6+**
- **pip** (Python package installer)

---

## **Dependencies**
Install the following Python dependencies using `pip`:

```bash
pip install pynput
```

---

## **Setting Up the Environment**

### **1. Create a Python Virtual Environment**

To keep the project dependencies isolated, create a virtual environment:

```bash
python -m venv ~/lazy_action_looper_env
```

### **2. Activate the Virtual Environment**

Activate the environment with the following command:

```bash
source ~/lazy_action_looper_env/bin/activate
```

### **3. Install Dependencies in the Virtual Environment**

While the virtual environment is active, install the required dependencies:

```bash
pip install pynput
```

### **4. Deactivate the Environment (Optional)**

After you finish using the environment, you can deactivate it:

```bash
deactivate
```

---

## **How to Use**

### **1. Record Actions**

Run the script to record your mouse and keyboard actions:

```bash
python record_actions.py
```

Instructions:
- Perform your mouse and keyboard actions.
- Press `ESC` to stop the recording.
- The recorded actions will be saved in a file named `events_log.json`.

### **2. Replay Actions**

Run the script to replay the recorded actions:

```bash
python replay_actions.py
```

Instructions:
- The program will ask how many times you want to repeat the recorded actions.
- Enter the number of loops and watch the actions replay.

---

### **Notes**
This tool was developed and tested on **Arch Linux**. It should work on other Linux distributions as well, but additional testing may be required.
