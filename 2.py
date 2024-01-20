import subprocess

# Caminho para o script de treinamento
train_script = "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\yolov5\\train.py"

# Executar o treinamento
subprocess.run([
    "python", train_script,
    "--img", "640",
    "--batch", "16",
    "--epochs", "50",
    "--data", "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\dataset\\CaminhaoPlaca.yaml",
    "--weights", "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\yolov5s.pt",
    "--cache"
])


# ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠

''' 

SÓ RODAR O 2 SE VOCE QUISER TREINAR NOVAMENTE !

'''


# ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