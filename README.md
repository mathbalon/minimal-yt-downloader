# 📹 Minimal YouTube Downloader

Um downloader simples e eficiente para vídeos do YouTube usando Python e Docker. Este projeto permite que você baixe vídeos do YouTube sem precisar instalar Python ou bibliotecas localmente - apenas tendo o Docker instalado em sua máquina.

## 📋 Sobre o Projeto

O **Minimal YouTube Downloader** foi desenvolvido para simplificar o processo de download de vídeos do YouTube. A principal vantagem desta solução é que ela utiliza containers Docker, eliminando a necessidade de:

- Instalar diferentes versões do Python
- Gerenciar dependências e bibliotecas Python
- Lidar com conflitos de ambiente
- Configurar ambientes virtuais

O projeto funciona da seguinte forma:

1. **Interface Interativa**: O usuário cola uma ou mais URLs do YouTube
2. **Validação**: O sistema verifica se as URLs são válidas
3. **Download Inteligente**: Baixa os vídeos na maior resolução disponível
4. **Sistema de Retry**: Tenta até 3 vezes em caso de falha
5. **Persistência**: Os vídeos são salvos em uma pasta local através de volumes Docker

### Características Principais

- ✅ **Sem instalação local**: Funciona apenas com Docker
- ✅ **Interface amigável**: Comandos simples e mensagens claras
- ✅ **Download em alta qualidade**: Sempre na melhor resolução disponível
- ✅ **Sistema de retry**: Tentativas automáticas em caso de erro
- ✅ **Validação de URLs**: Verifica URLs antes do download
- ✅ **Múltiplos downloads**: Suporte a várias URLs de uma vez

## 🛠️ Tecnologias e Bibliotecas

### Core Technologies

- **Docker**: Containerização para isolamento e portabilidade
- **Python 3.9**: Linguagem de programação principal
- **Bash**: Scripts de automação para facilitar o uso

### Bibliotecas Python

- **pytubefix**: Biblioteca principal para download de vídeos do YouTube
- **tqdm**: Barras de progresso para feedback visual durante downloads
- **urllib**: Tratamento de erros HTTP durante o processo

### Ferramentas de Desenvolvimento

- **Docker Slim Images**: Imagem Python otimizada para menor tamanho
- **Docker Volumes**: Persistência de dados entre execuções
- **Error Handling**: Sistema robusto de tratamento de erros

## 🚀 Como Usar (Apenas Docker)

### Pré-requisitos

- Docker instalado em sua máquina ([Instalar Docker](https://docs.docker.com/get-docker/))

### Passo a Passo

1. **Clone o repositório**:

   ```bash
   git clone <url-do-repositorio>
   cd minimal-yt-downloader
   ```

2. **Execute o script de automação**:

   ```bash
   chmod +x minimal-yt-downloader.sh
   ./minimal-yt-downloader.sh
   ```

3. **Primeira execução**:
   - O script irá construir automaticamente a imagem Docker
   - Criar a pasta `Videos Downloaded` se não existir
   - Iniciar o container interativo

4. **Use o programa**:
   - Cole uma ou mais URLs do YouTube quando solicitado
   - Confirme o download
   - Os vídeos serão salvos na pasta `app/Videos Downloaded`

### Comandos Úteis

- **Forçar atualização da imagem**:

  ```bash
  ./minimal-yt-downloader.sh --u
  ```

- **Execução manual do container**:

  ```bash
  docker run -it --rm -v "$(pwd)/app/Videos Downloaded:/app/Videos Downloaded" minimal-yt-downloader
  ```

## 💻 Instalação Local para Desenvolvimento

Se você preferir executar o código diretamente em sua máquina (para desenvolvimento ou customização):

### Requisitos do Sistema

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório**:

   ```bash
   git clone <url-do-repositorio>
   cd minimal-yt-downloader
   ```

2. **Crie um ambiente virtual** (recomendado):

   ```bash
   python -m venv venv
   
   # No macOS/Linux:
   source venv/bin/activate
   
   # No Windows:
   venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install --upgrade pip
   pip install pytubefix tqdm
   ```

4. **Navegue para a pasta do aplicativo**:

   ```bash
   cd app
   ```

5. **Execute o programa**:

   ```bash
   python minimal-yt-downloader.py
   ```

### Estrutura do Projeto

```text
minimal-yt-downloader/
├── app/
│   ├── minimal-yt-downloader.py    # Código principal
│   └── Videos Downloaded/          # Pasta dos vídeos baixados
├── Dockerfile                      # Configuração do container
├── minimal-yt-downloader.sh        # Script de automação
└── README.md                       # Este arquivo
```

### Desenvolvimento

Para modificar ou estender o código:

1. **Edite o arquivo principal**: `app/minimal-yt-downloader.py`
2. **Teste localmente**: Execute com Python para testar mudanças
3. **Atualize o Docker**: Use `./minimal-yt-downloader.sh --u` para reconstruir a imagem

## 📝 Notas Importantes

- Os vídeos são baixados na melhor qualidade disponível
- O programa valida URLs antes de tentar o download
- Em caso de erro, o sistema tenta até 3 vezes automaticamente
- Os vídeos ficam salvos localmente mesmo após encerrar o container
- O script shell funciona em sistemas Unix (macOS/Linux)

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades através de Pull Requests.

---

**Disclaimer**: Este projeto é apenas para fins educacionais. Respeite os termos de uso do YouTube e os direitos autorais dos conteúdos.
