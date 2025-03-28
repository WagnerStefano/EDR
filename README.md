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
  	<br>suspicious_processes - Lista de processos considerados suspeitos.
  	<br>suspicious_extensions - Extensões de arquivos que podem indicar atividades maliciosas.
   	<br> LOG_FILE - Nome do arquivo onde serão registrados os eventos suspeitos.

![image](https://github.com/user-attachments/assets/444018f1-cdea-404e-932f-f92ff5267e24)

 

3. Função para registrar logs de atividades suspeitas
 Objetivo: Sempre que um processo suspeito for detectado, ele será registrado no arquivo edr_log.txt.<br>
 	with open (LOG_FILE, "a”) Abre o arquivo em modo de anexação ("a"), garantindo que novos eventos sejam adicionados sem apagar os antigos.<br>
 	log.write - Escreve a informação no arquivo TXT.<br>
print - Exibe um alerta no terminal.<br>

![image](https://github.com/user-attachments/assets/d072f333-5924-4278-9060-ce6397d02e06)



4.Função para Monitoramento de Processos.
Objetivo: Monitorar todos os processos em execução no sistema.
 	psutil.process_iter(attrs=['pid', 'name', 'cmdline']) - Obtém informações sobre todos os processos ativos.<br>
 	process_name - Nome do processo.<br>
 	pid - ID do processo.<br>
	cmdline - Comando usado para iniciar o processo.<br>
	command = '  '.join(cmdline) - Junta os argumentos do comando em uma única string para facilitar a leitura. 
 <br>
 ![image](https://github.com/user-attachments/assets/d88f5b1a-97cd-4630-87f6-b54927d7143f)


 


5.  Verificação do Processo suspeito.
Process_name.lower() in suspecious_processes: - inicia a verificação passando o parâmetro nome do processo em lower case para identificação e armazenagem em Log. <br>
Log_SA(process_name, pid, command) – Registra as informações listadas sobre o processo.<br>
		Psutil.Process(pid).terminate() – Finaliza o processo detectado com base
	em seu pid. <br>
 ![image](https://github.com/user-attachments/assets/5779e237-200b-4244-8440-500847ee00e1)

	 

6. Verifica se um Comando possui extensões suspeitas.
		Any(ext int command for ext in suspecious_extensions): - Verifica
	Se arquivos listados no início da aplicação (.bat .sh .py) foram iniciados. <br>
Log_SA(process_name, pid, command) – Registra as informações caso um arquivo no formato listado seja executado. <br>
Psutil.Process(pid).terminate() – Finaliza o arquivo suspeito com base no PID registrado. <br>
![image](https://github.com/user-attachments/assets/e7479d87-7c38-424b-ba4e-71301c741cbf)


	 
	
7. Tratamento De Erros.
		Except (psutil.NoSuchProcess, psutil.ACessDenied, psutil.ZombieProcess):
		Pass – Em casos em que o processo já esteja encerrado ou haja uma restrição de acesso já aplicada ou listada para que seja ignorada o código ignora o “erro” e continua executando a verificação e finalização. <br>
  ![image](https://github.com/user-attachments/assets/178255ee-3130-4c49-9aee-d2f62daad98e)

	 

8. Pausa.
		time.sleep(2) #intervalo de verificações – uma pausa aplicada para evitar e monitorar o consumo da aplicação, afim de chegar ao uso constante a partir da inicialização do SO. <br>
  ![image](https://github.com/user-attachments/assets/19700839-9fea-4c22-8f57-4cd912af7cfc)

	 

9. Parâmetros Padão de inicialização.
		if __name__ == "__main__”: - Em Python Arquivos .py são chamados de módulos e cada modulo pode ser executado diretamente como um APP ou divididos/importados em módulos, por tanto para identificar esses módulos utilizamos a variável __name__ que indicara o nome do modulo que estará em execução. <br>
	Portanto utilizando a variável __name__ para nomear o módulo que não foi importado automaticamente o parâmetro é atualizado para __main__ e manterá este padrão de execução. <br>
		print("[INFO] Monitoramento de Processos Iniciado!")
   		 monitor_process() – Exibe a informação de inicio de execução da aplicação com a informação “ Monitoramento de Processos Iniciado! ”.
   ![image](https://github.com/user-attachments/assets/10133e36-b53f-48ff-b4fe-f805bcc79aa4)


	 


 
