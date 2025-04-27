# **1. Table of Contents**

**Request of Proposal**

**Introduction**

Purpose of Document

Major Problems and Project Goal

Proposed System Overview

Definitions, Acronyms, and Abbreviations

References

Overview of document

**General Description**

Product Perspective

Major Functions and Features

User Characteristics

General Constraints

Assumptions and Dependencies

**Software Requirements**

**Functional Requirements**

Requirements with I/O

**External Interfaces**

User Interfaces

Hardware Interfaces

Software Interfaces

Communication Interfaces

Internet Connections/Networking

Configuration Options

Installation

User Documentation

**Non-Functional Requirements**

Performance Requirements

Operational and Environment
Requirements

Reliability and Availability

Backup and Security

Maintainability

Transferability/Portability/Usability

Documentation and Training

Exception Handling

Testing Requirements

**Design Constraints**

**Log of Meetings, Reviews and
Meetings**

**Change Control**

**Appendix**

**Signature part of Client**

**Work Structure Breakdown**

**ER-Diagram**

**Data Flow Diagram**

**Terms and Conditions**

---

# 2. Request of Proposal

WealthWise Financial Advising is a digital platform designed to help individuals make informed financial decisions through personalized services. The platform provides access to certified financial advisors, a range of financial tools, and the latest market news, allowing users to manage personal wealth and investments efficiently.

The core of our platform revolves around offering personalized financial advice through one-on-one consultations with certified advisors, covering areas such as retirement planning, budgeting, and investment strategies, etc. Users can easily schedule appointments through an integrated booking system that ensures a hassle-free experience. In addition to personalized advisory services, WealthWise offers exclusive financial events where users can register and attend seminars, workshops, and webinars led by financial educators.

The platform also features a financial education resource, offering access to market news, stock analysis, and insights into current financial trends. This allows users to stay informed on the latest developments that might affect their investments and financial decisions.

Furthermore, we provide a variety of financial calculators, including those for loan interest, Mortgage calculator, budgeting, and retirement planning insurance coverage, etc. all designed to give users a hands-on approach to their financial management. Clients can input their financial data and receive tailored insights, helping them make smarter financial decisions.

The platform offers a range of subscription plans that give users access to premium features, including personalized financial advice from certified advisors, advanced tools for detailed portfolio analysis, and exclusive content designed to help users achieve their specific financial goals.

We are looking for a software company willing to build this system for us, and your company came highly recommended. We look forward to working with you on this system that will allow our financial advising platform to run much more smoothly and efficiently in the future.

---

# **3. Introduction**

# 3.1 Purpose of Document

This document defines all requirements for the software system Arqer is creating for WealthWise. This document shall be completed before development begins. It shall serve as a written contract between the client and our team that defines all the software we shall implement. The requirements were obtained from the proposal request and various meetings with the client. 

---

# 3.2 Major Problems and Project Goals

## 3.2.1 Major Problems

### **Data Security and Privacy Risks**

    WealthWise deals with sensitive financial information and plans. This makes it a tempting target for cyberattacks. A data breach will lead to lawsuits, significant financial penalties, identity endangerment, compromised user safety, and loss of trust in our system.

    To mitigate this risk, Arqer shall enforce strong encryption protocols and comply with data protection regulations like GDPR and PCI DSS (Payment Card Industry Data Security Standard) and should use multi-factor authentication where feasible.

### **Implementation of Video Conferencing**

     To implement features such as advisor meetings, webinars, and other events, the website requires a video conferencing gateway. This will be external to our system and will be a challenge to implement. Additionally, disruptions to any of these components will cause downtime.

     To implement this, Arqer shall implement flexible API’s to third-party video conferencing services (ex. Google Meets, Zoom). Arqer should, where feasible, build redundancy into the system by integrating dependable services via alternative third-party services. Any implemented services and APIs implemented shall be ones of good repute within the given industry.

### Payment

     In order to implement payment-based subscriptions, the website will require payment gateways. This will be a challenge as said gateways will be outside our system and will carry sensitive data.

     To implement this, Arqer shall integrate payment gateways, financial data providers, and other APIs into the website and resolve compatibility and dependency issues with said services. services implemented should include PayPal and credit cards (visa, Master Card, etc.).

### **Managing Real-Time Data Updates**

     Features like market news and stock data require real-time updates and can be resource-intensive. Other systems, such as advisor scheduling and event scheduled will also require real-time data syncing.

     To create the best user experience and have any data as up-to-date as possible. Arqer shall cache data as necessary and feasible, redirect the users to the actual data source where applicable, and implement database management systems such as the ACID (atomic, consistency, isolation, and durability) model.

## 3.2.2 Objectives (Project Goals)

### Centralize WealthWise’s Services

     The primary goal of this website is to bring all of WeathWise’s services to one central website. Arqer shall bring all listed services (see Software Requirements section) to one central website.

### Providing Accessibility to Certified Advisors

     One major service WeathWise provides access to conferencing with certified financial advisors. Arqer shall allow users to hold video calls with certified financial advisors. Users shall be able to schedule a video meeting with a financial advisor through an event scheduler that allows for meeting scheduling, editing, and cancellation.

### Provide Advanced Financial Tools (Calculators)

     To allow users to make sound financial decisions, Arqer shall implement a variety of calculators including a loan interest calculator, a mortgage calculator, a budgeting tool (by subscription), a retirement planning calculator, and an insurance coverage calculator.

### Education and News Resources

     To allow users to stay up-to-date on financial education and news, Arqer shall implement a learning hub with resources such as news articles, financial tutorials, webinars, and other educational resources as necessary. External resources shall be accessed via relevant APIs and gateways.

### Secure Payment

     To allow system monetization and subscriptions, Arqer shall implement systems to allow the user to make payments to WealthWise. Said payments shall be made secure via reputable third-party services such as PayPal and its 128-bit SSL protocol.

### System Security Monitoring

     Site administrators shall be able to monitor the system and log events. Significant system events (log-ins, data transfers, API requests) shall be logged. An intruder detection system shall be used to identify unauthorized access to or tampering with the system.

### Intuitive UI/UX

     The website should be designed such that the target user shall be able to navigate to every feature and tool without significant delay or loss of user experience. This shall be achieved through intuitive web design that clearly indicates where tools are located throughout the site.

---

# 3.3 Proposed System Overview

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/e9e01e21-7958-4f99-86a1-29782b482ac0/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/5ec8a1d7-8974-45ca-85fe-5821ce6cb069/image.png)

https://embed.figma.com/board/V6dnjsxDZXoo3r9OuhEHsB/SE-305---Proposed-System?node-id=0-1&t=U0MkLDbpQsWXzWzY-1&embed-host=notion&footer=false&theme=system

---

# 3.4 Context Model

![WealthWise SystemContext Model.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/b57f1e34-cf86-4278-ac97-00220b19fee2/WealthWise_SystemContext_Model.png)

### **1. Payment Gateway APIs**

Payment gateways securely manage all financial transactions, from subscription purchases to event ticket sales and consultation fees.

**a. PayPal API**

This will let users pay with PayPal accounts and credit or debit cards.  PayPal’s REST API will be used for initiating transactions, subscriptions management, refund processing, and transaction history. The transaction communications shall be properly secured using TLS encryption. Listen for status updates related to the payments in the form of webhooks provided by the PayPal integration for events like payment successful, failed, and refunded. The integration shall, in substance, follow the guidelines on PCI DSS by PayPal for secure transactions.

