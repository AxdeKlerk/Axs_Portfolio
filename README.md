# Ax’s Portfolio

A personal developer portfolio built with Django, designed to showcase my coding projects, experience, and personality. This site blends professionalism with a touch of who I am — an organised, methodical full-stack developer with a background in criminology, catering, and a lifelong love of heavy music. The goal is simple: present my work clearly, confidently, and authentically.

---

## Table of Contents

- [Ax’s Portfolio](#axs-portfolio)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1 Aim, Purpose and Goal of the Site](#11-aim-purpose-and-goal-of-the-site)
    - [1.2 Target Audience](#12-target-audience)
  - [2. Features](#2-features)
    - [2.1 Home](#21-home)
    - [2.2 About](#22-about)
    - [2.3 Projects](#23-projects)
    - [2.4 Blog](#24-blog)
    - [2.5 CV](#25-cv)
    - [2.6 Contact](#26-contact)
    - [2.7 Footer](#27-footer)
  - [3. Tech Stack](#3-tech-stack)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Database](#database)
    - [Deployment \& Version Control](#deployment--version-control)
  - [4. Planning and Development](#4-planning-and-development)
    - [4.1 Development Notes](#41-development-notes)
    - [4.2 User Stories](#42-user-stories)
      - [4.2.1 Home Page](#421-home-page)
      - [4.2.2 About Page](#422-about-page)
      - [4.2.3 Projects Section](#423-projects-section)
      - [4.2.4 Blog](#424-blog)
      - [4.2.5 CV Page](#425-cv-page)
      - [4.2.6 Contact Page](#426-contact-page)
    - [4.3 Agile Methodology](#43-agile-methodology)
      - [4.4 Summary](#44-summary)
    - [5 Debugging](#5-debugging)
    - [6 Testing](#6-testing)
  - [7. Future Enhancements](#7-future-enhancements)
  - [8. Deployment (Heroku)](#8-deployment-heroku)
    - [8.1 Clone the Repository](#81-clone-the-repository)
    - [8.2 Clone the Repository to VS Code](#82-clone-the-repository-to-vs-code)
    - [8.3 Create and Activate a Virtual Environment](#83-create-and-activate-a-virtual-environment)
  - [8.4 Install Project Dependencies](#84-install-project-dependencies)
    - [8.5 Prepare the Project for Heroku](#85-prepare-the-project-for-heroku)
    - [8.6 Set Up a Heroku Account and CLI](#86-set-up-a-heroku-account-and-cli)
    - [8.7 Create a Heroku App](#87-create-a-heroku-app)
    - [8.8 Configure Environment Variables on Heroku](#88-configure-environment-variables-on-heroku)
    - [8.9 Configure a Custom Domain on Heroku](#89-configure-a-custom-domain-on-heroku)
      - [8.9.1 Update DNS Records at the Domain Provider](#891-update-dns-records-at-the-domain-provider)
      - [8.9.2 Verify Domain Configuration](#892-verify-domain-configuration)
      - [8.9.3 Enable HTTPS (Automatic)](#893-enable-https-automatic)
    - [8.10 Push the Project to Heroku](#810-push-the-project-to-heroku)
    - [8.11 Final Project Setup on Heroku](#811-final-project-setup-on-heroku)
    - [8.12 Open the Live Site](#812-open-the-live-site)
    - [8.13 Summary](#813-summary)
  - [9. Performance Optimisation](#9-performance-optimisation)
    - [9.1 CSS Optimisation](#91-css-optimisation)
    - [9.2 Image Optimisation](#92-image-optimisation)
  - [10. Credits and Acknowledgements](#10-credits-and-acknowledgements)
    - [10.1 Credits](#101-credits)
    - [10.2 Acknowledgements](#102-acknowledgements)

---

## 1. Introduction

### 1.1 Aim, Purpose and Goal of the Site

The purpose of Ax’s Portfolio is to provide a clear, professional, and authentic presentation of my work as a junior full-stack developer. It showcases my Code Institute projects, documents my learning journey through a personal blog, and offers a polished snapshot of who I am — in both personality and skill.

The goal is to create a personal platform that reflects my growth, confidence, and evolving developer identity.

### 1.2 Target Audience

This portfolio is aimed at:
- Employers reviewing my coding ability  
- Recruiters looking for clean, professional examples of work  
- Tutors and mentors assessing my growth  
- Fellow developers and students  
- Anyone interested in my development journey  

---

## 2. Features

### 2.1 Home
A clean landing page introducing the site and providing direct navigation to key areas.

### 2.2 About
A personal introduction covering:
- My background and career transition  
- My learning style and problem-solving approach  
- A voice-recorded version of the About page (coming soon — iframe embedded)

### 2.3 Projects
Showcases all four Code Institute portfolio projects with:
- Project summary  
- Key features  
- Tools used  
- Learning outcomes  

### 2.4 Blog
A simple blog system including:
- Individual blog detail pages  
- Learning reflections  
- Behind-the-scenes notes  
- Personal workflow commentary  

### 2.5 CV
A dedicated CV page displaying:
- Both sides of my CV  
- On-page previews  
- Downloadable **PDF** and **.doc** files  

### 2.6 Contact
A direct contact page for enquiries with form validation.

### 2.7 Footer
Footer links include:
- GitHub  
- LinkedIn  

---

## 3. Tech Stack

### Backend
- Django  
- Python  

### Frontend
- HTML  
- CSS  
- (JavaScript coming soon — for embedded audio playback)

### Database
- PostgreSQL (Render deployment)  
- SQLite (local development)

### Deployment & Version Control
- GitHub  
- Render  

---

## 4. Planning and Development

### 4.1 Development Notes

This project follows clean, well-structured Django practices:

- Template inheritance  
- Static file handling  
- Database-backed content (projects & blog)  
- Separate development and production settings  
- Maintainable and readable folder structure  

---

### 4.2 User Stories

#### 4.2.1 Home Page  
As a **visitor**, I want to **immediately understand what the site is about**, so that I **know I’ve reached a developer portfolio**.

#### 4.2.2 About Page  
As a **recruiter**, I want to **quickly learn who Ax is**, so that I **understand his background and personality**.

#### 4.2.3 Projects Section  
As a **potential employer**, I want to **view Ax’s completed projects**, so that I **can evaluate his coding ability and project experience**.

#### 4.2.4 Blog  
As a **developer or tutor**, I want to **read Ax’s reflections and progress**, so that I **can understand his learning journey**.

#### 4.2.5 CV Page  
As a **recruiter**, I want to **view and download Ax’s CV**, so that I **can assess his experience and save the file for review**.

#### 4.2.6 Contact Page  
As a **visitor**, I want to **easily get in touch**, so that **I can contact Ax for opportunities or questions**.

---

### 4.3 Agile Methodology

*(…your full Agile section here — unchanged…)*

---

#### 4.4 Summary

All features across the site were designed with simplicity, speed, and responsive behaviour in mind. Every page follows a consistent visual theme, ensuring a cohesive experience on any device. The combination of **Bootstrap**’s responsive utilities and **Django**’s backend logic keeps the site clean, efficient, and scalable for future upgrades.  

### 5 Debugging

Please refer to the debugging documentation for detailed descriptions of all bugs found, fixed and learned from. It can be found here: [DEBUGGING.md](DEBUGGING.md)

---

### 6 Testing

Please refer to the testing documentation for detailed descriptions of the tests completed found here: [TESTING.md](TESTING.md)

---

## 7. Future Enhancements

Planned improvements include:

- Embedded voice-recorded “About Me” section  
 

---

## 8. Deployment (Heroku)

This section outlines the full process for deploying Ax’s Portfolio from GitHub to a local development environment using VS Code, and then hosting the application live on Heroku with a production PostgreSQL database provided by Neon.

### 8.1 Clone the Repository

- Navigate to GitHub and click the “+” icon to create a new repository
- Enter a repository name and optional description
- Choose Public or Private
- Do not initialise with a README, .gitignore, or license
- Click Create repository

### 8.2 Clone the Repository to VS Code

- Open VS Code and access the integrated terminal
- Navigate to the directory where the project will live
- Copy the repository URL from GitHub
- Use Clone Git Repository in VS Code or clone via terminal
- Open the cloned project folder in VS Code

### 8.3 Create and Activate a Virtual Environment

- Create a virtual environment inside the project root
- Activate the environment according to your operating system
- Confirm activation by checking that the environment name appears in the terminal prompt
- This isolates project dependencies and prevents conflicts with system-wide packages.

## 8.4 Install Project Dependencies

- Install all required packages using the requirements.txt file
- Key dependencies include:
- Django – Backend web framework
- Gunicorn – WSGI server required by Heroku
- dj-database-url – Parses the database URL into Django settings
- psycopg2-binary – PostgreSQL database adapter
- WhiteNoise – Static file handling in production
- If requirements.txt does not yet exist, install dependencies manually and generate it before continuing.

### 8.5 Prepare the Project for Heroku

- Create a Procfile at the project root containing: `web: gunicorn config.wsgi`
- Ensure gunicorn, dj-database-url, and psycopg2-binary are installed
- Confirm static file settings and WhiteNoise configuration
- Commit all changes to GitHub

### 8.6 Set Up a Heroku Account and CLI

- Create an account at Heroku.com
- Download and install the Heroku CLI for your operating system
- Log in via the CLI to authenticate your local environment

### 8.7 Create a Heroku App

- Use the Heroku CLI or dashboard to create a new app
- Assign a unique app name
- Heroku will automatically generate a remote Git endpoint

### 8.8 Configure Environment Variables on Heroku

- Open the app in the Heroku Dashboard
- Navigate to Settings → Reveal Config Vars
- Add the following environment variables:
- DEBUG = False
- SECRET_KEY = Django secret key
- DATABASE_URL = Neon PostgreSQL connection string
- ALLOWED_HOSTS = Heroku app domain
- CSRF_TRUSTED_ORIGINS = Heroku app URL
- Sensitive values are stored securely and are not committed to version control.

### 8.9 Configure a Custom Domain on Heroku

This project is configured to use a custom domain (axdeklerk.co.uk) instead of the default Heroku subdomain.

- Add the Custom Domain in Heroku
- Open the application in the Heroku Dashboard
- Navigate to Settings → Domains
- Click Add domain
- Enter the custom domain: `axdeklerk.co.uk`
- Heroku will generate a DNS target (DNS record value)

#### 8.9.1 Update DNS Records at the Domain Provider

- Log in to the domain registrar or DNS provider managing axdeklerk.co.uk
- Create or update a CNAME or ALIAS/ANAME record (depending on provider support)
- Point the domain to the DNS target provided by Heroku
- Remove any conflicting A records that may override the custom domain
- DNS propagation may take several minutes to several hours to complete.

#### 8.9.2 Verify Domain Configuration

- Return to the Heroku Domains section
- Confirm the custom domain shows as active
- Visit [https://axdeklerk.co.uk](https://axdeklerk.co.uk) in a browser to verify successful routing

#### 8.9.3 Enable HTTPS (Automatic)

- Heroku automatically provisions SSL certificates for verified custom domains
- HTTPS is enabled once DNS propagation completes
- No manual certificate configuration is required

### 8.10 Push the Project to Heroku

- Ensure the Heroku remote is connected to the local repository
- Push the project code to Heroku
- Heroku will automatically install dependencies and build the application

### 8.11 Final Project Setup on Heroku

- Run database migrations using the Heroku CLI
- Create a Django superuser for admin access
- Confirm static files are collected and served correctly
- Verify the site loads correctly via the custom domain

### 8.12 Open the Live Site

- Open the deployed application using: `https://axdeklerk.co.uk`
- Confirm navigation, static assets, and database-backed content load correctly

### 8.13 Summary

Deployment was successful, with the application running stably under a custom domain using DEBUG=False. HTTPS is enabled, static files are served correctly, and the site behaves consistently in production.

---

## 9. Performance Optimisation

These optimisations focus on improving real-world performance while keeping the project simple, maintainable, and aligned with its portfolio scope.

### 9.1 CSS Optimisation

To improve performance in production, **CSS** files were manually minified using an online [CSS minification tool](https://www.toptal.com/developers/cssminifier). This process removes unnecessary whitespace and comments, reducing file size while preserving styling behaviour.

- Original readable CSS files were retained for development
- Minified CSS is served in production
- No build tools or preprocessors were required

### 9.2 Image Optimisation

Images used throughout the site were optimised to reduce file size and improve load performance in production. Compression was applied without altering image dimensions or visual quality.

- Images were compressed using online image optimisation tools
- Original filenames and paths were preserved to avoid broken references
- Optimised images reduce bandwidth usage and improve page load times

---

## 10. Credits and Acknowledgements

### 10.1 Credits

This project was created independently but draws on the support and documentation of the following resources:

- [Adobe Express](https://new.express.adobe.com/?xProduct=&xProductLocation=&locale=en-US) for the logo creation
- [AI Image Upscaler](https://imgupscaler.com/) - for upscaling the About image for better quality
- [Balsamic](https://balsamiq.com/) for the wireframes
- [BootStrap](https://simple.wikipedia.org/wiki/Bootstrap_(front-end_framework)) - used for the layout and styling of the website
- [Bootstrap Docs](https://getbootstrap.com/) for reference to all Bootstrap syntax
- [Chat-GPT](https://chatgpt.com/) - An AI tool used for understanding where things went wrong, how to fix code and generally used for deeper understanding of software development and the principles and languages used for coding
- [coolors.co](https://coolors.co/) for the colour palette
- [CSS](https://en.wikipedia.org/wiki/CSS) - used for main content styling
- [Django](https://simple.wikipedia.org/wiki/Django_(web_framework)) - used for the backend of the website
- [draw.io](https://app.diagrams.net/) for the ERD
- [Ecotrust](https://ecotrust-canada.github.io/markdown-toc/) - used to generate table of contents
- [Heroku](https://id.heroku.com)
- [GMAIL](https://mail.google.com)
- [Google Fonts](https://fonts.google.com/) - for typography
- [Google Images](https://images.google.co.uk/) - for the band and venue logos
- [HTML](https://en.wikipedia.org/wiki/HTML) - used to build main site content
- [JavaScript](https://simple.wikipedia.org/wiki/JavaScript) - used for all interactivity within the website
- [JSHint](https://jshint.com/) for Javascript validation
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) - for the performance and accessibility testing
- [Loom](https://www.loom.com) - for responsive video
- [MSWord](https://www.microsoft.com/en-us/microsoft-365/word) - used for grammar and spelling checking
- [Neon](https://neon.com/) - for a Postgres database platform
- [Perplexity](https://www.perplexity.ai/) - An AI tool used for general queries and learning
- [Python](https://simple.wikipedia.org/wiki/Python_(programming_language)) - used for the backend of the website
- [Short Pixel](https://shortpixel.com/) - for image optimisations
- [Slack Edit](https://stackedit.io/) - for markdown references
- [Slack Overflow](https://stackoverflow.com/questions) - for general queries
- [TinyWow](https://tinywow.com) Image Compressor
- [Toptal](https://www.toptal.com/developers/cssminifier)
- [W3schools](https://www.w3schools.com/) a constant source of reference for all html, CSS, JavaScript, BootStrap and Django explanations
- [W3C Markup Validation Service](https://validator.w3.org/) for the html validation
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for the CSS validation
- [VC Code](https://code.visualstudio.com/)

### 10.2 Acknowledgements

Special thanks to:

- **Richard Wells** - Code Institute Mentor for his continued support even after I completed the course
- **Julia** — for constant support  
- **Friends & Family** —  *Julie*, *Paul*, *Thambiso*, *Matthew* & *Elaine* - thank you for your, sometimes brutal, honesty and constructive feedback  
- **Barry** — (my dog) for ensuring I take breaks and maintain balance  

