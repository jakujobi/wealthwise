https://jackssdstate-my.sharepoint.com/:w:/g/personal/nguyentrung_nguyen_jacks_sdstate_edu/EbdGGzzD0jRDujYvMFowCdkB_ayq2lzSS449rV76n9ys-g?e=Yut838

# Introduction - Sawyer

## Purpose of Acceptance Test

This document is to be used upon the completion of the program. The ATP aims to outline our strategy and methods to ensure our program satisfies the requirements. It acts as a way to catch and correct faults before final deployment. It also serves the purpose of verifying that the program is what the end-user and stakeholders actually want. By completing the ATP, the team can be assured that we have properly completed our contract. 

## Proposed System Overview or Configuration Chart

Our system is broken into five main apps that can be navigated from the navigation bar. The calculations app contains each financial calculation, including the budgeting tool. The scheduling app includes all the tools advisors need to make, edit, and delete events. Users also register for events through the scheduling app. The learning hub app redirects users to a separately hosted service that hosts the learning hub content. The admin app allows admins to edit any data in the database and create advisors. The user's apps enable new users to register or existing ones to log in and out. It also allows users to edit their account settings and subscriptions. The chart below shows how the website pages for these apps are represented on the website.

![image.png](attachment:71e31ce8-f947-4081-a035-2082848a0dce:image.png)

## Definitions, Acronyms, and Abbreviations

## Testing Principles Used

The test cases are all designed using black box testing, meaning the code was only examined after an error was identified. Black box testing was chosen over white box testing because it closely simulates how a user interacts with the system, ensuring that functionality aligns with requirements without bias from the implementation details. This approach allows testers to focus on output rather than code structure. 

Error guessing will be used to determine what fields to input for each test case. Error guessing relies on the developer’s intuition to identify potentially problematic areas. This approach saves time by avoiding writing and executing a comprehensive set of test cases. While it may allow some errors to slip through, the focus of this program prioritizes speed and feature development overachieving zero defects.

## Overview of Rest of ATP

This document outlines test cases to verify whether the program meets its requirements. It also includes details on the hardware and software used during testing, which may be relevant for troubleshooting future errors. Additionally, it provides a test schedule to establish the order and deadlines for test completion. Finally, a section is included for client and developer review and approval once testing is complete.

---

---

# Hardware and Software used for testing

To make sure our acceptance test activities are consistent, reliable, and reproducible, we shall do evaluations within a controlled and clearly defined hardware and software environment.

| **Category** | **Details** |
| --- | --- |
| **Operating Systems** | Windows 11 Pro (Versions 23H2 and 24H2) |
| **Web Browsers** | Mozilla Firefox ^136.0, Microsoft Edge ^122.0, Google Chrome ^122.0 |
| **Hardware Specs** | Intel Core i7 @ 2.3GHz, 16GB RAM, 1920x1080 screen resolution |
| **Mobile Devices** | Android 13 emulator (Pixel 6) on DevTools |
| **Network Environment** | Stable 100 Mbps Wi-Fi; latency simulation via Chrome DevTools |
| **Testing Tools** | Manual UI testing using browser DevTools; internal test logs and reports |
| **Development Tools** | GitHub (source control), Localhost test environments, PgAdmin, PostgreSQL |

## Operating Systems

We shall perform all tests using Microsoft Windows platforms, reflecting the intended production environment and what our customers shall most likely use. Specifically, we shall use:

- Windows 11 Pro, Version 23H2
- Windows 11 Pro, Version 24H2

These versions shall allow us to validate compatibility across both stable and near-future releases. They shall also be readily available to our team.

---

### Web Browsers

To validate cross-browser compatibility and ensure a consistent user experience, we shall manually test the platform using these browsers:

- Mozilla Firefox, Version ^136.0
- Microsoft Edge, Version ^122.0
- Google Chrome, Version ^122.0.6261.111

These browsers shall represent the most commonly used environments by our target users. We shall use the default browser settings unless a test requires specific conditions, such as incognito mode or cleared cache.

---

### Hardware Specifications

We shall do all tests on machines that meet or exceed the following baseline hardware specifications:

- Processor: Intel Core i7 (2.3GHz, Quad-Core)
- RAM: 16 GB
- Display Resolution: 1920×1080 (Full HD)
- Graphics: Integrated Intel Graphics or equivalent

These configurations shall enable us to run all platform features smoothly, including complex user interfaces, real-time interactions, and analytics dashboards.

---

### Network Conditions

Our tests shall be done using the SDSU Student and Faculty networks. This stable local network environment shall closely mirror the typical company Wi-Fi that our users might use. Our setup shall include:

- Connection Type: Secure Wi-Fi
- Internet Speed: 100 Mbps broadband
- Latency Testing: Simulated using Chrome DevTools to throttle network speeds and emulate slower connections

This approach shall help us identify latency-related issues and monitor system responses under constrained conditions.

---

### Testing Tools and Methodology

We shall base our testing strategy on structured manual testing and use several tools to support the process:

- Browser DevTools: To monitor network activity, debug errors, and inspect DOM elements
- Localhost Server: We shall host most modules on `localhost:8000` for test execution
- GitHub: For source control and release version tracking
- Jira: To log bugs, document test results, and coordinate issue resolution
- Internal Test Logs: Maintained by each tester to track inputs, outputs, and observations

---

This controlled environment shall make sure our tests are valid, reproducible and mirror that of real user experiences after production.

---

# Test Schedule and Test Sets