**b. Stripe API**

Stripe is to process subscriptions and event payments for flexibility in various payment types, including credit cards and ACH transfers. Used for dynamically building the payment form, securely capturing credit card information. Stripe tokens to represent details of the card, not actual details of it, so no sensitive information is passed around.

Payment processing, refunds, subscription setup. Stripe webhooks will report the platform about transaction statuses, subscription renewals, and failures of payments.

### **2. Email Service APIs**

These APIs shall handle automated email communications for all account verifications, notifications, reminders, and marketing purposes.

**a. SendGrid API**

SendGrid shall be employed for the delivery of all transactional emails, which include verification of account, password reset, event reminders, notifications.

The platform will use SMTP Relay provided by SendGrid for sending emails and the Web API for more customized sending of emails-for example, bulk sends. The template setup via SendGrid will maintain a consistent look for verification emails, password reset emails, notification emails, etc SendGrid’s analytics API will be used to track delivery, opens, clicks, and errors for the emails.

**b. Twilio API - For SMS Notifications**

Twilio will be used to send out SMS notifications for critical alerts, such as appointment reminders or urgent security updates.

This will use Twilio’s RESTful API to send, receive, and track delivery statuses of SMSs. This allows automatic sending of SMS based on users’ preferences. Twilio can be used to introduce SMS-based 2FA.

### **3. Video Conferencing APIs**

These APIs will allow virtual consultations between clients and their respective advisors to take place, thus enabling remote financial advisory services.

**a. Zoom API**

The application will use Zoom for secure video calls between users and advisors for virtual consultations. OAuth 2.0 will be used for authentication of Zoom accounts on the platform for scheduling meetings. The Meeting API will be responsible for exposing create, manage, and delete functionality from inside the platform for virtual meetings.

The Zoom Embedded SDK can be employed to offer in-browser video calls so that the users may not have to leave the comfort of the platform.  Webhooks will notify Zoom on events like the start of a meeting and the end of a meeting. It provides a well-known, reliable, and secure virtual meeting solution that is necessary for remote financial consultations.

**b. Google Meet API**

It will be an alternative for users whose preferred video conferencing platform is Google Meet. OAuth 2.0 Authentication: OAuth will be used for the authorization of Google accounts and to manage meetings.

Google Meet will be integrated with the Google Calendar API to automatically add meetings to calendars and invite others. This provides functionality for creating, managing, and deleting meetings right within the platform. 

### **4. Financial Data APIs**

These APIs will deliver real-time financial information to the **Learning Hub**, calculators, and market news updates.

**a. Alpha Vantage API**

Alpha Vantage offers real-time and historical market data - stock prices, forex, and economic indicators.  The application will make a call to the Alpha Vantage’s API and fetch financial data for real-time stock tickers, charts, and investment analysis tools. Rate limiting is used to manage API call limits and ensure stable performance.

b. **Yahoo Finance API**

The API will be utilized to retrieve the quotations of stocks, financials of companies, and trends of industries for **Learning Hub**. This API will be used to provide fresh data on stock, charts, and financial news to keep the users well informed. Integration with Alpha Vantage and data from Yahoo Finance will provide wider insights and comparisons.

### **5. Authentication and Security APIs**

These APIs will manage authentication for users, access controls, and data security.

**a. Auth0 API**

It will be used by Auth0 for user authentication: secure login, registration, and session management. For single sign-on capability, user authentication is taken care of by Auth0 using these protocols. MFA can also be configured in Auth0 to allow for an extra layer of security. Auth0’s API will be used for managing user roles, permissions, and access controls within the system.

### **6. Calendar and Scheduling APIs**

These are APIs that provide appointment management, event management, and user scheduling.

**a. Google Calendar API**

It will provide users and the advisors with the capability of creating, editing, and managing appointments and events within the platform. The events should be created, edited, and deleted while automatically synchronizing with the Google Calendars of users. OAuth authentication allows the users to securely grant access to their calendars. Improvement the user experience is brought about by it, thereby ensuring smooth event and appointment management.

**b. Microsoft Outlook Calendar API**

This API shall provide to Outlook users the same functionality for scheduling, as given to Google Calendar users. Sync with the users’ Outlook Calendars and thereby manage appointments and events. This user authentication should be done in a secure way so that they may provide access to their calendar.

### **8. APIs for Analytics and Reporting**

These represent data visualization, reporting, and analytics about the users.

**a. Google Analytics API**

Google Analytics will be used in keeping track of user interactions, feature usage, as well as event attendance that shall help admins understand how users behave. It needs to be able to track user engagement metrics, conversion rates, and session data. The admin dashboard will have insights into user behavior and platform performance with the help of Google Analytics data.

---

# 3.5 Definitions, Acronyms, and Abbreviations

- ACID: A database model designed for data synchronicity standing for atomic, consistency, isolation, and durability
- ADA: Americans with Disabilities Act
- AES: Advanced Encryption Standard
- API: Application Programming Interface
- ARIA: Accessible Rich Internet Applications
- AWS: Amazon Web Services
- DFD: Data Flow Diagram
- GDPR: General Data Protection Regulation
- IDS: Intruder Detection System
- IP: Internet Protocol
- JWS: JSON Web Tokens
- PCI DSS: Payment Card Industry Data Security Standard
- RD: Requirement Document
- SFTP: Secure File Transfer Protocol
- SQL: Structured Query Language
- SSL: Internet communication security protocol: Secure Sockets Layer
- REST: An architecture for distributed systems (REpresentational State Transfer)
- TLS: Internet communication security protocol: Transport Layer Security
- UI: User Interface
- UX: User Experience
- WCAG: Web Content Accessibility Guidelines
- Web app: a website with application functionality
- WSB: Work Structure Breakdown

---

# 3.6 References

SendGrid Website: https://sendgrid.com/en-us

This website is the home page of SendGrid, our proposed emailing API our site will use to email users for various purposes.

JWS Website: https://sendgrid.com/en-us

This website is the home page of JWS, our proposed system to manage web tokens.

Sharding reference: https://www.geeksforgeeks.org/database-sharding-a-system-design-concept/ 

This site overviews the sharding methodology we have proposed for our database.

