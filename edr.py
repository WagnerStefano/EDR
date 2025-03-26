import psutil
import os
import time

#listagem de processos

suspecious_processes = ["cmd.exe", "powershell.exe", "bash", "sh", "python.exe"]
suspecious_extensions = [".bat", ".sh", ".py"]
LOG_FILE = "edr_log.txt"

#SA = Suspecious Activity / Atividades suspeitas
def log_SA(process_name, pid, command):
    with open(LOG_FILE, "a") as log:
        log.write(f"[ALERTA] Processo suspeito detectado!: {process_name} (PID: {pid}) - Comando: {command}\n")
    print (f"[ALERTA] {process_name} (PID: {pid}) identificado! Comando: {command}")

    """
    O que é o PID
    """
# monitor de processos
def monitor_process(): 
    while True:
        for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
            try:
                process_name = process.info['name']
                pid = process.info['pid']
                cmdline = process.info['cmdline']
                command = ' '.join(cmdline) if cmdline else "[Sem comando]"

                #verifica o processo
                if process_name.lower() in suspecious_processes:
                    log_SA(process_name, pid, command)
                    psutil.Process(pid).terminate()#finaliza o processo

                if any(ext in command for ext in suspecious_extensions):
                    log_SA(process_name, pid, command)
                    psutil.Process(pid).terminate()#finaliza o processo

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        time.sleep(2)  #intervalo de verificações

if __name__ == "__main__":
    print("[INFO] Monitoramento de Processos Iniciado!")
    monitor_process()