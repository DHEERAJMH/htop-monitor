from django.shortcuts import render
import subprocess
import datetime

def index(request):
    return render(request, "htop/index.html")  # Render homepage

def system_info(request):
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True).split("\n")
    except subprocess.CalledProcessError:
        top_output = ["Error retrieving process information"]

    header_lines = top_output[:5]  # First 5 lines contain system stats
    process_lines = top_output[6:]  # Remaining lines contain process details

    process_list = []
    for line in process_lines:
        parts = line.split()
        if len(parts) > 10:
            process_list.append({
                "PID": parts[0], "USER": parts[1], "PR": parts[2],
                "NI": parts[3], "VIRT": parts[4], "RES": parts[5],
                "SHR": parts[6], "CPU_PERCENT": parts[8], "MEM_PERCENT": parts[9],
                "TIME+": parts[10], "COMMAND": " ".join(parts[11:])
            })

    return render(request, "monitor/system_info.html", {
        "server_time": server_time,
        "header_lines": header_lines,
        "process_list": process_list
    })
