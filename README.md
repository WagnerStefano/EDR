										EDR

O que é: o EDR (Endpoint Detection and Response) é um sistema de verificação para códigos maliciosos e resposta automatizada que pode gerar um relatório sobre a ameaça e finalizar a sua execução, com as funcionalidades básicas de Monitoramento de processos, Detecção de Execução de scripts maliciosos, Registro de Eventos no sistema e Respostas Automatizadas.

Escalabilidade e Manutenção: Pensando em escalabilidade da ferramenta utilizamos a Library Psutil que tem uma boa capacidade de monitoramento, em próximas atualizações da ferramenta podemos adicionar uma comunicação com Telegram ou Email para que avisos sejam enviados em tempo real, além de disponibilizar um Painel Web que pode gerar um gráfico de ameaças identificadas e tratadas além lista-las para que haja um controle e conhecimento, este painel pode ser desenvolvido com Python, Flask, JavaScript e PostgreSQL.
  algumas alterações da aplicação seriam necessárias como alterar o Log.txt para um arquivo JSON que seria lido pelo JavaScript e possibilitaria a interação com a pagina Web alterando os Gráficos e parâmetros.
Desenvolvimento da Ferramenta: Voltando ao desenvolvimento da ferramenta em sua versão 1.0, temos as seguintes funcionalidades presentes no protótipo, Verificação de Scripts em execução, Geração de Logs em um arquivo TXT e finalização dos códigos maliciosos e aplicações, aqui vão alguns passos do desenvolvimento.

1.	Preparação do Ambiente de Desenvolvimento (VSCode)
Instalação da ferramenta Psutil, dentro do VSCode, abra o terminal e insira o seguinte comando

		pip install psutil

![image](https://github.com/user-attachments/assets/0301d3e9-e0ba-445c-959d-0bff2564bd5c)
  A Biblioteca Psutil  (process and system utility) é uma biblioteca multiplataforma para recuperar informações sobre processos em execução e utilização do sistema (CPU, memória, discos, rede, sensores) em Python. É útil principalmente para monitoramento do sistema, criação de perfil e limitação de recursos de processo e gerenciamento de processos em execução.


2.	Pontos de desenvolvimento
Criação de um Script para para monitoramento de processos como executáveis perigosos: cmd.exe, powershell.exe, python.exe, bash, sh, etc.
Execução de scripts: .bat, .sh, .py e outros que possam ser usados para ataques.
Imports: Psutil para monitoramento de processos ativos no sistema.
	          OS Utilizado para interagir com o sistema operacional.
	          Time Utilizado para adicionar pausas no Loop de monitoramento.
![image](https://github.com/user-attachments/assets/c75cf4f6-354a-463e-b72e-fdb9742e5fdf)

 

Definição de Listas de Processos Suspeitos e Extensões:
  	suspicious_processes - Lista de processos considerados suspeitos.
  	suspicious_extensions - Extensões de arquivos que podem indicar atividades maliciosas.
   	 LOG_FILE - Nome do arquivo onde serão registrados os eventos suspeitos.

![image](https://github.com/user-attachments/assets/444018f1-cdea-404e-932f-f92ff5267e24)

 

3. Função para registrar logs de atividades suspeitas
 Objetivo: Sempre que um processo suspeito for detectado, ele será registrado no arquivo edr_log.txt.
 	with open (LOG_FILE, "a”) Abre o arquivo em modo de anexação ("a"), garantindo que novos eventos sejam adicionados sem apagar os antigos.
 	log.write - Escreve a informação no arquivo TXT.
print - Exibe um alerta no terminal.

![image](https://github.com/user-attachments/assets/d072f333-5924-4278-9060-ce6397d02e06)

 
