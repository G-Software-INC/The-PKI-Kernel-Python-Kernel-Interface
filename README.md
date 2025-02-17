PKI Kernel Documentation
Overview
The PKI Kernel (Python Kernel Interface) serves as a foundational tool for developers creating Python-based pseudo operating systems. It provides a stable, low-level interface to the filesystem, facilitating operations that Python cannot handle natively.

Installation
To use the PKI Kernel, ensure you have Python 3 installed. The kernel can be included in your project by copying the pki_kernel.py file into your project directory.

Core Features
File Operations: Open, read, write, close, seek, rename, and delete files.
Directory Operations: List directory contents and retrieve file statistics.
Error Handling: Custom error handling through the PKIError exception class.
Library Integration: Optionally loads a C shared library for advanced operations.
Usage
To use the PKI Kernel in your project, follow these steps:

Importing the Kernel: Start by importing the kernel into your project.

Creating an Instance: Instantiate the PKI Kernel.

File Operations:

Open a file using the appropriate flags.
Read from or write to the file using file descriptors.
Close the file when done.
Seek to different positions within the file as needed.
Directory Operations:

List the contents of a directory.
Retrieve statistics for a specific file.
Renaming and Deleting Files: Rename or delete files as required.

Error Handling
The PKI Kernel uses a custom exception class PKIError to handle errors that may occur during file operations. This allows developers to implement robust error handling in their applications.

Subsystem Calls
The PKI Kernel interacts with the filesystem through several subsystem calls, including:

pki_open: Opens a file and returns its file descriptor.
pki_read: Reads data from the file descriptor.
pki_write: Writes data to the file descriptor.
pki_close: Closes the file descriptor.
pki_seek: Changes the file pointer position.
pki_list_directory: Lists contents of a directory.
pki_stat_file: Retrieves statistics of a file.
pki_rename: Renames a file.
pki_delete: Deletes a file.
Conclusion
The PKI Kernel provides a robust and efficient interface for managing file operations within Python pseudo operating systems. By utilizing this kernel, developers can focus on building their OS functionality without worrying about low-level filesystem interactions.
