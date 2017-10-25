# Entities
## Person
+ citizen id
+ first name
+ middle name
+ last name

## Role
+ id
+ name
+ description
+ permissions

## Permission
+ name
+ description
+ id

## Employee (subclass of: Person)
+ id
+ rank
+ division
+ roles

## Account
+ id
+ role
+ username
+ password
+ log

## Activity
+ id
+ name
+ goal
+ objectives
+ status
+ schedule
+ participants

## Schedule
+ id
+ name
+ description
+ location
+ start date_time
+ end date_time

## ISO Audit (subclass of: Activity)
+ id
+ auditors
+ auditees
