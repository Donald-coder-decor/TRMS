Feature: Employee Login Process

  Scenario: Testing Login for employee
    Given The Employee is on the Login Home Page'
    When Employee enters Username as <username>'
    When Employee enters Password as <password>'
    When Employee should click on the login button
    Then The Employee should be on the  login Page




  Scenario: Supervisor  logging in
    Given The Supervisor is  ready to login
    When The Supervisor put in the passsword
    When The Supervisor clicks on the Login Button
    Then The Supervisor should be on the Login and his special view Home page

  Scenario: The Department Head logging in
#    Given The Department Head is  ready to login
    When The Department Head put in the passsword
    When The Department Head clicks on the Login Button
    Then The Department Head should be on the Login anda Home page

   Scenario: The Benco loggin in
#    Given The Benco is  ready to login
    When The Benco put in the passsword
    And  The Benco put in the username
    When The Benco clicks on the Login Button
    Then The Benco should be on the Login anda Home page

  Scenario: Employee submitting reimbursement
#    Given Employee is alrealdy on the Login in page
    When Employee types in the location
    When Employee types in the Description
    When Employee types in the grade format
    When Employee types in Event type
    When Employee clicks on submit form button
    Then The Benco should be on the Login anda Home page


    #Supivisor appraval
    When Superivisor is on the approval page
    When Supervisor type in the Employee ID
    When Supervisor clicks the Approval button
    Then The form is approved