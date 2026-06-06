#!/usr/bin/env python3
"""
EDUCATIONAL ILOVEYOU WORM SIMULATION
-------------------------------------
This script mimics the behaviour of the ILOVEYOU virus (2000) for learning purposes.
IT DOES NOT SEND REAL EMAILS OR OVERWRITE SYSTEM FILES.
All actions are either simulated or restricted to a safe test folder.
"""

import os
import shutil
import random
import string

# ================= CONFIGURATION =================
# SAFETY: ONLY files inside this folder will be touched.
TEST_FOLDER = "./iloveyou_sandbox"
SIMULATE_EMAIL = True          # Set to True to just print email actions
SIMULATE_PASSWORD_STEAL = True  # Set to True to simulate password theft
OVERWRITE_EXTENSIONS = ['.txt', '.jpg', '.mp3', '.doc', '.vbs', '.js']

# ================= CORE FUNCTIONS =================

def prepare_sandbox():
    """Create a test environment with dummy files."""
    if not os.path.exists(TEST_FOLDER):
        os.makedirs(TEST_FOLDER)
    print(f"[*] Sandbox created at {TEST_FOLDER}")

    # Create some dummy files to "infect"
    for i, ext in enumerate(OVERWRITE_EXTENSIONS):
        fname = os.path.join(TEST_FOLDER, f"test_file_{i}{ext}")
        with open(fname, 'w') as f:
            f.write(f"Original content of {fname}\n")
    print("[*] Dummy files created for demonstration.")

def worm_self_copy():
    """Return the content of the worm (its own code)."""
    with open(__file__, 'r') as f:
        return f.read()

def overwrite_files():
    """
    Simulate overwriting files: replace their content with the worm's code.
    In the simulation, we copy the original to a .bak file first (safe practice).
    """
    worm_code = worm_self_copy()
    for root, dirs, files in os.walk(TEST_FOLDER):
        for file in files:
            # Check extension (case-insensitive)
            _, ext = os.path.splitext(file)
            if ext.lower() in OVERWRITE_EXTENSIONS:
                full_path = os.path.join(root, file)
                # Backup original before overwriting (educational safety)
                backup_path = full_path + '.bak'
                shutil.copy2(full_path, backup_path)
                # Overwrite with worm code
                with open(full_path, 'w') as f:
                    f.write(worm_code)
                print(f"[!] OVERWRITTEN: {full_path} (backup: {backup_path})")

def simulate_email_propagation():
    """
    Simulate sending emails via Outlook (like the original).
    In reality, this only prints what it would do.
    """
    print("\n[*] Simulating email propagation via Outlook...")
    contacts = ["alice@example.com", "bob@example.com", "carol@example.com"]
    subject = "ILOVEYOU"
    body = "kindly check the attached LOVELETTER coming from me."
    attachment_name = "LOVE-LETTER-FOR-YOU.txt.vbs"

    for contact in contacts:
        print(f"    -> To: {contact}")
        print(f"       Subject: {subject}")
        print(f"       Body: {body}")
        print(f"       Attachment: {attachment_name} (contains worm code)")
        # In a real attack, the worm would use the Outlook COM object:
        # outlook = win32com.client.Dispatch("Outlook.Application")
        # mail = outlook.CreateItem(0)
        # mail.To = contact
        # mail.Subject = subject
        # mail.Body = body
        # mail.Attachments.Add(attachment_name)
        # mail.Send()
    print("[*] Email simulation complete (no real emails sent).\n")

def simulate_password_steal():
    """
    Simulate stealing cached passwords (e.g., from Internet Explorer).
    Only prints what it would attempt.
    """
    print("[*] Simulating password theft...")
    # The original virus looked for stored passwords in the registry
    # or tried to read cached credentials. We'll just print.
    print("    -> Attempting to read Windows Credential Manager...")
    print("    -> Searching for stored internet passwords...")
    # Dummy "stolen" data
    fake_passwords = ["user:admin / pass:12345", "user:john / pass:iloveyou"]
    print("    [!] Stolen passwords (dummy):")
    for pwd in fake_passwords:
        print(f"        {pwd}")
    print("[*] Password theft simulation complete.\n")

def add_to_registry():
    """
    Simulate adding a registry key to run the worm on startup
    (the original did this to persist). Only prints.
    """
    print("[*] Simulating registry persistence...")
    print("    -> Would add to HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    print("       Name: MSKernel32")
    print("       Value: wscript.exe C:\\path\\to\\worm.vbs")
    print("[*] Registry simulation complete.\n")

def main():
    print("=" * 60)
    print(" EDUCATIONAL ILOVEYOU WORM SIMULATION")
    print(" No real damage will be done.")
    print("=" * 60)

    prepare_sandbox()

    # Step 1: Overwrite files in test folder
    print("\n>>> Stage 1: File overwriting (in sandbox)")
    overwrite_files()

    # Step 2: Email propagation
    print("\n>>> Stage 2: Email propagation")
    if SIMULATE_EMAIL:
        simulate_email_propagation()

    # Step 3: Password stealing
    print("\n>>> Stage 3: Password theft")
    if SIMULATE_PASSWORD_STEAL:
        simulate_password_steal()

    # Step 4: Registry persistence (original also did this)
    print("\n>>> Stage 4: Registry persistence")
    add_to_registry()

    print("\n[*] Simulation finished. Check the sandbox folder for overwritten files.")
    print("[*] Remember: This code is for learning ONLY. Never use it maliciously.")

if __name__ == "__main__":
    main()