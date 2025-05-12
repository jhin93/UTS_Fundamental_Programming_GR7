# UTS_Fundamental_Programming_GR7

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project was developed in **Python**, well-suited for both CLI and GUI (using a library like Tkinter for the GUI). The structure assumes a single project directory containing both CLIUniApp and GUIUniApp, with shared model classes to ensure consistency in data handling.

---

### File Source Tree Structure

Below is the proposed file source tree structure for the project. It includes separate directories for CLI and GUI components, shared model classes, and utility functions. Each file is described to clarify its purpose and how it supports the roles of the CLI and GUI developers.

<img width="294" alt="tree" src="https://github.com/user-attachments/assets/22be48dc-eb8f-4ba3-82e7-04aab4e67ee7" />



---

### Detailed Description of Files

#### Root Directory: `university_app/`
- **README.md**: Documentation specifying how to run the CLI and GUI applications, required dependencies (e.g., Python version, Tkinter for GUI), and any additional setup instructions. This ensures clarity for the Part 3 showcase and submission.

#### Directory: `cli/`
Contains files for CLIUniApp, split into controllers (logic) and views (user interface). The two CLI developers can divide responsibilities, with one focusing on student-related functionality and the other on admin-related functionality.

- **controllers/**
  - **student_controller.py**: Handles student system logic (registration, login, subject enrollment, removal, password changes). Interacts with `Student`, `Subject`, and `Database` models. Managed by the CLI developer responsible for the student subsystem.
  - **admin_controller.py**: Manages admin system logic (viewing students, grouping by grade, partitioning PASS/FAIL, removing students, clearing database). Interacts with the `Database` model. Managed by the CLI developer responsible for the admin subsystem.
  - **university_controller.py**: Controls the main university system menu, allowing navigation between student and admin subsystems. This can be handled by either CLI developer, as it’s a simple entry point.

- **views/**
  - **student_view.py**: Implements the CLI interface for student operations (menus for login, registration, and subject enrollment). Displays prompts and outputs per the sample I/O in `fundamental_final.pdf`. Managed by the student CLI developer.
  - **admin_view.py**: Implements the CLI interface for admin operations (menus for listing, grouping, partitioning, and deleting students). Follows sample I/O formatting. Managed by the admin CLI developer.
  - **university_view.py**: Displays the main university system menu (`(A) Admin`, `(S) Student`, `(X) Exit`). Simple and can be handled by either CLI developer.

- **main.py**: Entry point for CLIUniApp. Initializes the university system and starts the main menu loop. Either CLI developer can manage this file, as it integrates the controllers and views.

#### Directory: `gui/`
Contains files for GUIUniApp, focusing on the student-specific graphical interface with at least four windows (login, enrollment, subject, exception). The two GUI developers can split responsibilities, with one focusing on the login and exception windows and the other on the enrollment and subject windows.

- **views/**
  - **login_view.py**: Implements the login window using Tkinter, allowing students to input email and password. Validates credentials and redirects to the enrollment window. Managed by one GUI developer.
  - **enrollment_view.py**: Implements the enrollment window, enabling students to enroll in up to 4 subjects. Displays the current enrollment count and handles enrollment requests. Managed by the second GUI developer.
  - **subject_view.py**: Implements the subject window, listing enrolled subjects with their marks and grades. Managed by the second GUI developer.
  - **exception_view.py**: Implements the exception window, displaying error messages for invalid credentials, empty fields, or exceeding the 4-subject limit. Managed by the first GUI developer.

- **controllers/**
  - **gui_controller.py**: Manages the logic for GUIUniApp, coordinating between views and models. Handles login validation, subject enrollment, and error handling. Shared by both GUI developers, with clear method divisions (e.g., login-related vs. enrollment-related).

- **main.py**: Entry point for GUIUniApp. Initializes the Tkinter application and displays the login window. Managed by either GUI developer.

#### Directory: `models/`
Contains shared model classes used by both CLI and GUI applications to ensure data consistency. These are critical for all developers and should be developed early by one of the CLI or GUI developers with strong modeling skills.

- **student.py**: Defines the `Student` class with fields (`id`, `name`, `email`, `password`, `subjects`) and methods for enrollment, password changes, and grade calculation.
- **subject.py**: Defines the `Subject` class with fields (`id`, `mark`, `grade`) and logic for mark generation and grade calculation.
- **database.py**: Manages `students.data` file operations (create, read, write, clear). Ensures thread-safe access for CLI and GUI.

#### Directory: `utils/`
Contains utility functions shared across CLI and GUI applications to avoid code duplication.

- **validators.py**: Implements regular expressions for email (`@university.com`) and password (uppercase start, 5+ letters, 3+ digits) validation. Used by both CLI and GUI for consistent input validation.
- **id_generator.py**: Provides functions for generating unique student IDs (6-digit) and subject IDs (3-digit) with zero-padding. Used by model classes.

#### Directory: `data/`
- **students.data**: The file storing student data (serialized Student objects). Created and managed by the `Database` class. Both CLI and GUI applications read/write to this file.

---

### Role Assignment and File Responsibilities
To align with your decision of 2 CLI and 2 GUI developers, here’s how the files map to roles:

- **CLI Developer 1 (Student Subsystem)**:
  - Primary: `cli/controllers/student_controller.py`, `cli/views/student_view.py`.
  - Secondary: `cli/main.py`, `cli/controllers/university_controller.py`, `cli/views/university_view.py` (shared with CLI Developer 2).
  - Collaboration: Uses `models/*` and `utils/*`.

- **CLI Developer 2 (Admin Subsystem)**:
  - Primary: `cli/controllers/admin_controller.py`, `cli/views/admin_view.py`.
  - Secondary: `cli/main.py`, `cli/controllers/university_controller.py`, `cli/views/university_view.py` (shared with CLI Developer 1).
  - Collaboration: Uses `models/*` and `utils/*`.

- **GUI Developer 1 (Login and Exception)**:
  - Primary: `gui/views/login_view.py`, `gui/views/exception_view.py`.
  - Secondary: `gui/controllers/gui_controller.py` (login-related methods), `gui/main.py` (shared with GUI Developer 2).
  - Collaboration: Uses `models/*` and `utils/*`.

- **GUI Developer 2 (Enrollment and Subject)**:
  - Primary: `gui/views/enrollment_view.py`, `gui/views/subject_view.py`.
  - Secondary: `gui/controllers/gui_controller.py` (enrollment-related methods), `gui/main.py` (shared with GUI Developer 1).
  - Collaboration: Uses `models/*` and `utils/*`.

- **Shared Responsibility**:
  - The `models/*` and `utils/*` directories are critical for all developers. One developer (preferably with strong data modeling skills, e.g., CLI Developer 1 or GUI Developer 1) should take the lead on these early in the project, with others providing input and testing.

---

### Rationale for Structure
- **Modularity**: Separating `models`, `controllers`, and `views` follows MVC (Model-View-Controller) principles, making the codebase maintainable and scalable.
- **Separation of CLI and GUI**: Dedicated `cli/` and `gui/` directories ensure that CLIUniApp and GUIUniApp are distinct, with shared `models/` and `utils/` to avoid duplication.
- **Shared Data**: The single `students.data` file is managed by `database.py`, ensuring consistency between CLI and GUI applications.
- **Alignment with Requirements**: The structure supports all required functionalities (student registration/login, subject enrollment, admin operations, GUI windows) and adheres to the sample I/O in `fundamental_final.pdf`.
- **Team Collaboration**: Files are grouped to allow each developer to focus on specific components while sharing critical model and utility code.

---

### Additional Notes
- **Dependencies**: The GUI will use Tkinter (Python’s standard library) for simplicity and compatibility. CLI requires no additional libraries beyond Python’s standard library.
- **File Format for `students.data`**: Consider using JSON or pickle for serialization, implemented in `database.py`. JSON is human-readable and easier for debugging.
- **Version Control**: Use Git for collaboration, with each developer working on their respective files and merging changes to `models/` and `utils/` carefully.
- **Submission**: Per `fundamental_final.pdf`, the project will be submitted as a `.zip` file (`group<group-number>-Cmp1<lab-number>.zip`). Include both CLI and GUI in the same folder, with `README.md` explaining how to run each.

This structure ensures a clear division of work, supports the project’s requirements, and facilitates collaboration among the four team members. Let me know if you need further details or specific code snippets for any file!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=othneildrew/Best-README-Template" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
