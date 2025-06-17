# System_Monitoring_Bet
Este repositório contém o projeto desenvolvido para o seminário da disciplina de **Estrutura de Dados I**, focado em resolver um problema do mundo real: **Cassino Online**.


## Estrutura do Repositório

O repositório é organizado da seguinte forma:

-   **`docs/`**: Contém o relatório técnico do projeto.
  
-   **`src/`**: Contém todos os códigos-fonte da aplicação.
  
    -   `main.py`: Ponto de entrada principal para rodar todo o cassino.
      
    -   **`uteis/`**: Pacote para módulos de uso geral.
       
        -   `ferramentas.py`: Funções auxiliares como limpar a tela.
           
    -   **`contas/`**: Pacote para o gerenciamento de contas e usuários.
      
        -   `usuario.py`: Definição da classe `User`.
        
        -   `acesso.py`: Métodos de login, criação e exclusão de contas.
            
    -   **`interface/`**: Pacote para a interface do usuário no terminal.
        
        -   `menu.py`: Definição da classe `Menu` e da lógica de navegação.
           
    -   **`jogos/`**: Pacote contendo a lógica dos jogos do cassino.
       
        -   `roleta.py`: Lógica do jogo da Roleta.
          
        -   `caca_niquel.py`: Lógica do jogo Caça-Níquel.
     
          
## Como executar
Para rodar este projeto, siga os passos abaixo:

1.  **Clone o Repositório:**
    ```sh
    git clone https://github.com/JoaoVituu/System_Monitoring_Bet
    cd System_Monitoring_Bet
    ```
    
2. **Execute o seguinte comando:**
   ```sh
    python -m src.main
    ```

   
## Integrantes do Grupo:
* João Vitor Monteiro dos Santos
* Allex França Pereira
* Gabriel Rezende Borges
* Enzo Henrique Barcelos de Brito  
