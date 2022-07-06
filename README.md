# Python_withAlgebra

:us: Projects developed by Fábio Mori in 2020 with Python using linear algebra functions to solve some problems. Add more things in here

:brazil: Projetos, desenvolvidos pelo Fábio Mori, em 2020, com Python utilizando funções de Álgebra Linear para solucionar problemas.

# Sistemas Lineares com Python
## Programando Álgebra Linear
### Numpy

* Biblioteca de código aberto para computação numérica em Python.
* Os conceitos de vetorização, indexação e transmissão em forma de arrays multidimensionais.
* Contém funções matemáticas geradoras de números aleatórios e álgebra linear.
* Facilidade de entendimento e curva de aprendizagem rápida.
* Comum no desenvolvimento de redes neurais de aprendizagem profunda, processamento de imagem e computação gráfica.
* Comando para importar as funcionalidades do Numpy para utilização no algorítmo.
   * `import numpy as np`    

### Linalg

* Um submódulo da biblioteca Numpy que contém um conjunto de funções de álgebra linear.
* Comandos diretos para obtenção de auto valores, autovetores e determinantes.
* Pode calcular a norma de um vetor, o posto de uma matriz e diversas operações para solucionar sistemas lineares.
* Comando para obter a matriz inversa, que é essencial para solução de combinações lineares (as matrizes transposta, diagonal e identidade são obtidas diretamente pelo Numpy).
* Obtém a solução de problemas lineares __A.x=b__
* Comando para importar as funcionalidades do Linalg do Numpy para utilização no algorítmo.
   * `from numpy import linalg as lin`    

### Matplotlib

* Biblioteca de código aberto para computação gráfica em Python
* Cria visualizações estáticas e dinâmicas para análise e visualização do usuário
* Gráficos com qualidade e personalizáveis como estilos de linha, fonte, eixos, legendas em ambiente interativo
* Muito bem utilizado em conjunto com a biblioteca Numpy para a vizualização dos resultados das operações matriciais em sistemas lineares
* Possibilidades para importar as funcionalidades do Matplotlib para utilização no algorítmo
   *`import matplotlib as mpl`
   *`import matplotlib.pyplot as plt`
   
