<h1>Desafio de programação para a Academia Capgemini</h1>

<h2>Considerações iniciais</h2>
<p align="justify">Apesar da preferência no desafio pela linguagem Java, possuo apenas conhecimentos básicos em HTML, CSS, Javascript e Python. Os códigos foram produzidos utilizando Python (versão 3.9.10), o qual tenho estudado mais atualmente.</p>
<p align="justify">Um sistema de <em>loop</em> usando uma variável "continuar" e uma função <em>while</em> foi criado nas três aplicações para que o teste possa ser repetido até que o usuário deseje encerrar.</p>
<p><strong>Passos para rodar as aplicações:</strong></p>
<ul>
<li>O Primeiro passo é ter Python no computador. Caso não possua Python, será necessário instalar de acordo com o sistema operacional. Link: https://www.python.org/downloads/. Preferencialmente a versão 3.9.10, que é mais estável. É indicado ainda marcar a opção “PATH” no início da instalação.</li>
<li>Baixe os arquivos, na opção “Code -> Download Zip” (Botão verde no menu do repositório do github). Extraia os arquivos para um local de fácil acesso.</li>
<li>Abra o Prompt de Comando (cmd) e acesse a pasta dos arquivos. Por exemplo, no Windows e mantendo na pasta padrão de downloads, basta usar o comando no cmd: 
cd Downloads\Desafio_capgemini-main</li>
<li>Agora basta executar o arquivo desejado, apenas escrevendo seu nome e extensão: questao01; questao02; questao03.</li>
<li>Ao sair de uma aplicação, o cmd ainda estará no mesmo diretório, então basta escrever o próximo arquivo a ser testado.</li>
</ul>

        
<h3 align="center">Questão 01</h3>				
<p align="justify"> <strong>Desafio: </strong>Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.</p>
<p align="justify"><strong>Sobre o código: </strong>A aplicação foi escrita de maneira bem simples e direta, tendo em vista que a tarefa é bem simples.</p>
<p></p>

<h3 align="center">Questão 02</h3>				
<p align="justify"> <strong>Desafio: </strong>Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios:</p>
<ul>
<li>Possui no mínimo 6 caracteres.</li>
<li>Contém no mínimo 1 digito.</li>
<li>Contém no mínimo 1 letra em minúsculo.</li>
<li>Contém no mínimo 1 letra em maiúsculo.</li>
<li>Contém no mínimo 1 caractere especial. Os caracteres especiais são: <strong>!@#$%^&*()-+</strong></li>
</ul>
<p align="justify">Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte. Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura.</p>
<p align="justify"><strong>Sobre o código: </strong>O código inicia com variáveis para cada critério, que são apresentados logo em seguida ao pedir para o usuário digitar a senha a ser testada. Após obter a senha, ignoramos eventuais espaçamentos em branco e transformamos a <em>string</em>em uma lista, para podermos fazer comparações elemento por elemento. Segue-se para o teste dos critérios, alterando o valor para <em>True</em> se houver elementos na lista que comportem as exigências.</p>
<p align="justify">Quanto ao teste de caracteres especiais, como foi dado um conjunto específico de caracteres a serem observados, foi criada uma lista própria para a comparação. Seria fácil alterar o código para abarcar outros caracteres especiais baseados no ASCII, apenas trocando esta lista por <em>string.punctuation</em>.</p>
<p align="justify">Com o resultado da análise dos elementos, a senha será considerada forte se, e somente se, todos os parâmetros forem respeitados (todas as variáveis devem ser <em>True</em>). Caso contrário, a senha será considerada fraca e será revelado o critério(s) faltante(s).</p>
<p></p>

<h3 align="center">Questão 03</h3>		
<p align="justify"> <strong>Desafio: </strong>Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.</p>
<p align="justify"><strong>Sobre o código: </strong>Esta questão em particular deu bastante trabalho por causa da interpretação do desafio. O “Exemplo 1” não é compatível com o “Exemplo 2”. Após ponderar sobre os elementos, principalmente o fato de se falar em “pares” e em “<em>substrings</em>”, passei a trabalhar com o objetivo de obter um par de variáveis que fossem <em>substrings</em> (elementos sequenciais) e anagramas em si. Dito isto, passei a considerar que o “Exemplo 1” está errado, pois a saída que representa o total de pares de <em>substrings</em> que são anagramas na pala “ovo” seria “2” e não “3” ([o, o], [ov, vo]).</p>
<p align="justify">Partindo deste entendimento, gerar o código se tornou uma tarefa suave (pois o trabalho foi entender o que o desafio queria). Primeiro, registra-se a entrada de uma palavra, ignorando espaçamentos vazios. Uma lista é gerada a partir da palavra para facilitar os arranjos. Algumas variáveis também são criadas para fazer as comparações devidas, além de guardar as <em>substrings</em> e os anagramas desejados. </p>
<p align="justify">O código passa a gerar a lista de <em>substrings</em>. Com esta lista guardada, cada elemento passa por uma verificação com os elementos restantes, em uma comparação quantitativa (quantidade de elementos deve ser igual) e qualitativa (a combinação dos elementos deve ser igual). Se aprovado em ambos os critérios, o par de <em>substrings</em> é salvo na lista de anagramas. Por fim, é impressa a palavra, o conjunto de pares de <em>substrings</em> que são anagramas (para conferência) e a quantidade destes pares (a saída desejada pelo desafio em questão).</p>
<p></p>

<p></p>
<h4>Mensagem final:</h4>
<p align="justify">Espero que as aplicações estejam do agrado e, desde já, agradeço pela oportunidade e atenção.</p>
<p><strong><em>Yuri Aoyama da Costa</em></strong></p>
<p></p>