| Test # | FWBS # | Test Name | Test Description | Who | Date | P/F |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | 1.1 | User registration | This test ensures the user can successfully register an account, passwords can be tested, and email verification is successful. | Draix | Apr. 30 |  |
| T2 | 1.2 | User login | This test ensures the user can successfully re-authenticate with valid credentials. | Draix | Apr. 30 |  |
| T3 | 1.3 | Password recovery | This test ensures the user can change a their password by with access of their registered email. | Draix | Apr. 30 |  |
| T4 | 1.4 | Profile Management | This test ensures the user can update their profile with relevant information and advisor specific fields are only present for advisors. | Draix | Apr. 30 |  |
| T5 | 1.5 | Subscription Management | This test ensure the user can see their subscription status and transaction history. Additionally, this test ensures payments can be made to purchase a subscription. | Draix | Apr. 30 |  |
| T6 | 1.6 | Interaction History | This test ensures the user can see their event and consultant history. | Draix | Apr. 30 |  |
| T7 | 1.7 | Advisor management system | This test ensures an advisor can be added by an administrator and can be managed by admins as needed. | Draix | Apr. 30 |  |
| T8 | 1.8 | Messaging and Notification | This test ensures in app messages and notifications as well as email notifications are working. | Draix | Apr. 30 |  |
| T9 | 3.1 | Advisor Booking System | This test ensures the advisor booking system for users allow users to search, filter, ensure confirmation and reminder. | Sawyer | Apr. 30 |  |
| T10 | 3.2 | Virtual Consultation Session | This test checks if the creation of virtual consultation sessions and their virtual meetings links are functioning well. | Sawyer | Apr. 30 |  |
| T11 | 5.2 | Event Integration | This test checks if the event registration system allows users to lookup and register for event. | Sawyer | Apr. 30 |  |
| T12 | 5.1 | Create and manage event | This test ensures that event creation, editing, and deleting is functioning for advisors.  | Sawyer | Apr. 30 |  |
| T13 | 6.1 | Payment Gateway Integration | This test ensures that the system can handle all matters dealing with money transaction processing, subscription payments securely and properly. | Norman | Apr. 30 |  |
| T14 | 6.2 | Transaction Management | This test ensures the system returns the correct invoice and receipts to the user. Additionally, check if the user can initiate a refund or cancellation. | Norman | Apr. 30 |  |
| T15 | 7.1 | User Reports | Test if the system can create a full financial reports and customize report options of a user. | Norman | Apr. 30 |  |
| T16 | 7.2 | Administrative Analytics | This test ensure the admin be able to monitor and create report about user metrics, system analytics such as active user number, consultation rates, platform performance… And admin also can generate reports on system metrics in income and health. | Norman | Apr. 30 |  |
| T17 | 2.1 | Loan Calculator | Validates that users can input loan terms to calculate accurate monthly payments, total interest, and overall loan cost with a visual breakdown of principal vs. interest. | John | Apr.30 |  |
| T18 | 2.2 | Mortgage Calculator | Validates that users can input loan terms to calculate accurate monthly payments, total interest, and overall loan cost with a visual breakdown of principal vs. interest. | John | Apr.30 |  |
| T19 | 2.4 | Retirement Calculator | Ensures that users can project retirement savings based on current age, contributions, and expected returns, and receive feedback on meeting retirement goals. | John | Apr.30 |  |
| T20 | 2.3 | Budgeting Tool | Checks that users can enter income and expenses to generate a monthly surplus/deficit, track savings progress, and receive warnings for overspending. | John | Apr.30 |  |
| T21 | 2.5 | Insurance Calculator | Ensures the system can estimate life insurance coverage needs by evaluating income replacement, debt payoff, education costs, and existing policy coverage. | John | Apr.30 |  |
| T22 | 2.6 | Student Loan Calculator | Confirms users can evaluate student loan repayment options and see the effect of extra payments on interest savings and payoff timeline. | John | Apr.30 |  |
| T- | 2.7 | Car Payment Calculator  | Verifies car loan calculations based on vehicle price, trade-in value, taxes, and fees, and displays monthly payment and total cost with a breakdown. | John | Apr.30 |  |
| T- | 2 | Calculator responsiveness | This test ensures that all calculator interfaces are responsive and function correctly across different devices and screen sizes. | John | Apr. 30 |  |
| T23 | 4.1 | Market News | This test ensures that the learning module displays the latest financial news articles from external news APIs, providing users with up-to-date market information. | John | Apr.30 |  |
| T24 | 4.2 | Learning Module | This test ensures that the learning module blog integrates properly with the main WealthWise platform, and that it displays the main blog homepage with featured articles, categories, and navigation elements. | John | Apr.30 |  |
|  |  |  |  |  | Apr.30 |  |
|  |  |  |  |  | Apr.30 |  |
|  |  |  |  |  | Apr.30 |  |

---

# Error Handling Policy - Draix

If a test case fails, developers must document the failed test number(s), error messages, and relevant details. Upon completing the acceptance test, they should identify any product issues.

Developers have 48-72 hours to resolve these issues, after which another acceptance test is scheduled with the client. This follow-up test will repeat all cases—both failed and passed. The cycle continues until the product passes all tests or gains client approval.

Errors should be mitigated through the outlined error handling methodology:

**Back-end:**

- Use try-except blocks to catch and log critical errors.
- Implement logging for debugging and monitoring.
- Validate user inputs to prevent database errors and security issues.

**Front-end:**

- Utilize error boundaries in React to handle UI errors.
- Display user-friendly error messages for input validation, API failures, and connectivity issues.

---

# Individual Test Cases

## 1. User Management System

## **T1. User Registration (FWBS 1.1)**

| Test Number | T1 |
| --- | --- |
| Test Module | User Registration |
| F/S(WBS) number | 1.1 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the user can successfully register an account, passwords are verified, and email verification is preformed.

**Setup:** Navigate to the “User Registration” page. This can be achieved by clicking “Register” on the navigation bar. You will now be presented with the user registration page. Enter the relevant data, check “I agree to the Terms of Service and Privacy Policy”, and click “Register” when complete.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser |
| Password | 1qazXSW@ |
| Confirm Password | 1qazXSW@ |
| Agree to TOS | Yes |

Output: Successful user account creation.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser |
| Password | 1qazXSW@ |
| Confirm Password | 2123qazXSW@2 |
| Agree to TOS | Yes |

Output: User entity will not be created - passwords do not match.

| **Input Label** | **Data** |
| --- | --- |
| Username | TakenUser |
| Password | 1qazXSW@ |
| Confirm Password | 1qazXSW@ |
| Agree to TOS | Yes |

Output: User not created - an account with this username already exists.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser |
| Password | 1qazXSW |
| Confirm Password | 1qazXSW |
| Agree to TOS | Yes |

Output: User not created - password requirement not met, missing at least one special character.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser |
| Password | 1qazXSW@ |
| Confirm Password | 1qazXSW@ |
| Agree to TOS | No |

Output: User not created - terms of service and privacy policy not agreed to. Prompt the user to agree with them.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T2. User login (FWBS 1.2)**

| Test Number | T2 |
| --- | --- |
| Test Module | User login |
| F/S(WBS) number | 1.2 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the user can successfully re-authenticate with valid credentials.

**Setup:** Navigate to the “User Login” page. This can be achieved by clicking “Login” on the navigation bar. You will now be presented with the user login page. Enter the relevant data and click “Login” when complete.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser |
| Password | 1qazXSW@ |

**Output:** User successfully logged in.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser |
| Password | 1qazXSW@2 |

**Output:** User will not be logged in - username and password do not match.

| **Input Label** | **Data** |
| --- | --- |
| Username | ExUser765456765 |
| Password | 1qazXSW@ |

**Output:** User will not be logged in - username and password do not match.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T3. Password recovery (FWBS 1.3)**

| Test Number | T3 |
| --- | --- |
| Test Module | Password recovery |
| F/S(WBS) number | 1.3 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the user can change their password with access to their registered email.

