# Introduction

## Purpose of Unit and Integration Testing

Unit testing is all about checking each small piece of a program on its own. It makes sure that every little function or module does exactly what it's supposed to do before the rest of the code comes into play. Once confident that the individual parts are working correctly, integration testing steps in. This type of testing combines these parts to see how they work together as a whole. It helps catch any problems that might arise when the parts interact with each other—sort of like making sure all the pieces of a puzzle fit well before frame it. By finding and fixing issues early on, both unit and integration testing help create software that is more reliable and easier to maintain.

## Proposed System Overview or Configuration Chart

Our system is broken into five main apps that can be navigated from the navigation bar. The calculations app contains each financial calculation, including the budgeting tool. The scheduling app includes all the tools advisors need to make, edit, and delete events. Users also register for events through the scheduling app. The learning hub app redirects users to a separately hosted service that hosts the learning hub content. The admin app allows admins to edit any data in the database and create advisors. The user's apps enable new users to register or existing ones to log in and out. It also allows users to edit their account settings and subscriptions. The chart below shows how the website pages for these apps are represented on the website.

![image.png](attachment:71e31ce8-f947-4081-a035-2082848a0dce:image.png)

## Definitions, Acronyms, and Abbreviations

[Grab from ATP - rmb to remove the ATP related def]

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

# Error Handling Policy

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

# Testing Sets

| **Test #** | FWBS# | Test Name | Test Description | Who | Date | P/F |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.1 | User Registration | This test to ensure the data validation for user registration handle properly | Sawyer | April 22 | P |
| 2 | 1.2 | User Login* | Test the login if the system handle the login request logic correctly using white box testing method.  | John | April 22 | P |
| 3 | 1.4 | Profile Management | Test the profile management system to ensure that the user can view and update their profile information | Norman | April 22 | P |
| 4 | 2.3 | Budgeting Tool | Test the tool to make sure that user can perform calculations and save their records to the database. | Draix | April 22 | P |
| 5 | 5-1.2 | Event Management System - Database - User Login | This is an integration test. Test to ensure that the event management system handles request from different user type and fetch/update data from/to the database | Draix | April 22 | P |

[*] white box testing

---

# Unit Tests

## T1. User Registration (FWBS# 1.1)

[here]

## T2. User Login (FWBS# 1.2)

[here]

## T3. Profile Management (FWBS# 1.4)

| Test Number | T3 |
| --- | --- |
| Test Module | Profile Management |
| F/S(WBS) number | 1.4 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

Purpose of module: This module tests the profile management system to ensure that the user can view and update their profile information

Set up: The user logs into the system, then, on the home page, selects “Profile.” Under “Profile”, click “Edit Profile.” User edit field(s) and click “Save changes”

| **Input Label** | **Data** |
| --- | --- |
| First name | [Empty] |
| Last name | [Empty] |
| Phone number | [Empty] |
| Address | [Empty] |
| City | [Empty] |
| State | [Empty] |
| Country | [Empty] |
| Postal code | [Empty] |
| Profile picture | [Empty] |

Output: show pop-up warning “Please fill out this field” at the first name field.

| **Input Label** | **Data** |
| --- | --- |
| First name | c |
| Last name | [Empty] |
| Phone number | [Empty] |
| Address | [Empty] |
| City | [Empty] |
| State | [Empty] |
| Country | [Empty] |
| Postal code | [Empty] |
| Profile picture | [Empty] |

Output: show pop-up warning “Please fill out this field.” at the last name field.

| **Input Label** | **Data** |
| --- | --- |
| First name | [Empty] |
| Last name | c |
| Phone number | [Empty] |
| Address | [Empty] |
| City | [Empty] |
| State | [Empty] |
| Country | [Empty] |
| Postal code | [Empty] |
| Profile picture | [Empty] |

Output: show pop-up warning “Please fill out this field.” at the first name field.

| **Input Label** | **Data** |
| --- | --- |
| First name | Aden |
| Last name | Bill |
| Phone number | [Empty] |
| Address | [Empty] |
| City | [Empty] |
| State | [Empty] |
| Country | [Empty] |
| Postal code | [Empty] |
| Profile picture | [Empty] |

Output: update user profile with first name of “Aden” and last name of “Bill”.

