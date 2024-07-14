# Apex

<div align="center">
  <img src=".github/assets/logo.jpg" width="500" height="500" align="center">
</div>

## What is Apex?
Apex is a simple and lightweight project to create a new project by using a blueprint for ANY LANGUAGE! 
Apex find all tags and variables in the blueprint and replace them with the values that you provide.  
You need know the syntax of the tags and variables to use Apex correctly in your blueprint.

## How to use Apex?
You can install it with pip:
```bash
pip install apex
```

After install the Apex, you can use it in your terminal:
```bash
apex path/to/blueprint
```

After that, Apex will ask you for selecting the tags and the values of variables in the blueprint.

## Apex Syntax

### tags in blueprint
Tag is a section of code that labeled with a name. You can use tags in your blueprint to customize the blueprint for your project.  
The syntax of the tag in file is:

```python
def func_one():
    pass

# @apex:tag_name:tag
def func_two():
    pass
# @apex:end
```

You can specify the tag name in comment with `@apex:tag_name:tag`. To end the tag section, you can
use `@apex:end` in the comment.
Apex will find the tag section and asking you that want this section or not.  
If you want to use tag for just file or folder, you can use the tag syntax in the file or folder name.
```bash
|
|--- file_name@apex:tag_name:tag
|
|--- folder_name@apex:tag_name:tag
    |
    |--- file_name
```

### tags in blueprint
To use variables in the blueprint, you can use the syntax below:

```python
def func_one():
    print("@apex:variable_name:var")
```

For declaring a variable anywhere in the blueprint, you just need write `@apex:variable_name:var`.
Apex will find the variable and asking you for the value of the variable.

