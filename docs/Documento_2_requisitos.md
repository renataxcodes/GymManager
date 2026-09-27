# Documento de Requisitos — Gerenciador de Treinos

**Projeto:** Gerenciador de Treinos
**Disciplina:** Gerência de Configuração
**Documento:** Documento 2 — Documento de Requisitos
**Versão:** 1.0
**Status:** Em desenvolvimento

---

## 1. Introdução

### 1.1 Propósito

Este documento tem como objetivo apresentar e especificar os requisitos do sistema **Gerenciador de Treinos**, definindo suas principais funcionalidades, características, restrições e necessidades para o desenvolvimento da aplicação.

O sistema será desenvolvido para auxiliar profissionais de educação física, especialmente personal trainers, na criação, organização e gerenciamento de treinos. Os alunos também poderão utilizar o sistema para consultar os treinos disponibilizados pelo profissional.

Este documento servirá como referência para o desenvolvimento do sistema e será considerado um **Item de Configuração (IC)** do projeto, sendo controlado por meio de versionamento.

### 1.2 Escopo

O **Gerenciador de Treinos** será uma aplicação web destinada ao gerenciamento de treinos entre personal trainers e alunos.

O sistema permitirá que o personal trainer cadastre e gerencie alunos, cadastre exercícios e crie treinos personalizados. Os alunos poderão acessar seus treinos e visualizar as informações dos exercícios definidos pelo profissional.

As principais funcionalidades previstas são:

* Autenticação de usuários;
* Cadastro e gerenciamento de alunos;
* Cadastro e gerenciamento de exercícios;
* Criação e edição de treinos;
* Associação de treinos aos alunos;
* Visualização dos treinos pelos alunos;
* Visualização das informações dos exercícios.

### 1.3 Fora do Escopo

Não fazem parte do escopo inicial do sistema:

* Pagamento de mensalidades;
* Prescrição médica;
* Diagnóstico de doenças;
* Integração com dispositivos de monitoramento físico;
* Integração com academias externas;
* Aplicativo mobile nativo;
* Consultas ou diagnósticos médicos.

### 1.4 Visão Geral do Sistema

O sistema será uma aplicação web composta por dois tipos principais de usuários:

* **Personal Trainer:** responsável pelo gerenciamento dos alunos, exercícios e treinos;
* **Aluno:** responsável por consultar os treinos disponibilizados pelo personal trainer.

O personal poderá criar treinos personalizados para seus alunos, adicionando exercícios e definindo informações como séries, repetições, carga e intervalo.

O aluno poderá acessar sua conta e consultar os treinos que foram disponibilizados pelo personal.

### 1.5 Definições e Acrônimos

| Termo            | Definição                                                            |
| ---------------- | -------------------------------------------------------------------- |
| RF               | Requisito Funcional                                                  |
| RNF              | Requisito Não Funcional                                              |
| IC               | Item de Configuração                                                 |
| CRUD             | Create, Read, Update e Delete                                        |
| Personal Trainer | Profissional responsável pela elaboração e gerenciamento dos treinos |
| Aluno            | Usuário que realiza os treinos cadastrados pelo personal             |
| Treino           | Conjunto organizado de exercícios destinado a um aluno               |
| Exercício        | Atividade física cadastrada no sistema                               |

---

# 2. Descrição Geral

## 2.1 Perspectiva do Produto

O Gerenciador de Treinos será desenvolvido como uma aplicação web acessível por meio de navegadores.

A aplicação será composta por uma interface de usuário, uma camada responsável pelo processamento das informações e um banco de dados responsável pelo armazenamento dos dados do sistema.

As tecnologias previstas para o desenvolvimento são:

* HTML;
* CSS;
* JavaScript;
* Python;
* Flask;
* MySQL.

## 2.2 Funções Principais

As principais funções do sistema serão:

* Realizar login;
* Controlar o acesso de acordo com o tipo de usuário;
* Cadastrar alunos;
* Consultar alunos;
* Alterar dados dos alunos;
* Excluir alunos;
* Cadastrar exercícios;
* Consultar exercícios;
* Criar treinos;
* Editar treinos;
* Excluir treinos;
* Adicionar exercícios aos treinos;
* Definir séries, repetições, carga e intervalo;
* Associar treinos aos alunos;
* Permitir que o aluno visualize seus treinos.

## 2.3 Características dos Usuários

