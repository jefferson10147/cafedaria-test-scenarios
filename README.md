# Test cases: Cafedaria page

<table>
    <tr>
        <td>
            In this project, you may find the test cases for the Cafedaria page
            With the following stack of technologies like Python 3, Selenium, and Behave.
        </td>
    </tr>
</table>

## How to execute this project (UNIX Systems)

1- Clone this project, on your local machine:

```bash
$ git clone https://github.com/jefferson10147/cafedaria-test-scenarios
```

2- Navigate to the directory and create a Python virtual environment:

```bash
$ cd cafedaria-test-scenarios
$ python3 -m venv ./venv
```

3- Activate env:

```bash
$ source your_venv/bin/activate
```

4- Install dependencies:

```bash
$ pip install -r requirements.txt
```

## Examples of execution:

- To run all the test cases from a specific feature file:
```bash
$ behave features/tests/main_page.feature
```

- To run a specific test case from a specific feature file:
```bash
$ behave features/tests/main_page.feature --name 'User can add two products to the cart'
```
