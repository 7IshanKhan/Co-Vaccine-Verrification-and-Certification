Co-Vaccine E-Verification & Certification

Overview:
The E-Vaccine Verification System is a Python console application designed to manage vaccination data efficiently. It supports three types of users: Admin, Vaccinator, and Client. Admin can manage vaccinators, view vaccination records and statistics, and delete records. Vaccinators can log in to add new vaccination records. Clients can verify their vaccination status and generate vaccination certificates.

Features:

Admin:

* Login with credentials (username: admin, password: ADMIN)
* View all vaccination records
* View vaccination statistics with bar and pie chart visualizations
* Delete vaccination records
* Add, view, and delete vaccinator accounts

Vaccinator:

* Login with username and password
* Add new vaccination records (ID, Name, Vaccine, Dose, Date)

Client:

* Verify vaccination status by ID
* Generate vaccination certificate as a text file

Folder Structure:
E-Vaccine-System/
├── main.py
└── modules/
├── **init**.py
├── admin_module.py
├── client_module.py
├── vaccinator_module.py
└── database_module.py

Installation:

1. Clone the repository.
2. Install required Python packages: pandas, numpy, matplotlib
3. Run the system using: python main.py

Usage:

* Start the program by running main.py
* Select your role: Client, Vaccinator, or Admin
* Admin login is required for Admin actions
* Clients can verify their vaccination status and generate certificates
* Vaccinators can log in and add new vaccination records

Dependencies:

* Python 3.x
* pandas
* numpy
* matplotlib

Notes:

* All IDs are stored as strings to ensure correct verification
* Admin can manage both vaccination data and vaccinator accounts securely
* Certificates are generated as simple text files
