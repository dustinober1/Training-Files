import shutil
import psutil

disk = shutil.disk_usage("/")
avg = disk.free/disk.total*100

print(disk)
print(f"Percentage Free: {avg}")

for i in range(5):
    cpu = psutil.cpu_percent(0.5)
    print(f"{cpu}% of CPU is being used.")
    