# 🔋 Battery Alert Notifier (Windows Only)

A Python script that monitors your laptop battery and sends **Windows notifications** when the battery reaches specific levels (5%, 10%, 20%, 30%, 40%, 50%).  

This script **only works on Windows** using `plyer.notification`.

---

## 🚀 Features
👉 **Battery level alerts** at different percentages  
👉 **Works on Windows 10 & 11**  
👉 **Runs in the background**  
👉 **Automatic startup using Task Scheduler**  

---

## 📥 Installation

### **1️⃣ Install Python (If Not Installed)**
Ensure you have Python **3.6+** installed. Download from:  
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

### **2️⃣ Clone This Repository**
```sh
git clone https://github.com/hxz456/battery-alert-notifier
cd battery-alert-notifier
```

### **3️⃣ Manual Run**
```sh
python main.py
```
This will run the script until the terminal is closed. When the terminal is closed, the script will stop running.

OR

### **3️⃣ Automatic Setup Background Run**

## Follow The Below Steps

### **Step 1: Find Python's Path**
Open **Command Prompt (cmd)** and run:
```sh
where python
```
Copy the path of `python.exe`, for example:  
`C:\Users\YourUser\AppData\Local\Programs\Python\Python39\python.exe`

### **Step 2: Open Task Scheduler**
1. Press `Win + R`, type **`taskschd.msc`**, and hit **Enter**.
2. In the left panel, right-click **Task Scheduler (Local)** and choose **Create Basic Task**.

### **Step 3: Configure the Task**
1. **Name the task**: Enter a name like `Battery Notifier` and click **Next**.
2. **Trigger**: Select **Daily**, click **Next**, set the start time, and click **Next** again.
3. **Action**: Choose **Start a Program** and click **Next**.

### **Step 4: Set Up the Python Script Execution**
- **Program/script**: Paste the path of `python.exe` (found in Step 1).
- **Add arguments (optional)**: Enter the full path to your script , for example : 
  `C:\Users\YourUser\battery-alert-notifier\main.py`
- **Start in (optional)**: Enter the folder where the script is located , for example :  
  `C:\Users\YourUser\battery-alert-notifier`

### **Step 5: Configure the Trigger**
1. **Begin the task**: Select **On a schedule**.
2. **Select Daily** and set:
   - **Start date and time**: `2/20/2025 11:20:15 AM`
   - **Recur every**: `1 day`
3. **Advanced settings**:
   - **Repeat task every** `5 minutes` for a duration of `1 day`.
   - Ensure **Enabled** is checked.

### **Step 6: Finish and Test**
1. Click **Finish**.
2. In Task Scheduler, find your task under **Task Scheduler Library**.
3. Right-click the task and select **Run** to test.

Now, your script will run automatically in the background at the scheduled time! 🚀

---

## ⚠️ Notes
- If the script doesn’t run, try enabling **"Run with highest privileges"** in the task properties.
- To stop the script from running automatically, delete the task from Task Scheduler.

Happy Coding! 🎉
