# Tutorial de utilização da API de Currículos

### Instalação

* Fazer o download da api em: [https://github.com/weberxw/delin](https://github.com/weberxw/delin)
* Instalar as dependências que estão no arquivo *requirements.txt*, de preferência em um [virtualenv](https://virtualenv.pypa.io/en/latest/)
* Uma vez dentro do diretório *delin/myrest*, executar os comandos abaixo para realizar as migrações no banco de dados e criar um super usuário, que será usado para acessar a interface de autenticação da api:
    * python3 manage.py makemigrations
    * python3 manage.py migrate
    * python3 manage.py createsuperuser (definir um usuário e senha)
    * python3 manage.py runserver

* Fazer Login na página [http://localhost:8000/admin](http://localhost:8000/admin) utilizando o super usuário criado anteriormente.
* Em *DJANGO OAUTH TOOLKIT*, clicar em *Applications* e depois em *Add Applications*.
* Não alterar os campos *Client ID* e *Client Secret*, eles são gerados automaticamente.
* Definir *Client Type* como Confidential e *Authorization grant type* como Resource owner password-based.
* Definir um nome para a aplicação que será responsável pela autenticação da api e clicar em Save.


### Permissões

* Ainda em [http://localhost:8000/admin](http://localhost:8000/admin), no menu *Users* é possível criar usuários com permissões específicas, basta ao criar um novo usuário definir a respectiva permissão em *User Permissions*. Por exemplo, um usuário que somente pode VISUALIZAR a lista de currículos terá somente a permissão: *myapp | resume | can view resume*. Esse usuário não será capaz de CRIAR ou EDITAR currículos. Ainda existem opções *can add resume*, *can change resume* e *can delete resume* para personalizar usuários com permissões diferentes.

* Feitos todos os passos até aqui a api deverá estar pronta para operar normalmente, bastando executar os comandos abaixo:

### Autenticação

* Executar o seguinte comando:
```
curl -X POST http://localhost:8000/o/token/ -H "content-type: application/x-www-form-urlencoded" -d "grant_type=password&client_id={CLIENT_ID_CADASTRADO}&client_secret={CLIENT_SECRET_CADASTRADO}&username={USERNAME}&password={PASSWORD}"
```

* A resposta deve ser a seguinte:
```
{"access_token": "suLSxrfXjrGM2wzsu5H4Wq06HLPfRh", "token_type": "Bearer", "refresh_token": "0VSzsrr1BMezryaCrZaZkGUxp4miBK", "expires_in": 36000, "scope": "read groups write"}
```

* O  access_token da resposta deve ser utilizado em todos os comandos executados a seguir, sem ele a resposta terá erro de autenticação na api.




### Utilização da API

Feita a autenticação e extraído o access_token da resposta, basta enviar os comandos de utilização da api, que são os seguintes:

#### Inserção de um novo Currículo
```
curl -X POST http://127.0.0.1:8000/insert/ -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}" -H 'content-type: application/json' -d '{"name": "Fulano", "address": "Rua Tal", "profession": "Profissão X", "education": "Faculdade Tal"}'
```

#### Visualização de todos os Currículos
```
curl -X GET http://localhost:8000/resumes/ -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}"
```

#### Visualização com ordem específica

###### Ordenar por ID: 
```
curl -X GET http://localhost:8000/resumes/?ordering=id -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}"
```
###### Ordenar por Nome:
```
curl -X GET http://localhost:8000/resumes/?ordering=name -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}"
```

#### Visualização com filtro específico

###### Visualização por nome:
```
curl -X GET http://localhost:8000/resumes/?name=Lucas -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}" -H "Accept: application/json"
```
###### Visualização por profissão:
```
curl -X GET http://localhost:8000/resumes/?profession=Estudante -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}" -H "Accept: application/json"
```
###### Visualização por educação:
```
curl -X GET http://localhost:8000/resumes/?education=Tecnico -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}" -H "Accept: application/json"
```

#### Edição de um currículo existente
```
curl -X PUT http://localhost:8000/update/{USER_ID}/ -H "Authorization: Bearer {ACCESS_TOKEN_USUARIO_CADASTRADO}" -H 'content-type: application/json' -d '{"name": "Fulano de tal", "address": "Rua X", "profession": "Profissão Y", "education": "Faculdade Y"}'
```
**Qualquer comando executado por um usuário sem a devida permissão (ver no tópico sobre Permissões) retornará o seguinte erro: {"detail":"You do not have permission to perform this action."}. O superusuário tem permissão pra executar todos os comandos.**


### Autor

Lucas Weber – weberxw@gmail.com