# 🦠 Educational ILOVEYOU Worm Simulation

> **⚠️ STRICT WARNING**  
> This project is a **fully simulated, sandboxed model** of the infamous ILOVEYOU computer worm (2000).  
> It is intended **exclusively for cybersecurity education, malware analysis training, and self‑defence learning**.  
> **Never run this code outside an isolated, air‑gapped virtual machine or the provided sandbox directory.**  
> By using this software, you agree to use the knowledge responsibly. The author assumes no liability for misuse.

![ILOVEYOU Virus](https://via.placeholder.com/800x200?text=ILOVEYOU+Worm+Simulation+Educational+Demo)  
*[Add an actual banner image here – e.g., a screenshot of the simulation running, or a diagram of the worm's lifecycle]*

---

## 📖 Table of Contents
- [🦠 Educational ILOVEYOU Worm Simulation](#-educational-iloveyou-worm-simulation)
  - [📖 Table of Contents](#-table-of-contents)
  - [📚 Introduction](#-introduction)
  - [🎯 What This Simulation Does](#-what-this-simulation-does)
  - [🚨 Disclaimer](#-disclaimer)
  - [🧠 How the Original Worm Worked](#-how-the-original-worm-worked)
  - [⚙️ Architecture of the Simulation](#️-architecture-of-the-simulation)
  - [📁 Files \& Project Structure](#-files--project-structure)
  - [🛠️ Setup \& Requirements](#️-setup--requirements)
  - [▶️ Usage – Running the Simulation](#️-usage--running-the-simulation)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. (Optional) Inspect the code](#2-optional-inspect-the-code)
    - [3. Run the simulation](#3-run-the-simulation)
    - [4. Observe the output](#4-observe-the-output)
    - [5. Check the sandbox folder](#5-check-the-sandbox-folder)
  - [📸 Interactive Walkthrough (with Screenshots)](#-interactive-walkthrough-with-screenshots)
    - [Stage 1: File Overwriting](#stage-1-file-overwriting)
    - [Stage 2: Email Propagation (Simulated)](#stage-2-email-propagation-simulated)
    - [Stage 3: Password Theft (Simulated)](#stage-3-password-theft-simulated)
    - [Stage 4: Registry Persistence (Simulated)](#stage-4-registry-persistence-simulated)
  - [🔧 Customisation \& Safe Experiments](#-customisation--safe-experiments)
  - [📊 Educational Objectives](#-educational-objectives)
  - [🔒 Safety Features Explained](#-safety-features-explained)
  - [📄 Complete Simulation Code](#-complete-simulation-code)
  - [❓ Frequently Asked Questions](#-frequently-asked-questions)
  - [📚 References \& Further Reading](#-references--further-reading)
  - [📝 License](#-license)

---

## 📚 Introduction
In May 2000, the **ILOVEYOU worm** (also known as VBS/LoveLetter) spread across millions of computers worldwide, causing an estimated **$10–15 billion** in damages. It arrived as an email with the subject “ILOVEYOU” and an attachment named `LOVE-LETTER-FOR-YOU.txt.vbs`. Because Windows hid file extensions by default, many users saw only a harmless `.txt` file, not a dangerous Visual Basic Script. Once opened, the worm overwrote personal files, stole passwords, and emailed itself to every contact in Microsoft Outlook.

This repository contains a **Python‑based simulation** that recreates the worm’s behaviour in a **completely controlled environment**. No real emails are sent, no system files are altered, and all destructive actions are redirected into a sandbox folder. The goal is to let you **study the mechanics of the attack** and understand why such simple malware was so devastating – without any risk.

---

## 🎯 What This Simulation Does
| Stage               | Original Worm Behaviour                                      | Simulation Behaviour (Safe)                                                                 |
|---------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **File Overwriting** | Overwrote `.jpg`, `.mp3`, `.doc`, `.vbs` etc. with its own code | Overwrites only files inside `./iloveyou_sandbox/`. Original files are backed up as `.bak` |
| **Email Spread**    | Used Outlook COM to send itself to every contact              | Prints the email details to the console; **does not send any real email**                   |
| **Password Theft**  | Tried to read cached passwords and sent them to an attacker   | Prints fake stolen credentials to the terminal                                             |
| **Persistence**     | Added a registry key to run on startup                        | Prints the registry key it *would* add                                                     |

All dangerous actions are **deactivated by default** and can be toggled on/off with simple Boolean flags.

---

## 🚨 Disclaimer
**This project is for authorised security research and education ONLY.**  
- Do **not** modify the code to target real file systems, email servers, or networks.  
- Do **not** distribute the code in a manner that could cause harm.  
- The author(s) **disclaim all responsibility** for any damage caused by misuse.  

If you are learning about malware, always work inside an **isolated virtual machine** with no network access. The provided sandbox makes it safe, but **always verify the `TEST_FOLDER` path** before execution.

---

## 🧠 How the Original Worm Worked
1. **Arrival** – Email with VBS attachment disguised as a love letter.
2. **Execution** – Victim double‑clicks the attachment. Windows Script Host runs the VBS.
3. **Propagation** – Worm uses Outlook’s COM object to iterate through all contacts and send a copy of itself.
4. **Destruction** – Searches local and network drives for files with certain extensions, overwrites them with a copy of the worm (rendering them useless).
5. **Theft** – Tries to steal dial‑up passwords or cached internet credentials.
6. **Persistence** – Modifies registry so the worm runs again when the computer starts.

The simulation follows the same logical flow but replaces real actions with harmless printouts and sandboxed file operations.

---

## ⚙️ Architecture of the Simulation
