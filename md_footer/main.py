import argparse
import json
import os
import shutil
from datetime import datetime

class MDFooter:
    def __init__(self):
        self.setup_default_environment()
        self.execute()

    def setup_default_environment(self):
        # Get documents folder on any os
        self.documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
        # Create Md-Footer folder if it doesn't exist
        self.md_footer_dir = os.path.join(self.documents_dir, "Md-Footer")
        if not os.path.exists(self.md_footer_dir):
            os.mkdir(self.md_footer_dir)
        # Create templates folder if it doesn't exist
        self.templates_dir = os.path.join(self.md_footer_dir, "templates")
        if not os.path.exists(self.templates_dir):
            os.mkdir(self.templates_dir)
        # Create vars.json file if it doesn't exist
        self.vars_file = os.path.join(self.md_footer_dir, "vars.json")
        if not os.path.exists(self.vars_file):
            with open(self.vars_file, "w") as f:
                f.write(json.dumps({
                    "username": "Default User",
                    "twitter": "@default_user",
                    "email": "default_user@gmail.com",
                    "website": "https://default_user.github.io",
                    "github": "default_user"
                }))
        # Set up default template
        default_template_path = os.path.join(self.templates_dir, "default.md")
        if not os.path.exists(default_template_path):
            with open(default_template_path, "w") as f:
                f.write(self.default_template_content())

        # Set up default variables
        if os.path.getsize(self.vars_file) == 0:
            default_vars = {
                "username": "Default User",
                "twitter": "@default_user",
                "email": "default_user@gmail.com",
                "website": "https://default_user.github.io",
                "github": "default_user"
            }
            with open(self.vars_file, "w") as f:
                json.dump(default_vars, f)

    def default_template_content(self):
        return (
            "# Footer\n\n"
            "This is a default footer template for md-footer.\n\n"
            "Created by: {username}\n"
            "Twitter: {twitter}\n"
            "Email: {email}\n"
            "Website: {website}\n"
            "GitHub: {github}\n"
        )


    def add_template(self, name, location):
        try:
            location = os.path.abspath(location)
            template_path = os.path.join(self.templates_dir, f"{name}.md")
            if os.path.exists(template_path):
                print("Template already exists")
            elif not os.path.exists(location):
                print("Location doesn't exist")
            else:
                shutil.copyfile(location, template_path)
                print(f'Template "{name}" added successfully')
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_template(self, name):
        try:
            # Check if the template exists
            if not os.path.exists(os.path.join(self.templates_dir, f"{name}.md")):
                print(f"Template '{name}' doesn't exist")
            else:
                # Delete the template
                os.system(f"rm {os.path.join(self.templates_dir, f'{name}.md')}")
                print(f'Template "{name}" deleted successfully')
        except Exception as e:
            raise e

    def list_templates(self):
        try:
            templates = os.listdir(self.templates_dir)
            print("Templates:")
            for template in templates:
                template_path = os.path.join(self.templates_dir, template)
                size = os.path.getsize(template_path)
                modified_time = datetime.fromtimestamp(os.path.getmtime(template_path)).strftime('%Y-%m-%d %H:%M:%S')
                print(f"  - {template} (Size: {size} bytes, Last Modified: {modified_time})")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def load_vars_from_file(self, file_path):
        try:
            file_path = os.path.abspath(file_path)
            if not os.path.exists(file_path):
                print("File doesn't exist")
                return

            # Copy the file to vars.json
            shutil.copyfile(file_path, self.vars_file)
            print(f"Variables loaded from '{file_path}'")
        except Exception as e:
            print(f"An error occurred: {e}")

    def set_variable(self, name, value):
        try:
            # Read the vars.json file
            with open(self.vars_file, "r") as f:
                vars = json.load(f)
            # Set the variable
            vars[name] = value
            # Write the vars.json file
            with open(self.vars_file, "w") as f:
                json.dump(vars, f)
            print(f'Variable "{name}" set to "{value}"')
        except Exception as e:
            raise e
        pass

    def list_variables(self):
        try:
            vars = self.load_vars()
            print("Variables:")
            for key, value in vars.items():
                print(f"  - {key}: {value}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_vars(self):
        try:
            # Read the vars.json file
            with open(self.vars_file, "r") as f:
                vars = json.load(f)
            # Set the default variables
            vars["current_date"] = datetime.now().strftime("%Y-%m-%d")
            vars["current_time"] = datetime.now().strftime("%H:%M:%S")
            return vars
        except Exception as e:
            raise e

    def run_append(self, input_file, template_name):
        try:
            print(f'Appending template "{template_name}" to "{input_file}"')
            # Check if template exists
            if not os.path.exists(os.path.join(self.templates_dir, f"{template_name}.md")):
                print(f"Template '{template_name}' doesn't exist")
                return
            
            input_file = os.path.abspath(input_file)
            # Read the vars.json file
            vars = self.load_vars()
            # Read the template
            with open(os.path.join(self.templates_dir, f"{template_name}.md"), "r") as f:
                template = f.read()
            # Append the template to the input file
            with open(input_file, "a") as f:
                try: f.write(f"\n\n{template.format(**vars)}")
                except KeyError as e: 
                    var = str(e).split("'")[1]
                    print(f"Variable '{var}' not found in vars.json")
            print(f'Appended template "{template_name}" to "{input_file}"')
        except Exception as e:
            raise e
        pass

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description="md-footer CLI tool",
            epilog="Use 'md-footer <command> --help' for more information on a specific command."
        )

        subparsers = parser.add_subparsers(dest="command", required=True, title="commands")

        # Add command
        add_parser = subparsers.add_parser(
            "add",
            help="Add a new template"
        )
        add_parser.add_argument(
            "input_file",
            help="Location of the template file to add"
        )
        add_parser.add_argument(
            "name",
            nargs="?",
            help="Name of the template (defaults to file name)"
        )

        # Remove command
        remove_parser = subparsers.add_parser(
            "remove",
            help="Remove an existing template"
        )
        remove_parser.add_argument(
            "name",
            help="Name of the template to remove"
        )

        # Templates command
        templates_parser = subparsers.add_parser(
            "templates",
            help="List all available templates"
        )

        # Variable command
        var_parser = subparsers.add_parser(
            "var",
            help="Set a variable to be used in templates"
        )
        var_parser.add_argument(
            "name",
            help="Name of the variable"
        )
        var_parser.add_argument(
            "value",
            help="Value of the variable"
        )

        # Load-vars command
        load_vars_parser = subparsers.add_parser(
            "load-vars",
            help="Load variables from a JSON file"
        )
        load_vars_parser.add_argument(
            "file_path",
            help="Path of the JSON file to load variables from"
        )

        # Run command
        run_parser = subparsers.add_parser(
            "run",
            help="Append a template to the specified Markdown file"
        )
        run_parser.add_argument(
            "input_file",
            help="Path of the Markdown file to append the template to"
        )
        run_parser.add_argument(
            "-t", "--template",
            default="default",
            help="Name of the template to append (defaults to 'default')"
        )

        # List-vars command
        list_vars_parser = subparsers.add_parser(
            "list-vars",
            help="List all stored variables"
        )
        return parser
    
    def execute(self):
        parser = self.parse_args()
        args = parser.parse_args()

        if args.command is None:
            parser.print_help()
        elif args.command == "add":
            template_name = args.name if args.name else os.path.basename(args.input_file)
            self.add_template(template_name, args.input_file)
        elif args.command == "remove":
            self.delete_template(args.name)
        elif args.command == "templates":
            self.list_templates()
        elif args.command == "var":
            self.set_variable(args.name, args.value)
        elif args.command == "load-vars":
            self.load_vars_from_file(args.file_path)
        elif args.command == "run":
            self.run_append(args.input_file, args.template)
        elif args.command == "list-vars":
            self.list_variables()


if __name__ == "__main__":
    MDFooter()
