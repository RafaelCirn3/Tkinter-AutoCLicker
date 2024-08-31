# Autoclicker com Tkinter

Este projeto é um autoclicker simples desenvolvido usando Python e a biblioteca Tkinter para a interface gráfica. Ele permite que os usuários realizem cliques automáticos com opções de personalização, como o intervalo de tempo entre os cliques, o número de cliques por execução, e a escolha entre o botão esquerdo ou direito do mouse.

## Funcionalidades

- Iniciar e parar o autoclicker com um clique de botão ou pressionando a tecla `F8`.
- Definir o intervalo de tempo entre os cliques em segundos.
- Escolher o número de cliques por execução (1 ou 2 cliques).
- Selecionar qual botão do mouse usar (esquerdo ou direito).
- Interface gráfica amigável utilizando Tkinter com widgets estilizados.

## Requisitos do Sistema

- Python 3.x
- Bibliotecas Python:
  - tkinter (incluso por padrão no Python)
  - pyautogui
  - keyboard

## Instalação

1. **Clone o repositório ou baixe o código fonte.**

    ```bash
    git clone https://github.com/seu-usuario/autoclicker-tkinter.git
    cd autoclicker-tkinter
    ```

2. **Instale as dependências necessárias.**

    Você pode instalar as bibliotecas necessárias usando o pip:

    ```bash
    pip install pyautogui keyboard
    ```

3. **Execute o script Python.**

    ```bash
    python autoclicker_tkinter.py
    ```

## Como Usar

1. **Defina o delay entre cliques:** Use o campo de entrada para especificar o tempo em segundos entre cada clique. O valor padrão é `0.1` segundos.

2. **Escolha o número de cliques por execução:** Selecione entre 1 ou 2 cliques usando os botões de opção.

3. **Selecione o botão do mouse:** Escolha entre o botão esquerdo ou direito para os cliques automáticos.

4. **Controle o autoclicker:** 
   - Pressione o botão `Start` para iniciar o autoclicker.
   - Pressione o botão `Stop` para parar o autoclicker.
   - Use a tecla `F8` para alternar entre iniciar e parar o autoclicker.

5. **Status do autoclicker:** O status atual do autoclicker (Running/Stopped) será exibido na interface, com feedback visual para facilitar o uso.

## Observações

- Certifique-se de que a janela da aplicação Tkinter esteja em foco ou minimizada ao usar o autoclicker em outras janelas.
- A tecla `F8` é usada como atalho global para iniciar/parar o autoclicker. Pode ser necessário ajustar se `F8` for utilizado por outras aplicações.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
