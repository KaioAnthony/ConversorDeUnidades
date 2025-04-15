# Explicação do Conversor de Unidades

Este código é um conversor de unidades de armazenamento (byte, kilobyte, megabyte, gigabyte e terabyte) utilizando a biblioteca `customtkinter` para criar uma interface gráfica. Aqui está uma explicação detalhada de como ele funciona:

### 1. **Configuração Inicial**
O código importa `customtkinter` e define:
- **Modo de aparência** (`System`): Adapta-se ao tema do sistema operacional.
- **Tema de cores padrão** (`dark-blue`).

Depois, cria uma janela principal (`root`) com título `"Conversor de Unidades"` e dimensões `450x400`.

### 2. **Função de Conversão**
A função `converter()` recebe um valor digitado pelo usuário e converte entre unidades de armazenamento com base nas seleções feitas nos menus suspensos. Ela:
- Obtém o valor numérico inserido (`entry.get()`).
- Lê as unidades de origem (`origem.get()`) e destino (`destino.get()`).
- Aplica regras matemáticas para conversão (multiplicação ou divisão por 1024).
- Exibe o resultado no label `resultado`.
- Lida com erros, como entradas inválidas (`ValueError`).

### 3. **Interface Gráfica**
A interface exibe:
- Um campo de entrada (`CTkEntry`) para digitação do valor.
- Dois menus suspensos (`CTkOptionMenu`) para selecionar unidades de origem e destino.
- Um botão `"Converter"` que chama `converter()`.
- Um label para mostrar o resultado da conversão.

### 4. **Alternância de Tema**
A função `trocar_modo()` permite alternar entre os modos **Dark** e **Light**. O botão `"Trocar Tema"` chama essa função, ajustando a aparência da interface conforme necessário.

### 5. **Execução**
`root.mainloop()` inicia a interface gráfica e mantém a janela aberta até o usuário fechá-la.

