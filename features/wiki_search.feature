#Feature: Employee log in
#
#  Scenario Outline: Searching for various keywords
#    Given The Employee is on the TRSM Home Page
#    When The User types <marcdon>  and password <1010>in the search bar
#    When The User clicks the search button
#    Then The title should be <title>
#
#  Examples:
#    |   word      |  title                                                    |
#    |   Mario     | marcdon - Tuition Reimbursement Service Management  App   |
#    |   Wario     | jude - Tuition Reimbursement Service Management  App      |
#    |   Kirby     | Donald - Tuition Reimbursement Service Management  App    |
#    |   Ganondorf | Ganon - Tuition Reimbursement Service Management  App     |
