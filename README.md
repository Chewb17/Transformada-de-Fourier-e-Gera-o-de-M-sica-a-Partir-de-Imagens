Trabalho Disciplina Seminário IX 24.3: Música, Matemática e Computação.

Membros do Grupo:

Lucas Coelho de Moraes.
Luiz Guilherme Almas Araujo.


Título: Transformada de Fourier e Geração de Música a Partir de Imagens

Resumo:
Este trabalho propõe uma abordagem inovadora para a geração musical utilizando conceitos da matemática aplicada e da computação. A partir da Transformada de Fourier, extraímos informações espectrais de uma imagem e as utilizamos para criar uma composição musical em formato MIDI. O objetivo é demonstrar como padrões visuais podem ser convertidos em estruturas sonoras, explorando a interseção entre música, matemática e computação.

Objetivos:

Aplicar a Transformada de Fourier para analisar a estrutura de uma imagem digital.

Converter a magnitude dos coeficientes espectrais em notas musicais dentro da escala MIDI.

Criar uma composição automática com variações de tempo, intensidade e acordes.

Explorar conceitos de aleatoriedade e variação para tornar a música mais expressiva.

Metodologia:

Carregamento da Imagem: Utilizamos a biblioteca OpenCV para carregar uma imagem e separá-la nos canais de cor RGB.

Análise Espectral: Aplicamos a Transformada de Fourier para cada canal e extraímos a magnitude dos coeficientes.

Mapeamento para Notas Musicais: Normalizamos os valores para o intervalo de notas do piano (MIDI 21 a 108).

Criação do Arquivo MIDI: Utilizamos a biblioteca MIDIUtil para gerar um arquivo musical, incorporando variações na intensidade, tempo e acordes.

Execução e Análise: O arquivo MIDI gerado será executado para análise musical, comparando padrões visuais com os padrões sonoros resultantes.

Resultados Esperados:

Geração de uma peça musical única baseada nas características da imagem fornecida.

Análise da influência das cores e padrões visuais na estrutura musical gerada.

Reflexão sobre a conversão de dados visuais em sons e suas possíveis aplicações em arte digital e música generativa.

Conclusão:
Este trabalho pretende demonstrar como técnicas matemáticas, como a Transformada de Fourier, podem ser aplicadas à música computacional, transformando imagens em composições sonoras. Além de apresentar uma perspectiva artística e científica, o projeto abre caminhos para novas formas de expressão e criação musical utilizando algoritmos.

Recursos Necessários:

Computador com Python instalado.

Bibliotecas: OpenCV, NumPy, SciPy, MIDIUtil.

Software para reprodução de arquivos MIDI (ex.: VLC, Musescore).

Cronograma:

Pesquisa e fundamentação teórica.

Implementação e testes do código.

Análise dos resultados.

Preparação da apresentação.

Apresentação final do seminário.

Bibliografia:

ALLAN, D. Mathematics and Music. Oxford University Press, 2016.

ROADS, C. The Computer Music Tutorial. MIT Press, 1996.

Documentação oficial das bibliotecas utilizadas.




Git Tutorial
Instalação
Pra instalar, basta acessar a página de downloads e seguir as instruções
Pra se conectar, utilize os seguinte comandos: (Substitua o nome e o e-mail para o seu)

git config --global user.name "nomeDeUsuario"
git config --global user.email "email"
Primeira Configuração
Pelo terminal entre na pasta onde irá guardar o projeto: cd /caminho/para/a/pasta, depois inicialize o git na pasta com o comando: git init

Outro jeito de fazer o citado acima: clique com o botão direito na pasta e selecione "Git Bash Here" para abrir o terminal do git

Crie um clone do repositório: git clone https://github.com/Chewb17/Trabalho-Eng.-Computacional.git

Entre na pasta criada pelo comando clone: cd /caminho/para/a/pasta/nova

Crie sua branch usando como o padrão o nome da feature que você está a desenvolver: git checkout -b nome_da_feature

Após criada a branch você será redirecionado automaticamente a ela, neste espaço que você desenvolverá sua parte do projeto

Rotina
Adicione as alterações feitas: git add .

Cheque em qual branch você está e quais alterações foram adicionadas: git status

Dê um commit com uma mensagem especificando as alterações realizadas: git commit -m "mensagem especificando o que foi feito"

Envie o commit feito para sua branch: git push origin suabranch

Quando estiver tudo pronto
Volte para a main: git checkout main

Atualize a main: git pull

Volte para a sua branch: git checkout nomedabranch

Mescle a main com a sua branch : git merge main

Corrija os possíveis conflitos

Confirme o merge (apenas quando solicitado pelo Scrum Master): git push origin suabranch

Espera a confirmação do seu SCRUM

Volte para a main: git checkout main

Mescle a main com as alterações enviadas para sua branch (apenas quando solicitado pelo Scrum Master): git merge suabranch

Confirme o merge (apenas quando solicitado pelo Scrum Master): git push origin main

Comandos Básicos
Para atualizar a main: git pull

Para atualizar alguma branch: git pull origin branch

Ver informações da branch: git status

Para trocar de branch: git checkout branch_desejada

Adicionar todas as alterações feitas: git add .

Adicionar alteração específica: git add arquivo-especifico

Para mesclar sua branch com a main (estando dentro da sua branch): git merge main

Para confirmar o merge: git push origin suabranch