**Setup:** While on the “user login” page, click on the “Forgot Password” link. A link will be sent to the email on file for that username. Follow the link in the email to the password reset page. Enter your New Password and the Confirm Password and click “Reset Password”.

| **Input Label** | **Data** |
| --- | --- |
| Password | 2wsxCDE# |
| Confirm Password | 2wsxCDE# |

**Output:** Password successfully reset.

| **Input Label** | **Data** |
| --- | --- |
| Password | 2wsxCDE# |
| Confirm Password | 2wsxCDE#2 |

**Output:** Password not reset - passwords entered do not match.

| **Input Label** | **Data** |
| --- | --- |
| Password | 2wsxCD |
| Confirm Password | 2wsxCD |

**Output:** Password not reset - password does not meet requirements.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T4. Profile Management (FWBS 1.4)**

| Test Number | T4 |
| --- | --- |
| Test Module | Profile Management |
| F/S(WBS) number | 1.4 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the user can update their profile with relevant information hand advisor specific fields are only present for advisors.

**Setup:** Navigate to the “User Profile” page by clicking “Profile” on the navigation bar. Next, click “Edit Profile”. Enter any relevant information you wish to change. Click “Save”.

| **Input Label** | **Data** |
| --- | --- |
| Account Type | User |
| email | my.test.email@email.com |
| Advisor Field Present | No |

**Output:** Advisor fields not present; email updated to my.test.email@.email.com

| **Input Label** | **Data** |
| --- | --- |
| Account Type | Advisor |
| email | my.test.email@email.com |
| Advisor Field Present | Yes |

**Output:** Advisor fields present; email updated to my.test.email@email.com

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T5. Subscription Management (FWBS 1.5)**

| Test Number | T5 |
| --- | --- |
| Test Module | Subscription Management |
| F/S(WBS) number | 1.5 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the user can see their subscription status and transaction history. Additionally, this module ensures payments can be made to purchase a subscription.

**Setup:** From the “User Profile” page, click “Subscription” on the left side of the page. Click “Transaction History” or “Subscribe” as relevant.

| **Input Label** | **Data** |
| --- | --- |
| Subscribed | Yes |
| Transaction History Clicked | No |
| Subscribe Clicked | No |

**Output:** No payment history data shown; no payment fields shown; subscription status is shown: "subscribed”.

| **Input Label** | **Data** |
| --- | --- |
| Subscribed | No |
| Transaction History Clicked | No |
| Subscribe Clicked | No |

**Output:** No payment history data shown; no payment fields shown; subscription status is shown: "You have not subscribed”.

| **Input Label** | **Data** |
| --- | --- |
| Subscribed | No |
| Transaction History Clicked | Yes |
| Subscribe Clicked | No |

**Output:** Payment history data shown; no payment fields shown; subscription status is shown: “not subscribed”.

| **Input Label** | **Data** |
| --- | --- |
| Subscribed | No |
| Transaction History Clicked | No |
| Subscribe Clicked | Yes |

**Output:** No payment history data shown; payment fields are shown; subscription status is shown: “not subscribed”.

**Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T6. Interaction History (FWBS 1.6)**

| Test Number | T6 |
| --- | --- |
| Test Module | Interaction History |
| F/S(WBS) number | 1.6 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the user can see their event and consultant history.

**Setup:** From the “User Profile” page, click “Interaction History”.

| **Input Label** | **Data** |
| --- | --- |
| Event History Data Present | Yes |
| Consultation History Data Present | Yes |

**Output:** Data for all events and consultations shown.

| **Input Label** | **Data** |
| --- | --- |
| Event History Data Present | No |
| Consultation History Data Present | Yes |

**Output:** Data for all consultations shown. “No Event History” is shown.

| **Input Label** | **Data** |
| --- | --- |
| Event History Data Present | Yes |
| Consultation History Data Present | No |

**Output:** Data for all events shown. “No Consultation History” is shown.

| **Input Label** | **Data** |
| --- | --- |
| Event History Data Present | No |
| Consultation History Data Present | No |

**Output:** “No Consultation History” shown. “No Event History” is shown.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T7. Advisor management system (FWBS 1.7)**

| Test Number | T7 |
| --- | --- |
| Test Module | Advisor management system |
| F/S(WBS) number | 1.7 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures an advisor can be added by an administrator and can be managed by admins as needed.

**Setup:** Navigate to the admin page by going to “localhost:8000/admin” and login with admin credentials. Click on the user you wish to modify.

| **Input Label** | **Data** |
| --- | --- |
| StaffStatus | No |
| ChangeToStaff | Yes |
| DeleteUser | No |

**Output:** User will be promoted to advisor.

| **Input Label** | **Data** |
| --- | --- |
| StaffStatus | No |
| ChangeToStaff | No |
| DeleteUser | No |

**Output:** User will not be promoted to advisor.

| **Input Label** | **Data** |
| --- | --- |
| StaffStatus | Yes |
| ChangeToStaff | No |
| DeleteUser | No |

**Output:** Advisor will be demoted to user.

| **Input Label** | **Data** |
| --- | --- |
| StaffStatus | Yes |
| ChangeToStaff | Yes |
| DeleteUser | Yes |

**Output:** Advisor account will be deleted.

| **Input Label** | **Data** |
| --- | --- |
| StaffStatus | Yes |
| ChangeToStaff | No |
| DeleteUser | Yes |

**Output:** Advisor account will be deleted.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T8. Messaging and Notification (FWBS 1.8)**

| Test Number | T8 |
| --- | --- |
| Test Module | Messaging and Notification |
| F/S(WBS) number | 1.8 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures in app messages and notifications as well as email notifications are working.

**Setup:** Navigate to “User Profile” by clicking “Profile” on the navigation bar. Click “Message”.

| **Input Label** | **Data** |
| --- | --- |
| sender | user1 |
| recipient | user2 |
| messageType | message |
| message | Hello |

**Output:** user2 receives an in-app message: “Hello”. User1 will get an update about the message status.

| **Input Label** | **Data** |
| --- | --- |
| sender | System |
| recipient | user2 |
| messageType | message |
| message | You have renewed your subscription. |

**Output:** user2 receives an in-app message and email notification: “You have renewed your subscription.”.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T9. Advisor Booking System (FWBS 3.1)**

| Test Number | T9 |
| --- | --- |
| Test Module |  Advisor Booking System |
| F/S(WBS) number | 3.1 |
| Software Setup | OS: Windows 11 23H2; Google Chrome, Version ^122.0.6261.111 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module allows users to book an consultation session with an advisor

**Setup:** Navigate to the “Schedule” page. This can be achieved by clicking “Calendar” on the navigation bar. You must login as a user and not a advisor. Search and filter with the search box show on the page to look for advisor and book a session with them. If there is upcoming meeting, the system will show a reminder on user screen.