AWS Website[:](https://aws.amazon.com/) https://aws.amazon.com/

This website is the home page of AWS, our proposed system for cloud infrastructure.

PCI DSS Website[:](https://aws.amazon.com/) https://www.pcisecuritystandards.org/

This website is the home page of PCI DSS, our proposed standard for payment security.

Security Onion Website[:](https://aws.amazon.com/) https://www.pcisecuritystandards.org/

This website is the home page of Security Onion, our proposed IDS

Nessus Website: https://www.tenable.com/products/nessus

This website is the home page of Security Onion, our proposed vulnerability scanner.

---

# 3.7 Overview of Document

     This document provides the client with detailed information about every feature,
component, and process related to the system. First, we will cover the general description of the system, including the product perspective, key functions and features, user characteristics, and general constraints such as design and process limitations, along with assumptions, dependencies, and modifiability.
     Next, we will outline the software requirements, identifying the functional requirements
like input/output, networking, and configuration, as well as non-functional requirements such as exception handling, testing, backup, and security. We will also briefly describe the design constraints to ensure the system aligns with the brand’s colors and preferences.
     After detailing the system requirements, we will review meeting logs, meeting policies, and the review process. Following that, we will present the change control policy, which outlines the procedures for handling change requests. Finally, the document will conclude with an appendix and the terms and conditions.

---

---

# **4. General Description**

## 4.1 Product Perspective

The new digital platform, called WealthWise Financial Advising, unifies financial services of all kinds onto one platform, allowing non-professionals to manage their private wealth and investments more effectively. It will thus combine personalized financial advisory services,  financial tools, educational resources, event management, and secure payment processing in a single, user-friendly app.

### **System Interfaces**

The system will require interfaces for payment gateways, financial data providers, video conferencing, and email notifications.

Payment Gateways APIs shall be used for processing the payments via Stripe, PayPal, and various credit cards such as MasterCard or Visa.

Financial Data Providers API shall extend to news services, stock platforms, and education resource sites to receive current market news in real-time, current stock data, financial trends, and education resources such as videos, tutorials, and courses.

Video conferencing tool APIs shall extend to Google Meets, and Zoom as applicable to facilitate engaging with consultations, virtually, between the clients and their advisors.

Email and Notification Services APIs shall extend to external sources to inform users of critical information as relevant (eg. scheduled event, meeting starting soon). These shall act as a means of communication and notification. Services implemented should include SendGrid and/or Twilio.

### **User Interfaces**

The web application shall be accessible through the website using the desktop browsers Chrome, Firefox, Edge, and Safari and be accessible through both Android and iPhones. The Web app shall adjust its size to accommodate differing screen sizes and shall follow all web accessibility norms to include color contrast and keyboard navigation. 

### **Hardware Interfaces**

Server-side operations shall be able to be hosted on scalable cloud services, such as AWS or Azure, and implemented such that such horizontal scalability is possible.

Client-side operations shall be accessible independently of hardware. Both Desktop and mobile access shall be implemented.

### **Software Interfaces**

Server-side operations shall be operating system-independent and require Python, SQL, and HTML support.

Client-side operations shall be accessible via Chrome, Firefox, Edge, or Safari browsers and be accessible through both Android and iPhone devices

Interaction between the client and server shall take place via RESTful APIs. Future enhancements may integrate other third parties.

### **Memory and Storage Constraints**

Server-side resources shall be sufficient to store all relevant user information, backup, and application logs. These shall be sufficient for the proposed peak user load of 25,000 concurrent peak users.

Client-side resources should be very limited. Storage shall be allocated for storing cookies and local caching, to increase performance.

### **Operations**

The web app shall have 3 nines of availability, or 99.9% availability (uptime), with less than or equal to .1% downtime. Scheduled maintenance shall take place during non-peak hours with prior user notification.

### **Site Adaptation Requirements**

The web app should translate into various languages and different regional settings, as needed.

---

## 4.2 Major Functions and Features

### Event Scheduling

Users and site administrators shall be able to schedule events via a planning calendar. This will allow the creation and scheduling of events. Furthermore, the creator of the event or the site administrators shall be able to modify, reschedule, or delete the event. Users shall be able to register for the event ahead of time to allow event participation.

### Providing Accessibility to Certified Advisors

The web app shall allow users and advisors to hold video meetings following an appointment scheduling. Users shall be able to schedule a video meeting with a financial advisor through an event scheduler that allows for meeting scheduling, editing, and cancellation.

### Subscription

The web app shall have a free and subscription tier. The free tier will allow access to all website features except for the budget planning feature. Users shall be able to make payments to WealthWise in order to gain the subscription tier and access to the budget planning feature.

### Financial Calculators & Planner

The web app shall include a loan interest calculator, a mortgage calculator, a retirement planning calculator, student loan, car loan, and an insurance coverage calculator. 

The budget planner shall allow the user to input income sources and amounts, fixed expenses, variable expenses, and savings goals and return a comprehensive budget overview, breaking down percentages of income sources and total percent allocation to expenses; spending analysis, which will break down of expenses by percentage; and recommendations for savings, which suggests categories that the user may be overspending on by comparison against percentages determined by the site’s certified financial advisors.

### Learning Hub

The learning hub shall feature market news and stock data in real time. The learning hub shall also provide users with resources such as news articles, financial tutorials, webinars, and other educational resources as desired.

### System Security Monitoring

The web app shall have sufficient cyber security incident monitoring. Significant system events (log-ins, data transfers, API requests) shall be logged. An intruder detection system, such as Security Onion, shall be used to identify unauthorized access to or tampering with the system.

---

## 4.3 User Characteristics

General users are people seeking financial advice. They can have a wide range of interests and technical proficiencies, from young professionals to seniors seeking retirement advice. Software should be intuitive for users since many may have novice technical expertise. Since these users will voluntarily use the software, it should focus on acceptability. 

Financial advisors are another type of user who interacts with the software. These users can be assumed to have a higher degree of technical knowledge and some training in the software. They shall user use the software repeatedly. We should focus on appealing to efficiency for these users so it interrupts their work as little as possible.

---

## 4.4 General Constraints

Server-side architecture shall support Python, SQL, and HTML, as they will be the primary languages used to build the system architecture. Servers shall also be run on scalable hardware or user-scalable cloud computing solutions such as AWS.

Integration: All features (learning hub, event planner, advisor meetings, etc.) shall be integrated on the same website, allowing the user to move between each.

Security: any sensitive data shall be end-to-end encrypted in transport using TLS or SSL as applicable and encrypted while at rest using 256-bit AES.

Performance: The website shall not excessively waste system resources and feel responsive to the user having a maximum response time of 10 seconds.

Dependability: The website shall remain primarily in a state of uptime during its service period with 3 nines of availability (99.9%).

Compatibility: The website shall work on current versions of Chrome, Firefox, Edge, and Safari and be accessible on iOS and Android.

Privacy: Data collected by Arqer shall remain within company control at all times and not be shared with outside parties.

Availability: The website shall remain available under a peak user load of 25,000 concurrent users.

Data storage: Data shall be stored in compliance with relevant laws and regulations, including GBPR and laws and regulations of the host country and region. 

Localization: the website shall be accessible to all targeted locations and regions.

User Experience: Control of the website should be intuitive to the target user, allowing seamless navigation without degradation of user experience.

---

## 4.5 Assumptions and Dependencies

### **Assumptions**

**System assumption:**

The system shall run on a server to provide services to the customer. Users can use their up-to-date web browser (Chrome, Edge, Firefox, or Safari) to connect to the server and perform actions on their devices.

The system shall be able to handle 25,000 simultaneously without issue. It should also perform flawlessly, efficiently, securely, and respond timely. The system should maintain an average response time of at most 10 seconds. Additionally, maintain high availability.

The system shall handle most services, use APIs to fetch information from third-party or external service providers and be able to store all encrypted data in a database.

The system shall also be able to frequently back up the system without interrupting services for longer than 2 hours during non-peak hours. They also should include error correction codes via single-bit parity to maintain data integrity; and protection against bypasses such as injections or database bugs.

**User assumptions:** 

There shall be three user types: customers, advisors, and system administrators. 

Each user group shall have a different system view based on their access level/permission and role.

Customers who have subscriptions shall be able to use all the features.

Advisors shall not be able to modify the system information/data directly as the system administrators. 

System administrators shall have sufficient permissions to modify the system directly. Additionally, they shall be able to control every component in the system.

### **Dependencies**

- The website should be dependent on video hosting services (Google Meets and Zoom), APIs (news, education resources), and databases (PostgreSQL).
- The server system shall support Python, HTML, and SQL.
- The account management system should be dependent on the database system and payment process of third-party transaction services (PayPal, Stripe, Master Card, Visa).
- System administration should depend on all other components to monitor the system as a whole (the monitoring system requires a system to monitor).

---

# 5. Software Requirements

Requirements numbering has been reset for clarity when referring to requirements. Requirement numbering will be prepended with “(Req)”

# 5.1 Functional Requirements

## **(Req)1. User Management System**

The **User Management System** will be the backbone of the WealthWise website including user account creation, log in, profile management, and interaction with other components.

### **(Req)1.1 User Registration**

- **(Req)1.1.1 Display of Form**
    - User shall be able to create an account by clicking the "register" button on the login page, entering an email that will double as a username, and choosing a password.
    - Fields allowing entering of information such as financial goals shall be optional for clients.
    - Registration page should display a clean and user-friendly form with an input field for email, password, and basic user information including a phone number.
- **(Req)1.1.2 Data Validation**
    - The data from this interaction shall be encrypted using TLS to ensure the password remains secure.
    - The website shall perform front end validation to include ensuring the email is syntactically valid (could feasibly be a real email address), the password meets complexity requirements (see below), and all required fields are filled.
    - The system shall the entered email is not a duplicate and display an error message when a user tries to create an account with a duplicate email.
    - Passwords shall be at least 12 characters in length. They must have at least one capital letter, one lowercase letter, one number, and a special character. Stored passwords will be salted to protect against brute-force attacks.
- **(Req)1.1.3 Email Verification:**
    - Upon entering in and submitting all information, the system shall send a confirmation email to the provided email address using SendGrid. This confirmation email shall contain time-sensitive link. This link shall allow the user to validate that they own the email they entered.
    - If the users fail to verify their account within 24 hours, their account information shall be deleted and their account shall not be created.
    - Emails containing verification links shall be encrypted using TLS to mitigate security risks.

### **(Req)1.2 User Login**

- **(Req)1.2.1 Requirements**
    - The user shall be able to access their account using the email and password they created the account with. The user shall enter their credentials on the login page and click login.
    - The password in transit shall be encrypted using TLS to ensure it remains secure. The user shall be authenticated and allowed to access the website if the credentials match. Should the user fail to log in 3 times, their account shall be locked out for 3 minutes.
    - Once authenticated, the system should establish JWT with the client for easy authentication. This effectively allows “remember me”.

### **(Req)1.3 Password Recovery**

- **(Req)1.3.1 Password Reset Request**
    - If the user wishes to reset their password, whether it is forgotten or not, they shall be able do so by clicking "reset password". SendGrid shall send a password reset link that expires in 10 minutes. Upon clicking the link, the user may then choose a new password using the same requirements seen in 1.1.
- **(Req)1.3.2 Token Validation**
    - When the user clicks on the reset link, the system shall first verify the token has not expired. If it is still valid, the user shall be requested to create a new password using the same requirements seen in 1.1.
    - When the password is reset, the system shall log the user out of all running sessions. Users will then need to log in again with their new credentials to access the site.

### **(Req)1.4 Profile Management**

- **(Req)1.4.1 Profile Viewing and Editing**
    - A logged in user shall be able to edit their personal information from their profile including their name, phone number, address, email, profile picture, financial goals, and privacy settings. For advisors, the system shall display ratings from previous clients.
    - The system shall verify the validity of address fields. Only letters shall appear in the city, state, county, etc. Phone numbers, shall be in the format XXX-XX-XXX, and characters shall appear in the name field.
    - If the account type is an advisor, the system shall allow the advisor to upload certification/licenses through SFTP, allow editing bio and area(s) of expertise.
- **(Req)1.4.2 Advisor-Specific Fields**
    - The Advisors shall be able to edit additional fields to include certifications, licenses, bio, and areas of specialization.
    - The system shall allow secure file uploads via SFTP for certifications.
- **(Req)1.4.3 Privacy Settings**
    - Users shall be able to choose what information other users can see to include financial goals and contact information. Should the user keep any information private, only administrators shall be able to view mentioned information.

### **(Req)1.5 Subscription Management**

- **(Req)1.5.1 Subscription Status Viewing**
    - The user shall be able to view subscription information from their profile including whether they have an active subscription, the date until subscription expiration, a summary of their plan, benefits, billing cycle, expiration date, and renewal status.
- **(Req)1.5.2 Transaction History**
    - The user shall be able to view a complete history of past transactions, including the date of payment, amount paid, and method of payment.
    - The downloadable receipts included in every transaction entry shall be available for personal record-keeping by the users or for expense tracking.
- **(Req)1.5.3 Subscription Modification**
    - The user shall be able to view all subscription packages, pricing options, and their respective features. The user shall be able to cancel a subscription, renew an existing subscription, or buy a subscription.
    - As of now, the subscription options include choosing between a monthly pricing of $10 per month or yearly pricing at $100 per year. With a subscription, users get access to the budget planning tool and certian learing resources. Once the subscription is made, the user shall get immediate access to those features.
- **(Req)1.5.4 Payment Management**
    - The user shall be able to subscribe by using either PayPal, Stripe, or credit cards-Master Card or Visa. Data shall be secured based on the vendor's security options: for example, PayPal uses 128-bit SSL.
    - Payment history collected shall include amount, date, relevant payment information-such as credit card information or PayPal information, and shall be recorded in the database.
    - The user shall be able to activate auto-renewal via a check box on the menu. In this case, the website would have permission to access stored payment information automatically at any point in time to purchase subscriptions. This shall able to be turned off by de-selecting the same auto-renew box.
- **(Req)1.5.5 Payment Security**
    - In addition to vendor specific security standards, transactions shall be secured as per the PCI-DSS standards.

### **(Req)1.6 Interaction History**

- **(Req)1.6.1 Consultation History**
    - The date and time, name of advisor, and rating of an advisor shall be stored in the database after a meeting for future reference in the profile of the user.
    - The customer shall be able to rate the advisor on a scale of 1-10, which shall be visible in the advisor's profile and the particular user's profile which shall be visible only to the user or administrators.
    - Any files the counselor creates and uploads via SFTP to the server shall be downloadable from the consultation history entry in the customer profile.
- **(Req)1.6.2 Event Participation History**
    - The date, time, and name of the event shall remain in the database after the event attendance and will be displayed for later reference in the user's profile.
    - Any documents posted by an event organizer via SFTP shall be downloadable from the event history entry in the user profile.

### **(Req)1.7 Advisor Management**

- **(Req)1.7.1 Advisor Management System**
    - The system shall allow advisors to view, previous client interaction, including dates, name of client, and client rating.
    - The system shall allows the Advisor to block off dates and times they will not be available for consultation.
    - Advisors shall be able to calendar (Google calendar or Outlook) allows the advisors to select time slots when they are available for consultation. They can "Available", "Busy, or "Out of Office" a time with date and time.
    - Advisors shall be able to set up reoccurring availability slots (e.g. Every Monday from 10:00 AM to 2:00 PM).
    - Any change in the availability, like adding or removing slots, shall be replicated in real time to the client-side booking interface for the most up-to-date scheduling options.
- **(Req)1.7.2 Advisor Account Creation**
    - In addition to the user account requirements, account creation for advisors shall be only available via an administrator. An administrator must approve an admin account before it’s integration into the system.
    - Once the necessary information is submitted, an advisor's profile is automatically set to "Pending Approval," wherein the admins verify the credentials provided.
- **(Req)1.7.3 Administrator Verification**
    - In the dashboard, administrators shall have access to all advisor applications. Administrators shall be able to approve or reject an advisor account. After approval by the admin, the account shall be allows to be created.
    - Applications rejected shall automatically trigger an email including the reasons for rejection, along with further action required.

### **(Req)1.8 Messaging and Notifications**

- **(Req)1.8.1 In-App Messaging**
    - The system shall allow users to securely message other users and advisors within the website. Chat shall allow sharing of files and text
    - The messaging interface shall allow the user to send and receive messages in real-time, showing the typing indicator, read receipt, and timestamp of messages.
- **(Req)1.8.2 Message Encryption**:
    - Messages shall be end-to-end encrypted to protect users' privacy using TLS. Messages shall be saved to for 3 months before they are deleted automatically.
    - Users shall be able to archive or delete conversations.
- **(Req)1.8.3 Notifications and Alerts**
    - Events to be notified include appointment reminders, new messages, renewals, and upcoming events.
    - Notifications come via in-app, email, or SMS, whichever is preferred by the user. In this respect, different options provide a guarantee that no user will miss any updates, since at least one of the means of communication will be preferred.
- **(Req)1.8.4 Message settings**
    - The system shall allow users to personalize notification settings to include or exclude certain alerts. For instance, users may want to receive consultation reminders and not marketing emails.
    - As events approach, the system shall send reminders via SendGrid (email) reminding the user of the date and time the event will be held, whether virtually or physically.

---

## **(Req)**2. Financial Tools and Calculators

The various financial calculators allows the user access to use tools to have informed financial decisions.

### **(Req)**2.1 Loan Interest Calculator

The loan calculator is an easy way for users to become educated about what their loan will cost over time.

- **(Req)2.1.1 User Input**
    - User shall be able to provide a loan amount, interest rate, loan term in years or months, and frequency of payments.
    - The system shall only take numeric values and shall require the user to fill out all fields before it begins calculation.
- **(Req)2.1.2 Calculation**
    - The system shall utilize the input values to calculate the monthly payment, total interest paid, and amortization schedule. The amortization schedule shall also break down each payment into principal and interest, it would allow users to see how this repayment structure changes over time.

### **(Req)2.2 Mortgage Calculator**

The Mortgage Calculator allows the user to calculate how much it is going to cost every month to buy a home.

- **(Req)2.2.1 User Input**
    - The user shall be able to input home price, down payment amount or in percent, interest rate, and loan term in years.
    - The system shall check for input validity (numbers only) and offers a choice between fixed-rate or adjustable-rate mortgages.
- **(Req)2.2.2 Calculations**
    - The system shall calculate the monthly mortgage payment, total interest paid, and total cost of the loan, with consideration of a down payment.
    - The system shall also allow users to view how changing the down payment alters the monthly payment and total amount paid via an input value that will recalculate the total cost of the mortgage.
- **(Req)2.2.3 Detailed Outputs**
    - The system shall display a payment schedule that itemizes the payment amount between principal and interest per payment.
    - The system shall, upon user request, show comparisons of how altering the percent down payment or interest rate for affects the user's per monthly payment.

### **(Req)2.3 Budgeting Tool**

The Budgeting Tool will allow the user to have full insight into his or her financial standing in order to allocate income accordingly and denote areas of possible savings.

- **(Req)2.3.1 User Input**
    - Users shall be able to fill in their various sources of income, fixed and varied, their expenses fixed and varied expenses, and savings goals.
- **(Req)2.3.2 Calculation Process**
    - The system shall categorize both income and expenses. The system shall calculate percentage of income spent in each expense category, and identifies categories in which the user may be over-spending based on data values set by the site’s advisors.
    - Increase Savings Recommendations - Based on user input of cost saving goals, the system shall make recommendations to improve savings using benchmarks provided by advisors - for example, no more than 30% of income on housing.

### **(Req)2.4 Retirement Planning Calculator**

The Retirement Planning Calculator forecasts the user's requirement for retirement and gives actionable insights based on the goals of personal savings.

- **(Req)2.4.1 User Input**
    - The system shall allow the user to enter their present age, expected retirement age, present savings, monthly contributions, and the expected rate of return.
- **(Req)2.4.2 Calculation Process**
    - The system shall compute total savings at retirement time, with compound interest factored in for the period under consideration.
- **(Req)2.4.3 Recommendations**
    - Should the system calculate that the users is not on target to achieve their retirement goals, the system shall recommend increasing monthly contributions or adjusting their retirement age.

### **(Req)2.5 Insurance Coverage Calculator**

The Insurance Coverage Calculator enables users to analyze their insurance requirements and possible shortcomings in the prevailing coverage.

- **(Req)2.5.1 User Input**
    - The system shall allow the user entered: age, number of dependents, current insurance coverage, and any other risks the user would want to covered.
- **(Req)2.5.2 Output Presentation**
    - The system shall calculate the amount of coverage required for various types of insurance, including, life, health, and disability.
    - The system shall also calculate gaps between the current and recommended coverage, and suggest purchasing additional policies where required.
    - The results should show recommended policy amounts, potential providers, and estimated premiums.

### 2.6. Student Loan

The student loan calculator functions to estimate monthly payments, total interest, and the overall cost of a student loan.

- **2.6.1 User input**
    - The user shall be able to provide details such as loan amount, interest rate, and repayment term.
- **2.6.2 Output**
    - The system shall provide an estimate of monthly payments, total interest, and overall cost, and allows for comparisons between different repayment plans.
    - Additionally, the calculator should factor in early repayment options to show how making extra payments can reduce the total interest and shorten the loan term.

### 2.7. Car Payment

The car payment calculator allows to estimate their monthly car payments, help users understand the total cost of the loan, including interest, and provide a clear picture of what their monthly payments will be.

- **2.7.1. User input**
    - The system shall allows the user to enter their loan amount, interest rate, loan term, and down payment.
- **2.7.2. Output**
    - The system shall show monthly payment, total interest paid, total loan cost, amortization schedule, payoff date, and impact of extra payments.
    - It also shall comparedifferent loan options and adjusting factors like loan length or down payment to find a manageable payment plan.

---

## **(Req)3. Financial Advisory System**

The **Financial Advisory System** shall provide the individual financial consultations with certified advisors.

### **(Req)3.1 Advisory Booking System**

An Advisory Booking System shall allow searching for advisors by availability and expertise and book consultations accordingly.

- **(Req)3.1.1 Search and Filter Options**
    - Users shall be able to filter the advisors on specializations, including retirement planning, investment strategy; ratings; availability; language; and cost per session.
    The results shall be sorted dynamically based on user preferences and advisor ratings, always reflecting the best matches for each user's needs.
- **(Req)3.1.2 Booking Process**
    - Once the selection of an advisor is made, it shall provide users with the facility to look at available time slots and choose when best for them.
    - The user shall be able to select a time slot from the implemented calendar system (Google Calendar or Outlook).
    - The appointment cost shall be clearly visible here, along with a cancellation policy and a brief on what one should expect during the session.
- **(Req)3.1.3 Confirmation and Reminders**
    - Automated emails at the time of booking a slot shall be generated for both user and the advisor.
    - Appointment details along with the time shall be shared via e-mail. Automatic reminders via email or phone shall be sent 24 hours and 1 hour before consultations avoid no-shows.

### **(Req)3.2 Consultation Sessions**

The consultation sessions may be in-person or virtual. Whichever mode of consultation is available depends upon the preference of the user and on the availability of the advisor.

- **(Req)3.2.1 In-Person Consultations:** The locations and directions shall be provided to the users in advance via Email (SendGrid) for sessions. The user Check-in shall also available through the mobile application.
- **(Req)3.2.2 Virtual Consultations**: Links provided for virtual consultation are secured via TLS and only visible to the particular user and advisor. Virtual sessions are encrypted via TLS for security and privacy; screen sharing, document sharing, or chart sharing shall be integrated during sessions.

---

## **(Req)**4. Market News and Financial Education

The web application keeps the user updated with relevant financial news and a knowledge base for teaching aids to keep them informed about making financially correct decisions.

### **(Req)**4.1 Market News

- **(Req)4.1.1 Content Aggregation**
    - The user shall be able to view news from various top sources, including financial news portals, stock exchanges, and leading economic indicators.
    - The system shall allows user to customize the news feed about desired topics: stock performance, to bond yields, new trends, and macro economics.
- **(Req)4.1.2 Real-time Updates**
    - Feeds shall be delivered in real-time so that users gain access to the most relevant current market information and analysis.

### **(Req)4.2 Learning Tools**

Learning tools introduce users to financial acumen and provide a fundamental tool for their further development.

- **(Req)4.2.1 Type of Contents**
    - Resources shall be sorted into budgeting, investing, retirement planning, and risk management categories. Each of these categories shall have articles to further an individual in knowledge, video tutorials, webinars, and interactive guides.
- **(Req)4.2.2 Interactive learning**
    - Quizzes, assessments, interactive activities, and practice scenarios shall allow users to test their knowledge. Learning progress is tracked in the system database to include activity completed by ID and date completed.
    - The user shall receive a certificate for certain learning pathways, like "Budgeting Basics."

---

## **(Req)5. Event Management System**

The Event Management System provides financial seminars, workshops, and webinars that give users an opportunity to learn more about personal finance and network with professionals.

### **(Req)5.1 Create and Manage Events**

- **(Req)5.1.1 Creating an Event**
    - The system shall allow organizers to create an event and input details including time, speaker, topic, and location-physical or virtual. The system will allow user registration, hence enabling the organizer to set limits on seats, ticket prices, and deadlines for registration.
    - The system shall implement a calendar view using Google Calendar or Outlook to allow event scheduling, modification, and deletion.
    - When the event registration deadline data passes, the system shall automatically “gray out” the event listing and close user registration.
- **(Req)5.1.2 Editing and Deleting Events**
    - At any point, organizers shall be able to change the details of events as listed in 5.1.1, and changes will be in real time for registered users and the calendar on the events page. In turn, events can be cancelled - which entails automated notifications and processes for refunding paid attendees.

### **(Req)**5.2 User Event Interaction

Users can search for, sign up to, and attend events both in-person and virtually.

- **(Req)5.2.1 Event Discovery**
    - Users shall be able to filter the event calendar events by date, topic, speaker, or event type; for example, webinar, in person. Events should be suggested based on user interests, past attendance, and subscription status.
    - User registration should be intuitive. Users shall be sent a confirmation email via SendGrid after having signed up.
- **(Req)5.2.2 Event Engagement**
    - Following events, attendees shall be able to view resources such as slides, recordings, and further readings by the speakers. Attendees shall be able to be sent feedback forms via email upon completion of the event for data collection and use in upcoming events.

---

## **(Req)6. Payment Processing System**

The Payment Processing System handles all matters dealing with money transaction processing, subscription payments, buying event tickets, and refunds.

### **(Req)6.1 Payment Gateway Integration**

Different integrated payment gateways provide the user with diverse options to make their payments.

- **(Req)6.1.1 Supported Gateways** Users shall be able to make payments using credit/debit cards, PayPal, or Stripe.
- **(Req)6.1.2 Secure Transaction Handling** All transactions shall be encrypted following the standards of PCI-DSS compliance and any standards used by the vendor (ex. PayPal uses 128-bit SSL), ensuring protection of data at all levels.
- **(Req)6.1.3 Error Handling** Should a payment fails or subscription allocation fail, any transaction will be fully cancelled (the resource not allocated, and any transferred money cancelled), an error message displayed, and a prompt to retry displayed. The user shall be able to retry the payment immediately after the transaction is fully cancelled.

### **(Req)**6.2 Transaction Management

Transaction management ensures transparency in record keeping, and offers access to full payment history.

- **(Req)6.2.1 Invoicing and Receipts**
    - Automated invoices and receipts for every successful transaction shall be sent to users via email (SendGrid), which are archived in the user's profile via storage in the database, storing date of transaction, payment amount, vendor payment details, and item purchased. Said information shall be visible in the user’s profile and shall be downloadable at any time.
- **(Req)6.2.2 Refunds and Cancellations**
    - Refunds shall be possible through the vendor’s system as applicable/possible by set policies. A successful refund shall be noted in the transaction history for the amount refunded and sends notifications via email (SendGrid) to the users.

---

## **(Req)7. Reporting and Analytics**

The system shall implement system for reporting user analytics to depict user activities and platform engagement for users and administrators as appropriate..

### **(Req)7.1 User Reports**

- **(Req)7.1.1 Financial Reports**
    - Users shall be able to generate progress reports in the budget calculator, and use said reports to gauge progress towards their financial goals. Such reports include graphs that analyses user income vs expenses, home mortgage payment percentage overtime, and retirement investments over time.
- **(Req)7.1.2 Customization Options**
    - Users shall be able to generate custom reports by selecting any particular period, financial category, or goal.

### **(Req)**7.2 Administrative Analytics

The system shall implement an administrator's dashboard that shows the administrator the performance of the platform along with the behavior of the users.

- **(Req)7.2.1 Usage Metrics of the Platform**
    - An administrator shall be able to monitor active user numbers, daily logins, consultation rates, and event attendance. Further growth metrics include new user registrations, subscriptions, and revenue trends to give a high-level view of the performance of the platform. Reports shall be generated by querying the database for relevant data and compiling the relevant statistics.
        - Passwords shall be hashed using MD5 and salted before storage. Even in the event of a database breach, encrypted passwords cannot be used by an attacker. An encrypted data breach is not a data breach.
- **(Req)7.2.2 Tracking Revenue**
    - An administrator shall be able to generate reports on income from subscriptions, event tickets sold, and transaction volume are available to administrators. Revenue data shall be  further categorized by source, time period, and user segment, making it supportive for strategic decisions. Reports shall be generated by querying the database for relevant data and compiling the relevant statistics.

# 5.2 Non-Functional Requirements

---

## **(Req)**8. Security

WealthWise operates or will operate under sensitive financial information. Thus, security forms the basis of this site. This section analyses how the system will protect data in order to gain and uphold user trust.

### **(Req)**8.1 Encryption

- **(Req)8.1.1 Data at Rest**
    - All sensitive data including but not limited to: user credentials, personal information, financial data, and logs of communication shall be encrypted using state-of-the-art encryption algorithms, e.g., AES-256.
    - Said database encryption shall take place on the server to assure data security against unauthorized access.
- **(Req)8.1.2 Data in Transit**
    - Any data exchanged between the client and the server shall be over SSL/TLS protocols. Thus, no useable interception of the data can occur during transmission.
    HTTPS will be used to impose secure communication among all pages.
    Vulnerability scans using software such as NESSUS will make sure that periodic identification of any weakness within the data transmission process is identified and takes measures to remove them.

### **(Req)**8.2 Access Control

The system shall be capable of enforcing most rigid access controls in order for sensitive information and functionalities to be provided only to users who are duly authorized for the same purpose.

- **(Req)8.2.1 Role-Based Access Control (RBAC)**
    - RBAC shall assign different designations to various roles, such as client, advisor, admin, and many more.
    - The users shall only see features that are assigned to their role; therefore, controlling functions or unauthorized access.
- **(Req)8.2.2 Session Management**
    - The session tokens shall time limited and will re-prompt authentication after long periods of inactivity.
    - Session tracking shall be implemented, which checks concurrency of session from different IPs and asks confirmation from user.
- **(Req)8.2.3 Audit Logs**
    - All user activities, particularly modifications of sensitive data, shall be logged in an event viewer, such as Security Onion.
    - Logging shall monitor the following activities attempts at logging on, password changes, profile data changes, transactions. Logs will record the time, user, IP address, port numbers, action, and success or failure of said action.
    - Logs shall be stored on the server, susceptible to periodic inspection via a tool such as Security Onion in case of suspicion.

---

## **(Req)9. Accessibility**

The platform shall be made available to a wide range of users.

### **(Req)9.1 ADA Compliance**

- **(Req)9.1.1 Requirements Standards**
    - The platform shall be developed to meet the requirements for ADA and WCAG 2.1 compatibility. The system shall also be developed to meet or exceed the levels of compatibility required by WCAG 2.1 Level AA to ensure access without barriers in the platform by people with disabilities.
- **(Req)9.1.2 Screen Reader Support**
    - All user-facing content including forms, navigation elements, images, and buttons shall be compatible with screen readers. Descriptive alt text for images and ARIA labels for interactive elements will be provided so that screen readers can correctly interpret content.

---

## **(Req)10. Backup**

Backup mechanisms shall be implemented to ensure data integrity and platform availability and mitigated unexpected incidents.

### **(Req)10.1 Backup Strategies**

- **(Req)10.1.1 Manual**
    - The system shall provide manual backup options to allow system administrators to backup the system before a suspected incident, failed scheduled backup, or before a major system overhaul. The manual system backup shall be implemented with standard operating system commands, such as Window’s robust copy (robocopy) command.
- **(Req)10.1.2 Schedule**
    - Daily incremental and weekly full backups shall be able to be scheduled at the site administrator’s discretion, which shall create a full snapshot of both the database and file storage. This will ensure device failure or cyberattacks do not result in total data loss.

---

## **(Req)11. Performance and Scalability**

The platform shall be built to accommodate a large number of users and transactions without impacting the performance and responsiveness of the platform during peak conditions.

### **(Req)**11.1 Performance Optimization

The system needs to optimize performance so that interactions are fast and responsive, hence minimum delay and resultant dissatisfaction among end-users.

- **(Req)11.1.1 Response Time**
    - Maximum time elapsed before the system responds to any action made from the user shall not exceed more than 10 seconds under a normal load. On average, pages should load in 3 seconds. Database queries and calculations should take less than 10 seconds.
    - Caching mechanisms: Data that is often accessed, such as news feeds, educational resources, and user profiles, should be cached (in server memory or in local browsers as applicable) to return the responses quickly.
    - Asynchronous processing should be implemented for longer operations, such as data import and report generation.
    - Database indexing and query optimization should be implemented to speed up data retrieval and result in faster access times for user profile information, financial tools, and the history of transactions.

### **(Req)**11.2 CPU and Memory Usage

- **(Req)11.2.1 Objective**
    - The system shall utilize no more than 5% of a 2.3 GHz CPU per user session, and utilize less than 1 GB of RAM per session, keeping performance high even multiple client instances are running.
- **(Req)11.2.2 Load balancing**
    - Server capacity should be distributed across multiple servers to prevent any server to reach its maximum capacity and bottle necking the system.
    - Memory-intensive operations, such as printing large reports, should be run on a dedicated server to lighten the load on the web servers.

### **(Req)11.3 Concurrency**

- **(Req)11.3.1 Goal**
    - The platform shall be able to support up to 25,000 concurrent users without noticeably compromising its performance.
- **(Req)11.3.2 Implementation**
    - In real-time or near real-time services, such as instant messaging or event notification, WebSockets shall handle the connection to manage simultaneous connections properly. The application should use database connection pooling as a method to handle simultaneous requests to the database, reducing variability in performance due to high loads.

### **(Req)**11.4 Horizontal Scaling

- **(Req)11.4.1 Objective**
    - The system shall handle up to 25,000 users by adding capacity through horizontal scaling.
    - Separate servers should be implemented for independent components for user management, subscription management, and financial tools, all of which should be independently scalable.
- **(Req)11.4.2 Cloud infrastructure**
    - Cloud infrastructure, such as AWS should be utilized. New instances can easily be added if the system sees spikes in load. Auto-scaling mechanisms shall, if could infrastructure is implemented, dynamically apportion resources based on the traffic patterns that develop.

### **(Req)**11.5 Data Scaling

- **(Req)11.5.1 Requirement**
    - The database shall scale with the ever-increasing data load from users, advisors, transactions, logs, and content.
- **(Req)11.5.2 Implementation**
    - Large databases shall be partitioned using Sharding so the data will be distributed across several servers. Data archiving should be considered for data not utilized after 3 months to take the load off from the primary database, therefore allowing faster retrieval times of current data.

---

---

# **6. Log of Meetings, Reviews, and Meetings[sic]**

### 25 September 2024 - Virtual Team Meeting

Attendees: Draix, John, Norman, Sawyer

The team discussed the Introduction and Work Structure Breakdown sections of the Requirement Document following the reception of the Request of Proposal from the client. The team talked through initial thoughts and confusion about the requirements.

### 26 September 2024 - Client Meeting

Attendees: Draix, John, Norman, Sawyer, Dr. Albujasim

The team met with the client and discussed a fair portion of the requirements and initial insight into what types of diagrams were necessary and how the WSB should be developed.

### 7 October 2024 - In-Person Team Meeting

Attendees: Draix, John, Norman, Sawyer

The team met and started jointly filling out sections of the Introduction and started the design of the WSB. The team then assigned responsibility for the remaining sub-sections to its members.

### **8 October 2024 - Client Meeting**

Attendees: Draix, John, Norman, Sawyer, Dr. Albujasim

The team met with the client and discussed the full feature list the website should implement. The team also gained additional insight into how the client wanted the Proposed System Overview and the Work Structure Breakdown to be formatted and developed. The team agreed to work asynchronously on the remaining sections and meet virtually before submitting the increment of the RD known as “Assignment 2”

### 9 October 2024 - Virtual Team Meeting

Attendees: Draix, John, Norman, Sawyer

The team met to review the final changes to the remaining sections of the Introduction and WBS before the final submission the next day.

### 18 October 2024 - Virtual Team Meeting

Attendees: Draix, John, Norman, Sawyer

The team met to review the full requirements for the RD. Initial thoughts for how the requirements needed to be specified were considered and the next meeting time was set up. 

### 21 October 2024 - In-person Team Meeting

Attendees: Draix, John, Norman, Sawyer

The team met and began jointly filling out all sections of the RD. Most notably, initial versions of all requirements were filled out. All remaining sections were assigned to members to be worked on Asynchronously.

### 22 October 2024 - Client Meeting

Attendees: Draix, John, Norman, Sawyer, Dr. Albujasim

The team met with the client to discuss the depth of specification for the final requirements. Questions concerning Change Control, Meeting Review, and Terms and Conditions were also discussed. The team decided to finish the RD asynchronously and meet virtually before submitting the “final” RD.

### 23 October 2024 - Team Meeting

Attendees: Draix, John, Norman, Sawyer

The team met and reviewed the final changes to the RD before the RD was submitted to the client.

---

# 7. Change Control

Change requests shall propagate from meetings with the client or upon written notification from the client. Potential changes to the Requirements Document shall be requested, negotiated, specified, and validated as necessary. Once this is complete, the Requirements Document shall be updated to reflect the specified changes, and an entry in the “Log of Meetings, Reviews, and Meetings[sic]” section shall be made detailing the changes to the requirements, the date of the change, and any relevant data, such as revision of cost estimate.

---

# 8. Appendix

## 8.1 Work Structure Breakdown

![SE 305 - Work Breakdown Structure.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/c3de0b01-90b9-416a-8720-fa2c2feacd77/SE_305_-_Work_Breakdown_Structure.png)

## 8.2 ER Diagram

![Wealthwise ER Diagram.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/a381500a-442f-4ac7-8852-b588d9ff98a7/Wealthwise_ER_Diagram.png)

## 8.3 Data Flow Diagram

![SE 305 - Data flow diagram.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/fbbfcb96-3500-4a71-abea-50c4e8cdb7b3/SE_305_-_Data_flow_diagram.png)

https://www.figma.com/board/V6dnjsxDZXoo3r9OuhEHsB/SE-305---Project?node-id=0-1&t=gbVGcPtO5FHmWHHq-1

---

# **9. Terms and Conditions**

These Terms and Conditions (“Agreement”) constitute a binding contract between the client and Arqer (“Service Provider”) for the use of our services to develop software as outlined in this Requirements Document.

Party A (Client):

Legal entity’s name: _____________________________________________________

Party B (Service Provider):

Legal entity’s name: Arqer Software Development Agency

## (9.)1. **Scope of Work**

### (9.)1.1 **Services Provided**

- The developer team agrees to design, develop, assess, and deploy the software system as specified in the RD document.
- All work shall be performed according to the specifications and timelines mutually agreed upon by both parties.

### (9.)1.2 **Change Requests**

- Any modifications or additions to the project scope shall be documented and approved in writing by both parties.
- Additional work arising from change requests should result in adjustments to the project timeline and costs.

## (9.)2. **Project Timeline**

### (9.)2.1 **Milestones**

- The project shall follow a schedule of milestones, each with specific deliverables and deadlines.
- Both parties agree to adhere to the project timeline unless modifications are mutually agreed upon.

### (9.)2.2 **Delays**

- The Developer shall promptly inform the Client of any circumstances that may delay the project.
- Delays caused by the Client, including late approvals or feedback, should result in timeline adjustments.

## (9.)3. **Payment Terms**

### (9.)3.1 **Fees and Invoicing**

- The total project cost is $0, payable in installments as follows:
    - **20%** upon signing this Agreement.
    - **30%** upon completion of the initial prototype.
    - **50%** upon final delivery and acceptance.

### (9.)3.2 **Payment Schedule**

- Invoices shall be issued according to the milestone completions.
- Payments shall be paid within 7 days of invoice receipt.

### (9.)3.3 **Additional Costs**

- Any additional expenses incurred due to scope changes or Client requests shall be billed separately with prior approval.

## (9.)4. **Intellectual Property Rights**

### (9.)4.1 **Ownership**

- Upon full payment, all intellectual property rights for the developed software, including source code and documentation, shall transfer to the Client.

### (9.)4.2 **Developer's Tools**

- The Developer shall retain ownership of any pre-existing materials or generic modules used in the project, provided they do not contain the Client's proprietary information.

## (9.)5. **Confidentiality**

### (9.)5.1 **Non-Disclosure**

- Both parties agree to keep all confidential information strictly confidential and not disclose it to any third parties without prior written consent.

### (9.)5.2 **Data Protection**

- The Developer must implement industry-standard security measures to protect the Client's data.

## (9.)6. **Warranties and Liabilities**

### (9.)6.1 **Warranty and Maintenance Period**

- The Developer offers a warranty period of 1 month from the date of final acceptance, or until the end of the course, whichever comes first, during which any defects will be corrected at no additional charge.

### (9.)6.2 **Limitation of Liability**

- The Developer's total liability under this Agreement shall not exceed the total fees paid by the Client.

## (9.)7. **Maintenance and Support**

### (9.)7.1 **Post-Deployment Support**

- Maintenance and support services beyond the warranty period should be provided under a separate agreement.

### (9.)7.2 **Updates and Upgrades**

- Any updates or upgrades requested by the Client shall be subject to additional fees and timelines.

## (9.)8. **Termination**

### (9.)8.1 **Termination by Client**

- The Client may terminate this Agreement with a 30-day written notice. Fees for services rendered up to the termination date shall be paid immediately.

### (9.)8.2 **Termination by Developer**

- The Developer may terminate this Agreement if the Client fails to make payments or breaches any terms, with a 30-day written notice.

## (9.)9. **Dispute Resolution**

### (9.)9.1 **Negotiation**

- Both parties agree to attempt to resolve disputes through mutual negotiation.

### (9.)9.2 **Arbitration**

- If negotiation fails, disputes will be settled by arbitration in accordance with the rules of the state of South Dakota.

## (9.)10. **Governing Law**

- This Agreement shall be governed by and construed in accordance with the laws of the state of South Dakota.

## (9.)11. **Force Majeure**

- Neither party shall be liable for delays or failures due to causes beyond their reasonable control, such as natural disasters, war, or government actions.

## (9.)12. **Entire Agreement**

- This Agreement constitutes the entire understanding between both parties and supersedes all prior agreements, whether written or oral.

## (9.)13. **Amendments**

- Any amendments to this Agreement shall be made in writing and signed by both parties.

## (9.)14. **Severability**

- If any provision of this Agreement is found to be unenforceable, the remaining provisions shall remain in effect.

## (9.)15. **Notices**

- All notices shall be in writing and delivered to the addresses provided by both parties.

---

**By signing below, both parties acknowledge that they have read, understood, and agree to the terms and conditions outlined in this Agreement.**

### **Party A’s Representative**

- **Name**: _______________________________
- **Title**: ________________________________
- **Signature**: ____________________________
- **Date**: _________________________________

### **Party B’s Representative**

- **Name**: _______________________________
- **Title**: ________________________________
- **Signature**: ____________________________
- **Date**: _________________________________

---

---

View the document here: [Arqer_Project.docx](https://jackssdstate-my.sharepoint.com/:w:/r/personal/nguyentrung_nguyen_jacks_sdstate_edu/Documents/1.%20On%20Going/SE%20305%20-%20Foundations%20of%20Software%20Engineering/Assignments/Arqer/Arqer_Project.docx?d=wce1df6a987e449d7ac2fa4bdaefa9951&csf=1&web=1&e=Vj3YYI)

PDF here: 

[Arqer_Project.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/4b6a3c18-8556-4a5f-9342-51b171258d4c/7ce6a55f-b6fa-494b-8444-cf622620d6ec/Arqer_Project.pdf)