| **Input Label** | **Data** |
| --- | --- |
| First name | Aden |
| Last name | Bill |
| Phone number | 555 555 555 |
| Address | 2387 13st |
| City | Sunny |
| State | PA |
| Country | US |
| Postal code | 502339 |
| Profile picture | [Empty] |

Output: update the user profile with all the information provided.

| **Input Label** | **Data** |
| --- | --- |
| First name | Aden |
| Last name | Bill |
| Phone number | 555 555 555 |
| Address | 2387 13st |
| City | Sunny |
| State | PA |
| Country | US |
| Postal code | 502339 |
| Profile picture | Picture uploaded |

Output: Update the user profile with all the information provided, update the profile picture with the uploaded image file, and save the image file to the system.

| **Input Label** | **Data** |
| --- | --- |
| First name | Aden |
| Last name | Bill |
| Phone number | 555 555 555 |
| Address | 1009 9th St |
| City | Sunny |
| State | PA |
| Country | US |
| Postal code | 502339 |
| Profile picture | clear |

Output: update user profile address from “2387 13st” to “1009 9th St.” and clear the profile picture

## T4. Budgeting Tool (FWBS# 2.3)

| Test Number | T4 |
| --- | --- |
| Test Module | Budgeting Tool |
| F/S(WBS) number | 2.3 |
| Software Setup | OS: Windows 11 23H2; Mozilla Firefox Version 136.0 |
| Hardware Setup | CPU 2.3GHz Intel Core i7; Memory 16 GB |

**Purpose of module**: This module tests the budgeting tool to ensure the user can calculate, store, and retrieve their input information.

**Set up**: The user first logs into the system. Then, on the home page, selects “Calculators.” Next, the user clicks “Budgeting Tool”. The user then inputs the data or clicks buttons as per each test case.

| **Input Label** | **Data** |
| --- | --- |
| Fixed Income | [Empty] |
| Variable Income | [Empty] |
| One Year Savings Goal | [Empty] |
| Housing | [Empty] |
| Taxes | [Empty] |
| Car Payment | [Empty] |
| Internet and Phone | [Empty] |
| Subscriptions | [Empty] |
| Food | [Empty] |
| Entertainment | [Empty] |
| Personal Items | [Empty] |
| Utilities | [Empty] |
| Transportation | [Empty] |
| Medical | [Empty] |
| Miscellaneous | [Empty] |
| Budget Month | January [default] |
| Budget Year | [Empty] |

**Action**: User clicks “Calculate”.

**Output**: User returned to the top of the page with “Fixed Income” field showing “Please enter a number” pop-up.

| **Input Label** | **Data** |
| --- | --- |
| Fixed Income | 6400 |
| Variable Income | 200 |
| One Year Savings Goal | 2000 |
| Housing | 1000 |
| Taxes | 400 |
| Car Payment | 100 |
| Internet and Phone | 50 |
| Subscriptions | 50 |
| Food | 1000 |
| Entertainment | 200 |
| Personal Items | 100 |
| Utilities | 300 |
| Transportation | 100 |
| Medical | 200 |
| Miscellaneous | 100 |
| Budget Month | May |
| Budget Year | 2024 |

**Action**: User clicks “Calculate”.

**Output**: 

Warning: 

Spending on food exceeds the recommended value of 12.5%.

Savings Goal:
You are on track to meet your savings goal! You will have $36000.0 in a year!

**Action**: User clicks “Save to Database”.

**Output**: Under “Previous Results”, an entry with matching data is presented.

| **Input Label** | **Data** |
| --- | --- |
| Fixed Income | 7000 |
| Variable Income | 0 |
| One Year Savings Goal | 2000 |
| Housing | 2500 |
| Taxes | 400 |
| Car Payment | 100 |
| Internet and Phone | 50 |
| Subscriptions | 50 |
| Food | 800 |
| Entertainment | 200 |
| Personal Items | 100 |
| Utilities | 300 |
| Transportation | 100 |
| Medical | 200 |
| Miscellaneous | 100 |
| Budget Month | June |
| Budget Year | 2024 |

**Action**: User clicks “Calculate”.

**Output**: 

Warning:

Spending in housing exceeds recommended value of 30.0%.

Savings Goal:
You are on track to meet your savings goal! You will have $25200.0 in a year!

**Action**: User clicks “Save to Database”.

**Output**: Under “Previous Results”, a second entry with matching data is present.

