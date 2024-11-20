# LIGHTNING-ALERTING-SYSTEM-USING-IOT

## About the Project  
This project helps save lives by providing early warnings about lightning. It uses data from **APSDMA** to detect areas where lightning might happen and alerts people with **phone calls** instead of text messages, making it more effective, especially for those who can’t read. A **buzzer** is also used to alert nearby people and animals.  

---

## How It Works  
1. APSDMA provided a CSV file with:  
   - Lightning possibility (`0` or `1`).  
   - Dummy Phone numbers in the affected areas.  
2. When lightning is detected (`1`), the system:  
   - **Calls the phone numbers** in the file.  
   - Sounds a **buzzer** for nearby alerts.  

---

## Note  
- For security reasons, the **CSV file is not shared** here.  
- We tested the system with our **own phone numbers** for the project. No actual calls were made to people in real areas.  

---

## What You Need  
- Raspberry Pi Pico  
- GSM SIM 900A module  
- Buzzer  
- APSDMA CSV file  (make your own file, with a binary column )

---

## Why It’s Useful  
- **Quick Alerts**: Phone calls ensure better communication than text messages.  
- **Inclusive**: Helps even illiterate people.  
- **Animal Safety**: Buzzer alerts nearby livestock too.  

---

![image](https://github.com/user-attachments/assets/83f42d7a-c7dc-47ba-9883-7fdbf965f157)


## Acknowledgments  
Thanks to **APSDMA** for their support and the data provided.  

--- 

## License  
This project is open-source under the MIT License.  