| Input Label | Data |
| --- | --- |
| User login | No |
| Advisor found | No/yes |
| Selected advisor availability | No/yes |
| Confirmed upcoming meeting | No |

Output: redirect user to the login page

| Input Label | Data |
| --- | --- |
| User login | Yes |
| Advisor found | No |
| Selected advisor availability | No |
| Confirmed upcoming meeting | No |

Output: show the list of all advisor.

| Input Label | Data |
| --- | --- |
| User login | Yes |
| Advisor found | Yes |
| Selected advisor availability | Yes |
| Confirmed upcoming meeting | No |

Output: list all the advisor that match the search text. For the selected advisor, allow user to book a session with them.

| Input Label | Data |
| --- | --- |
| User login | Yes |
| Advisor found | Yes |
| Selected advisor availability | No |
| Confirmed upcoming meeting | No |

Output: list all the advisor that match the search text. For the selected advisor, show user warning “advisor is not available” on the list and disable the booking button.

| Input Label | Data |
| --- | --- |
| User login | No |
| Advisor found | No/yes |
| Selected advisor availability | No/yes |
| Confirmed upcoming meeting | Yes |

Output: send the reminder to the user preference communication method only.

| Input Label | Data |
| --- | --- |
| User login | Yes |
| Advisor found | No |
| Selected advisor availability | No/yes |
| Confirmed upcoming meeting | Yes |

Output: send the reminder to the user preference communication method and pop up notification on their view.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T10.** Virtual Consultation Session **(FWBS 3.2)**

| Test Number | T10 |
| --- | --- |
| Test Module | Virtual Consultation Session |
| F/S(WBS) number | 3.2 |
| Software Setup | OS: Windows 11 23H2; Google Chrome, Version ^122.0.6261.111 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module allows users and advisors to join a video call service 

**Setup:** Navigate to the “Schedule” page. This can be achieved by clicking “Calendar” on the navigation bar. Make a consultation session for an advisor and user account. Then click the video call service link in the upcoming events section.

| **Input Label** | **Data** |
| --- | --- |
| Is valid credential | True |
| Video call service link | True |

Output: Direct advisor/user to the video hosting service successfully

| **Input Label** | **Data** |
| --- | --- |
| Is valid credential | False |
| Video call service link | True |

Output: redirect user to login page.

| **Input Label** | **Data** |
| --- | --- |
| Is valid credential | False/True |
| Video call service link | False |

Output: show error and make log report to the system. Send request to the video call service to create a new room.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T11.** Event Registration **(FWBS 5.2)**

| Test Number | T11 |
| --- | --- |
| Test Module | Event Registration |
| F/S(WBS) number | 5.2 |
| Software Setup | OS: Windows 11 23H2; Google Chrome, Version ^122.0.6261.111 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This test checks if the event registration system allows user to lookup and register for event.

**Setup:** Navigate to the “Schedule” page. This can be achieved by clicking “Calendar” on the navigation bar. You will now be presented with a list of upcoming events. 

| Input Label | Data |
| --- | --- |
| User login | No |
| Event registration | Yes/No |

output: redirect user to the login page

| Input Label | Data |
| --- | --- |
| User login | Yes |
| Event registration | No |

output: show the list of events and user registered events

| Input Label | Data |
| --- | --- |
| User login | Yes |
| Event registration | Yes |

output: show the event detail in the confirmation page for user to double check their registration. 

### **Acceptance of Test**

**Date:** 30 April 2025

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T12.** Event Creation and Editing **(FWBS 5.1)**

| Test Number | T12 |
| --- | --- |
| Test Module | Event and Advisor Booking |
| F/S(WBS) number | 5.1 |
| Software Setup | OS: Windows 11 23H2; Google Chrome, Version ^122.0.6261.111 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module allows advisors to create, edit, and delete events

**Setup for creating:** Must login as an advisor. be Navigate to the “Schedule” page. This can be achieved by clicking “Calendar” on the navigation bar. Click on the create new event button.

| **Input Label** | **Data** |
| --- | --- |
| Date and Time Start | 28 April 2025, 13:00 |
| Date and Time End | 30 April 2025, 13:00 |
| Description |  |
| Title | Steak Fest |
| Location | Brookings |

Output: Invalid because the start time has already occurred. Show error “Start and end time must be in the future”

| **Input Label** | **Data** |
| --- | --- |
| Date and Time Start | 30 April 2025, 13:00 |
| Date and Time End | 20 April 2025, 13:00 |
| Description |  |
| Title | Steak Fest |
| Location | Brookings |

Output: Invalid because the end time is before the start time. Show error “end time must be after the start time”.

| **Input Label** | **Data** |
| --- | --- |
| Date and Time Start | 30 April 2025, 13:00 |
| Date and Time End | 30 April 2025, 14:00 |
| Description | Hello Good Sir |
| Title |  |
| Location |  |

Output: Invalid because event requires a title and location

| **Input Label** | **Data** |
| --- | --- |
| Date and Time Start | 30 April 2025, 13:00 |
| Date and Time End | 30 April 2025, 14:00 |
| Description | Hello Good Sir |
| Title | Steak Fest |
| Location | Brookings |

Output: Creates a new event that is displayed in the list of events

**Setup for editing:** Must login as an advisor. Navigate to the “Schedule” page. This can be achieved by clicking “Calendar” on the navigation bar. Click on the edit event button on a newly created event. 

| **Previous Input Label** | **Previous Data** | **New Data** |
| --- | --- | --- |
| Date and Time Start | 30 April 2025, 13:00 | N/A |
| Date and Time End | 30 April 2025, 14:00 | 30 April 2025, 12:00 |
| Description | Hello Good Sir | N/A |
| Title | Steak Fest | N/A |
| Location | Brookings | N/A |
| Delete |  | False |

Output: Invalid because new end time is before previous start time

| **Previous Input Label** | **Previous Data** | **New Data** |
| --- | --- | --- |
| Date and Time Start | 30 April 2025, 13:00 | N/A |
| Date and Time End | 30 April 2025, 14:00 | N/A |
| Description | Hello Good Sir | N/A |
| Title | Steak Fest |  |
| Location | Brookings |  |
| Delete |  | False |

Output: Invalid because event needs a title and location

| **Previous Input Label** | **Previous Data** | **New Data** |
| --- | --- | --- |
| Date and Time Start | 30 April 2025, 13:00 | N/A |
| Date and Time End | 30 April 2025, 14:00 | 1 May 2025, 17:00 |
| Description | Hello Good Sir | What’s new |
| Title | Steak Fest | Willy Wonka |
| Location | Brookings | Lawsuit Impending |
| Delete |  | False |

Output: Updates the event with new values that should be displayed on the event list

