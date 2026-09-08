import os
import sys
import glob
import subprocess
import time

def processar_video_ffmpeg(caminho_video):
    if not os.path.exists(caminho_video):
        print(f"\n❌ Erro: O arquivo '{caminho_video}' não existe nesta pasta.")
        return

    # Gera o nome da pasta automaticamente baseado no nome do vídeo (sem o .mp4)
    nome_base = os.path.splitext(os.path.basename(caminho_video))[0]
    nome_pasta_limpo = f"frames_{nome_base.replace(' ', '_')}"
    
    # Cria a pasta de destino se ela não existir
    if not os.path.exists(nome_pasta_limpo):
        os.makedirs(nome_pasta_limpo)
        print(f"\n📁 Criando pasta: {nome_pasta_limpo}")
    else:
        print(f"\n📁 Utilizando pasta existente: {nome_pasta_limpo}")

    print(f"🎬 Processando com FFmpeg: {os.path.basename(caminho_video)}")
    tempo_inicio = time.time()

    # O caminho de saída formatado para salvar as fotos (ex: frames_video/frame_0001.png)
    padrao_saida = os.path.join(nome_pasta_limpo, "frame_%04d.png")

    # Monta o comando do FFmpeg exatamente como você usaria no terminal do Windows
    # -y serve para sobrescrever arquivos antigos sem perguntar
    comando = [
        'ffmpeg',
        '-y',
        '-i', caminho_video,
        '-r', '30',       # Força a extração a exatos 30 frames por segundo
        '-q:v', '1',      # Qualidade máxima de exportação
        padrao_saida
    ]

    try:
        # Executa o FFmpeg em segundo plano ocultando as centenas de linhas de log dele
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        # Conta fisicamente quantos arquivos de imagem foram gerados na pasta
        total_frames = len([f for f in os.listdir(nome_pasta_limpo) if f.endswith('.png')])
        tempo_total = time.time() - tempo_inicio

        print(f"✨ Concluído! {total_frames} frames gerados com sucesso em {tempo_total:.2f}s.")
        print(f"💡 Fórmula para usar no seu Image Component do PsychoPy Builder:")
        print(f"   $'./{nome_pasta_limpo}/frame_%04d.png' % ((int(t * 30) % {total_frames}) + 1)")
        print("-" * 60)

    except FileNotFoundError:
        print("\n❌ Erro: O FFmpeg não foi encontrado no seu computador.")
        print("Certifique-se de que o FFmpeg está instalado e adicionado ao 'PATH' do seu Windows.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro durante a execução do FFmpeg: {e}")

# --- Fluxo Principal de Execução ---
if __name__ == "__main__":
    print("==================================================")
    print("   MOTOR DE EXTRAÇÃO DE FRAMES (VIA FFMPEG)")
    print("==================================================")
    
    # Pergunta qual arquivo processar
    entrada = input("Digite o nome do vídeo com extensão (ou aperte ENTER para todos os .mp4): ").strip()
    
    if entrada:
        processar_video_ffmpeg(entrada)
    else:
        # Busca automática por todos os arquivos .mp4 na pasta atual
        videos_mp4 = glob.glob("*.mp4")
        if not videos_mp4:
            print("\n❌ Nenhum arquivo .mp4 foi encontrado nesta pasta.")
        else:
            print(f"\n🔍 Encontrado(s) {len(videos_mp4)} vídeo(s) .mp4. Iniciando processamento em lote...")
            print("=" * 60)
            for video in videos_mp4:
                processar_video_ffmpeg(video)
                
    input("\nPressione Enter para fechar...")