### Personal Trainer

O personal trainer será responsável pelo gerenciamento dos alunos e pela elaboração dos treinos.

Suas principais funções serão:

* Realizar login;
* Cadastrar alunos;
* Consultar alunos;
* Editar dados dos alunos;
* Excluir alunos;
* Cadastrar exercícios;
* Consultar exercícios;
* Criar treinos;
* Editar treinos;
* Excluir treinos;
* Adicionar exercícios aos treinos;
* Definir séries, repetições, carga e intervalo;
* Associar treinos aos alunos.

### Aluno

O aluno utilizará o sistema principalmente para consultar seus treinos.

Suas principais funções serão:

* Realizar login;
* Visualizar seus dados;
* Visualizar seus treinos;
* Visualizar os exercícios;
* Visualizar séries e repetições;
* Visualizar cargas e intervalos cadastrados.

## 2.4 Restrições

O sistema deverá respeitar as seguintes restrições:

* O acesso às funcionalidades deverá ser controlado de acordo com o tipo de usuário;
* Os dados deverão ser armazenados em um banco de dados;
* Funcionalidades administrativas deverão estar disponíveis somente para usuários autorizados;
* O sistema deverá funcionar em navegadores modernos;
* Os principais artefatos do projeto deverão ser controlados por versionamento;
* Alterações relevantes deverão ser registradas no histórico do projeto.

## 2.5 Suposições

Consideram-se as seguintes suposições:

* Os usuários possuirão acesso à internet;
* O personal trainer será responsável pelo cadastro e gerenciamento dos treinos;
* Os dados fornecidos pelos usuários serão válidos;
* O sistema será utilizado inicialmente em ambiente web;
* O banco de dados estará disponível para o funcionamento da aplicação.

---

# 3. Requisitos Específicos

## 3.1 Requisitos Funcionais

### RF01 — Cadastro de Personal

O sistema deverá permitir o cadastro de personal trainers, armazenando as informações necessárias para sua identificação e acesso ao sistema.

### RF02 — Cadastro de Aluno

O sistema deverá permitir que o personal trainer cadastre alunos, informando seus dados básicos.

### RF03 — Consulta de Alunos

O sistema deverá permitir que o personal trainer consulte os alunos cadastrados.

### RF04 — Alteração de Aluno

O sistema deverá permitir que o personal trainer altere os dados de um aluno cadastrado.

### RF05 — Exclusão de Aluno

O sistema deverá permitir que o personal trainer exclua um aluno cadastrado, respeitando as regras de integridade do banco de dados.

### RF06 — Login

O sistema deverá permitir que personal trainers e alunos realizem autenticação utilizando suas credenciais.

### RF07 — Controle de Acesso

O sistema deverá identificar o tipo de usuário autenticado e disponibilizar somente as funcionalidades correspondentes ao seu perfil.

### RF08 — Cadastro de Exercícios

O sistema deverá permitir que o personal trainer cadastre exercícios, incluindo informações como nome, descrição e grupo muscular.

### RF09 — Consulta de Exercícios

O sistema deverá permitir a consulta dos exercícios cadastrados.

### RF10 — Criação de Treino

O sistema deverá permitir que o personal trainer crie um treino para um aluno.

### RF11 — Adição de Exercícios ao Treino

O sistema deverá permitir que o personal trainer adicione exercícios a um treino.

### RF12 — Configuração dos Exercícios

O sistema deverá permitir que o personal trainer informe dados relacionados aos exercícios, como:

* Séries;
* Repetições;
* Carga;
* Intervalo.

### RF13 — Edição de Treino

O sistema deverá permitir que o personal trainer altere as informações de um treino existente.

### RF14 — Exclusão de Treino

O sistema deverá permitir que o personal trainer exclua um treino existente.

### RF15 — Associação de Treino ao Aluno

O sistema deverá permitir que um treino seja associado a um aluno específico.

### RF16 — Visualização do Treino pelo Aluno

O sistema deverá permitir que o aluno visualize os treinos associados ao seu perfil.

### RF17 — Visualização dos Exercícios

O sistema deverá permitir que o aluno visualize os exercícios pertencentes ao seu treino.

### RF18 — Visualização das Informações do Exercício

O sistema deverá apresentar ao aluno informações como séries, repetições, carga e intervalo, quando essas informações estiverem cadastradas.

### RF19 — Histórico de Treinos

