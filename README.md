# Advanced_Encryption_Tool

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: MOHAMMED ZUBAIR UDDIN ZAMEER

*INTERN ID*: CITSOD850

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION

The **Advanced Encryption Tool** is a secure and user-friendly application built using Python that allows users to encrypt and decrypt files using the AES-256 encryption standard. AES-256 (Advanced Encryption Standard with a 256-bit key) is widely regarded as one of the most secure symmetric encryption algorithms currently available, and it is used by governments, banks, and cybersecurity professionals to protect sensitive data. This tool provides a graphical interface that simplifies the process of encrypting and decrypting files, making high-level security accessible to non-technical users. The interface consists of a file path input field, a password entry field, and two buttons for encryption and decryption actions. Behind the scenes, the application uses the `pycryptodome` library to handle AES operations, ensuring cryptographic security, and the `tkinter` library to deliver a clean and intuitive graphical user interface (GUI).

When the user selects a file and enters a password, the tool generates a secure 256-bit key from the password using a Key Derivation Function (KDF) with salt and PBKDF2, which prevents brute-force and dictionary attacks. During encryption, the tool creates a random Initialization Vector (IV) for added security and ensures that the file is padded to meet AES block size requirements. The encrypted file is then saved with the original filename plus an `.enc` extension, and all cryptographic parameters such as the salt and IV are stored in the output to enable correct decryption later. When decrypting, the tool reads the salt and IV from the encrypted file, regenerates the key from the provided password, and securely restores the original file content. If the wrong password is entered, the decryption will fail gracefully, preserving data confidentiality.

This project demonstrates not only cryptographic best practices but also proper application design. It separates the logic of encryption and decryption from the interface layer, making the code modular and maintainable. The tool is highly portable and can run on any system that has Python 3.6+ installed. The GUI makes it ideal for students, researchers, and small businesses that need a lightweight yet secure encryption solution without the complexity of command-line tools or the cost of commercial software. Additionally, the tool includes checks for user errors, such as empty input or invalid file paths, and provides feedback through simple popup messages.

In summary, this Advanced Encryption Tool offers robust file protection using AES-256 encryption wrapped in an easy-to-use graphical interface. It bridges the gap between powerful cryptography and user accessibility, empowering individuals to take control of their data security. The project highlights key aspects of secure programming, including proper key management, encryption standards, GUI design, and usability. With real-world applications in securing personal documents, academic research, financial records, and more, this tool exemplifies how strong encryption practices can be implemented in an approachable and efficient manner using Python.

## OUTPUT

<img width="620" height="288" alt="Screenshot 2025-07-19 150743" src="https://github.com/user-attachments/assets/501d9309-5e86-4986-949e-e453304e682d" />

<img width="1005" height="500" alt="Screenshot 2025-07-19 150825" src="https://github.com/user-attachments/assets/b9845af8-22d2-4dad-97d9-737c32d139e8" />

<img width="1002" height="490" alt="Screenshot 2025-07-19 150849" src="https://github.com/user-attachments/assets/d1c99d78-7a8a-4b3b-82c0-55070842d9c1" />