| **Input Label** | **Data** |
| --- | --- |
| Fixed Income | 7100 |
| Variable Income | 0 |
| One Year Savings Goal | 2000 |
| Housing | 2500 |
| Taxes | 400 |
| Car Payment | 100 |
| Internet and Phone | 50 |
| Subscriptions | 50 |
| Food | 800 |
| Entertainment | 200 |
| Personal Items | 100 |
| Utilities | 300 |
| Transportation | 100 |
| Medical | 200 |
| Miscellaneous | 100 |
| Budget Month | June |
| Budget Year | 2024 |

**Action**: User clicks “Save To Database”.

**Output**: The previous entry for June 2024 is updated with the input information, as the budget Month and Year match.

**Action**: User clicks “Load” on the June 2024 entry.

**Output**: Data from the June 2024 entry is loaded into the form.

| **Input Label** | **Data** |
| --- | --- |
| Fixed Income | 7200 |
| Variable Income | 0 |
| One Year Savings Goal | 2000 |
| Housing | 2500 |
| Taxes | 400 |
| Car Payment | 100 |
| Internet and Phone | 50 |
| Subscriptions | 50 |
| Food | 800 |
| Entertainment | 200 |
| Personal Items | 100 |
| Utilities | 300 |
| Transportation | 100 |
| Medical | 200 |
| Miscellaneous | 100 |
| Budget Month | July |
| Budget Year | 2024 |

**Action**: User clicks “Save To Database”.

**Output**: Under “Previous Results”, a third entry with matching data is presented.

**Action**: User clicks “Delete” on the May 2024 entry.

**Output**: Under “Previous Results”, only 2 entries, those for June and July of 2024, are presented.

---

# Integration Tests

## T5. Event Management System - Database - User Login (FWBS# 5 - 1.2)

### Case 1

Test composition: User Login, Event Management

User logged type: None

Request: View event

