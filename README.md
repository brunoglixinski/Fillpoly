# Preenchimento de Polígonos (Scanline / Fillpoly)

Projeto desenvolvido para a disciplina de Computação Gráfica.

## 🚀 Funcionalidades
- **Estruturas de Dados:** Implementação das tabelas `TA` (Edge Table/ Tabela de Arestas) e `AET` (Active Edge Table).
- **Tratamento de Arestas:** Descarte de arestas horizontais e cálculo do $1/m$.
- **Preenchimento:** Varredura por linha (scanline) utilizando geradores Python (`yield`) para desacoplamento da interface gráfica.

## 📁 Estrutura
- `geometria.py`: Contém as primitivas (`ponto`, `aresta`) e o algoritmo principal de preenchimento.