Assista uma aula da Escola Matriz explicando estes conceitos no link a seguir:
[Aula 21: Programando Álgebra Linear](https://youtu.be/xlJg_xhAa9o)  
Confira o exercício proposto e a solução em Python sobre este tema:
[Numpy e Matplotlib](https://github.com/DoctorNerds/Python_withAlgebra/tree/main/01.numpyWithMatplolib)
   
## Matrizes I
### Funções matriciais I

* Recursos do Numpy para obtenção de matrizes através dos comandos:
   * `np.matriz`: retorna uma matriz (o próprio Numpy não recomenda mais sua utilização, mas sim criar matrizes através das arrays).
   * `np.diag`: retorna os elementos da diagonal da matriz.
   * `np.eye`: cria uma matriz identidade.
   * `np.zeros`: cria uma matriz nula.
   * `np.transpose`: retorna a matriz transposta.
* Comandos para operações com arrays:
   * `np.array`: cria uma array.
   * `np.arrange` e `np.linspace`: retonar valores ou números com espaçamento uniforme em um intervalo determinado.
* Tipos de variáveis Numpy:
   * `np.int`: variável do tipo inteiro.
   * `np.float`: variável do tipo ponto flutuante.

### Fatiamento de dados

* Selecionar apenas algum pedaço específico de uma array ou uma matriz para realizar uma operação com ele.
* Utilizado quando queremos selecionar colunas ou linhas específicas da matriz para extrair resultados definidos de um banco de dados.
* Exemplos para uma matriz Amxn:
   * `A[:]` ou `A[:,:]`: todos os elementos da matriz.
   * `A[1,:]`: todos os elementos da linha 1.
   * `A[5,:]`: todos os elementos da linha 5.
   * `A[:,3]`: todos os elementos da coluna 3.
   * `A[1,10]`: elemento da linha 1, coluna 3.
   * `A[4,5:10]`: elementos da linha 4 da coluna 5 até a coluna 9.
   * `A[3:6,10]`: elementos da coluna 8 da linha 3 até a linha 5.

### Operações matriciais

* Utilizando as arrays do Numpy as operações entre vetores e matrizes se torna mais direta em comparação aos métodos com funções.
* Podemos fazer operações com matrizes inteiras ou com pedaços da matriz utilizando a técnica de fatiamento.
* Exemplos com duas matrizes A e B:
   * `A[0,:] + B[1,:]`: soma a linha 0 da matriz A com a linha 1 da matriz B.
   * `A + B`: soma as matrizes A e B.
   * `A * B`: multiplica elemento por elemento das matrizes A e B.
   * `A / B`: divide elemento por elemento das matrizes A e B.
   * `k * A`: multiplica a matriz A por um escalar k.
   * `A.dot(B)`: faz a multiplicação matricial (da forma correta) entre A e B.

Assista uma aula da Escola Matriz explicando estes conceitos no link a seguir:
[Aula 22: Matrizes I](https://youtu.be/jimdcV9fENM)  
Confira o exercício proposto e a solução em Python sobre este tema:
[Matrizes I](https://github.com/DoctorNerds/Python_withAlgebra/tree/main/02.matrices1)
  
## Matrizes II
### Funções matriciais II

* Recursos do submódulo linalg do Numpy acrescentam mais funcionalidades de Álgebra Linear como:
   * `linalg.eig`: calcula os autovalores e autovetores de uma matriz quadrada.
   * `linalg.eigvals`: calcula os autovalores de uma matriz quadrada.
   * `linalg.norm`: calcula a norma de um vetor ou matriz.
* Outras funções algébricas disponíveis apenas no linalg:
   * `linalg.inv`: calcula a matriz inversa. 
   * `linalg.det`: calcula a determinante da matriz.
   * `linalg.svd`: calcula a fatoração de uma matriz através da decomposição em valores singulares.
   * `linalg.solve`: resolve um sistema de equações matriciais lineares.

### Importando dados

* Podemos utilizar o Python para importar os dados com origem de outros softwares e sistemas de aquisição.
* Esta prática é muito comum para análise de dados através do big data.
* Existem muitas bibliotecas para desenvolver ciência de dados em Python e importar arquivos como o formato .csv (Excel).
* Exemplo para ler um arquivo .csv de avaliação dos usuários dos filmes da Netflix e gravar os dados na array "notas":
```
import csv
import numpy as np
   
notas=np.load('matriz_netflix.csv',
               delimiter=',',
               unpack=True,
               dtype='str')
 ```
### Plotando gráficos

* Para enxergarmos tendências e obtermos respostas muitas vezes precisamos visualizar graficamente a solução do problema.
* O matplotlib é a biblioteca mais popular de visualização de dados em Python e também é muito utilizado em conjunto da biblioteca Pandas para importar dados do Excel.
* Exemplo para ler e imprimir um arquivo .csv da variação de parâmetros de um ativo na bolsa de valores:
```
import matplotlib.pyplot as plt
import pandas as pd

BTC = pd.read_csv('BTC_5anos.csv’)

plt.figure(figsize=(25,15))
plt.title('Bitcoin Prices over Time (in USD)’)
plt.plot(BTC.Date, BTC.AdjClose, label='United States’)
plt.xticks(rotation=45)
plt.xlabel('Period')
plt.ylabel('Price US Dollars')
```

Assista uma aula da Escola Matriz explicando estes conceitos no link a seguir:
[Aula 23: Matrizes II](https://youtu.be/XIzoEeTBat4)  
Confira o exercício proposto e a solução em Python sobre este tema:
[Matrizes II](https://github.com/DoctorNerds/Python_withAlgebra/tree/main/03.matrices2)

## Combinações Lineares
### Solucionando Ax=b

* Uma das grandes aplicações práticas de Álgebra Linear presente em praticamente todas as áreas é a solução de combinações lineares definidas por Ax=b.
* Devemos equacionar um problema real na forma matricial para aplicar as soluções computacionais com conceitos de Álgebra Linear para chegar a uma solução.
* O número de linhas da matriz A estará relacionado ao número de equações do sistema e o número de colunas ao número de variáveis. 
* Um sistema pode não ter solução, ter uma única solução ou infinitas possibilidades.
* O posto da matriz A e a forma escolona reduzida da matriz composta por *A* e *b* são as ferramentas que iremos utilizar. 

### Forma escalonada reduzida

* A forma escalonada reduzida irá aplicar o método de eliminação ou fatoração na matriz aumentada *Ab* que transformará as equações do sistema em uma forma direta para obtermos sua solução.
* Ela nos dará as informações de colunas livres e colunas pivôs, posto da matriz, dimensões do espaço linha, coluna e nulo.
* Para sistemas onde não existe a inversa da matriz A vamos aplicar a forma escalonada reduzida para obter a resposta.
* Existem linguagens e softwares computacionais que possuem comandos diretos para solucionar uma matriz na forma escalonada reduzida, como o MatLab.

### Octave Online

* É uma ferramenta gratuita que possui compatibilidade com a linguagem do MatLab e pode ser utilizado para aprendizado, desenvolvimento e testes de algoritmos.
* MatLab é uma linguagem computacional feito para cálculos vetoriais, com matrizes e demais aplicações numéricas.
* Podemos criar uma função para determinar a forma escalonada reduzida de uma matriz ou utilizar funções disponíveis da linguagem utilizada no algoritmo.
* Vamos utilizar o MatLab ao invés do Python pois ele possui um comando específico para aplicar a forma escalonada `rref` (Row Reduction Echelon Form) além de podermos aprender outra linguagem computacional.

Assista uma aula da Escola Matriz explicando estes conceitos no link a seguir:
[Aula 24: Combinações Lineares](https://youtu.be/QXVvM1rqQHs)  

## Debate sobre análise de dados
### Big Data e indicadores de performance

* Na prática, apenas resolver um sistema e gerar os resultados é o suficiente?
* O que é uma análise de dados e qual a sua importância para obter conclusões e respostas sobre a aplicação de um sistema?
* Quais os tipos de gráficos e como escolher o melhor modelo para sua análise?
* O que são os KPI e qual sua utilidade e aplicação para a análise de dados?

Assista uma aula da Escola Matriz explicando estes conceitos no link a seguir:
[Aula 25: Debate sobre Análise de Dados](https://youtu.be/lrjlomNs0yc) 

## A seguir vamos apresentar estudos de caso baseados em problemas reais onde podemos aplicar Álgebra Linear com Python para obter uma solução. 

## Eletrificação veicular
### Veículos elétricos

* São veículos movidos através de motores elétricos e são considerados zero emissões pois não emitem gases nocivos para o ambiente.
* Diminui a poluição sonora já que emite menos ruído que os motores a combustão.
* A tecnologia que fornece energia para os carros elétricos são as baterias.
* Como é uma tecnologia ainda em desenvolvimento, o processo do tempo de recarga das baterias e sua autonomia ainda são uma desvantagem em comparação com os carros a combustão.
* Apesar do preço da compra de uma unidade ser alto, o preço da energia, necessária para recarregar, é mais barato que o preço da gasolina, necessária para reabastecer.

### Sustentabilidade

* É uma característica de um processo que devemos analisar em um determinado prazo para avaliarmos se uma atividade é sustentável ou não.
* Embora os carros elétricos não emitam poluentes quando estão se movimentando, sua construção envolve processos que podem ser nocivos ao meio ambiente.
* As baterias em seu processo de obtenção e/ou descarte devido a química presente nas células, podem causar malefícios ao meio ambiente.
* A forma como a energia utilizada para recarregar um carro elétrico é produzida também define a sustentabilidade do processo e está vinculada a matriz energética do país/estado ou região onde o veículo será produzido.

### Matriz Energética

* É uma representação dos recursos energéticos disponíveis em um país para serem utilizados em processos de produção.
* Muito diferente entre cada país devido a quantidade de recursos de fontes primárias de energia presentes em cada território.
* Petróleo, carvão, gás natural, água, Sol, vento e biomassa são exemplos de fontes primárias de energia.
* O Brasil possui uma das matrizes energéticas mais renováveis do mundo com a energia eólica, solar, etanol e seus recursos hídricos.
* Para que o processo da utilização de um veículo elétrico seja sustentável, a matriz energética do seu país também deve ser.

Assista uma aula da Escola Matriz explicando este estudo de caso e aplicando uma solução em Octave Online no link a seguir:
[Aula 26: Eletrificação Veicular](https://youtu.be/ljUtsJp8zUA)

## Criptografia de mensagens
### Criptografia

* É uma técnica de comunicação segura que se baseia em protocolos que definem como a mensagem será encriptada e transmitida para outro usuário que deverá fazer a decriptação desta mensagem para obter sua informação real.
* Somente o destinatário da mensagem deve ser capaz de obter o conteúdo verdadeiro da mensagem.
* Podemos aplicar o conceito da matriz como uma chave para embaralhar o conteúdo verdadeiro em mensagem criptografada e utilizar a inversa da matriz da para transformar esta mensagem em seu conteúdo original.
* As mensagens criptografadas são muito comuns de serem transmitidas através de comunicações seriais.

### Comunicação serial

* É o processo de enviar uma informação através de uma sequência de bits, números binários que podem assumir valores de 0 e 1.
* A sequência em que os bits são ordenados representa todo o conteúdo da informação que será transmitida e segue padrões estabelecidos de comunicação serial como o protocolo CAN.
* Contém informações sobre para quem a mensagem deverá ser entregue, código de verificação de erro, tamanho específico da mensagem e permite que possamos aplicar a técnica de criptografia, desde que quem receba a informação seja capaz de fazer a decriptação da mensagem.

### Segurança da informação

* Estamos vivendo uma era onde dados de todos os tipos como as informações pessoais, perfis de compras, viagens, comidas e preferências do usuário, conteúdos restritos de inteligência de empresas e governamentais, existem em um número gigantesco e suas informações representam uma grande vantagem competitiva e poder para quem os possui.
* Garantir a segurança dos dados é fundamental para garantir os direitos dos usuários e as informações de um governo.
* Existem muitos algoritmos desenvolvidos para proteger o conteúdo das informações, mas a técnica de criptografia é a base para entendermos como é possível proteger o conteúdo de uma mensagem de uma ponta a outra da comunicação.

Assista uma aula da Escola Matriz explicando este estudo de caso no link a seguir:
[Aula 27: Criptografia de mensagens](https://youtu.be/9IpPzkiEDEU)  
Confira o exercício proposto e a solução em Python sobre este estudo de caso:
[Criptografia](https://github.com/DoctorNerds/Python_withAlgebra/tree/main/04.criptography)

## Economia e mercado de ações
### Bolsa de valores

* É um ambiente de mercado de compra e venda onde se negociam ações de empresas de capital aberto.
* Ação é uma pequena parte da empresa e sua disposição é a composição societária dela, pois quando você compra uma ação de uma empresa na bolsa você também virá sócio dela.
* Apenas são negociadas ações das empresas que fizeram seu IPO (Initial Public Offering), ou seja, empresas que abriram seu capital disponibilizando suas ações em troca de investimento.
* A maior bolsa de valores hoje no Brasil se chama B3 e para um cidadão comum poder negociar seus investimentos nela deve fazer isso por intermédio de uma corretora de investimentos.

### Renda variável

* São ativos financeiros que possuem retornos não previsíveis, ao contrário da renda fixa que possui uma taxa de rentabilidade fixa no momento do investimento.
* O retorno de um ativo de renda variável tem sua rentabilidade ligada a empresa ou ativo principal, além do cenário econômico e político do país.
* Investir em renda variável possui maior risco, porém o retorno sobre o investimento tem um potencial muito maior que os investimentos de renda fixa.
* Ações são os ativos de renda variável mais comuns, porém existem outros como as ETFs (Exchange Traded Funds), BDRs (Brazilian Depositary Receipts), fundos de investimentos, fundos imobiliários, dentre outros.

### Carteira de ações e tipos de investidores

* Um investidor da bolsa de valores possui uma carteira de ações que pode ser composta por ativos de renda fixa e renda variável.
* A diversificação do capital investido é uma forma de ter mais estabilidade e segurança nos investimentos já que seu patrimônio não está vinculado ao resultado de apenas uma empresa ou ativo principal.
* Existem investidores do tipo trader e o buy and hold.
* O trader é um investidor que compra e vende ações diariamente de forma especulativa com objetivo de conseguir lucros a curto prazo.
* O buy and hold é um investidor de longo prazo que compra ativos com o objetivo de se tornar sócio da empresa, lucrar com seu crescimento e distribuição de dividendos.

Assista uma aula da Escola Matriz explicando este estudo de caso no link a seguir:
[Aula 28: Economia e mercado de ações](https://youtu.be/oH7gIm-WIl8)  
Confira o exercício proposto e a solução em Python sobre este estudo de caso:
[Sistema Linear](https://github.com/DoctorNerds/Python_withAlgebra/tree/main/05.linearSystem)

## Netflix
### Mercado digital

* Atualmente vivemos uma era onde o mercado digital vem crescendo e dominando quase todas as áreas de vendas e entretenimento.
* Não temos mais a necessidade de nos locomover até as lojas físicas quando desejamos comprar algo, podemos fazer isso através do site da gigante Amazon por exemplo.
* A educação a distância vem abrindo muitas oportunidades na melhoria do aprendizado no aluno através da internet.
* As reuniões empresariais se tornaram mais acessíveis e práticas através das salas de reuniões digitais.
* O mercado de filmes e conteúdo digital está cada vez mais popular em plataformas como a Netflix.

### Big data

* O mercado digital e o compartilhamento de informações entre as empresas digitais e seus consumidores em plataformas sociais como o Facebook, de compras como a Amazon ou de conteúdo interativo como a Netflix, faz com que cada vez mais as empresas possam conhecer o perfil de seus clientes.
* A empresa que conhece o perfil de seus clientes pode desenvolver seus produtos com as necessidades e preferências dos usuários.
* O big data da era atual cria uma disputa entre as empresas onde quem possuir mais dados obtém uma enorme vantagem de mercado, tornando os dados o recurso mais valioso e importante da era digital.

### Reconhecimento de padrões

* Muitos algoritmos são desenvolvidos para reconhecer padrões que definem os perfis dos usuários da sua plataforma.
* De acordo com o consumo do usuário, suas visitas mais frequentes, palavras chaves de pesquisas, lugares que frequentou, avaliações de produtos que consumiu, o algoritmo define padrões de usuários.
* A Netflix recomenda filmes e séries para seus assinantes com base nas preferências de clientes que tenham um perfil próximo ao dele.
* Se você se enquadra dentro de um perfil de usuário, a Netflix te recomenda produtos que usuários com o mesmo perfil que o seu já consumiram e aprovaram.

Assista uma aula da Escola Matriz explicando este estudo de caso no link a seguir:
[Aula 29: Netflix](https://youtu.be/pYpDN3EPkZ4)  
Confira o exercício proposto e a solução em Python sobre este estudo de caso:
[Netflix](https://github.com/DoctorNerds/Python_withAlgebra/tree/main/06.netflix)

## Das matrizes aos sistemas lineares presentes no cotidiano
### Conectando os pontos

* Aprendemos que a matemática e a teoria de álgebra linear são amplamente aplicáveis para o desenvolvimento da solução de muitos problemas do nosso cotidiano.
* Devemos conseguir enxergar as matrizes, os vetores e as combinações lineares presentes em cada problema que deve ser resolvido na prática.
* A álgebra nos diz como fazer e a programação como implementar.
* Através dos algoritmos podemos implementar álgebra linear em problemas reais.
* Tudo está conectado, a matemática não é apenas teoria, mas sim toda teoria e prática.

Assista uma aula da Escola Matriz debatendo estes conceitos no link a seguir:
[Aula 30: Das matrizes aos sistemas lineares presentes no cotidiano](https://youtu.be/4myZskWlAfQ)



   
