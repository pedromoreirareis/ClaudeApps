# Coruja Explica 🦉 — Ideias e melhorias para a próxima versão

## 1. Criar um novo prompt para textos curtos

Criar um novo prompt chamado **“Pequeno”**, destinado à geração de textos curtos, fáceis de ler e adequados para atividades rápidas de leitura e compreensão.

O prompt deverá seguir estas regras:

- **Quantidade máxima:** 200 palavras por texto.
- **Tempo de leitura:** no máximo 5 minutos.
- **Parágrafos:** preferencialmente 2 ou 3 parágrafos, com no máximo 3 ou 4 linhas por parágrafo.
- **Conteúdo:** manter as pequenas partes de conversas e os detalhes sobre a fonte de conhecimento, conforme a estrutura de conteúdo utilizada pelo aplicativo.
- **Objetivo:** gerar textos curtos, organizados e agradáveis de ler, sem excesso de informações, facilitando a leitura e a compreensão.

A quantidade de palavras, o número de parágrafos e os demais limites deverão respeitar as configurações definidas para esse prompt, quando houver configurações personalizadas.

## 2. Criar um prompt extremamente configurável

Criar um novo prompt chamado **“Personalizado”** (ou “Configurável”), que permita definir detalhadamente como a inteligência artificial deverá gerar o conteúdo.

Diferentemente dos demais prompts, que terão instruções e finalidades predefinidas, esse prompt deverá oferecer ampla liberdade de configuração, reunindo as possibilidades dos outros prompts em uma única opção.

Deverá permitir configurar, entre outros parâmetros:

- Quantidade mínima e máxima de palavras.
- Quantidade mínima e máxima de parágrafos.
- Quantidade mínima e máxima de linhas por parágrafo.
- Estrutura, formato e organização do texto.
- Inclusão de diálogos, curiosidades, perguntas, respostas e fontes de conhecimento.
- Demais características e elementos disponíveis nos outros prompts.

O objetivo é criar um **prompt universal e altamente configurável**, no qual eu possa definir os parâmetros desejados para cada texto, sem ficar limitado às regras predefinidas dos demais prompts.

Os outros prompts deverão continuar simples e prontos para uso, cada um com sua finalidade específica. O prompt “Personalizado” será a opção para quando eu quiser controlar detalhadamente a geração do conteúdo.

## 3. Organizar os prompts disponíveis no aplicativo

O aplicativo deverá disponibilizar, no mínimo, os seguintes prompts:

1. **Pequeno:** gera textos curtos, com até 200 palavras e tempo estimado de leitura de até 5 minutos, respeitando os demais parâmetros definidos.
2. **Leitura do dia:** mantém a finalidade do prompt já existente no aplicativo.
3. **Personalizado:** permite configurar detalhadamente a geração do conteúdo, incluindo os parâmetros disponíveis nos demais prompts.
4. **Entender:** mantém a finalidade de ajudar a compreender um conteúdo ou assunto.
5. **Adaptar texto pronto:** permite adaptar um texto existente, respeitando a finalidade desse prompt.
6. **Continuar no mesmo assunto:** permite gerar a continuação de um conteúdo, mantendo o assunto em desenvolvimento.
7. **Consertar formato:** permite corrigir a formatação de um texto, preservando seu conteúdo original.

Os nomes e as descrições deverão deixar claro para que serve cada opção, facilitando a escolha do prompt adequado antes de solicitar um texto à inteligência artificial.

Os prompts já existentes deverão manter suas finalidades. As configurações do prompt “Personalizado” não deverão alterar indevidamente o comportamento dos demais prompts.

## 4. Adicionar configurações de seleção de texto na leitura

Na área de configurações do aplicativo, adicionar duas opções para controlar o que será selecionado quando o usuário tocar no texto durante a leitura.

Essas opções deverão funcionar de maneira semelhante ao comportamento de seleção de texto do aplicativo **“O Esforço Vence”**, utilizado para atividades de alfabetização.

### 4.1. Ativar sílabas

Adicionar uma opção chamada **“Ativar sílabas”**.

Quando essa opção estiver ativada, ao tocar em uma palavra durante a leitura, o aplicativo deverá selecionar somente a sílaba correspondente ao ponto tocado, em vez de selecionar a linha inteira.

Essa funcionalidade será especialmente útil para atividades de alfabetização de crianças de 3 e 4 anos, permitindo trabalhar a identificação e a leitura de sílabas individualmente.

### 4.2. Ativar palavras

Adicionar uma opção chamada **“Ativar palavras”**.

Quando essa opção estiver ativada, ao tocar em uma palavra durante a leitura, o aplicativo deverá selecionar somente a palavra tocada, sem selecionar a linha inteira nem apenas uma sílaba.

### 4.3. Comportamento padrão

Quando nenhuma das duas opções estiver ativada, o aplicativo deverá manter o comportamento atual: **ao tocar em um ponto do texto, selecionar a linha inteira correspondente**.

### 4.4. Exclusividade entre as opções

As opções “Ativar sílabas” e “Ativar palavras” não poderão ficar ativadas simultaneamente, pois representam modos diferentes de seleção.

O comportamento esperado será:

- **Sílabas:** seleciona somente a sílaba tocada.
- **Palavras:** seleciona somente a palavra tocada.
- **Nenhuma opção ativada:** seleciona a linha inteira.

Ao ativar uma opção, a outra deverá ser desativada automaticamente.

Para a interface, avaliar qual componente representa melhor esse comportamento: caixas de seleção (*checkboxes*), interruptores (*switches*) ou botões de opção (*radio buttons*). A interface deverá impedir que os dois modos sejam ativados ao mesmo tempo e deixar o modo selecionado claramente identificado.

## 5. Orientações para a implementação

As melhorias deverão ser implementadas considerando a estrutura atual do Coruja Explica e as seguintes regras:

- Preservar as funcionalidades que já funcionam corretamente.
- Não modificar partes do aplicativo que não estejam relacionadas às melhorias solicitadas.
- Manter o funcionamento das funcionalidades existentes de leitura, formatação e preparação de textos.
- Garantir que os parâmetros do prompt “Pequeno” sejam respeitados na geração dos conteúdos.
- Garantir que o prompt “Personalizado” permita controlar os parâmetros disponíveis sem modificar as configurações predefinidas dos outros prompts.
- Garantir que os modos de seleção de texto funcionem corretamente em dispositivos móveis.
- Verificar se as novas configurações são mantidas após fechar e reabrir o aplicativo, conforme o comportamento esperado das configurações existentes.
- Testar as mudanças antes de disponibilizar a nova versão, verificando a lógica, a apresentação visual e possíveis efeitos sobre as funcionalidades existentes.

O objetivo é melhorar a flexibilidade do aplicativo sem comprometer o que já foi desenvolvido.

## Checklist de conferência

- [x] Criar a especificação do prompt para textos curtos.
- [x] Definir o prompt “Personalizado” como extremamente configurável.
- [x] Manter os demais prompts com finalidades predefinidas.
- [x] Esclarecer os comportamentos dos modos de seleção por sílaba, palavra e linha.
- [x] Preservar as orientações para implementação e testes.
- [ ] Confirmar se o texto representa exatamente o que você deseja antes de utilizá-lo como instrução de desenvolvimento.