Setup: (Attempt to) navigate to [localhost:8000/schedule/view](http://localhost:8000/schedule/view) with no user logged in (no schedule icon is present for unauthenticated users).

Result: Request denied; user is redirected to an error page.

### Case 2

Test composition: User Login, Event Management, Database

User logged type: User

Request: View event

Setup: Click “Schedule” on the top navigation bar with an authenticated account.

| **Input Label** | **Data** |
| --- | --- |
| DB Contents | 1 Event (test) |

Output: User is shown a page with one listed event, “test”.

Result: User is shown a current listing of events.

### Case 3

Test composition: User Login, Event Management, Database

User logged type: Advisor

Request: filter future events only

Setup: Click “Schedule” on the top navigation bar while logged in as an advisor account.

| **Input Label** | **Data** |
| --- | --- |
| DB Contents | 1 Event (test)
1 Consultation (client) |

Output: Advisor is shown a page with one listed event, “test”, and one listed consultation, “client”.

Result: Advisor is shown a current listing of events and consultations

### Case 4

Test composition: User login, Event Management, Database

User logged type: User

Request: Register for an event.

Setup: Click “Schedule” on the top navigation bar with an authenticated account.

| **Input Label** | **Data** |
| --- | --- |
| DB Contents | 1 Event (test) |

Action: Click “Register” next to the event labeled “test”.

Output: “You have successfully registered for the event “test”.

Result: User is successfully registered for an event.

### Case 5

Test composition: User login, Event Management, Database

User logged type: User

Request: Create an event

Setup: Click “Schedule” on the top navigation bar with an authenticated account. The user clicks “New Event”.

Result: Request denied; user is redirected to error page with message: “You are not authorized to create events”.

### Case 6

Test composition: User login, Event Management, Database

User logged type: Advisor

Request: Create an event with the below input cases sequentially:

| **Input Label** | **Data** |
| --- | --- |
| Title | [Empty] |
| Start Date Time | [Empty] |
| End Date Time | [Empty] |
| Description | [Any] |
| Location | [Any] |

Output: show a warning pop-up at the Title with the message: “Please fill out this field”.

| **Input Label** | **Data** |
| --- | --- |
| Title | This is an event |
| Start Date Time | [Empty] |
| End Date Time | [Empty] |
| Description | [Any] |
| Location | [Any] |

Output: show a warning pop-up at the Start Date Time field with the message: “Please fill out this field”.

| **Input Label** | **Data** |
| --- | --- |
| Title | This is an event |
| Start Date Time | April 23rd, 2025 - 09:00 AM |
| End Date Time | [Empty] |
| Description | [Any] |
| Location | [Any] |

Output: show a warning pop-up at the End Date Time field with the message: “Please fill out this field”.

| **Input Label** | **Data** |
| --- | --- |
| Title | This is an event |
| Start Date Time | April 23rd, 2025 - 09:00 AM |
| End Date Time | April 23rd, 2025 - 09:00 AM |
| Description | [Any] |
| Location | [Any] |

Output: Proceed with the filled form. Return the error message “End date must be after the start date.”

| **Input Label** | **Data** |
| --- | --- |
| Title | This is an event |
| Start Date Time | April 10th, 2025 - 09:00 AM |
| End Date Time | April 23rd, 2025 - 09:00 AM |
| Description | [Any] |
| Location | [Any] |

Output: Proceed with the filled form. Return the error message “Start or End date must be in the future.”

| **Input Label** | **Data** |
| --- | --- |
| Title | This is an event |
| Start Date Time | April 25th, 2025 - 09:00 AM |
| End Date Time | April 23rd, 2025 - 09:00 AM |
| Description | [Any] |
| Location | [Any] |

Output: Proceed with the filled form. Return the error message “End date must be after the start date.”

| **Input Label** | **Data** |
| --- | --- |
| Title | This is an event |
| Start Date Time | April 23rd, 2025 - 09:00 AM |
| End Date Time | April 25th, 2025 - 09:00 AM |
| Description | [Any] |
| Location | [Any] |

Output: Proceed with the filled form. Redirect user to the schedule view with the message: “Event created successfully”.

Result: Error cases are handled properly, and an event is created.

### Case 7

Test composition: User login, Event Management, Database

User logged type: Advisor

Prerequisite: Test case 6 completed; an event is already created.

Request: Modify event

Result: event information populated for modification. After the event is updated, redirect the user to the schedule view with a success message: “Event updated successfully”.

### Case 8

Test composition: User login, Event Management, Database

User logged type: Advisor

Prerequisite: Test case 6 completed; an event is already created.

Request: Delete event

Result: After the event is deleted, redirect the user to the schedule view with a success message: “Event deleted successfully.”

---

# Log of Meetings, Reviews, and Meetings

---

# Signature

**Date: 30 April 2025**

**Wealthwise:** 

Name:

Signature:

**Arqer:**

Name:

Signature:

---

# Appendix

---

[Introduction - Unit and Integration Test Plan](https://www.notion.so/Introduction-Unit-and-Integration-Test-Plan-1d0791d78b47809abf86d104f0699dfa?pvs=21)

[Hardware and Software used for testing - Unit and Integration Test Plan](https://www.notion.so/Hardware-and-Software-used-for-testing-Unit-and-Integration-Test-Plan-1d0791d78b478098838fc3b42d3e5e11?pvs=21)

[Testing Sets - Unit and Integration Test Plan](https://www.notion.so/Testing-Sets-Unit-and-Integration-Test-Plan-1d0791d78b4780958b3bcf1a7a9a9520?pvs=21)

[Error Handling Policy - **Unit and Integration Test Plan**](https://www.notion.so/Error-Handling-Policy-Unit-and-Integration-Test-Plan-1d0791d78b4780368b86db30041a072d?pvs=21)

[Unit Tests - **Unit and Integration Test Plan**](https://www.notion.so/Unit-Tests-Unit-and-Integration-Test-Plan-1d0791d78b478047b655ffaa0f6f23b6?pvs=21)

[Log of Meetings, Reviews, and Meetings - **Unit and Integration Test Plan**](https://www.notion.so/Log-of-Meetings-Reviews-and-Meetings-Unit-and-Integration-Test-Plan-1d0791d78b478076a0a2d8dae79cfea6?pvs=21)

[SIgnature - **Unit and Integration Test Plan**](https://www.notion.so/SIgnature-Unit-and-Integration-Test-Plan-1d0791d78b47807a8e9ddb6112812164?pvs=21)

[Appendix - Unit and Integration Test Plan](https://www.notion.so/Appendix-Unit-and-Integration-Test-Plan-1d0791d78b47807f8dd7f49a22788825?pvs=21)

| Title | [Empty] |
| --- | --- |
| Start Date Time | [Empty] |
| End Date Time | [Empty] |
| Description | [Any] |
| Location | [Any] |