| **Previous Input Label** | **Previous Data** | **New Data** |
| --- | --- | --- |
| Date and Time Start | 35 April 2025, 13:00 | N/A |
| Date and Time End | 35 April 2025, 14:00 | N/A |
| Description | Hello Good Sir | N/A |
| Title | Steak Fest | N/A |
| Location | Brookings | N/A |
| Delete |  | True |

Output: The event should be removed from the database and the event list

### **Acceptance of Test**

**Date:** 30 April 2025

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## T13. Payment Gateway Integration (FWBS 6.1)

| Test Number | T13 |
| --- | --- |
| Test Module | Payment Gateway Integration |
| F/S(WBS) number | 6.1 |
| Software Setup | OS: Windows 11 24H2; Microsoft Edge |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module**: ensures that the system can handle all matters dealing with money transaction processing, subscription payments securely and properly.

**Setup:** Select gateway to make a payment. The system will listen to the transaction status and check sum to ensure transaction security. 

| **Input Label** | **Data** |
| --- | --- |
| Transaction status | Succeed |
| SHA256 check sum match | Yes |

Output: Process to handle the payment by returning the success response

| **Input Label** | **Data** |
| --- | --- |
| Transaction status | Declined/Cancelled |
| SHA256 check sum match | Yes |

Output: Process to handle the payment by returning false response with the reason if applicable.

| **Input Label** | **Data** |
| --- | --- |
| Transaction status | Succeed/Declined/Cancelled |
| SHA256 check sum match | No |

Output: Process to initiate security report and return user to the error page.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## T14. Transaction Management (FWBS 6.2)

| Test Number | T14 |
| --- | --- |
| Test Module | Transaction Management |
| F/S(WBS) number | 6.2 |
| Software Setup | OS: Windows 11 24H2; Microsoft Edge |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

Purpose of Module: ensures the system returns the correct invoice and receipts to the user. Additionally, check if the user can initiate a refund or cancellation.

Setup: user navigate to the payment section. The system will return all the invoices and receipts from that specific user.

| **Input Label** | **Data** |
| --- | --- |
| User existed | Yes |
| Invoice data existed | No |
| Receipt data existed | No |

Output: show “You have no invoice and receipt” message.

| **Input Label** | **Data** |
| --- | --- |
| User existed | No |
| Invoice data existed | No |
| Receipt data existed | No |

Output: redirect user to login page.

| **Input Label** | **Data** |
| --- | --- |
| User existed | Yes |
| Invoice data existed | Yes |
| Receipt data existed | No |

Output: show user invoice data. No receipt would show.

| **Input Label** | **Data** |
| --- | --- |
| User existed | Yes |
| Invoice data existed | No |
| Receipt data existed | Yes |

Output: Show user receipt data. No invoice would show.

| **Input Label** | **Data** |
| --- | --- |
| User existed | Yes |
| Invoice data existed | Yes |
| Receipt data existed | Yes |

Output: show both user invoice and receipt data.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T15. User Reports (FWBS 7.1)**

| Test Number | T15 |
| --- | --- |
| Test Module | User Reports |
| F/S(WBS) number | 7.1 |
| Software Setup | OS: Windows 11 24H2; Microsoft Edge |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensures the system can create full financial reports and customized report for the user.

**Setup:** Navigate to “Reports” by clicking “Reports” on the navigation bar. Then click “Create report” for a full financial report using user financial data or select “Customize report” to create customized report.

| **Input Label** | **Data** |
| --- | --- |
| User financial data available | No |
| Create report selected | No/Yes |
| Customized report selected | No/Yes |

**Output:** Show message “You don’t have any financial data available on the system” with a button with label “Create new” that redirect them to create new financial record.

| **Input Label** | **Data** |
| --- | --- |
| User financial data available | Yes |
| Create report selected | No |
| Customized report selected | No |

**Output:** Show them the most recent of their data on the “Report” page

| **Input Label** | **Data** |
| --- | --- |
| User financial data available | Yes |
| Create report selected | Yes |
| Customized report selected | No |

**Output:** Generate the full report from user’s data. Open the report in new tab in a PDF format.

| **Input Label** | **Data** |
| --- | --- |
| User financial data available | Yes |
| Create report selected | No |
| Customized report selected | Yes |

**Output:** Show a list of available fields the user can select from. Generate a customize report from the selected fields. Open the report in new tab in a PDF format.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## **T16.** Administrative Analytics**(FWBS 7.2)**

| Test Number | T16 |
| --- | --- |
| Test Module | Administrative Analytics |
| F/S(WBS) number | 7.2 |
| Software Setup | OS: Windows 11 24H2; Microsoft Edge |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module:** This module ensure the admin be able to monitor and create report about user metrics and system metrics in income and health.

**Setup:** Navigate to the admin page at “localhost:8000/admin” and login with the admin account. navigate to “Reports” tab on the navigation bar.

| **Input Label** | **Data** |
| --- | --- |
| Admin role | No |
| User metrics available | No/Yes |
| System Metrics available | No/Yes |

**Output:** User will be redirected to the admin login page to login with an admin credential.

| **Input Label** | **Data** |
| --- | --- |
| Admin role | Yes |
| User metrics available | No |
| System Metrics available | No |

**Output:** Show error message “Data is not available” for the missing metrics

| **Input Label** | **Data** |
| --- | --- |
| Admin role | Yes |
| User metrics available | Yes |
| System Metrics available | No |

**Output:** Show the User metrics analytics and report. Show error “Data is not available” for system metrics sections.

| **Input Label** | **Data** |
| --- | --- |
| Admin role | Yes |
| User metrics available | No |
| System Metrics available | Yes |

**Output:** Show error “Data is not available” for the user metrics analytics and report. Show report and analysis for system metrics sections.

| **Input Label** | **Data** |
| --- | --- |
| Admin role | Yes |
| User metrics available | Yes |
| System Metrics available | Yes |

**Output:** Show report and analysis for the both sections.

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

## T17. Loan Calculator (FWBS 2.1)

| Test Number | T1 |
| --- | --- |
| Test Module | Loan Calculator |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72  |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose:** Validates correct calculation of monthly payment, total interest, and total cost for loan scenarios.

**Purpose of module:** This module allows users to calculate loan payments, total interest, and visualize payment breakdowns for various loan scenarios.

**Setup:** Navigate to "`Calculators`" > "`Loan Calculator`". Input data and click "`Calculate`".

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Loan Amount | $10,000 |
| Interest Rate | 5% |
| Loan Term | 5 years |

**Output:**

- Monthly Payment: $188.2
- Total Interest: $**1292.24**
- Total Cost: $**11292.24**
- Payment breakdown chart shows principal (88%) and interest (12%)

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Loan Amount | $10,000 |
| Interest Rate | 0% |
| Loan Term | 5 years |

