# Padroes-Projeto-Software
Trabalho final de engenharia II


# Padrão Factory - UserFactory

## Por que escolhi o padrão Factory?

Optei pelo padrão Factory porque ele facilita a criação de objetos de forma flexível e centralizada. Com o Factory, posso encapsular a lógica de instanciamento da classe `User`, tornando o código mais organizado, reutilizável e fácil de manter. Isso é especialmente útil quando a criação do objeto pode variar conforme parâmetros ou regras de negócio.

## Como vou usar

A classe `UserFactory` possui um método estático `create_user`, que recebe o nome do usuário e o papel (role), retornando uma instância da classe `User`. Assim, sempre que precisar criar um novo usuário, basta chamar:

```python
from src.factores.user_factory import UserFactory

user = UserFactory.create_user("Antonio")
print(user)
```

Dessa forma, centralizo a criação dos objetos `User` e posso modificar a lógica de criação em um único lugar, caso necessário no futuro.
