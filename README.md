# EP1 de Sistemas Distribuídos

Este repositório contém o código e os arquivos relacionados ao EP1 da disciplina de Sistemas Distribuídos.

## Estrutura do Projeto

- **analysis/**: Diretório destinado a análises realizadas no projeto.
- **build/**: Diretório para arquivos de build ou compilação.
- **images/**: Contém imagens utilizadas no projeto.
- **instructions for the project/**: Diretório com as instruções do projeto.
  - `ep.pdf`: Documento PDF com as instruções detalhadas do EP1.
- **output/**: Diretório para saída de dados ou resultados gerados pelo projeto.

## Como começar

* Leia o arquivo `ep.pdf` localizado em `instructions for the project/` para entender os requisitos do projeto.
  
* No terminal certifique-se de que todas as dependências necessárias estão instaladas (talvez seja necessário atualizá-lo):
```
    pip install grpcio grpcio-tools
```  
* Rodar o .proto
```
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

**Isso irá gerar dois arquivos:**

  1 calculator_pb2.py
  2 calculator_pb2_grpc.py
  
* Inicie o servidor:
```
    python server.py
```
* Inicie o cliente:
```
    python client.py
```
## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