**Output:**

- Monthly Payment: $166.67
- Total Interest: $0.00
- Total Cost: $10,000.00
- Payment breakdown chart shows principal (100%) and interest (0%)

**Test Case 3**

| Input Label | Data |
| --- | --- |
| Loan Amount | $0 |
| Interest Rate | 5% |
| Loan Term | 5 years |

**Output: show user warning “please type the correct loan amount”**

### **Acceptance of Test**

**Date: 30 April 2025**

**Wealthwise:** 

Name: 

Signature:

**Arqer:**

Name:

Signature:

---

## T18. Mortgage Calculator (FWBS 2.2)

| Test Number | T1 |
| --- | --- |
| Test Module |  |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72  |
| Hardware Setup |  |

**Purpose of Module:** This module allows users to calculate mortgage payments, total interest, and visualize payment breakdowns for home loans.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar. Click on "Mortgage Calculator" to access the tool. Enter the relevant data and click "Calculate" when complete.

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Home Price | $300,000 |
| Down Payment | $60,000 |
| Loan Term | 30 years |
| Interest Rate | 4.5% |

**Output:**

- Monthly Payment: $1,216.04
- Principal Amount: $**240000.0**
- Interest Amount: $**193156.26**

![image.png](attachment:efc504fe-5277-4239-94f3-a0d40c871a6a:image.png)

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Home Price | $300,000 |
| Down Payment | $30,000 |
| Loan Term | 15 years |
| Interest Rate | 4.5% |

**Output:**

- Monthly Payment: $**2053.05**
- Principal Amount: $**270000.0**
- Interest Amount: $**99549.54**

![image.png](attachment:13058784-cf58-4554-8520-bbd0e7b9a888:image.png)

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T19. Retirement Calculator (FWBS 2.4)

| Test Number | T1 |
| --- | --- |
| Test Module | Retirement Calculator |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of Module:** This module allows users to calculate retirement savings projections, determine if they're on track to meet retirement goals, and identify additional savings needed.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar. Click on "Retirement Calculator" to access the tool. Enter the relevant data and click "Calculate" when complete.

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Current Age | 30 |
| Retirement Age | 65 |
| Present Savings | $50,000 |
| Monthly Contributions | $500 |
| Rate of Return | 7% |
| Retirement Goal | $1,500,000 |

**Output:**

- Expected Savings at Retirement: $1,197,811.27
- Will Meet Goal: No
- Additional Monthly Savings Needed: $178.43
- Progress bar shows approximately 80% progress toward goal

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Current Age | 30 |
| Retirement Age | 65 |
| Present Savings | $100,000 |
| Monthly Contributions | $1,000 |
| Rate of Return | 7% |
| Retirement Goal | $1,500,000 |

**Output:**

- Expected Savings at Retirement: $2,295,622.54
- Will Meet Goal: Yes
- Additional Monthly Savings Needed: $0.00
- Progress bar shows 100% progress toward goal

---

**Test Case 3**

| Input Label | Data |
| --- | --- |
| Current Age | 50 |
| Retirement Age | 65 |
| Present Savings | $200,000 |
| Monthly Contributions | $1,000 |
| Rate of Return | 5% |
| Retirement Goal | $1,000,000 |

**Output:**

- Expected Savings at Retirement: $642,705.81
- Will Meet Goal: No
- Additional Monthly Savings Needed: $1,507.35
- Progress bar shows approximately 64% progress toward goal

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T20. Budgeting Tool (FWBS 2.3)

| Test Number | T1 |
| --- | --- |
| Test Module | Budgeting Tool |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of Module:** This module allows users to create and analyze budgets, and expenses, and track progress toward savings goals.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar. Click on "Budgeting Tool" to access the tool. Enter the relevant data and click "Analyze Budget" when complete.

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Fixed Income | $5,000 |
| Variable Income | $500 |
| One Year Savings Goal | $12,000 |
| Housing | $1,500 |
| Taxes | $1,000 |
| Car Payment | $400 |
| Internet and Phone | $150 |
| Subscriptions | $50 |
| Food | $600 |
| Entertainment | $200 |
| Personal Items | $150 |
| Utilities | $200 |
| Transportation | $100 |
| Medical | $200 |
| Miscellaneous | $100 |

**Output:**

- Total Income: $5,500
- Total Expenses: $4,650
- Monthly Surplus: $850
- Annual Savings: $10,200
- Savings Goal Message: "You are on track to save $10,200 this year, which is $1,800 short of your annual goal of $12,000."

![image.png](attachment:8c5a2c54-e059-4c19-9b45-b35820db8eef:image.png)

![image.png](attachment:7a4fee86-ffbb-4314-b9b9-ebe395dc4cf1:image.png)

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Fixed Income | $4,000 |
| Variable Income | $0 |
| One Year Savings Goal | $6,000 |
| Housing | $1,500 |
| Taxes | $800 |
| Car Payment | $400 |
| Internet and Phone | $150 |
| Subscriptions | $50 |
| Food | $600 |
| Entertainment | $300 |
| Personal Items | $200 |
| Utilities | $200 |
| Transportation | $100 |
| Medical | $100 |
| Miscellaneous | $100 |

**Output:**

- Total Income: $4,000
- Total Expenses: $4,500
- Monthly Surplus: -$500
- Annual Savings: -$6,000
- Overspend Areas Warning: "Your current spending exceeds your savings goal. You will have $-6000.0 by the end of a year. Consider reducing expenses, especially in any highlighted areas."

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T21. Insurance Calculator (FWBS 2.5)

| Test Number | T1 |
| --- | --- |
| Test Module | Insurance Calculator  |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of Module:** This module helps users estimate appropriate life insurance coverage based on financial obligations and family needs.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar. Click on "Insurance Calculator" to access the tool. Enter the relevant data and click "Calculate" when complete.

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Annual Income | $80,000 |
| Years to Replace | 10 |
| Outstanding Mortgage | $250,000 |
| Other Debts | $20,000 |
| Children's Education | $100,000 |
| Final Expenses | $15,000 |
| Existing Life Insurance | $100,000 |

**Output:**

- Income Replacement: $800,000
- Debt Payoff: $270,000
- Education Expenses: $100,000
- Final Expenses: $15,000
- Total Insurance Needs: $1,185,000
- Existing Coverage: $100,000
- Additional Coverage Needed: $1,085,000

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Annual Income | $80,000 |
| Years to Replace | 10 |
| Outstanding Mortgage | $250,000 |
| Other Debts | $20,000 |
| Children's Education | $100,000 |
| Final Expenses | $15,000 |
| Existing Life Insurance | $1,200,000 |

**Output:**

