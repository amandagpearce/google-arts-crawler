# Google Arts Crawler

Projeto criado como componente extra do MVP da disciplina de Back-end avançado do curso de pós-graduação em Desenvolvimento Full Stack da PUC-Rio. 

## O que é?
Web Crawler construído em Python que busca as urls das imagens de obras do site Google Arts and Culture. 

### Instalação com o Docker
2. Na raiz do projeto, crie a imagem:
```bash
  docker build -t g-arts-service .
```

3. Rode a imagem criada:
```bash
  docker run -p 5000:5000 g-arts-service
```

