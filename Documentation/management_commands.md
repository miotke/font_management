# Management Commands

Quick description and usage of each management command. This can also be found at the top of each
managment command file for inline documentation.

## create_users

This was based on a tutorial and would need a lot of work to be used as a production command.
It takes a name and generates an account with a randomized password, printing it all out to the console.

Usage: `python manage.py create_users Gus`


## add_font

This management command takes a directory of font files(.ost) and copies them
to the font_storage directory.

Usage: `python manange.py add_font [path_to_folder_of_fonts]`

## delete_font

This command takes a font family name that already exists in the font_storage
directory and removes it along with all files within that directory.

The command already assumes the entire path except for the font family group name
that needs to be passed in. This is currently font_storage/ but will need to be repalced
with whatever would be used as the file storage, i.e. AWS S3

Usage: `python manage.py delete_font [name of font group]`

## delete_database

--- DEVELOPMENT HELPER COMMAND ONLY ---

Deletes the database(db.sqlite3) and all migration files except `__init__.py`.

Usage: `python manage.py delete_database`
