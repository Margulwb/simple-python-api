# Backend

## Linux

### Install Flask package

```bash
sudo apt install python3
pip install flask
```

### Run pyhon api

```bash
python3 api.py
```

### Run on docker 

#### Build image

```bash
/backend/
docker build -t test:test .
docker run -it -p 5000:5000 test:test
```

## Windows

### Install Flask package

Install python

```bash
pip install flask
```

### Run pyhon api

```bash
python.exe api.py
```

# Endpoints API

# /users

Users API

## /users

Endpoint to get date

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/users
```

## /users/add

Endpoint to add date

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "hej", "age": 30000000}' http://127.0.0.1:5000/users/add
```

## /users/<index>

Endpoint to add date

```bash
curl -X DELETE http://127.0.0.1:5000/users/<index>
```

## /users/login

Endpoint to check user exist

```bash
curl -X POST -H "Content-Type: application/json" 
    -d '{
        "login": "example_login",
        "password": "example_login",
        "role": "example_role"
        }' http://localhost:5000/users/login
```

## /users/modify/<id>

Endpoint to modifying user data via ID

```bash
curl -X POST -H "Content-Type: application/json" 
    -d '{
            "login": "value1",
            "password": "value2"
        }' http://127.0.0.1:5000/users/modify/2
```

# /articles

Article API

## /articles

Endpoint to get date

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/articles
```

## /articles/add

Endpoint do dodawani kolejnych artykułów

```bash
curl -u $USER:$PASS -X POST -H "Content-Type: application/json; charset=utf-8"
    -d '{
        "id": 1,
        "title": "Chiny",
        "subTitle": "opis cywilizacji",
        "date": "02.06.2024",
        "content": [
            {
                "title": "Bonusy chińskiej cywilizacji",
                "content": [
                    "Centrum Miasta (Town Center) wystrzeliwuje pociski z armaty ręcznej",
                    "Mieszkańcy (Villagers) wznoszą o 50% szybciej budynki obronne, wszystkie inne budynki o 100% szybciej",
                    "Budynki ekonomiczne generują podatki, za każdy dostarczony zasób (bez względu na ilość zrzucanego surowca)",
                    "Budynki militarne generują podatki przy produkcji każdej jednostki i badanej technologii",
                    "Jednostka Imperial Official może zebrać maksymalnie 20 podatków od budynku
                    "Technologie chemii zostają przyznane za darmo po przejściu do IV ery",
                    "Doki pracują o 20% szybciej."
                ]
            }
        ]
    },' http://127.0.0.1:5000/articles/add
```

# /forum

Article API

## /forum

Endpoint to get date

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/forum
```

## /forum/like/<int:post>/<int:userId>

Endpoint to get like for post -> next request undo like

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/forum/like/<int:post>/<int:userId>
```

## /forum/unlike/<int:post>/<int:userId>

Endpoint to get unlike for post -> next request undo unlike

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/forum/unlike/<int:post>/<int:userId>
```

## /forum/like/<int:post>/<int:comment>/<int:userId>

Endpoint to get like for comment of post -> next request undo like

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/forum/like/<int:post>/<int:comment>/<int:userId>
```

## /forum/unlike/<int:post>/<int:comment>/<int:userId>

Endpoint to get unlike for comment of post -> next request undo unlike

```bash
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/forum/unlike/<int:post>/<int:comment>/<int:userId>
```

## /forum/addPost

Endpoint to add new Post in forum

```bash
 curl -X POST -H "Content-Type: application/json; charset=utf-8" 
    -d '{
        "userId": 1,
        "title": "Przykładowy tytuł",
        "content": "To jest treść posta z polskimi znakami: ąćęłńóśźż"
        }' http://127.0.0.1:5000/forum/addPost
```
# simple-python-api
