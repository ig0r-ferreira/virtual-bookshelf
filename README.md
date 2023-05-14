<div align="center">
    <h1 >Virtual Bookshelf</h1>
    <div>
        <img src="demo.gif"  alt="Virtual Bookshelf">
    </div>
    <br>
    <p>A simple virtual bookshelf to practice CRUD with SQLite and SQLAlchemy.</p>
</div>

## Tools used
<div>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" alt="Python" title="Python">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40" alt="Flask" title="Flask">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="40" alt="SQLite" title="SQLite">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" width="40" alt="SQLAlchemy" title="SQLAlchemy">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" width="40" alt="Pytest" title="Pytest">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40" alt="HTML 5" title="HTML 5">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40" alt="CSS 3" title="CSS 3">&ensp;
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="40" alt="Bootstrap" title="Bootstrap">&ensp;
</div>

## How to install and run

1. Clone the project.
2. Create an `.env` file in the root of the project and define the following variables:
    
    ```properties
    FLASK_APP="virtual_bookshelf"
    FLASK_SECRET_KEY="your SECRET KEY here"
    ```
    Use the following command to create a **SECRET KEY**: `python -c 'import secrets; print(secrets.token_hex())'`
3. Open the terminal from the project folder and install by running:
    ```
    poetry install
    ```
4. Initialize the database (run this command only once):
    ```
    flask init-db
    ```
5. Run the app:
   ```
   flask --debug run
   ```

## How to run the tests

Once you have installed the project, run:
``` 
task test
```

## Author

-   [Igor Ferreira](https://github.com/ig0r-ferreira)

## License

This project is under license from [MIT](LICENSE).
