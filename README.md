<div align="center">
    <h1 >Virtual Bookshelf</h1>
    <div>
        <img src="demo.gif"  alt="Virtual Bookshelf" style="display: block;">
    </div>
    <br>
    <p>A simple virtual bookshelf to practice CRUD with SQLite and SQLAlchemy.</p>
</div>

## Tools used
<div>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" title="Python" width="40" style="margin-right:10px;">
    <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="Flask" title="Flask" width="40" style="margin-right:10px; filter: invert(100%) sepia(100%) saturate(0%) hue-rotate(41deg) brightness(103%) contrast(101%);">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" title="SQLite" width="40" style="margin-right:10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" alt="SQLAlchemy" title="SQLAlchemy" width="40" style="margin-right:10px; filter: invert(1) hue-rotate(180deg) saturate(10);">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" alt="Pytest" title="Pytest" width="40" style="margin-right:10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" title="HTML5" width="40" style="margin-right:10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" title="CSS3" width="40" style="margin-right:10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap" title="Bootstrap" width="40" style="margin-right:10px;">
</div>

## How to install and run

1. Clone the project.
2. Create an `.env` file in the root of the project and define the following variables:
    
    ```properties
    FLASK_APP="virtual_bookshelf"
    FLASK_SECRET_KEY="your SECRET KEY here"
    ```
    Use this command to create a **SECRET KEY**: `python -c 'import secrets; print(secrets.token_hex())'`
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