O sistema poderá permitir que o aluno consulte treinos anteriormente disponibilizados.

---

# 3.2 Requisitos Não Funcionais

### RNF01 — Segurança

O sistema deverá controlar o acesso às funcionalidades de acordo com o perfil do usuário.

### RNF02 — Autenticação

O sistema deverá realizar a autenticação dos usuários antes de permitir o acesso às funcionalidades restritas.

### RNF03 — Usabilidade

A interface deverá apresentar navegação simples, organizada e compreensível para os usuários.

### RNF04 — Responsividade

A aplicação deverá adaptar sua interface a diferentes tamanhos de tela, permitindo sua utilização em computadores, tablets e smartphones.

### RNF05 — Desempenho

O sistema deverá apresentar tempo de resposta adequado para as operações comuns de cadastro, consulta, alteração e exclusão.

### RNF06 — Integridade dos Dados

O sistema deverá manter a consistência e integridade das informações armazenadas no banco de dados.

### RNF07 — Disponibilidade

As funcionalidades deverão estar disponíveis para os usuários autorizados enquanto o sistema estiver em funcionamento.

### RNF08 — Compatibilidade

O sistema deverá funcionar em navegadores modernos.

### RNF09 — Manutenibilidade

O código deverá ser organizado de maneira que facilite futuras alterações, correções e manutenção.

### RNF10 — Versionamento

Os principais artefatos do projeto deverão ser controlados por meio de um sistema de controle de versão, permitindo acompanhar as alterações realizadas durante o desenvolvimento.

---

# 4. Modelagem

## 4.1 Atores

O sistema terá inicialmente dois atores principais:

### Personal Trainer

Responsável pelo gerenciamento dos alunos, exercícios e treinos.

### Aluno

Responsável pela consulta dos treinos e exercícios disponibilizados pelo personal trainer.

## 4.2 Casos de Uso

### Personal Trainer

* Realizar login;
* Cadastrar aluno;
* Consultar aluno;
* Editar aluno;
* Excluir aluno;
* Cadastrar exercício;
* Consultar exercício;
* Criar treino;
* Editar treino;
* Excluir treino;
* Adicionar exercícios ao treino;
* Definir séries, repetições, carga e intervalo;
* Associar treino ao aluno.

### Aluno

* Realizar login;
* Consultar seus dados;
* Visualizar seus treinos;
* Visualizar exercícios;
* Visualizar séries;
* Visualizar repetições;
* Visualizar carga;
* Visualizar intervalo.

## 4.3 Diagrama de Casos de Uso

O diagrama de casos de uso deverá representar os atores **Personal Trainer** e **Aluno** e suas respectivas interações com o sistema.

O arquivo deverá ser armazenado em:

```text
/diagramas/caso-de-uso.png
```

## 4.4 Diagrama de Classes Conceitual

O diagrama de classes deverá representar as principais entidades do sistema.

### Usuário

* id
* nome
* email
* senha
* tipo_usuario

### Personal

* id
* dados pessoais
* dados profissionais

### Aluno

* id
* dados pessoais
* personal responsável

### Exercício

* id
* nome
* descrição
* grupo muscular

### Treino

* id
* nome
* descrição
* aluno
* personal

### Item do Treino

* id
* treino
* exercício
* séries
* repetições
* carga
* intervalo

O arquivo deverá ser armazenado em:

```text
/diagramas/diagrama-de-classes.png
```

---

# 5. Protótipos de Interface

Os protótipos deverão representar as principais telas previstas para o sistema.

Inicialmente, serão consideradas as seguintes telas:

1. Tela de Login;
2. Dashboard do Personal Trainer;
3. Cadastro de Aluno;
4. Lista de Alunos;
5. Cadastro de Exercício;
6. Lista de Exercícios;
7. Cadastro de Treino;
8. Edição de Treino;
9. Dashboard do Aluno;
10. Visualização do Treino.

Os protótipos deverão ser armazenados no diretório:

```text
/prototipos/
```

---

# 6. Rastreabilidade

A rastreabilidade tem como objetivo relacionar os requisitos aos respectivos **Itens de Configuração (ICs)** do projeto, permitindo acompanhar a evolução dos artefatos durante o desenvolvimento.

## 6.1 Itens de Configuração