- Income Replacement: $800,000
- Debt Payoff: $270,000
- Education Expenses: $100,000
- Final Expenses: $15,000
- Total Insurance Needs: $1,185,000
- Existing Coverage: $1,200,000
- Additional Coverage Needed: $0

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T22. Student Loan Calculator (FWBS 2.6)

| Test Number | T1 |
| --- | --- |
| Test Module | Student Loan Calculator |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of Module:** This module helps users analyze student loan repayment options and visualize the impact of different payment strategies.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar. Click on "Student Loan Calculator" to access the tool. Enter the relevant data and click "Calculate" when complete.

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Loan Amount | $30,000 |
| Interest Rate | 5.8% |
| Loan Term | 10 years |
| Extra Payment | $0 |

**Output:**

- Monthly Payment: $330.06
- Total Interest: $9,607.20
- Total Payment: $39,607.20
- Loan Payoff Date: March 2035
- Payment breakdown chart shows principal (76%) and interest (24%)

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Loan Amount | $30,000 |
| Interest Rate | 5.8% |
| Loan Term | 10 years |
| Extra Payment | $100 |

**Output:**

- Monthly Payment: $430.06
- Total Interest: $7,553.92
- Total Payment: $37,553.92
- Loan Payoff Date: June 2033
- Payment breakdown chart shows principal (80%) and interest (20%)
- Savings from extra payments: $2,053.28

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T23. Car Payment Calculator (FWBS 2.7)

| Test Number | T23 |
| --- | --- |
| Test Module | Car Payment Calculator |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of Module:** This module helps users calculate car loan payments and analyze the total cost of vehicle ownership.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar. Click on "Car Payment Calculator" to access the tool. Enter the relevant data and click "Calculate" when complete.

### Test Scenarios:

**Test Case 1**

| Input Label | Data |
| --- | --- |
| Vehicle Price | $25,000 |
| Down Payment | $5,000 |
| Trade-in Value | $0 |
| Loan Term | 60 months |
| Interest Rate | 4.5% |
| Sales Tax | 6% |
| Title & Registration | $300 |

**Output:**

- Loan Amount: $21,800
- Monthly Payment: $405.83
- Total Interest: $2,549.80
- Total Cost: $30,349.80
- Payment breakdown chart shows principal (89%) and interest (11%)

**Test Case 2**

| Input Label | Data |
| --- | --- |
| Vehicle Price | $25,000 |
| Down Payment | $5,000 |
| Trade-in Value | $8,000 |
| Loan Term | 48 months |
| Interest Rate | 4.5% |
| Sales Tax | 6% |
| Title & Registration | $300 |

**Output:**

- Loan Amount: $13,800
- Monthly Payment: $315.44
- Total Interest: $1,341.12
- Total Cost: $22,641.12
- Payment breakdown chart shows principal (91%) and interest (9%)

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T24. Calculators (FWBS 4.1)

| Test Number | T24 |
| --- | --- |
| Test Module | Calculator Navigation & Integration |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of Module:** This test ensures that the calculator hub page displays all available calculators and that navigation between calculators works correctly.

**Setup:** Navigate to the "Calculators" page by clicking "Calculators" on the navigation bar.

### **Validation Points:**

| Test Case | Expected Result |
| --- | --- |
| Calculator Hub Display | All 7 calculators are displayed with appropriate icons and descriptions: Loan, Mortgage, Retirement, Budgeting Tool, Insurance, Student Loan, and Car Payment Calculator |
| Navigation to Loan Calculator | Clicking on "Loan Calculator" navigates to the loan calculator page |
| Navigation to Mortgage Calculator | Clicking on "Mortgage Calculator" navigates to the mortgage calculator page |
| Navigation to Retirement Calculator | Clicking on "Retirement Calculator" navigates to the retirement calculator page |
| Navigation to Budgeting Tool | Clicking on "Budgeting Tool" navigates to the budgeting tool page |
| Navigation to Insurance Calculator | Clicking on "Insurance Calculator" navigates to the insurance calculator page |
| Navigation to Student Loan Calculator | Clicking on "Student Loan Calculator" navigates to the student loan calculator page |
| Navigation to Car Payment Calculator | Clicking on "Car Payment Calculator" navigates to the car payment calculator page |
| Return to Calculator Hub | Clicking "Back to Calculators" from any calculator page returns to the calculator hub |
| Consistent Design | All calculator pages maintain consistent design elements, including header styling, form layouts, and results presentation |

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

## T25. Financial News

| Test Number | T1 |
| --- | --- |
| Test Module | Financial News |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of module:** This module displays the latest financial news articles from external news APIs, providing users with up-to-date market information.

**Setup:** Navigate to the WealthWise learning hub where the Financial News component is displayed.

### Test Scenarios:

| **ID** | **Test Case** | **Expected Result** |
| --- | --- | --- |
| FN-01 | Load the homepage and verify the Financial News component is visible | Component displays with "Latest Financial News" heading |
| FN-02 | Verify news articles are displayed (when API key is valid) | Up to 5 financial news articles are displayed with clickable links |
| FN-03 | Click on a news article link | Link opens the original article in a new browser tab |
| FN-04 | Test with invalid/missing API key | Error message "Could not load news. Please try again later." is displayed |
| FN-05 | Test component responsiveness on mobile device | Component maintains proper layout and readability on small screens |

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T25. Learning Module(FWBS 4.2)

| Test Number | T1 |
| --- | --- |
| Test Module | Learning Module |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

**Purpose of module:** This test ensures that the learning module integrates properly, and handle user request for available resource and interactive learning.

**Setup:** Navigate to the WealthWise learning hub homepage. Then, select “Learning” to view all the active resource.

### Test Scenarios:

