import webbrowser as wb
import subprocess


urls = {
    "work":["https://www.coursera.org/programs/hec-pak-learning-program-j8ady","https://chatgpt.com/","https://www.youtube.com/","https://www.linkedin.com/feed/?trk=onboarding-landing"]
}

for url in urls["work"]:
    wb.open_new_tab(url)
    

subprocess.run(r"explorer.exe shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", shell=True)