| Código | Item de Configuração     |
| ------ | ------------------------ |
| IC01   | Plano de Projeto         |
| IC02   | Documento de Requisitos  |
| IC03   | Diagrama de Casos de Uso |
| IC04   | Diagrama de Classes      |
| IC05   | Protótipos de Interface  |
| IC06   | Código-Fonte             |
| IC07   | Banco de Dados           |
| IC08   | README                   |

## 6.2 Matriz de Rastreabilidade

| Requisito | Descrição                     | Item de Configuração      |
| --------- | ----------------------------- | ------------------------- |
| RF01      | Cadastro de Personal          | IC06 / IC07               |
| RF02      | Cadastro de Aluno             | IC06 / IC07               |
| RF03      | Consulta de Alunos            | IC06 / IC07               |
| RF04      | Alteração de Aluno            | IC06 / IC07               |
| RF05      | Exclusão de Aluno             | IC06 / IC07               |
| RF06      | Login                         | IC03 / IC06 / IC07        |
| RF07      | Controle de Acesso            | IC03 / IC06               |
| RF08      | Cadastro de Exercícios        | IC06 / IC07               |
| RF09      | Consulta de Exercícios        | IC06 / IC07               |
| RF10      | Criação de Treino             | IC03 / IC04 / IC06 / IC07 |
| RF11      | Adição de Exercícios          | IC04 / IC06 / IC07        |
| RF12      | Configuração dos Exercícios   | IC04 / IC06 / IC07        |
| RF13      | Edição de Treino              | IC06 / IC07               |
| RF14      | Exclusão de Treino            | IC06 / IC07               |
| RF15      | Associação de Treino ao Aluno | IC04 / IC06 / IC07        |
| RF16      | Visualização do Treino        | IC05 / IC06               |
| RF17      | Visualização dos Exercícios   | IC05 / IC06               |
| RF18      | Informações do Exercício      | IC05 / IC06               |
| RF19      | Histórico de Treinos          | IC05 / IC06 / IC07        |
| RNF01     | Segurança                     | IC06 / IC07               |
| RNF02     | Autenticação                  | IC06 / IC07               |
| RNF03     | Usabilidade                   | IC05 / IC06               |
| RNF04     | Responsividade                | IC05 / IC06               |
| RNF05     | Desempenho                    | IC06 / IC07               |
| RNF06     | Integridade dos Dados         | IC07                      |
| RNF07     | Disponibilidade               | IC06 / IC07               |
| RNF08     | Compatibilidade               | IC05 / IC06               |
| RNF09     | Manutenibilidade              | IC06                      |
| RNF10     | Versionamento                 | IC01 / IC02 / IC06 / IC07 |

---

# 7. Controle de Mudanças

As alterações realizadas nos requisitos e demais artefatos do projeto deverão ser registradas por meio do sistema de controle de versão utilizado pela equipe.

As alterações deverão possuir mensagens de commit claras, permitindo identificar o conteúdo modificado.

Exemplos:

```text
docs: adiciona documento de requisitos
docs: atualiza plano de projeto
docs: adiciona diagrama de casos de uso
docs: atualiza matriz de rastreabilidade
feat: adiciona cadastro de alunos
feat: adiciona cadastro de exercícios
feat: adiciona gerenciamento de treinos
fix: corrige cadastro de alunos
```

Alterações significativas nos requisitos deverão ser registradas em uma nova versão do documento, mantendo o histórico das versões anteriores.

---

# 8. Controle de Versões do Documento

| Versão | Data    | Descrição                          | Responsável |
| ------ | ------- | ---------------------------------- | ----------- |
| 1.0    | 09/2026 | Criação do Documento de Requisitos | Equipe      |

---

# 9. Considerações Finais

Este Documento de Requisitos apresenta as principais características, funcionalidades e restrições previstas para o desenvolvimento do **Gerenciador de Treinos**.

O documento servirá como referência para as etapas seguintes do projeto, orientando o desenvolvimento do sistema, a elaboração do banco de dados, a criação das interfaces e a implementação das funcionalidades.

Durante o desenvolvimento, os requisitos poderão ser alterados conforme as necessidades identificadas pela equipe. Essas alterações deverão ser registradas e controladas de acordo com as práticas de Gerência de Configuração adotadas no projeto.

A utilização da rastreabilidade permitirá relacionar os requisitos aos respectivos Itens de Configuração, facilitando o acompanhamento das mudanças e a manutenção dos artefatos do projeto.
