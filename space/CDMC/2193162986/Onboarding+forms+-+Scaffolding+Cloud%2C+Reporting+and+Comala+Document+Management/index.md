# Onboarding forms - Scaffolding Cloud, Reporting and Comala Document Management

In this article, we demonstrate how to use three apps together to onboard new employees: **Scaffolding Forms and Templates** to create an onboarding form, **Comala Document Management** to create an onboarding workflow, and **Reporting for Confluence** to generate a report summarizing the data in the onboarding forms.

## **Step 1: Create the onboarding form using Scaffolding Forms and Templates**

Start by creating a form using Scaffolding Forms and Templates for Confluence. This app allows you to define customizable form fields to capture essential onboarding information. In our use case, we are capturing the following details:

- **Laptop Selection**
- **Special Accommodations**
- **T-shirt Size**
- **Credit Card Information**
- **Onboarding Date**
- **Onboarding Feedback**

Once the fields are defined, save the form as a template. New employees will use this template to complete the required onboarding information.

## **Step 2: Manage the onboarding workflow using Comala Document Management**

After creating the form, we will manage the onboarding process using Comala Document Management. This allows for customizable workflows to ensure the form goes through the appropriate review and approval process.

Workflow Overview:

- **Complete Onboarding Form**: This is the first state where the new employee fills out and submits the form.
- **Review**: The form is automatically sent to the hiring manager for review. They can either approve the form, request changes, or reject it.
- **Approved**: Once approved, authorized personnel, such as HR representatives, can access and modify the form.

The workflow includes transition rules for each state. For example:

- If the hiring manager needs the employee to modify their laptop selection, they can reject the form, which sends it back to the Complete Onboarding Form state.
- After the employee updates the form, it is re-submitted for approval.

Once approved, the onboarding form is marked as complete, but HR or other authorized users can still modify it if needed, sending it back into the review state.

## **Step 3: Generate reports Using Reporting for Confluence**

Once onboarding forms have been completed, tracking and reporting on the data captured is important. This is where Reporting for Confluence comes in.

To generate a report:

1. Create a new report page and insert the Reporting for Confluence macro.
2. Set up queries to pull in data from the relevant forms, filtering by space and using data fields from the Scaffolding forms. For example, you can report on the Laptop Selection field for all employees who have submitted their onboarding forms.
3. Add Scaffolding blocks to display form-specific fields such as T-shirt Size and Special Accommodations.
4. The result is a comprehensive report that summarizes all onboarding form data in a single page, allowing HR teams to easily view and analyze the submitted information.

### Onboarding workflow - Part 1

### Onboarding workflow - Part 2

### Onboarding workflow - Part 3

Combining Scaffolding Forms and Templates, Comala Document Management, and Reporting for Confluence allows you to create a seamless onboarding workflow that ensures proper form submission, review, approval, and reporting. This process automates much of the administrative overhead while ensuring accurate and timely data collection and processing.