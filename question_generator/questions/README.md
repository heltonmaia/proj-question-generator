# Pasta Padrão de Questões - questions

Esta é a pasta padrão para armazenar todas as questões geradas pelo Python Question Generator.

## Estrutura da Pasta

```
questions/
├── README.md                    # Este arquivo
├── question_ch5_0001.txt        # Arquivo de questão (formato texto)
├── question_ch5_0001.py         # Solução da questão
├── question_ch5_0001.sh         # Script de teste
├── question_ch5_0001_test.txt   # Casos de teste
└── passed/                      # Subpasta para questões aprovadas
    ├── question_ch5_0001.txt    # Questões que passaram nos testes
    ├── question_ch5_0001.py     # Soluções aprovadas
    ├── question_ch5_0001.sh     # Scripts de teste aprovados
    └── question_ch5_0001_test.txt # Casos de teste aprovados
```

## Tipos de Arquivos

- **`.txt`**: Arquivo principal da questão com enunciado, solução e testes
- **`.py`**: Arquivo Python com a solução da questão
- **`.sh`**: Script bash para executar os testes automaticamente
- **`_test.txt`**: Arquivo com casos de teste para validar a solução

## Processo de Geração

1. **Geração**: Questões são criadas a partir do material online
2. **Processamento**: Arquivos `.txt` são convertidos em `.py`, `.sh` e `_test.txt`
3. **Teste**: Scripts `.sh` executam os testes automaticamente
4. **Filtragem**: Questões que passam nos testes são movidas para `passed/`
5. **PDF**: Questões aprovadas são compiladas em um PDF final

## Configuração

Esta pasta é criada automaticamente pelo sistema se não existir. É a pasta padrão para todas as operações do gerador de questões.

## Uso

- Use esta pasta para armazenar todas as questões geradas
- As questões aprovadas serão automaticamente organizadas na subpasta `passed/`
- O sistema sempre verifica se esta pasta existe antes de executar operações 