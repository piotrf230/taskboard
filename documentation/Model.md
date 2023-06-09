# Task Model
Tasks are saved as database entities, containing the following information:
- **id** - unique, automatically assigned integer
- **created** - date, when the task was created
- **updated** - date, when the task was last updated
- **name** - a short char sequence (required)
- **description** - a long optional char sequence (default - empty string)
- **status** - indicates the status of the task (new[default], in_progress, done)
- **user** - indicates the user assigned to the task

Every creation, update, and delete operation on task, a TaskHistory entity is created, which contains the following fields:

- **id** - unique, atomatically assigned integer
- **created** - date, idicates the operation date
- **action** - idicates the operation (create, update, delete)
- **task** - indicates the affected task's id number

- **name** (copy of affected task's field)
- **description** (copy of affected task's field)
- **status** (copy of affected task's field)
- **user** (copy of affected task's field)

fields are saved after the creation or update, and before the delete operation.

# User Model
Application uses Django User model and authentication system.