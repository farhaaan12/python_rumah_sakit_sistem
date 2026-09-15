# Python CRUD Application for Healthcare System

A comprehensive Python CLI application for managing Patient Data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the Healthcare industry (Hospitals, Clinics, or Medical Centers), specifically addressing the need to manage patient registration and medical queue data efficiently. Accurate patient record management plays a crucial role in ensuring smooth medical administrative processes and timely care delivery.

**Benefits:**

* Improved patient data accuracy and consistency through strict input validation
* Streamlined patient registration and lookup processes
* Reduced administrative errors during patient check-in
* Efficient searching mechanism supporting both Patient ID and partial Name matching

**Target Users:**

This application is designed for Medical Receptionists, Clinic Administrators, and Healthcare Support Staff to facilitate their daily tasks related to patient registration, updates, and record retrieval.

## Features

* **Create (Tambah Data Pasien):**
    * Add new patient entries with auto-generated incremental IDs.
    * Essential input fields: `Nama`, `Umur`, `Keluhan`, `No HP`, and `Alamat`.
    * Strict input validation rules to prevent empty fields, non-numeric age, or invalid age values (≤ 0).
    * Confirmation prompt before saving new data.
* **Read (Daftar & Cari Data Pasien):**
    * Display all registered patients in a structured tabular format.
    * Dynamic search functionality (`filter_search`) supporting both exact ID lookups and partial case-insensitive Name searching.
    * Smart disambiguation: Displays candidate lists if multiple patients match a search keyword.
    * Interactive retry mechanism allowing users to search again if no records are found without returning to the main menu.
* **Update (Ubah Data Pasien):**
    * Search and modify existing patient details (`Nama`, `Umur`, `Keluhan`, `No HP`, `Alamat`).
    * Clear preview of current data before requesting updated inputs.
    * Save confirmation to prevent accidental overwrites.
* **Delete (Hapus Data Pasien):**
    * Safely remove patient records after fetching via the smart search filter.
    * Displays target patient details for verification before final deletion confirmation.

## Installation

1. **Prerequisites:**
    * Python 3.x (Python 3.8 or higher recommended)
    * Built-in standard library modules (No third-party packages required)

2. **Installation:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/python-rumah-sakit-sistem.git
    cd python-rumah-sakit-sistem
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations Guide:**
    * **1. Daftar Pasien:** View all patient records in a clean table format.
    * **2. Tambah Data Pasien:** Register a new patient by entering their personal details and primary complaints.
    * **3. Cari Data Pasien:** Search for a patient by entering their ID or Name (supports partial name input).
    * **4. Ubah Data Pasien:** Search for a patient, view their current record, and update their information.
    * **5. Hapus Data Pasien:** Search for a patient and confirm removal from the system.
    * **6. Keluar:** Safely exit the application.

## Data Model
This project utilizes an in-memory `list` of `dictionaries` (`pasien_list`) to represent patient records. The following fields are stored for each entry:

* `id_pasien`: (Integer) - Unique identifier automatically generated for each patient.
* `nama`: (String) - Full name of the patient.
* `umur`: (Integer) - Age of the patient in years (must be > 0).
* `keluhan`: (String) - Medical complaint or symptoms reported by the patient.
* `no_hp`: (String) - Active phone number for patient contact.
* `alamat`: (String) - Residential address or city of origin.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request or submit an issue if you encounter any problems or have suggestions for improvements.