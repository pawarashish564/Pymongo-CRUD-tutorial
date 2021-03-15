<h1 align="center">
  <!-- <img src=".github/logo.png" width="80"  -->
     <!-- height="80"/><br> -->
PyMongo CRUD Tutorial
</h1>

<p align="center">
Simple CLI for  performing CRUD Operations to mongodb atlas .
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python%20%20%F0%9F%90%8D-3.8-blueviolet">
  <img src="https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github">
</p>

</p>

<br>
<br>

[![📟](https://raw.githubusercontent.com/ahmadawais/stuff/master/images/git/usage.png)](./../../)
### Usage


```sh
# install dependencies
pipenv install 

# select * from collection
python app.py --pass **** --find

# select one record from collection where age=29
python app.py --pass **** --find-one age 29

# add new record into collection
python app.py --pass **** --add

# update record starting two values are search keys (age,29) -> updated with {city:Washington username: JO}
python app.py --pass **** --update-one age 29 city Washington username JO

#delete record with age=29
python app.py --pass **** --delete-one age 29

```

### 📄 Bug reports, feature requests, etc

This is an ongoing project and I welcome contributions and suggestions! Feel free to submit a PR.
