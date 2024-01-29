# md-footer

`md-footer` is a simple, yet powerful command-line tool designed to manage Markdown footers across multiple documents. Born out of the need for consistent footer content in Markdown files, this tool provides an easy way to append predefined footers, including social media links, contact information, and more, to your Markdown documents.

![md-footer banner](https://github.com/glizzykingdreko/md-footer/blob/main/img/banner.png)

[![PyPI version](https://badge.fury.io/py/md-footer.svg)](https://badge.fury.io/py/md-footer)


This is just a quick and easy project, will be adding more features soon if someone interested in it.

## Table of Contents
- [md-footer](#md-footer)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Getting Started](#getting-started)
    - [Templates](#templates)
      - [Creating a New Template](#creating-a-new-template)
      - [Deleting a Template](#deleting-a-template)
      - [Listing Templates](#listing-templates)
    - [Variables](#variables)
      - [Setting a Variable](#setting-a-variable)
      - [Variable Format in Templates](#variable-format-in-templates)
      - [Variables File Format](#variables-file-format)
      - [Listing Variables](#listing-variables)
    - [Appending Footer to Markdown Files](#appending-footer-to-markdown-files)
    - [Loading Variables from a JSON File](#loading-variables-from-a-json-file)
  - [Real-World Examples](#real-world-examples)
  - [Contribution](#contribution)
  - [License](#license)
  - [My links (added by md-footer :D)](#my-links-added-by-md-footer-d)

## Installation

`md-footer` can be installed using pip. Ensure you have Python 3.6 or higher installed on your system.

To install `md-footer`, run:

```
pip install md-footer
```

## Getting Started

After installing `md-footer`, you can begin setting up templates and variables to customize your footers.

### Templates

A **template** is a Markdown file that serves as a blueprint for the footer to be appended. It can include static text and placeholders for variables.

#### Creating a New Template

To add a new template:

```
md-footer add <template-file-path> [template-name]
```

If `template-name` is not provided, the file name is used as the template name.

#### Deleting a Template

To delete an existing template:

```
md-footer remove <template-name>
```

#### Listing Templates

To list all available templates:

```
md-footer templates
```

By default, you can use the `default.md` template that comes with `md-footer`. This template includes a sample footer with contact information and social media links. So you can use it by running:

```
md-footer run <markdown-file-path> -t default
```

### Variables

Variables are placeholders in a template that get replaced with their set values. 

#### Setting a Variable

Set a variable using:

```
md-footer var <variable-name> <value>
```

Example:

```
md-footer var email "example@email.com"
```

#### Variable Format in Templates

In templates, variables are denoted by curly braces:

```
{variable_name}
```

For example, `{email}` in a template will be replaced with the value of the `email` variable.

#### Variables File Format

The `vars.json` file is a JSON formatted file where variable values are defined. Example:

```json
{
    "email": "example@email.com",
    "twitter": "@exampleTwitter",
    "website": "https://example.com"
}
```

#### Listing Variables

To list all variables and their values:

```
md-footer list-vars
```

This command displays all the variables currently stored and their associated values, which are used when templates are processed.
By default are    `current_date` and `current_time` variables are set to the current date and time respectively.


### Appending Footer to Markdown Files

To append a footer to a Markdown file:

```
md-footer run <markdown-file-path> -t [template-name]
```

If `template-name` is not provided, the default template is used.

### Loading Variables from a JSON File

To load variables from a JSON file:

```
md-footer load-vars <json-file-path>
```

## Real-World Examples

1. **Consistent Footers in Project Documentation**: Maintain consistent footer sections in GitHub READMEs with updated contact information and links.
2. **Automating Blog Post Footers**: Quickly append a standard footer with author info and calls to action in Markdown-based blog posts.
3. **Educational Content and Course Notes**: Append additional resources and contact information to educational materials and notes.

## Contribution

Contributions to `md-footer` are welcome! Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

`md-footer` is released under the MIT License. See the [LICENSE](LICENSE) file for more details. 

## My links (added by md-footer :D)
- [Website](https://glizzykingdreko.github.io)
- [GitHub](https://github.com/glizzykingdreko)
- [Twitter](https://mobile.twitter.com/glizzykingdreko)
- [Medium](https://medium.com/@glizzykingdreko)
- [Email](mailto:glizzykingdreko@protonmail.com) 
- [Buy me a coffee ❤️](https://www.buymeacoffee.com/glizzykingdreko)