| **ID** | **Test Case** | **Expected Result** |
| --- | --- | --- |
| LM-01 | Verify "Return to WealthWise" link exists in header | Link is visible in the header navigation area |
| LM-02 | Click on "Return to WealthWise" link | User is redirected to [https://wealthwise.onrender.com](https://wealthwise.onrender.com/) |
| LM-03 | Test header responsiveness on mobile device | "Return to WealthWise" link is accessible in mobile menu |
| LM-04 | Navigate to a blog post and verify header persistence | "Return to WealthWise" link remains accessible |
| LM-05 | Test navigation after filtering by tags | "Return to WealthWise" link remains accessible |

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

## T#. # Calculator (FWBS )

| Test Number | T1 |
| --- | --- |
| Test Module |  |
| F/S(WBS) number |  |
| Software Setup | - **Operating System**: Windows 11 Education 24H2;
- **Browser**: Microsoft Edge 134.0.3124.72 
- **Network**: Xtream 5GHz Wifi at 1201mb/s |
| Hardware Setup | - **Processor**; 13th Gen Intel(R) Core(TM) i7-1355U 1.70 GHz
- **Memory**: 32 GB |

### Test Scenarios:

### **Acceptance of Test**

**Date: 30 April 2025**

Signature:

Name:

**Arqer:**

Signature:

Name: 

**Wealthwise:** 

---

# Log of Meetings, Reviews, and Meetings

**Weekly meeting report and review – 2/20/2025**

- Planning for presentation
- Fixing build errors in environment
- Adjusting to do list, things need to be done before Monday: calculator navigation, insurance calculator, mortgage calculator, learning hub – stocks, schedule – event
- Double check and resolve open issues

**Meeting with client – 2/1/2025**

- Discussing questions for the presentation
- Confirming the project modules

**Code review 2/21/2025**

- Fixing bug and attempting to implement connection between web and database.

**Team code report and review – 2/26/2025**

- Wrapping up for presentation by fixing bugs
- Finalize components that the team decided to demonstrate

**Weekly meeting report and review 2/26/2025**

- Assigned new task for team members
- Continuing to be implementing learning hub
- Fix front-end for homepage and calculators. Create a base HTML file and style across the project
- Modify user profile and register form. Add features: change password, delete account, and forgot password button
- Modify budget calculator
- Planning for payment and subscription module
- Continuing on scheduling and 404 HTTP response handling.

**Weekly meeting report and review – 3/6/2025**

- Planning for the acceptance test plan document
- Assigning test sets and document section
- Review front-end for the current available web pages

---

# Project Acceptance Signatures for Client and Developer

By signing this document, you are confirming that the project has been completed to the standards outlined in the agreed-upon requirements and scope. Your signature acknowledges that you have thoroughly reviewed the deliverables and find them to meet the expectations and specifications initially defined. Additionally, you agree that the project is ready for its next phase, whether that involves deployment, maintenance, or closure, and that all parties have fulfilled their respective responsibilities. This signature represents mutual agreement and approval of the project's completion.

…

---

# Appendix

---

## **Appendix A: Glossary of Terms**

| **Term / Acronym** | **Definition** |
| --- | --- |
| **Acceptance Testing** | A phase of software testing where the system is tested for acceptability. It ensures the software meets business requirements and is ready for delivery. |
| **ATP** | Stands for Acceptance Test Plan. A document outlining the scope, test cases, environment, and acceptance criteria for validating a product. |
| **FWBS** | Functional Work Breakdown Structure. A numbering system used to categorize software functions/modules being tested. |
| **Test Case (T#)** | A specific scenario or procedure designed to verify a particular functionality or feature. Identified by a test number (e.g., T1, T2). |
| **P/F** | Pass/Fail. Indicates whether a test case passed or failed based on expected outcomes. |
| **UI** | User Interface. The visual elements through which a user interacts with the application. |
| **API** | Application Programming Interface. A set of protocols for building and integrating software applications. |
| **Advisor** | A user type in the system with specialized privileges to offer financial guidance, book consultations, and appear in the advisor directory. |
| **Admin** | A user with elevated permissions who can manage users, advisors, events, analytics, and platform configurations. |
| **User** | A general platform user with access to standard functionalities like registration, login, subscriptions, and consultations. |
| **Consultation** | A virtual or scheduled session between a user and an advisor, typically involving financial or investment advice. |
| **Subscription** | A recurring payment plan granting users access to premium services or advisor consultations. |
| **Transaction** | A record of a user’s payment activity, including subscriptions, refunds, and payment history. |
| **Interaction History** | A log or page showing a user's past events and consultations with advisors. |
| **Error Guessing** | A test design technique where testers apply experience to guess where defects might be found. |
| **Checksum (SHA256)** | A cryptographic hash used to verify the integrity of transaction data, ensuring it hasn't been tampered with. |
| **Manual Testing** | Testing performed by humans, executing test cases without automation tools. |
| **DevTools** | Browser-based tools (e.g., Chrome DevTools) used by developers and testers to inspect HTML, monitor network traffic, and debug JavaScript. |
| **Localhost** | The local testing environment (usually at `localhost:8000`) where the application is run and tested before deployment. |
| **In-App Messaging** | Messaging system within the platform allowing users or the system to send messages directly to user accounts. |
| **Notification System** | System component that alerts users via email or in-app messages about relevant events, updates, or actions. |
| **Invoice** | A bill generated for a completed payment, usually including itemized charges. |
| **Receipt** | A confirmation document issued after successful payment, confirming transaction details. |
| **Refund** | A return of funds to the user due to a cancelled or erroneous transaction. |
| **Consultation Rate** | A system metric showing the frequency or volume of consultations between users and advisors. |
| **Platform Health** | General system status including uptime, error rates, and system performance indicators. |
| **PDF Report** | A downloadable, printable report generated by the system based on user data or analytics, typically in PDF format. |
| **Latency Simulation** | The act of artificially slowing down a network connection to test how the system responds under less-than-ideal conditions. |
| **Custom Report** | A user-generated report where specific fields and metrics are selected for inclusion. |
| **System Metrics** | Quantitative measurements that reflect the performance, usage, and technical status of the platform. |

---

---

# Pages

[Introduction - Acceptance Test Plan](https://www.notion.so/Introduction-Acceptance-Test-Plan-d410f3ea1112442eaf58138c2ee63086?pvs=21)

[Hardware and Software used for testing - Acceptance Test Plan](https://www.notion.so/Hardware-and-Software-used-for-testing-Acceptance-Test-Plan-084425c2a5fb4dd89377fb19a829bbd6?pvs=21)

[Test Schedule and Test Sets - Acceptance Test Plan](https://www.notion.so/Test-Schedule-and-Test-Sets-Acceptance-Test-Plan-76bc40f16eb046c6b0731f3d49c2d314?pvs=21)

[Error Handling Policy - Acceptance Test Plan](https://www.notion.so/Error-Handling-Policy-Acceptance-Test-Plan-1bfe296772e8447a98b70587c41d9506?pvs=21)

[Individual Test cases - Acceptance Test Plan](https://www.notion.so/Individual-Test-cases-Acceptance-Test-Plan-b3905f8e27f94c1ca02d69f282ca6608?pvs=21)

[Log of Meetings, Reviews, and Meetings](https://www.notion.so/Log-of-Meetings-Reviews-and-Meetings-9c165fc059ed4ce1a3d77bf5aaa55420?pvs=21)

[Project Acceptance Signatures for Client and Developer - Acceptance Test Plan](https://www.notion.so/Project-Acceptance-Signatures-for-Client-and-Developer-Acceptance-Test-Plan-6722627aff28434898bfd00730323845?pvs=21)

[Appendix - Acceptance Test Plan](https://www.notion.so/Appendix-Acceptance-Test-Plan-5ddfbaeb0f894d5eae19b4504ee2a55a?pvs=21)