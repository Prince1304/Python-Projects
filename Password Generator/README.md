# Password Generator 🔐

A secure, interactive Python-based command-line tool that generates highly secure, randomized passwords. The application ensures that every generated password adheres to strict strength criteria before presenting it to the user.

## 🌟 Features

* **Custom Length:** Allows users to specify the exact length of the password (minimum 4 characters).
* **Strict Security Verification:** Automatically filters out weak passwords. Every accepted password is guaranteed to contain at least:
    * One lowercase letter
    * One uppercase letter
    * One numeric digit
    * One special character (`@`, `#`, `$`, `%`, `&`)
* **Regeneration Loop:** Generates a new password instantly at the press of a button, or allows you to exit smoothly.
* **Visual Polish:** Clean, easy-to-read command-line interface with stylized borders and standard security reminders.

--- 

## 🛠️ How It Works

1. **Initialization:** The program sets up the generator and prompts you for a password length.
2. **Generation:** It randomly picks characters from a combined pool of upper/lowercase letters, digits, and select special characters.
3. **Validation:** It runs a criteria check on the generated string. If it lacks any of the required character types, it discards it and silently creates another until a secure one is found.
4. **User Action:** Displays the valid password. You can then press `Enter` to generate another one or type `S` to safely exit the application.

---

## 🚀 Getting Started

### Prerequisites

You only need **Python 3.x** installed on your system. This project relies entirely on Python's built-in libraries (`random`, `string`, and `time`), so no external `pip` installations are required.

### Installation & Running

1. Clone or download the repository files.
2. Save the script as `MyPasswords.py`.
3. Open your terminal or command prompt, navigate to the directory, and run:

```bash
python MyPasswords.py
```
## 🖥️ Output Preview
```
**********************************************************************
                      Welcome To Password Maker                       
**********************************************************************
Initializing Password Generator ...
Setup is completed.
**********************************************************************
Enter the length of the password you would like to generate: 3
**********************************************************************
Password Length must be greater than 4
**********************************************************************
Enter the length of the password you would like to generate: 
Please enter a valid Digit length.
**********************************************************************
Enter the length of the password you would like to generate: 12
************************************************----------------------
Generating password ...
----------------------------------------------------------------------
 Do Not Share  Do Not Share  Do Not Share  Do Not Share  Do Not Share 
----------------------------------------------------------------------
 1.                          kR9#mP2$vXqA                          
----------------------------------------------------------------------
 Do Not Share  Do Not Share  Do Not Share  Do Not Share  Do Not Share 
----------------------------------------------------------------------

Enter 'S' for stop else Press 'Enter' For New Password:

New Password Arrive after 15 Seconds.. 

----------------------------------------------------------------------
 Do Not Share  Do Not Share  Do Not Share  Do Not Share  Do Not Share 
----------------------------------------------------------------------
 2.                          5&bZ!wL1pQ#m                          
----------------------------------------------------------------------
 Do Not Share  Do Not Share  Do Not Share  Do Not Share  Do Not Share 
----------------------------------------------------------------------

Enter 'S' for stop else Press 'Enter' For New Password: s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prince Kyada - 'Your Security is Our Responsibility!!'
Thanks for using Password Generator!!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
